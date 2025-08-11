
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Lying Down Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
NUM_LIGHTS = 15
lights = []

# Sad man's body parts positions (simplified)
body_parts = {
    "head": [WIDTH // 2, HEIGHT // 4],
    "torso": [WIDTH // 2, HEIGHT // 2],
    "left_arm": [WIDTH // 2 - 50, HEIGHT // 2 + 30],
    "right_arm": [WIDTH // 2 + 50, HEIGHT // 2 + 30],
    "left_leg": [WIDTH // 2 - 30, HEIGHT // 2 + 80],
    "right_leg": [WIDTH // 2 + 30, HEIGHT // 2 + 80]
}

# Distribute lights on the body parts
for i in range(NUM_LIGHTS):
    part = list(body_parts.values())[i % len(body_parts)]
    lights.append([part[0] + (math.sin(i * 2 * math.pi / NUM_LIGHTS) * 20), part[1] + (math.cos(i * 2 * math.pi / NUM_LIGHTS) * 20)])

# Animation loop
clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill(BLACK)

    # Update light positions
    for i, light in enumerate(lights):
        part = list(body_parts.values())[i % len(body_parts)]
        angle += 0.01
        light[0] = part[0] + (math.sin((i + angle) * 2 * math.pi / NUM_LIGHTS) * 20)
        light[1] = part[1] + (math.cos((i + angle) * 2 * math.pi / NUM_LIGHTS) * 20)

    # Draw lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light[0]), int(light[1])), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
