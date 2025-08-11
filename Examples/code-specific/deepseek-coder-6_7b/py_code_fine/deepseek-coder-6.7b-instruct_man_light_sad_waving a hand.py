
import pygame
import pygame.gfxdraw

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a list to hold the point lights
point_lights = []

# Create the point lights
for i in range(15):
    x = WIDTH // 2
    y = HEIGHT // 2
    point_lights.append([x, y])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the point lights
    for light in point_lights:
        pygame.gfxdraw.pixel(screen, light[0], light[1], WHITE)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
