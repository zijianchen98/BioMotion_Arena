
import pygame
import math
import sys

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Point-light Stimulus")
clock = pygame.time.Clock()

# Define 3D coordinates for a human figure (x, y, z)
points_3d = [
    # Head
    (0.0, 0.15, 0.0),
    # Shoulders
    (-0.1, 0.25, 0.05), (0.1, 0.25, -0.05),
    # Elbows
    (-0.15, 0.35, 0.1), (0.15, 0.35, -0.1),
    # Wrists
    (-0.2, 0.45, 0.15), (0.2, 0.45, -0.15),
    # Hips
    (-0.08, 0.55, -0.05), (0.08, 0.55, 0.05),
    # Knees
    (-0.1, 0.7, -0.1), (0.1, 0.7, 0.1),
    # Ankles
    (-0.12, 0.85, -0.15), (0.12, 0.85, 0.15),
    # Torso (mid-spine)
    (0.0, 0.4, 0.0),
    # Chest
    (0.0, 0.3, 0.0)
]

def project(point, theta, width, height):
    """Project 3D point to 2D screen coordinates with Y-axis rotation"""
    x, y, z = point
    # Apply rotation around Y-axis
    x_rot = x * math.cos(theta) + z * math.sin(theta)
    # Scale and translate coordinates
    screen_x = int((x_rot + 0.5) * width)
    screen_y = int((1.2 - y) * height / 1.5)  # Adjust vertical position
    return (screen_x, screen_y)

# Animation parameters
theta = 0.0
d_theta = 0.015  # Slow rotation speed for heavy movement

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Update and draw all points
    for point in points_3d:
        x, y = project(point, theta, width, height)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 8)  # White points

    pygame.display.flip()
    theta += d_theta
    clock.tick(30)  # Maintain 30 FPS for smooth animation

pygame.quit()
sys.exit()
