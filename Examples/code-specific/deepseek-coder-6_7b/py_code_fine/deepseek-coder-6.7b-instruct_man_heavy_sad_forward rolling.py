
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Set up the point light
light_pos = [0, HEIGHT // 2]
light_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Move the point light
    light_pos[0] += light_speed

    # Draw the point light
    pygame.draw.circle(screen, (255, 255, 255), light_pos, 10)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
