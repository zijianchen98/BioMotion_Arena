
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

# Set up the light position and speed
light_x, light_y = 0, HEIGHT // 2
speed = 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the light
    pygame.gfxdraw.pixel(screen, light_x, light_y, WHITE)

    # Update the light position
    light_x += speed

    # If the light reaches the right edge, start moving left
    if light_x > WIDTH:
        light_x = 0

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
