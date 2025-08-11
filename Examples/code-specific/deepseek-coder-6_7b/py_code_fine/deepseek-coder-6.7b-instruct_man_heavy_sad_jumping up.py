
import pygame
import sys

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
    x = i * (WIDTH // 15)
    point_lights.append(pygame.Rect(x, HEIGHT // 2, 10, 10))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the point lights
    for light in point_lights:
        pygame.draw.rect(screen, WHITE, light)

    # Update the display
    pygame.display.flip()

    # Move the point lights
    for light in point_lights:
        light.move_ip(1, 0)
        if light.right > WIDTH:
            light.left = 0
