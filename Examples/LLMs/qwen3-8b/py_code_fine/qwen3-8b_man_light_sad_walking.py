
import numpy as np
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define the skeleton points for a human figure (simplified)
skeleton_points = [
    (400, 300),   # Hip
    (300, 200),   # Left knee
    (200, 250),   # Left ankle
    (300, 350),   # Left foot
    (500, 200),   # Right knee
    (600, 250),   # Right ankle
    (500, 350),   # Right foot
    (400, 300),   # Hip
    (350, 200),   # Spine
    (350, 100),   # Head
    (320, 150),   # Left shoulder
    (280, 180),   # Left elbow
    (250, 200),   # Left wrist
    (380, 150),   # Right shoulder
    (420, 180),   # Right elbow
    (450, 200),   # Right wrist
    (350, 200),   # Spine
    (350, 250),   # Pelvis
    (350, 300),   # Spine
    (350, 350),   # Spine
    (350, 400),   # Spine
    (350, 450),   # Spine
    (350, 500),   # Spine
    (350, 550),   # Spine
]

# Define the point-light positions (indices from skeleton_points)
point_light_indices = [0, 2, 3, 5, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19]

# Initialize point light positions
point_lights = [pygame.Vector2(skeleton_points[i]) for i in point_light_indices]

# Animation parameters
speed = 0.05
angle = 0
rotation_speed = 0.01
scale = 1.0
scale_speed = 0.001

# Main loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation
    angle += rotation_speed
    scale += scale_speed

    # Apply rotation and scaling to skeleton points
    for i in range(len(skeleton_points)):
        x, y = skeleton_points[i]
        x = x * scale
        y = y * scale
        x_rot = x * math.cos(angle) - y * math.sin(angle)
        y_rot = x * math.sin(angle) + y * math.cos(angle)
        skeleton_points[i] = (x_rot + 400, y_rot + 300)

    # Update point light positions
    for i in range(len(point_lights)):
        x, y = point_lights[i]
        x = x * scale
        y = y * scale
        x_rot = x * math.cos(angle) - y * math.sin(angle)
        y_rot = x * math.sin(angle) + y * math.cos(angle)
        point_lights[i] = (x_rot + 400, y_rot + 300)

    # Clear screen
    screen.fill(BLACK)

    # Draw point lights
    for x, y in point_lights:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
