
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Bowing Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Center coordinates
center_x, center_y = width // 2, height // 2

# Define point-light parameters
points = [
    # Head
    {'base_x': 0, 'base_y': -120, 'amp_x': 15, 'amp_y': 60, 'freq': 0.8, 'phase': 0},
    # Shoulders
    {'base_x': -40, 'base_y': -90, 'amp_x': 12, 'amp_y': 50, 'freq': 0.8, 'phase': 0.1},
    {'base_x': 40, 'base_y': -90, 'amp_x': 12, 'amp_y': 50, 'freq': 0.8, 'phase': 0.1},
    # Elbows
    {'base_x': -70, 'base_y': -60, 'amp_x': -18, 'amp_y': 40, 'freq': 0.8, 'phase': 0.2},
    {'base_x': 70, 'base_y': -60, 'amp_x': -18, 'amp_y': 40, 'freq': 0.8, 'phase': 0.2},
    # Hands
    {'base_x': -90, 'base_y': -30, 'amp_x': -25, 'amp_y': 30, 'freq': 0.8, 'phase': 0.3},
    {'base_x': 90, 'base_y': -30, 'amp_x': -25, 'amp_y': 30, 'freq': 0.8, 'phase': 0.3},
    # Hips
    {'base_x': -25, 'base_y': 0, 'amp_x': 5, 'amp_y': 20, 'freq': 0.8, 'phase': 0.4},
    {'base_x': 25, 'base_y': 0, 'amp_x': 5, 'amp_y': 20, 'freq': 0.8, 'phase': 0.4},
    # Knees
    {'base_x': -20, 'base_y': 50, 'amp_x': 3, 'amp_y': 10, 'freq': 0.8, 'phase': 0.5},
    {'base_x': 20, 'base_y': 50, 'amp_x': 3, 'amp_y': 10, 'freq': 0.8, 'phase': 0.5},
    # Feet
    {'base_x': -30, 'base_y': 100, 'amp_x': 0, 'amp_y': 5, 'freq': 0.8, 'phase': 0.6},
    {'base_x': 30, 'base_y': 100, 'amp_x': 0, 'amp_y': 5, 'freq': 0.8, 'phase': 0.6},
    # Torso
    {'base_x': 0, 'base_y': -60, 'amp_x': 10, 'amp_y': 40, 'freq': 0.8, 'phase': 0},
    # Lower back
    {'base_x': 0, 'base_y': -20, 'amp_x': 8, 'amp_y': 25, 'freq': 0.8, 'phase': 0.2}
]

# Main animation loop
clock = pygame.time.Clock()
t = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    
    # Update and draw points
    for point in points:
        x = center_x + point['base_x'] + point['amp_x'] * math.sin(point['freq'] * t + point['phase'])
        y = center_y + point['base_y'] + point['amp_y'] * math.sin(point['freq'] * t + point['phase'])
        pygame.draw.circle(screen, white, (int(x), int(y)), 6)
    
    pygame.display.flip()
    clock.tick(30)
    t += 0.04

pygame.quit()
sys.exit()
