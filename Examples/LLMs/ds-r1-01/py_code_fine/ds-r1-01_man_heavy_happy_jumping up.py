
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define 15 points with base positions and movement parameters
points = [
    # Head
    {'base_x': 0, 'base_y': -50, 'amp_x': 0, 'amp_y': 0, 'phase_x': 0, 'phase_y': 0},
    # Left shoulder
    {'base_x': -20, 'base_y': -40, 'amp_x': -5, 'amp_y': 0, 'phase_x': 0, 'phase_y': 0},
    # Right shoulder
    {'base_x': 20, 'base_y': -40, 'amp_x': 5, 'amp_y': 0, 'phase_x': 0, 'phase_y': 0},
    # Left elbow
    {'base_x': -30, 'base_y': -30, 'amp_x': -10, 'amp_y': 0, 'phase_x': 0, 'phase_y': 0},
    # Right elbow
    {'base_x': 30, 'base_y': -30, 'amp_x': 10, 'amp_y': 0, 'phase_x': 0, 'phase_y': 0},
    # Left hand
    {'base_x': -40, 'base_y': -20, 'amp_x': -15, 'amp_y': 5, 'phase_x': 0, 'phase_y': 0},
    # Right hand
    {'base_x': 40, 'base_y': -20, 'amp_x': 15, 'amp_y': 5, 'phase_x': 0, 'phase_y': 0},
    # Left hip
    {'base_x': -15, 'base_y': 0, 'amp_x': -5, 'amp_y': 0, 'phase_x': 0, 'phase_y': 0},
    # Right hip
    {'base_x': 15, 'base_y': 0, 'amp_x': 5, 'amp_y': 0, 'phase_x': 0, 'phase_y': 0},
    # Left knee
    {'base_x': -20, 'base_y': 20, 'amp_x': -5, 'amp_y': -10, 'phase_x': 0, 'phase_y': 0},
    # Right knee
    {'base_x': 20, 'base_y': 20, 'amp_x': 5, 'amp_y': -10, 'phase_x': 0, 'phase_y': 0},
    # Left foot
    {'base_x': -25, 'base_y': 40, 'amp_x': -5, 'amp_y': 10, 'phase_x': 0, 'phase_y': 0},
    # Right foot
    {'base_x': 25, 'base_y': 40, 'amp_x': 5, 'amp_y': 10, 'phase_x': 0, 'phase_y': 0},
    # Torso center
    {'base_x': 0, 'base_y': -25, 'amp_x': 0, 'amp_y': 0, 'phase_x': 0, 'phase_y': 0},
    # Mid-back
    {'base_x': 0, 'base_y': 10, 'amp_x': 0, 'amp_y': 0, 'phase_x': 0, 'phase_y': 0},
]

# Animation parameters
time = 0
speed = 0.05
amplitude = 30  # Jump height

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate torso position (centered horizontally)
    x_torso = width // 2
    y_torso = height // 2 + amplitude * (1 - math.cos(time))

    # Update and draw each point
    for point in points:
        dx = point['amp_x'] * math.sin(time + point['phase_x'])
        dy = point['amp_y'] * math.sin(time + point['phase_y'])
        x = x_torso + point['base_x'] + dx
        y = y_torso + point['base_y'] + dy
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)
    time += speed

pygame.quit()
sys.exit()
