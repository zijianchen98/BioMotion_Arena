
import pygame
import math
import sys
import time

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Turning Happy Man")
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Joint positions relative to a centered body
# We will animate a 15-point-light stick figure representing a man turning around

# Define the body parts and their relative positions (simplified)
# The body will be centered at (WIDTH // 2, HEIGHT // 2)
# The positions are relative to the center of the body

# Each point is a tuple (x_offset, y_offset, label)
points = [
    (0, -100, "head"),
    (-20, -60, "left_ear"),
    (20, -60, "right_ear"),
    (-30, -30, "left_shoulder"),
    (30, -30, "right_shoulder"),
    (-20, 0, "left_elbow"),
    (20, 0, "right_elbow"),
    (-10, 10, "left_hand"),
    (10, 10, "right_hand"),
    (0, 30, "torso"),
    (-20, 60, "left_hip"),
    (20, 60, "right_hip"),
    (-10, 90, "left_knee"),
    (10, 90, "right_knee"),
    (-5, 120, "left_foot"),
    (5, 120, "right_foot"),
]

# Initial center of the body
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Animation parameters
angle = 0  # rotation angle in radians
rotation_speed = 0.02  # radians per frame
gravity = 0.1  # simulate heavy weight
bounce = 0  # simulate bounce from turning

# Store the original positions for rotation
original_positions = [(x, y) for x, y, _ in points]

# Main animation loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update angle for turning
    angle += rotation_speed

    # Compute the new positions after rotation
    rotated_points = []
    for x, y, label in points:
        # Rotate the point around the center
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        new_x = x * cos_theta - y * sin_theta
        new_y = x * sin_theta + y * cos_theta
        rotated_points.append((new_x, new_y))

    # Draw the point-light stimulus
    for dx, dy in rotated_points:
        px = center_x + dx
        py = center_y + dy + bounce
        pygame.draw.circle(screen, WHITE, (int(px), int(py)), 5)

    # Simulate heavy weight by adding a bounce effect
    bounce += gravity
    if bounce > 20:
        gravity = -0.1
    if bounce < -10:
        gravity = 0.1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
