
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Number of point lights
NUM_LIGHTS = 15

# Point light properties
lights = []
for i in range(NUM_LIGHTS):
    angle = 2 * math.pi * i / NUM_LIGHTS
    radius = 200
    x = SCREEN_WIDTH // 2 + radius * math.cos(angle)
    y = SCREEN_HEIGHT // 2 + radius * math.sin(angle)
    lights.append((x, y))

# Animation parameters
clock = pygame.time.Clock()
FPS = 60
angle_offset = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update point light positions
    for i in range(NUM_LIGHTS):
        angle = 2 * math.pi * i / NUM_LIGHTS + angle_offset
        radius = 200
        x = SCREEN_WIDTH // 2 + radius * math.cos(angle)
        y = SCREEN_HEIGHT // 2 + radius * math.sin(angle)
        lights[i] = (x, y)

    # Draw point lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, light, 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    # Increment angle offset for smooth motion
    angle_offset += 0.01

# Quit Pygame
pygame.quit()
