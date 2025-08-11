
import numpy as np
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Bowing Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Number of point-lights
NUM_LIGHTS = 15

# Define body parts and their positions (approximate for a human figure)
body_parts = {
    'head': (WIDTH // 2, HEIGHT // 2 - 100),
    'torso': (WIDTH // 2, HEIGHT // 2),
    'left_upper_arm': (WIDTH // 2 - 80, HEIGHT // 2),
    'left_lower_arm': (WIDTH // 2 - 120, HEIGHT // 2 + 50),
    'right_upper_arm': (WIDTH // 2 + 80, HEIGHT // 2),
    'right_lower_arm': (WIDTH // 2 + 120, HEIGHT // 2 + 50),
    'left_upper_leg': (WIDTH // 2 - 40, HEIGHT // 2 + 150),
    'left_lower_leg': (WIDTH // 2 - 80, HEIGHT // 2 + 200),
    'right_upper_leg': (WIDTH // 2 + 40, HEIGHT // 2 + 150),
    'right_lower_leg': (WIDTH // 2 + 80, HEIGHT // 2 + 200),
    'left_hand': (WIDTH // 2 - 140, HEIGHT // 2 + 70),
    'right_hand': (WIDTH // 2 + 140, HEIGHT // 2 + 70),
    'left_foot': (WIDTH // 2 - 100, HEIGHT // 2 + 250),
    'right_foot': (WIDTH // 2 + 100, HEIGHT // 2 + 250),
    'neck': (WIDTH // 2, HEIGHT // 2 - 80)
}

# Assign point-lights to body parts
point_lights = []
for part in body_parts:
    point_lights.append({
        'pos': np.array(body_parts[part]),
        'vel': np.array([0, 0]),
        'radius': 5,
        'color': WHITE
    })

# Time variables for animation
time = 0
duration = 10  # seconds for one full bow cycle

# Animation parameters
amplitude = 30
frequency = 0.05
phase_shift = 0
damping = 0.99

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    time += 1 / FPS

    for light in point_lights:
        # Apply sine wave motion for bowing
        if light['pos'][1] < HEIGHT // 2 + 100:
            light['pos'][1] += amplitude * math.sin(frequency * time + phase_shift)
        else:
            light['pos'][1] = HEIGHT // 2 + 100

        # Apply damping to simulate realistic motion
        light['pos'][1] *= damping

        # Draw the light
        pygame.draw.circle(screen, light['color'], (int(light['pos'][0]), int(light['pos'][1])), light['radius'])

    # Reset position if it goes too far
    for light in point_lights:
        if light['pos'][1] < HEIGHT // 2 - 100:
            light['pos'][1] = HEIGHT // 2 - 100

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
