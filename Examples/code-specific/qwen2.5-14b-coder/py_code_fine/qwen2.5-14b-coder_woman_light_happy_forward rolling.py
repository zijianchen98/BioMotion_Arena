
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_SPEED = 2

# Initial positions of point-lights
lights = []
for i in range(NUM_LIGHTS):
    angle = 2 * math.pi * i / NUM_LIGHTS
    x = WIDTH // 2 + 100 * math.cos(angle)
    y = HEIGHT // 2 + 100 * math.sin(angle)
    lights.append((x, y))

# Animation loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update positions
    for i in range(NUM_LIGHTS):
        angle = 2 * math.pi * i / NUM_LIGHTS
        x = WIDTH // 2 + 100 * math.cos(angle) + math.sin(pygame.time.get_ticks() / 1000) * LIGHT_SPEED
        y = HEIGHT // 2 + 100 * math.sin(angle) + math.cos(pygame.time.get_ticks() / 1000) * LIGHT_SPEED
        lights[i] = (x, y)

    # Draw background
    screen.fill(BLACK)

    # Draw point-lights
    for x, y in lights:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), LIGHT_RADIUS)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
