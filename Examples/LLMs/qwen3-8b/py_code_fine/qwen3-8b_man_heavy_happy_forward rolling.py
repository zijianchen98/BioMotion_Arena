
import numpy as np
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Happy Man Forward Rolling")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define the 15 point-light positions based on a simplified human skeleton
# These are approximate positions for a human body during a forward roll
# Positions are relative to the center of the screen (0, 0)
body_points = [
    (0, 0),            # Center (hip)
    (40, 0),           # Right hip
    (60, 0),           # Right knee
    (80, 0),           # Right foot
    (-40, 0),          # Left hip
    (-60, 0),          # Left knee
    (-80, 0),          # Left foot
    (0, 30),           # Torso
    (20, 30),          # Right shoulder
    (40, 30),          # Right elbow
    (60, 30),          # Right hand
    (-20, 30),         # Left shoulder
    (-40, 30),         # Left elbow
    (-60, 30),         # Left hand
]

# Normalize positions to screen coordinates
body_points = [(x * 1.5, y * 1.5) for x, y in body_points]

# Animation parameters
amplitude = 50
frequency = 0.005
phase_offset = [i * 0.1 for i in range(15)]  # Different phases for each point

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update positions with sine wave motion
    for i, (x, y) in enumerate(body_points):
        angle = frequency * (i + phase_offset[i]) + pygame.time.get_ticks() * 0.001
        dx = amplitude * math.sin(angle)
        dy = amplitude * math.cos(angle)
        new_x = x + dx
        new_y = y + dy
        # Apply a slight forward roll motion by shifting the body
        new_y += 10 * math.sin(angle * 0.5)
        # Apply a slight rotation to simulate forward roll
        new_x += 20 * math.sin(angle * 0.3)
        pygame.draw.circle(screen, WHITE, (int(new_x + WIDTH / 2), int(new_y + HEIGHT / 2)), 3)

    pygame.display.flip()

pygame.quit()
sys.exit()
