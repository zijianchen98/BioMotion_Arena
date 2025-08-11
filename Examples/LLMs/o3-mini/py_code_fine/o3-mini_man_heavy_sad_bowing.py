
"""
This program displays an animation of a 15-point biological motion point‐light
stimulus representing a heavy‐weight “sadman” bowing. The stimulus consists of 15 
white point-lights (representing key joints of a human body) moving on a solid 
black background. The points corresponding to the upper body (above the hip level)
rotate around the hip region to simulate a realistic, biomechanically plausible 
bowing motion.
"""

import sys
import math
import pygame

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-light Biological Motion: Bowing Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define a clock to control the animation framerate
clock = pygame.time.Clock()
FPS = 60

# Define the “model” skeleton joint positions in a coordinate system with the pivot
# (center between the hips) at the origin. Units are pixels.
# The 15 points (joints) are:
#   1. Head
#   2. Chest
#   3. Stomach
#   4. Left Shoulder
#   5. Right Shoulder
#   6. Left Elbow
#   7. Right Elbow
#   8. Left Hand
#   9. Right Hand
#   10. Left Hip
#   11. Right Hip
#   12. Left Knee
#   13. Right Knee
#   14. Left Foot
#   15. Right Foot

joints = [
    # (x, y) coordinates in model space; positive y is downward.
    (0, -200),    # Head
    (0, -150),    # Chest
    (0, -100),    # Stomach
    (-30, -150),  # Left Shoulder
    (30, -150),   # Right Shoulder
    (-50, -100),  # Left Elbow
    (50, -100),   # Right Elbow
    (-60, -50),   # Left Hand
    (60, -50),    # Right Hand
    (-20, 0),     # Left Hip
    (20, 0),      # Right Hip
    (-20, 50),    # Left Knee
    (20, 50),     # Right Knee
    (-20, 100),   # Left Foot
    (20, 100)     # Right Foot
]

# For a realistic bowing movement, we'll rotate the upper body (points above the hips).
# We consider joints with a y-coordinate less than 0 as belonging to the upper body.
def rotate_point(point, theta):
    """Rotate a 2D point (x, y) by theta radians."""
    x, y = point
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    x_new = x * cos_theta - y * sin_theta
    y_new = x * sin_theta + y * cos_theta
    return (x_new, y_new)

# Animation parameters
# Maximum forward bending angle in radians (40 degrees ≈ 0.698 rad).
max_angle = math.radians(40)
# Animation period in seconds (time to complete a full cycle of bending forward and back).
period = 4.0       # seconds
omega = 2 * math.pi / period

# Center of the model on the screen. The pivot (hip center) is placed at the center.
pivot_screen = (WIDTH // 2, HEIGHT // 2)

running = True
start_ticks = pygame.time.get_ticks()  # milliseconds

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate elapsed time in seconds
    elapsed = (pygame.time.get_ticks() - start_ticks) / 1000.0

    # Use a sine function to smoothly oscillate the angle between -max_angle and +max_angle.
    # The motion simulates a natural bow: bending forward and returning upright.
    theta = max_angle * math.sin(omega * elapsed)

    # Clear the screen to black
    screen.fill(BLACK)

    # For each joint, decide if it should rotate.
    # Points with a y-coordinate < 0 (upper body) are rotated by theta around the hip center (origin).
    for idx, point in enumerate(joints):
        x, y = point
        # Determine if this joint is part of the upper body.
        # Since the hip joint is at y==0, all joints with y < 0 will be rotated.
        if y < 0:
            x_rot, y_rot = rotate_point((x, y), theta)
        else:
            x_rot, y_rot = (x, y)
        # Convert the model coordinate (with pivot at (0,0)) to screen coordinate.
        # In Pygame, the y-axis increases downwards.
        screen_x = int(pivot_screen[0] + x_rot)
        screen_y = int(pivot_screen[1] + y_rot)
        # Draw the point-light as a small filled circle.
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), 5)

    # Update the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(FPS)

pygame.quit()
sys.exit()