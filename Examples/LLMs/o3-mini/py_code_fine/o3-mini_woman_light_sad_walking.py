
"""
A Python program using pygame that displays a point‐light animation of a
"sad woman" walking. The animation shows exactly 15 white dots on a black background.
The 15 points represent key joints of a human figure:
   1. head
   2. left_shoulder
   3. right_shoulder
   4. left_elbow
   5. right_elbow
   6. left_wrist
   7. right_wrist
   8. spine
   9. pelvis
  10. left_hip
  11. right_hip
  12. left_knee
  13. right_knee
  14. left_ankle
  15. right_ankle

The animation simulates a smooth, biomechanically plausible walking cycle.
Arm and leg swing are created with a sine function and the posture is made a bit “sad”
by a somewhat slumped (lowered) upper-body.
"""

import pygame
import math
import sys

# Screen settings
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 60
SPEED = 50   # pixels per second horizontal movement of the pelvis (walking speed)
omega = 2 * math.pi * 1.2  # angular frequency for the walking cycle (cycles per second ~1.2 Hz)
amp_leg = 5    # horizontal swing amplitude for the legs
amp_arm = 5    # horizontal swing amplitude for the arms
amp_pelvis = 2  # vertical bobbing amplitude for the pelvis

# Define the skeleton in local (body-centered) coordinates.
# All coordinates are given relative to the pelvis (which is at (0, 0)).
# The positions have been chosen to mimic a slightly slumped posture.
# (Positive y is downward.)
base_skeleton = {
    "pelvis": (0, 0),
    "spine": (0, -30),
    "head": (0, -60),
    "left_shoulder": (-15, -30),
    "right_shoulder": (15, -30),
    "left_elbow": (-25, -15),
    "right_elbow": (25, -15),
    "left_wrist": (-30, 0),
    "right_wrist": (30, 0),
    "left_hip": (-10, 0),
    "right_hip": (10, 0),
    "left_knee": (-10, 30),
    "right_knee": (10, 30),
    "left_ankle": (-10, 60),
    "right_ankle": (10, 60)
}

def update_skeleton(t, base_x, base_y):
    """
    Given the time t (seconds) and the pelvis base position (base_x, base_y),
    return a dictionary mapping joint names to their global positions (x, y)
    taking into account a walking cycle.
    """
    joints = {}
    # Pelvis vertical bobbing (simulate slight bounce)
    pelvis_v_offset = amp_pelvis * math.sin(omega * 2 * t)
    pelvic_pos = (base_x, base_y + pelvis_v_offset)
    # The pelvis in our skeleton is the reference point.
    joints["pelvis"] = pelvic_pos

    # Spine and head: shift them relative to pelvis.
    spine_offset = base_skeleton["spine"]
    joints["spine"] = (pelvic_pos[0] + spine_offset[0], pelvic_pos[1] + spine_offset[1])
    head_offset = base_skeleton["head"]
    # Slight forward tilt of the head to imply sadness (shifted a little to the right)
    head_tilt = 2  
    joints["head"] = (pelvic_pos[0] + head_offset[0] + head_tilt, pelvic_pos[1] + head_offset[1])

    # Shoulders (we keep them as in the base, perhaps a little droop to increase the "sad" impression)
    ls_offset = base_skeleton["left_shoulder"]
    rs_offset = base_skeleton["right_shoulder"]
    droop = 3  # drooping value: lower the shoulders
    joints["left_shoulder"] = (pelvic_pos[0] + ls_offset[0],
                               pelvic_pos[1] + ls_offset[1] + droop)
    joints["right_shoulder"] = (pelvic_pos[0] + rs_offset[0],
                                pelvic_pos[1] + rs_offset[1] + droop)

    # Arms: We simulate swing using a sine function.
    # The left arm (elbow and wrist) swings opposite to the right leg.
    left_arm_phase = math.sin(omega * t + math.pi)
    right_arm_phase = math.sin(omega * t)
    for joint in ["left_elbow", "left_wrist"]:
        offset = base_skeleton[joint]
        # add horizontal offset to simulate swinging; only modify x coordinate.
        joints[joint] = (pelvic_pos[0] + offset[0] + amp_arm * left_arm_phase,
                         pelvic_pos[1] + offset[1])
    for joint in ["right_elbow", "right_wrist"]:
        offset = base_skeleton[joint]
        joints[joint] = (pelvic_pos[0] + offset[0] + amp_arm * right_arm_phase,
                         pelvic_pos[1] + offset[1])
                         
    # Hips (remain rigid relative to pelvis)
    for joint in ["left_hip", "right_hip"]:
        offset = base_skeleton[joint]
        joints[joint] = (pelvic_pos[0] + offset[0],
                         pelvic_pos[1] + offset[1])
                         
    # Legs: simulate swinging by modifying the knee and ankle x positions.
    left_leg_phase = math.sin(omega * t)
    right_leg_phase = math.sin(omega * t + math.pi)  # opposite phase
    for joint in ["left_knee", "left_ankle"]:
        offset = base_skeleton[joint]
        joints[joint] = (pelvic_pos[0] + offset[0] + amp_leg * left_leg_phase,
                         pelvic_pos[1] + offset[1])
    for joint in ["right_knee", "right_ankle"]:
        offset = base_skeleton[joint]
        joints[joint] = (pelvic_pos[0] + offset[0] + amp_leg * right_leg_phase,
                         pelvic_pos[1] + offset[1])
    return joints

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion Animation: Sad Woman Walking")
    clock = pygame.time.Clock()

    # Starting horizontal location for pelvis (off-screen left)
    base_x = -100
    base_y = HEIGHT // 2 + 50  # center vertically, slightly lower

    running = True
    start_ticks = pygame.time.get_ticks()  # record start time
    while running:
        dt = clock.tick(FPS) / 1000.0  # in seconds
        # Update base_x to simulate forward walking motion.
        base_x += SPEED * dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Wrap-around after the figure moves off the right side.
        if base_x > WIDTH + 100:
            base_x = -100

        t = (pygame.time.get_ticks() - start_ticks) / 1000.0  # elapsed time in seconds
        joints = update_skeleton(t, base_x, base_y)

        # Clear the screen.
        screen.fill(BLACK)

        # Draw the 15 joints as white circles.
        for joint in ["head", "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",
                      "left_wrist", "right_wrist", "spine", "pelvis", "left_hip", "right_hip",
                      "left_knee", "right_knee", "left_ankle", "right_ankle"]:
            pos = (int(joints[joint][0]), int(joints[joint][1]))
            pygame.draw.circle(screen, WHITE, pos, 4)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()