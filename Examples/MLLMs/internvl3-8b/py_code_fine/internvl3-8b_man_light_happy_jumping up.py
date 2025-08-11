
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jumping Points Animation")

# Load the background (or use a black surface directly)
background = pygame.Surface((width, height))
background.fill(pygame.Color(0, 0, 0))
screen.blit(background, (0, 0))

# Define point-light positions
point_lights = [
    (200, 200),
    (300, 300),
    (400, 400),
    # Add coordinates of all 15 points here following the pattern in the example image
]

# Set up the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(pygame.Color(0, 0, 0))

    # Draw points
    for (x, y) in point_lights:
        # Draw point
        pygame.draw.circle(screen, pygame.Color(255, 255, 255, 255), (x, y), 5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
