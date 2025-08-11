
import numpy as np
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Waving Hand")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Number of points
NUM_POINTS = 15

# Initial positions of the points (simplified skeleton for waving hand)
# These positions are relative to a central point
base_positions = np.array([
    [0, 0],  # center of hand
    [-20, -10],
    [20, -10],
    [0, -20],
    [-10, -5],
    [10, -5],
    [-5, 0],
    [5, 0],
    [-15, 10],
    [15, 10],
    [0, 15],
    [-25, -15],
    [25, -15],
    [-10, 15],
    [10, 15],
], dtype=float)

# Initial center position
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Waving parameters
wave_angle = 0
wave_speed = 0.05

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update wave angle
    wave_angle += wave_speed

    # Calculate waving motion (sinusoidal for arm movement)
    arm_angle = math.sin(wave_angle) * 0.5

    # Apply waving motion to some points (simulate arm/hand movement)
    waved_positions = base_positions.copy()
    for i in range(NUM_POINTS):
        if i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
            # Apply rotation to simulate waving
            dx = waved_positions[i, 0] - base_positions[0, 0]
            dy = waved_positions[i, 1] - base_positions[0, 1]
            angle = math.atan2(dy, dx) + arm_angle
            distance = math.hypot(dx, dy)
            waved_positions[i, 0] = base_positions[0, 0] + distance * math.cos(angle)
            waved_positions[i, 1] = base_positions[0, 1] + distance * math.sin(angle)

    # Draw the points
    for x, y in waved_positions:
        px = int(center_x + x)
        py = int(center_y + y)
        pygame.draw.circle(screen, WHITE, (px, py), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
