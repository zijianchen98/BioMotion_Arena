
"""
This program shows a point‐light biological motion animation.
It displays a “happy woman” executing a forward jump using exactly 15 white point‐lights against a black background.
Each point represents a key joint of the body. The motion is simulated in a biomechanically plausible way.
Press the close [X] button on the window to exit.
"""

import pygame
import math
import sys
import time

# Screen settings
WIDTH, HEIGHT = 800, 600
FPS = 60

# Animation parameters
CYCLE_TIME = 2.0  # seconds per jump cycle
MAX_JUMP_HEIGHT = 100  # maximum vertical jump displacement, in pixels
FORWARD_DISTANCE = 200  # horizontal displacement during one jump cycle

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Body joints defined in "body space" (relative coordinates).
# There are 15 joints labeled as follows:
#
#   0: Head
#   1: Left Shoulder
#   2: Right Shoulder
#   3: Left Elbow
#   4: Right Elbow
#   5: Left Hand
#   6: Right Hand
#   7: Torso (center chest)
#   8: Left Hip
#   9: Right Hip
#   10: Left Knee
#   11: Right Knee
#   12: Left Foot
#   13: Right Foot
#   14: Mid-spine (just below head for extra detail)
#
# The coordinates are chosen so that y increases downward.
# They are roughly scaled for a human figure.
base_joints = [
    (0, -50),    # Head
    (-15, -30),  # Left Shoulder
    (15, -30),   # Right Shoulder
    (-30, -10),  # Left Elbow
    (30, -10),   # Right Elbow
    (-35, 10),   # Left Hand
    (35, 10),    # Right Hand
    (0, 0),      # Torso (center chest)
    (-10, 10),   # Left Hip
    (10, 10),    # Right Hip
    (-10, 30),   # Left Knee
    (10, 30),    # Right Knee
    (-10, 50),   # Left Foot
    (10, 50),    # Right Foot
    (0, -10)     # Mid-spine (for extra detail)
]

def get_joint_positions(elapsed_time):
    """
    Given the elapsed time (in seconds), compute the positions of the 15 point-lights in screen coordinates.
    The motion simulates a forward jump.
    """
    # Normalize time in the cycle [0, 1]
    t = (elapsed_time % CYCLE_TIME) / CYCLE_TIME

    # Compute global jump offsets.
    # Vertical offset: a parabolic jump. (Remember: on screen, smaller y means higher.)
    # At t=0 and t=1, jump_y is 0; at t=0.5 the jump peak is -MAX_JUMP_HEIGHT.
    jump_y = -4 * MAX_JUMP_HEIGHT * t * (1 - t)
    # Horizontal offset: moves linearly forward
    jump_x = FORWARD_DISTANCE * t

    # Compute some modulation factors to simulate limb movements:
    # Bend factor for legs (strongest at mid-jump, t=0.5)
    leg_bend = math.sin(math.pi * t)  # 0 at t=0 & t=1, 1 at t=0.5
    # Swing factor for arms (simulate slight swing; using 2*pi gives two swings per cycle)
    arm_swing = math.sin(2 * math.pi * t)

    # The body center (reference point for the figure) at start.
    base_center_x = 100  # starting x-position
    base_center_y = 300  # ground base line (when not jumping)

    # Global translation (adding the jump offsets)
    global_x = base_center_x + jump_x
    global_y = base_center_y + jump_y

    # We will compute a new list of joint positions.
    joint_positions = []

    # For each joint, start with the base coordinate and then apply modifications if needed.
    # We work on a copy of each coordinate.
    for i, (x, y) in enumerate(base_joints):
        new_x, new_y = x, y

        # Modify arms: indices 3,5 (left arm) and 4,6 (right arm)
        # Let them swing upward slightly (move upward when swinging).
        if i in [3, 5, 4, 6]:
            # A small swing: adjust y by up to 8 pixels (different for elbow and hand)
            if i in [3, 4]:  # elbows
                new_y += -5 * arm_swing
            else:  # hands
                new_y += -8 * arm_swing

        # Modify legs: bending during the jump.
        # For each leg, the knee and foot will move upward (i.e. their y value decreases) when bending.
        if i in [10, 11]:  # Knees
            new_y -= 10 * leg_bend
        if i in [12, 13]:  # Feet
            new_y -= 5 * leg_bend

        # Optionally, you could modify the head or other points slightly.
        if i == 0:  # Head: slight bobbing
            new_y += -3 * math.sin(math.pi * t)

        # Now, add the global translation.
        screen_x = int(global_x + new_x)
        screen_y = int(global_y + new_y)
        joint_positions.append((screen_x, screen_y))

    return joint_positions

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion: Jumping Woman")
    clock = pygame.time.Clock()

    start_time = time.time()
    running = True
    while running:
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen (fill with black)
        screen.fill(BLACK)

        # Compute current joint positions for this frame.
        joints = get_joint_positions(elapsed_time)

        # Draw each joint as a white circle (point-light)
        for pos in joints:
            # You can adjust the radius (here using 4 pixels) to make the points visible.
            pygame.draw.circle(screen, WHITE, pos, 4)

        # Update the display.
        pygame.display.flip()

        # Maintain FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()