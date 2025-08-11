
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
lights = [pygame.Rect(0, HEIGHT // 2, LIGHT_RADIUS, LIGHT_RADIUS) for _ in range(15)]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Move and draw the lights
    for light in lights:
        light.move_ip(1, 0)
        if light.right > WIDTH:
            light.left = 0
        pygame.draw.rect(screen, LIGHT_COLOR, light)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(100)
