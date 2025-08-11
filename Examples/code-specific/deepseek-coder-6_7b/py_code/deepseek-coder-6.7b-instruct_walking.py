
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the lights
lights = []
for i in range(15):
    x = i * (WIDTH // 15)
    lights.append(pygame.Rect(x, HEIGHT // 2, LIGHT_RADIUS, LIGHT_RADIUS))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the lights
    for light in lights:
        pygame.draw.rect(screen, LIGHT_COLOR, light)

    # Move the lights
    for i in range(len(lights)):
        light = lights[i]
        if i % 2 == 0:
            light.x += 1
            if light.x > WIDTH:
                light.x = 0
        else:
            light.x -= 1
            if light.x < 0:
                light.x = WIDTH

    # Update the display
    pygame.display.flip()
