
import pygame
import numpy as np
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Animation - Bowing Woman")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of point-lights
NUM_LIGHTS = 15

# Bowing parameters
MAX_BOW_HEIGHT = 100  # Maximum bowing angle in degrees
BOWING_PERIOD = 10  # Period of bowing in seconds
BOWING_SPEED = 2  # Speed of bowing in Hz

# Initialize point-lights
lights = []
center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
radius = 150  # Radius of movement around the center

for i in range(NUM_LIGHTS):
    angle = 2 * np.pi * i / NUM_LIGHTS
    lights.append({
        'pos': np.array([center_x + radius * np.cos(angle), center_y + radius * np.sin(angle)]),
        'offset': np.array([0.0, 0.0])
    })

# Main loop
clock = pygame.time.Clock()
running = True
start_time = pygame.time.get_ticks() / 1000.0  # Convert to seconds

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Get current time
    current_time = pygame.time.get_ticks() / 1000.0  # Convert to seconds

    # Calculate bowing angle
    bowing_angle = MAX_BOW_HEIGHT * np.sin(2 * np.pi * BOWING_SPEED * (current_time - start_time))

    # Update point-lights positions
    for light in lights:
        angle = 2 * np.pi * lights.index(light) / NUM_LIGHTS
        light['pos'] = np.array([center_x + radius * np.cos(angle), center_y + radius * np.sin(angle)])

        # Vertical offset based on bowing angle
        if angle <= np.pi:  # Upper half of the circle
            light['offset'] = np.array([0, bowing_angle * np.sin(angle)])
        else:  # Lower half of the circle
            light['offset'] = np.array([0, -bowing_angle * np.sin(angle)])

        # Draw point-light
        pygame.draw.circle(screen, WHITE, light['pos'] + light['offset'], 3)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
