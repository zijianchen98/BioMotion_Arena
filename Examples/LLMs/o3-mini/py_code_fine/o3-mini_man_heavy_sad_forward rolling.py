
"""
This program displays a point‐light animation of a “sadman with heavy weight”
performing a forward roll. The stimulus is rendered as exactly 15 white dots
(“point-lights”) on a solid black background. The points represent key joints
on the body and are transformed in a biomechanically plausible way to simulate a
smooth, coherent rolling action.

The animation works as follows:
 • A base “skeleton” of 15 points (head, neck, shoulders, elbows, hands, torso,
   hips, knees, and feet) is defined in local coordinates.
 • The center-of-mass of the skeleton is computed and used as the pivot for a
   rotation transformation.
 • In each frame the skeleton is rotated by an angle proportional to elapsed
   time (simulating the forward roll) while it is translated horizontally (simulating
   forward motion). The rotation + translation produces a smooth forward rolling
   motion.
 
Run with Python3 and make sure pygame is installed.
"""

import pygame
import sys
import math
from pygame.locals import QUIT

# Screen settings
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60

# Animation parameters
ROLL_RATE = 2.0         # radians per second (roll speed)
TRANSLATION_SPEED = 100  # pixels per second (forward motion)

# Define 15 point-lights for the skeleton (in local coordinates)
# The coordinates are chosen to roughly represent a human in a slightly drooped posture.
# Points: [Head, Neck, Left Shoulder, Right Shoulder, Left Elbow, Right Elbow,
#          Left Hand, Right Hand, Torso, Left Hip, Right Hip, Left Knee, Right Knee,
#          Left Foot, Right Foot]
base_points = [
    (0, -50),    # 0 Head
    (0, -45),    # 1 Neck
    (-15, -45),  # 2 Left Shoulder
    (15, -45),   # 3 Right Shoulder
    (-25, -30),  # 4 Left Elbow
    (25, -30),   # 5 Right Elbow
    (-30, -15),  # 6 Left Hand
    (30, -15),   # 7 Right Hand
    (0, -30),    # 8 Torso (mid chest)
    (-10, -10),  # 9 Left Hip
    (10, -10),   # 10 Right Hip
    (-10, 5),    # 11 Left Knee
    (10, 5),     # 12 Right Knee
    (-10, 25),   # 13 Left Foot
    (10, 25)     # 14 Right Foot
]

# Compute the center of mass of the skeleton to use as the rotation pivot.
sum_x = sum(p[0] for p in base_points)
sum_y = sum(p[1] for p in base_points)
n_points = len(base_points)
center_mass = (sum_x / n_points, sum_y / n_points)

def rotate_point(point, angle):
    """Rotate a point (x, y) by the given angle (radians) about the origin."""
    x, y = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    x_new = x * cos_a - y * sin_a
    y_new = x * sin_a + y * cos_a
    return (x_new, y_new)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Forward Roll Animation")
    clock = pygame.time.Clock()

    # Time tracking
    start_ticks = pygame.time.get_ticks()

    while True:
        # Handle events (quit on window close)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Calculate elapsed time in seconds
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0
        
        # Determine current rotation angle and translation offset.
        angle = ROLL_RATE * t
        translation_x = TRANSLATION_SPEED * t

        # Clear the background
        screen.fill(BLACK)

        # For each point in the skeleton, perform transformations:
        # 1. Translate the point so that the center_of_mass becomes the origin.
        # 2. Apply the rotation.
        # 3. Translate back and then apply the horizontal translation.
        transformed_points = []
        for pt in base_points:
            # Make the point relative to center-of-mass
            rel_x = pt[0] - center_mass[0]
            rel_y = pt[1] - center_mass[1]
            # Rotate the relative point by current angle
            r_x, r_y = rotate_point((rel_x, rel_y), angle)
            # Move back by adding center-of-mass
            final_x = r_x + center_mass[0]
            final_y = r_y + center_mass[1]
            # Apply a global translation in x (simulate forward rolling)
            final_x += translation_x
            transformed_points.append((final_x, final_y))

        # Optional: Center the skeleton vertically in the screen.
        # First, compute the vertical bounding box of the transformed points.
        ys = [pt[1] for pt in transformed_points]
        min_y, max_y = min(ys), max(ys)
        skeleton_height = max_y - min_y
        # Compute vertical offset so that skeleton is roughly centered.
        vertical_offset = (HEIGHT - skeleton_height) / 2 - min_y

        # Draw each point as a small white circle.
        for pt in transformed_points:
            # Apply vertical offset
            draw_x = int(pt[0])
            draw_y = int(pt[1] + vertical_offset)
            # Draw a circle of radius 4 pixels (point-light)
            pygame.draw.circle(screen, WHITE, (draw_x, draw_y), 4)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()