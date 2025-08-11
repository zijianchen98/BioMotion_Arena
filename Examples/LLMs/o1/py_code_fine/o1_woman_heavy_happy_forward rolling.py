#!/usr/bin/env python3
import pygame
import math
import sys
import time

# This program displays a simple point-light animation of a "heavy" happy woman
# performing a forward roll. It uses exactly 15 white point-lights on a black
# background. The motion is a stylized approximation intended to suggest a
# coherent biological rolling action.

# --------------------------------------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------------------------------------

def rotate_2d(point, theta):
    """Rotate a 2D point (x, y) around the origin (0,0) by angle theta (radians)."""
    x, y = point
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    rx = x * cos_t - y * sin_t
    ry = x * sin_t + y * cos_t
    return (rx, ry)

def translate_2d(point, dx, dy):
    """Translate a 2D point (x, y) by (dx, dy)."""
    x, y = point
    return (x + dx, y + dy)

# --------------------------------------------------------------------------------
# SKELETON MODEL
# --------------------------------------------------------------------------------
# We define a static "rest" skeleton (15 joints), oriented upright with arms out,
# centered roughly at the origin. Then we'll apply transformations over time
# to simulate a forward roll. The skeleton is only approximate and intended
# to give an impression of rolling motion.

# Indices of these 15 points:
#  0: head           1: neck          2: torso center 
#  3: right shoulder 4: right elbow   5: right wrist
#  6: left shoulder  7: left elbow    8: left wrist
#  9: right hip      10: right knee   11: right ankle
# 12: left hip       13: left knee    14: left ankle

rest_skeleton = [
    (0, -80),   # head
    (0, -60),   # neck
    (0, -30),   # torso center
    (20, -50),  # right shoulder
    (35, -45),  # right elbow
    (45, -40),  # right wrist
    (-20, -50), # left shoulder
    (-35, -45), # left elbow
    (-45, -40), # left wrist
    (15, 0),    # right hip
    (15, 25),   # right knee
    (15, 50),   # right ankle
    (-15, 0),   # left hip
    (-15, 25),  # left knee
    (-15, 50),  # left ankle
]

def get_skeleton_points(t):
    """
    Returns a list of 15 (x, y) positions for the skeleton at time t.
    t is in [0,1] for one full rolling cycle. We'll do a repeated roll:
    - The entire skeleton is rotated around a pivot on the floor to simulate a roll.
    - We add some extra 'swing' in arms/legs to give a sense of motion.
    """

    # Convert t to an angle for one full revolution (2*pi = 360 degrees).
    # We interpret this as one forward roll from t=0..1
    angle_full_roll = 2 * math.pi * t

    # We'll define a pivot on the ground from which we rotate the skeleton.
    # This pivot might approximate where the shoulders or hips contact, but
    # here we'll just set it below the skeleton's initial center.
    pivot_x, pivot_y = 300, 300

    # A small "swing" angle for limbs to create some motion cues
    limb_swing_amp = math.radians(20)
    limb_swing = limb_swing_amp * math.sin(2 * math.pi * t * 2.0)

    # We'll define the "heavy" trunk as being slightly compressed or curved
    # by modulating torso points (index 2) just a bit in the y-direction.
    trunk_bob = 5.0 * math.sin(2 * math.pi * t * 2.0)

    # Build a new skeleton instance from the rest_skeleton
    sk = list(rest_skeleton)

    # Torso center bob (index 2)
    cx, cy = sk[2]
    sk[2] = (cx, cy + trunk_bob)

    # Very rough arm and leg swing:
    # Right elbow (4) and wrist (5), left elbow (7) and wrist (8),
    # right knee (10) and ankle (11), left knee (13) and ankle (14).
    # We rotate them about their respective shoulder or hip.

    # Rotate right arm about right shoulder (3)
    shoulder_pt = sk[3]
    elbow_idx, wrist_idx = 4, 5
    sk[elbow_idx] = rotate_2d((sk[elbow_idx][0] - shoulder_pt[0],
                               sk[elbow_idx][1] - shoulder_pt[1]), limb_swing)
    sk[elbow_idx] = translate_2d(sk[elbow_idx], shoulder_pt[0], shoulder_pt[1])
    sk[wrist_idx] = rotate_2d((sk[wrist_idx][0] - shoulder_pt[0],
                               sk[wrist_idx][1] - shoulder_pt[1]), limb_swing)
    sk[wrist_idx] = translate_2d(sk[wrist_idx], shoulder_pt[0], shoulder_pt[1])

    # Rotate left arm about left shoulder (6)
    shoulder_pt = sk[6]
    elbow_idx, wrist_idx = 7, 8
    sk[elbow_idx] = rotate_2d((sk[elbow_idx][0] - shoulder_pt[0],
                               sk[elbow_idx][1] - shoulder_pt[1]), -limb_swing)
    sk[elbow_idx] = translate_2d(sk[elbow_idx], shoulder_pt[0], shoulder_pt[1])
    sk[wrist_idx] = rotate_2d((sk[wrist_idx][0] - shoulder_pt[0],
                               sk[wrist_idx][1] - shoulder_pt[1]), -limb_swing)
    sk[wrist_idx] = translate_2d(sk[wrist_idx], shoulder_pt[0], shoulder_pt[1])

    # Rotate right leg about right hip (9)
    hip_pt = sk[9]
    knee_idx, ankle_idx = 10, 11
    sk[knee_idx] = rotate_2d((sk[knee_idx][0] - hip_pt[0],
                              sk[knee_idx][1] - hip_pt[1]), -limb_swing)
    sk[knee_idx] = translate_2d(sk[knee_idx], hip_pt[0], hip_pt[1])
    sk[ankle_idx] = rotate_2d((sk[ankle_idx][0] - hip_pt[0],
                               sk[ankle_idx][1] - hip_pt[1]), -limb_swing)
    sk[ankle_idx] = translate_2d(sk[ankle_idx], hip_pt[0], hip_pt[1])

    # Rotate left leg about left hip (12)
    hip_pt = sk[12]
    knee_idx, ankle_idx = 13, 14
    sk[knee_idx] = rotate_2d((sk[knee_idx][0] - hip_pt[0],
                              sk[knee_idx][1] - hip_pt[1]), limb_swing)
    sk[knee_idx] = translate_2d(sk[knee_idx], hip_pt[0], hip_pt[1])
    sk[ankle_idx] = rotate_2d((sk[ankle_idx][0] - hip_pt[0],
                               sk[ankle_idx][1] - hip_pt[1]), limb_swing)
    sk[ankle_idx] = translate_2d(sk[ankle_idx], hip_pt[0], hip_pt[1])

    # Now rotate the entire skeleton about the pivot by angle_full_roll
    rotated_skeleton = []
    for (x, y) in sk:
        # Translate so pivot is origin, rotate, then translate back
        x -= 0
        y -= 100  # Shift skeleton up so it "rolls" around the pivot roughly
        rx, ry = rotate_2d((x, y), angle_full_roll)
        rx, ry = translate_2d((rx, ry), pivot_x, pivot_y)
        rotated_skeleton.append((rx, ry))

    return rotated_skeleton

# --------------------------------------------------------------------------------
# MAIN LOOP (PYGAME)
# --------------------------------------------------------------------------------

def main():
    pygame.init()
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Biological Motion: Forward Roll")

    clock = pygame.time.Clock()
    running = True

    start_time = time.time()
    duration = 2.0  # seconds for one full roll (t goes 0->1 in this time)

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Compute normalized time t in [0, 1]
        now = time.time()
        elapsed = (now - start_time)
        # We'll loop the roll indefinitely
        t = (elapsed % duration) / duration

        # Clear screen (black background)
        screen.fill((0, 0, 0))

        # Get the positions of the 15 points in the skeleton
        skeleton_points = get_skeleton_points(t)

        # Draw each point (white)
        for pt in skeleton_points:
            pygame.draw.circle(screen, (255, 255, 255), (int(pt[0]), int(pt[1])), 4)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()