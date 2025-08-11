
import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point Light Animation")

# Set up the clock
clock = pygame.time.Clock()

# Define the number of point lights
num_lights = 15

# Create a list to store the positions of the point lights
lights = [(random.randint(0, screen_width), random.randint(0, screen_height)) for _ in range(num_lights)]

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position of each point light
    for i, light in enumerate(lights):
        new_x = light[0] + random.randint(-1, 1)
        new_y = light[1] + random.randint(-1, 1)
        lights[i] = (new_x, new_y)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the point lights
    for light in lights:
        pygame.draw.circle(screen, (255, 255, 255), light, 2)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
