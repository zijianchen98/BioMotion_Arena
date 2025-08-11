
"""
This program displays a point‐light stimulus animation against a solid black background.
It depicts a happy, light‐weight man “bowing” using exactly 15 white point‐lights.
The upper body (head, shoulders, elbows, hands, and torso) rotates around the hip center
to simulate a smooth, natural and biomechanically plausible bowing movement.
Press the close window button or ESC to exit.
"""

import sys
import math
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

# Screen dimensions
WIDTH, HEIGHT = 600, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the 15 points coordinates for the standing figure in an upright posture.
# The indices of the points:
# 0: Head Top
# 1: Head Center
# 2: Left Shoulder
# 3: Right Shoulder
# 4: Left Elbow
# 5: Right Elbow
# 6: Left Hand
# 7: Right Hand
# 8: Torso (upper body mid)
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Foot
# 14: Right Foot
#
# All coordinates are given as (x, y)
# The figure is roughly centered on the screen.
points = [
    (300, 320),  # 0. Head Top
    (300, 350),  # 1. Head Center
    (265, 370),  # 2. Left Shoulder
    (335, 370),  # 3. Right Shoulder
    (250, 400),  # 4. Left Elbow
    (350, 400),  # 5. Right Elbow
    (240, 430),  # 6. Left Hand
    (360, 430),  # 7. Right Hand
    (300, 400),  # 8. Torso (upper body mid)
    (280, 450),  # 9. Left Hip
    (320, 450),  # 10. Right Hip
    (280, 500),  # 11. Left Knee
    (320, 500),  # 12. Right Knee
    (280, 550),  # 13. Left Foot
    (320, 550)   # 14. Right Foot
]

# The bowing motion will be applied to the upper body (points 0 to 8).
# The pivot for rotation is the hip center,
# calculated as the average of the left hip (index 9) and right hip (index 10).
def get_pivot():
    x9, y9 = points[9]
    x10, y10 = points[10]
    pivot_x = (x9 + x10) / 2
    pivot_y = (y9 + y10) / 2
    return (pivot_x, pivot_y)

# Function to rotate a point (x, y) around a pivot (cx, cy) by angle radians.
def rotate_point(point, pivot, angle):
    px, py = point
    cx, cy = pivot
    # Translate point back to origin:
    translated_x = px - cx
    translated_y = py - cy
    # Apply rotation:
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    rotated_x = translated_x * cos_a - translated_y * sin_a
    rotated_y = translated_x * sin_a + translated_y * cos_a
    # Translate back to pivot:
    new_x = rotated_x + cx
    new_y = rotated_y + cy
    return (new_x, new_y)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion: Happy Man Bowing")

    clock = pygame.time.Clock()

    # Define animation parameters.
    max_angle = math.radians(45)  # maximum bow angle in radians (45 degrees)
    frequency = 1.0               # oscillation frequency in Hz (1 cycle per second)

    pivot = get_pivot()

    # We run the animation until the window is closed.
    start_time = pygame.time.get_ticks() / 1000.0  # in seconds

    running = True
    while running:
        # Event handling.
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        # Clear the screen with black.
        screen.fill(BLACK)

        # Calculate elapsed time.
        t = pygame.time.get_ticks() / 1000.0 - start_time

        # Use a sine wave function for smooth periodic motion.
        # The angle oscillates between 0 (upright) and max_angle (bowed) and back.
        # Adjust the sine so that the motion is one full period (upright -> bowed -> upright).
        angle = max_angle * math.sin(2 * math.pi * frequency * t)

        # Prepare a list to hold current positions for all 15 points.
        current_positions = []

        # Apply rotation to the upper body points (indices 0 to 8).
        for i in range(9):
            new_pos = rotate_point(points[i], pivot, angle)
            current_positions.append(new_pos)
        # Lower body remains unchanged (indices 9 to 14).
        for i in range(9, 15):
            current_positions.append(points[i])

        # Draw each point as a white circle.
        point_radius = 5
        for pos in current_positions:
            # Rounding the coordinates to integers for drawing.
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), point_radius)

        pygame.display.flip()

        # Limit the animation to 60 frames per second.
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()