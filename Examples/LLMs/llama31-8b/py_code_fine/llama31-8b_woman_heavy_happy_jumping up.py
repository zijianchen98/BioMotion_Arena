
import pygame
import math
import numpy as np

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Number of point lights
NUM_LIGHTS = 15

# Point light positions and velocities
lights = np.zeros((NUM_LIGHTS, 2))
velocities = np.zeros((NUM_LIGHTS, 2))

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define a function to update the point light positions
def update_positions():
    global lights, velocities

    # Update the position of each point light
    for i in range(NUM_LIGHTS):
        # Calculate the new position based on the velocity
        lights[i] += velocities[i]

        # Ensure the point light stays within the window
        if lights[i, 0] < 0 or lights[i, 0] > WIDTH:
            velocities[i, 0] *= -1
        if lights[i, 1] < 0 or lights[i, 1] > HEIGHT:
            velocities[i, 1] *= -1

# Define a function to draw the point lights
def draw_lights():
    screen.fill(BLACK)
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light[0]), int(light[1])), 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the point light positions
    update_positions()

    # Draw the point lights
    draw_lights()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
