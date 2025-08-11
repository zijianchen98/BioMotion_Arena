#!/usr/bin/env python3
import pygame
import math
import sys

# ------------------------------
# Point-Light Biological Motion:
# Sad man with heavy weight turning around
# Exactly 15 white point-lights on black background
# ------------------------------

# ------------------------------
# 3D skeleton definition (15 points) in "sad" posture:
# Indices and approximate 3D offsets (x, y, z)
# The figure is somewhat hunched forward, arms/shoulders drooping.
# Skeleton layout (y-axis is up, x-axis is side-to-side, z-axis is forward/back).
#
#  0: Head
#  1: Neck
#  2: Left Shoulder
#  3: Left Elbow
#  4: Left Hand
#  5: Right Shoulder
#  6: Right Elbow
#  7: Right Hand
#  8: Torso (center, near chest)
#  9: Left Hip
# 10: Left Knee
# 11: Left Foot
# 12: Right Hip
# 13: Right Knee
# 14: Right Foot
# ------------------------------
BASE_SKELETON_3D = [
    (0.0,  1.00,  0.0),   # Head (slightly forward in rotation, but base is set)
    (0.0,  0.90,  0.0),   # Neck
    (-0.15, 0.90, 0.0),   # Left Shoulder
    (-0.20, 0.65, 0.05),  # Left Elbow
    (-0.15, 0.40, 0.05),  # Left Hand
    ( 0.15, 0.90, 0.0),   # Right Shoulder
    ( 0.20, 0.65, 0.05),  # Right Elbow
    ( 0.15, 0.40, 0.05),  # Right Hand
    (0.0,  0.70,  0.0),   # Torso
    (-0.10, 0.50, 0.0),   # Left Hip
    (-0.10, 0.25, 0.0),   # Left Knee
    (-0.10, 0.00, 0.05),  # Left Foot
    ( 0.10, 0.50, 0.0),   # Right Hip
    ( 0.10, 0.25, 0.0),   # Right Knee
    ( 0.10, 0.00, 0.05),  # Right Foot
]

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Animation parameters
FPS = 30
TOTAL_FRAMES = 60  # how many frames to animate
# We'll rotate from +90 degrees (side view facing left) to -90 degrees (side view facing right)
START_ANGLE_DEG = 90
END_ANGLE_DEG   = -90

# ------------------------------
# Rotation about Y-axis (in radians)
# ------------------------------
def rotate_y(point, angle_radians):
    """Rotate a 3D point (x, y, z) around the Y-axis by angle_radians."""
    x, y, z = point
    cos_a = math.cos(angle_radians)
    sin_a = math.sin(angle_radians)
    # Rotation around Y:  x' = x*cosA + z*sinA, z' = -x*sinA + z*cosA
    x_new = x * cos_a + z * sin_a
    y_new = y
    z_new = -x * sin_a + z * cos_a
    return (x_new, y_new, z_new)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion: Sad Man Turning Around")
    clock = pygame.time.Clock()

    frame_count = 0
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Compute current angle by interpolating between START_ANGLE_DEG and END_ANGLE_DEG
        t = frame_count / float(TOTAL_FRAMES)
        # clamp t in [0,1]
        if t > 1.0:
            t = 1.0
        current_angle_deg = START_ANGLE_DEG + (END_ANGLE_DEG - START_ANGLE_DEG) * t
        current_angle_rad = math.radians(current_angle_deg)

        # Clear screen (black background)
        screen.fill((0, 0, 0))

        # Transform and draw the 15 white points
        for pt3d in BASE_SKELETON_3D:
            rx, ry, rz = rotate_y(pt3d, current_angle_rad)

            # Project from 3D to 2D (simple orthographic)
            # We'll scale up a bit to fill screen
            scale = 200
            screen_x = int(WIDTH // 2  + rx * scale)
            screen_y = int(HEIGHT // 2 - ry * scale)  # y goes down in screen coords

            # Draw a small circle for each point (white)
            pygame.draw.circle(screen, (255, 255, 255), (screen_x, screen_y), 5)

        pygame.display.flip()

        frame_count += 1
        # Stop automatically if we reached total frames,
        # but you can let it loop or exit at this point.
        if frame_count > TOTAL_FRAMES:
            # If you want it to loop indefinitely, comment out the next line
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()