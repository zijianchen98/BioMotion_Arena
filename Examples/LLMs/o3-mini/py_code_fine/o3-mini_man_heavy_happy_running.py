
"""
This program displays an animation of a point‐light (15 white dots) stimulus representing a running,
heavy, happy man. The 15 dots are arranged as anatomical “joints” of a stick‐figure. For example,
the dots represent the head, shoulders, elbows, wrists, hips, knees, ankles, torso and belly.
We use sinusoidal oscillations to simulate biomechanically plausible arm and leg swings. The figure
moves continuously (left to right) on a solid black background.
"""

import sys, math, pygame

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
speed = 100  # horizontal speed in pixels per second
f = 2.0      # running cycle frequency in Hz
arm_amp = 10  # amplitude for arm swing in pixels
leg_amp = 15  # amplitude for leg swing in pixels
bounce_amp = 5  # amplitude for vertical bounce of the body center

# Body configuration (relative offsets from the body center)
# There are exactly 15 joints:
#  0: Head
#  1: Left Shoulder
#  2: Right Shoulder
#  3: Left Elbow
#  4: Right Elbow
#  5: Left Wrist
#  6: Right Wrist
#  7: Left Hip
#  8: Right Hip
#  9: Left Knee
# 10: Right Knee
# 11: Left Foot
# 12: Right Foot
# 13: Mid Torso (body center)
# 14: Belly

# Base positions (x, y offsets relative to body center)
# Units are in pixels.
base_joints = {
    "head":         (0, -60),
    "left_shoulder": (-15, -40),
    "right_shoulder": (15, -40),
    "left_elbow":   (-30, -20),
    "right_elbow":  (30, -20),
    "left_wrist":   (-45, 0),
    "right_wrist":  (45, 0),
    "left_hip":     (-10, 20),
    "right_hip":    (10, 20),
    "left_knee":    (-10, 50),
    "right_knee":   (10, 50),
    "left_foot":    (-10, 80),
    "right_foot":   (10, 80),
    "mid_torso":    (0, 0),
    "belly":        (0, 10)
}

def compute_joint_positions(t):
    """ Return a dictionary with computed positions for every joint (absolute screen coordinates). """
    # Compute body center position
    # The man runs from left to right and wraps around.
    x_body = ((speed * t) % (WIDTH + 100)) - 50  # start slightly off-screen left
    y_body = HEIGHT // 2 + bounce_amp * math.sin(2 * math.pi * f * t)  # small vertical bounce
    body_center = (x_body, y_body)
    
    # Compute arm swing and leg swing offsets based on the running cycle
    # For a heavy runner, the arms and legs swing in opposite phases.
    # left arm swings with phase 0, right arm with phase pi.
    arm_offset = arm_amp * math.sin(2 * math.pi * f * t)
    # For legs, use opposite phases: left leg in opposite phase to right leg.
    leg_offset_left = leg_amp * math.sin(2 * math.pi * f * t + math.pi)  # left leg
    leg_offset_right = leg_amp * math.sin(2 * math.pi * f * t)           # right leg

    joints = {}

    # Head (remains fixed relative to body center)
    base = base_joints["head"]
    joints["head"] = (body_center[0] + base[0], body_center[1] + base[1])
    
    # Shoulders (static relative to body center)
    base = base_joints["left_shoulder"]
    joints["left_shoulder"] = (body_center[0] + base[0], body_center[1] + base[1])
    base = base_joints["right_shoulder"]
    joints["right_shoulder"] = (body_center[0] + base[0], body_center[1] + base[1])
    
    # Left arm: elbow and wrist swing downward/upward with arm_offset.
    base = base_joints["left_elbow"]
    joints["left_elbow"] = (body_center[0] + base[0],
                            body_center[1] + base[1] + arm_offset)
    base = base_joints["left_wrist"]
    joints["left_wrist"] = (body_center[0] + base[0],
                            body_center[1] + base[1] + arm_offset)
    
    # Right arm: swing opposite in phase.
    base = base_joints["right_elbow"]
    joints["right_elbow"] = (body_center[0] + base[0],
                             body_center[1] + base[1] - arm_offset)
    base = base_joints["right_wrist"]
    joints["right_wrist"] = (body_center[0] + base[0],
                             body_center[1] + base[1] - arm_offset)
    
    # Hips (remain static relative to body center)
    base = base_joints["left_hip"]
    joints["left_hip"] = (body_center[0] + base[0], body_center[1] + base[1])
    base = base_joints["right_hip"]
    joints["right_hip"] = (body_center[0] + base[0], body_center[1] + base[1])
    
    # Left leg: add swing on knee and foot.
    base = base_joints["left_knee"]
    joints["left_knee"] = (body_center[0] + base[0],
                           body_center[1] + base[1] + leg_offset_left)
    base = base_joints["left_foot"]
    joints["left_foot"] = (body_center[0] + base[0],
                           body_center[1] + base[1] + leg_offset_left)
    
    # Right leg: add swing on knee and foot.
    base = base_joints["right_knee"]
    joints["right_knee"] = (body_center[0] + base[0],
                            body_center[1] + base[1] + leg_offset_right)
    base = base_joints["right_foot"]
    joints["right_foot"] = (body_center[0] + base[0],
                            body_center[1] + base[1] + leg_offset_right)
    
    # Mid torso is exactly the body center
    base = base_joints["mid_torso"]
    joints["mid_torso"] = (body_center[0] + base[0], body_center[1] + base[1])
    
    # Belly is a bit lower than the mid torso
    base = base_joints["belly"]
    joints["belly"] = (body_center[0] + base[0], body_center[1] + base[1] + 0)
    
    return joints

def main():
    start_ticks = pygame.time.get_ticks()  # milliseconds
    running = True
    while running:
        dt = clock.tick(60)  # aim for 60 fps
        current_ticks = pygame.time.get_ticks()
        t = (current_ticks - start_ticks) / 1000.0  # elapsed time in seconds

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update joint positions based on time t
        joints = compute_joint_positions(t)

        # Drawing
        screen.fill(BLACK)

        # Draw each joint as a white circle with radius 5
        for pos in joints.values():
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()