
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sadman Lying Down Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Point lights
num_lights = 15
lights = [(random.randint(0, width), random.randint(0, height)) for _ in range(num_lights)]
light_radius = 5

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(black)

    # Update point lights positions
    for i, (x, y) in enumerate(lights):
        angle = i * (2 * 3.14159 / num_lights)
        radius = 200 + 50 * abs(math.sin(pygame.time.get_ticks() / 1000 + angle))
        x = width // 2 + int(radius * math.cos(angle))
        y = height // 2 - int(radius * math.sin(angle))
        lights[i] = (x, y)

    # Draw point lights
    for x, y in lights:
        pygame.draw.circle(screen, white, (x, y), light_radius)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
