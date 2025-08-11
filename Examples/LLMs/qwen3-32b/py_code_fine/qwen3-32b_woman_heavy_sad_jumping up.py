
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Jumping with Heavy Weight - Biological Motion")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Joint positions (simplified 2D skeleton for a sad woman jumping with heavy weight)
# We'll model the body with 15 joints (point-lights)
# Each joint is a list of [x, y, vx, vy, phase]
# We'll use sine functions to simulate jumping and sagging motion with heavy weight

# Initial joint positions and motion parameters
joints = [
    # Head
    [WIDTH // 2, HEIGHT // 2 - 100, 0, 0, 0],
    # Shoulders
    [WIDTH // 2 - 40, HEIGHT // 2 - 60, 0, 0, 0],
    [WIDTH // 2 + 40, HEIGHT // 2 - 60, 0, 0, 0],
    # Elbows
    [WIDTH // 2 - 60, HEIGHT // 2, 0, 0, 0],
    [WIDTH // 2 + 60, HEIGHT // 2, 0, 0, 0],
    # Hands
    [WIDTH // 2 - 80, HEIGHT // 2 + 40, 0, 0, 0],
    [WIDTH // 2 + 80, HEIGHT // 2 + 40, 0, 0, 0],
    # Torso (upper)
    [WIDTH // 2, HEIGHT // 2 - 60, 0, 0, 0],
    # Torso (lower)
    [WIDTH // 2, HEIGHT // 2, 0, 0, 0],
    # Hips
    [WIDTH // 2 - 30, HEIGHT // 2 + 60, 0, 0, 0],
    [WIDTH // 2 + 30, HEIGHT // 2 + 60, 0, 0, 0],
    # Knees
    [WIDTH // 2 - 40, HEIGHT // 2 + 100, 0, 0, 0],
    [WIDTH // 2 + 40, HEIGHT // 2 + 100, 0, 0, 0],
    # Ankles
    [WIDTH // 2 - 50, HEIGHT // 2 + 140, 0, 0, 0],
    [WIDTH // 2 + 50, HEIGHT // 2 + 140, 0, 0, 0],
]

# Jumping motion parameters
jump_freq = 0.05
jump_amp = 20
gravity = 0.5
bounce_phase = 0

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update joint positions based on a jumping motion with sagging
    bounce_phase += 0.05

    for i, (x, y, vx, vy, phase) in enumerate(joints):
        # Base position
        base_x = x
        base_y = y

        # Jumping motion
        jump_y = jump_amp * math.sin(jump_freq * bounce_phase * (i % 3 + 1))
        sag_factor = 1.0 + 0.1 * i  # More sag for lower joints to simulate heavy weight

        # Apply sag and jump
        new_y = base_y - jump_y * sag_factor

        # Update joint
        joints[i] = [base_x, new_y, vx, vy, phase]

        # Draw the point-light
        pygame.draw.circle(screen, WHITE, (int(base_x), int(new_y)), 4)

    pygame.display.flip()

pygame.quit()
sys.exit()
