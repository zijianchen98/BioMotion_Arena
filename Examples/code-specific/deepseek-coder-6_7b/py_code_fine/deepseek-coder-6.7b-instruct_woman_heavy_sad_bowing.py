
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a list to hold the light objects
lights = []

# Create the light objects
for i in range(NUM_LIGHTS):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    light = pygame.rect.Rect(x, y, 10, 10)
    lights.append(light)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Update and draw the lights
    for light in lights:
        light.move_ip(random.randint(-5, 5), random.randint(-5, 5))
        pygame.draw.rect(screen, WHITE, light)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
