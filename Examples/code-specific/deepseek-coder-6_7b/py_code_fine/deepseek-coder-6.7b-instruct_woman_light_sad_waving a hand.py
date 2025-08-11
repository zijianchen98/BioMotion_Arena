
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
NUM_LIGHTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the light class
class Light:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 5)

# Create the lights
lights = [Light(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_LIGHTS)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the lights
    for light in lights:
        light.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
