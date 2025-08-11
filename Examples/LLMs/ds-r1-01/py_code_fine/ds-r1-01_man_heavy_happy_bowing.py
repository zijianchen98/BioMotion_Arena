
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Bowing")
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define point parameters for a bowing motion
points = [
    # Head
    {'x0': 400, 'y0': 150, 'amp_x': 25, 'amp_y': 40, 'phase': 0},
    # Shoulders
    {'x0': 350, 'y0': 200, 'amp_x': 20, 'amp_y': 30, 'phase': 0.2},
    {'x0': 450, 'y0': 200, 'amp_x': 20, 'amp_y': 30, 'phase': 0.2},
    # Elbows
    {'x0': 330, 'y0': 250, 'amp_x': 15, 'amp_y': 25, 'phase': 0.4},
    {'x0': 470, 'y0': 250, 'amp_x': 15, 'amp_y': 25, 'phase': 0.4},
    # Hands
    {'x0': 310, 'y0': 300, 'amp_x': -25, 'amp_y': 15, 'phase': 0.6},
    {'x0': 490, 'y0': 300, 'amp_x': -25, 'amp_y': 15, 'phase': 0.6},
    # Torso (upper, mid, lower)
    {'x0': 400, 'y0': 250, 'amp_x': 0, 'amp_y': 35, 'phase': 0.1},
    {'x0': 400, 'y0': 300, 'amp_x': 0, 'amp_y': 25, 'phase': 0.2},
    {'x0': 400, 'y0': 350, 'amp_x': 0, 'amp_y': 15, 'phase': 0.3},
    # Hips
    {'x0': 370, 'y0': 400, 'amp_x': -15, 'amp_y': 10, 'phase': 0.4},
    {'x0': 430, 'y0': 400, 'amp_x': -15, 'amp_y': 10, 'phase': 0.4},
    # Knees
    {'x0': 360, 'y0': 450, 'amp_x': -20, 'amp_y': 5, 'phase': 0.5},
    {'x0': 440, 'y0': 450, 'amp_x': -20, 'amp_y': 5, 'phase': 0.5},
    # Feet
    {'x0': 350, 'y0': 500, 'amp_x': -25, 'amp_y': 0, 'phase': 0.7},
    {'x0': 450, 'y0': 500, 'amp_x': -25, 'amp_y': 0, 'phase': 0.7},
]

# Ensure exactly 15 points
points = points[:15]

# Animation parameters
t = 0
dt = 0.04  # Controls animation speed

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update time
    t += dt
    t %= 2 * math.pi  # Keep t within [0, 2π)

    # Draw all points
    for point in points:
        x = point['x0'] + point['amp_x'] * math.sin(t + point['phase'])
        y = point['y0'] + point['amp_y'] * math.sin(t + point['phase'])
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 3)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
sys.exit()
