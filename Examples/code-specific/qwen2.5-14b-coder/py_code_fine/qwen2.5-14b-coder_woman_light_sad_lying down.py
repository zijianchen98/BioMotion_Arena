
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Lying Down Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of lights
NUM_LIGHTS = 15

# Light properties
lights = []
for i in range(NUM_LIGHTS):
    x = WIDTH // 2 + 100 * math.cos(2 * math.pi * i / NUM_LIGHTS)
    y = HEIGHT // 2 + 100 * math.sin(2 * math.pi * i / NUM_LIGHTS)
    lights.append([x, y])

# Animation parameters
angle = 0
angle_speed = 0.02

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update light positions
    angle += angle_speed
    for i in range(NUM_LIGHTS):
        lights[i][0] = WIDTH // 2 + 100 * math.cos(2 * math.pi * (i + angle) / NUM_LIGHTS)
        lights[i][1] = HEIGHT // 2 + 100 * math.sin(2 * math.pi * (i + angle) / NUM_LIGHTS)

    # Draw background
    screen.fill(BLACK)

    # Draw lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light[0]), int(light[1])), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
