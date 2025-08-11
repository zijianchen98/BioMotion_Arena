
import pygame
import pygame.gfxdraw

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
lights = [(WIDTH // 2, HEIGHT // 2, LIGHT_RADIUS) for _ in range(15)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the lights
    for light in lights:
        pygame.gfxdraw.filled_circle(screen, *light, LIGHT_COLOR)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
