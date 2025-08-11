
import pygame
import sys
import math
import numpy as np

# Configuration
WIDTH, HEIGHT = 800, 600
FPS = 30
LIGHT_RADIUS = 3
NUM_FRAMES = 60  # One full cycle of turning around

# Biological motion points (simplified model of a human turning around)
# We'll define joint positions relative to a central body and rotate them
JOINTS = [
    (0, -100),  # Head
    (0, -50),   # Torso top
    (0, 0),     # Torso center
    (0, 50),    # Torso bottom
    (-20, 20),  # Left shoulder
    (20, 20),   # Right shoulder
    (-20, 60),  # Left elbow
    (20, 60),   # Right elbow
    (-20, 90),  # Left hand
    (20, 90),   # Right hand
    (-20, -20), # Left hip
    (20, -20),  # Right hip
    (-20, -50), # Left knee
    (20, -50),  # Right knee
    (-20, -80), # Left foot
    (20, -80),  # Right foot
]

JOINTS = np.array(JOINTS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Man Turning Around")
clock = pygame.time.Clock()

# Main loop
frame = 0
running = True

while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))  # Black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate rotation angle based on frame
    angle = (2 * math.pi / NUM_FRAMES) * frame
    frame = (frame + 1) % NUM_FRAMES

    # Rotate the body around the center
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    rotated_joints = np.zeros_like(JOINTS)
    for i, (x, y) in enumerate(JOINTS):
        # Rotate around the center
        rx = x * math.cos(angle) - y * math.sin(angle)
        ry = x * math.sin(angle) + y * math.cos(angle)
        rotated_joints[i] = [rx + center_x, ry + center_y]

    # Draw the point lights
    for (x, y) in rotated_joints:
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), LIGHT_RADIUS)

    pygame.display.flip()

pygame.quit()
sys.exit()
