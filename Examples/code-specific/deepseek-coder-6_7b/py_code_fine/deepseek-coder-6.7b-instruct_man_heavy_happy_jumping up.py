
import pygame
import pygame.gfxdraw

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the point lights
point_lights = [(WIDTH // 2, HEIGHT // 2) for _ in range(15)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the point lights
    for x, y in point_lights:
        pygame.gfxdraw.pixel(screen, x, y, WHITE)

    # Move the point lights
    for i, (x, y) in enumerate(point_lights):
        if i % 2 == 0:
            y -= 1
        else:
            y += 1
        point_lights[i] = (x, y)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
