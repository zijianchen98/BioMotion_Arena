
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Turning Around")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Sad man properties
NUM_LIGHTS = 15
RADIUS = 10
SPEED = 0.5  # Speed of rotation

# Function to calculate the position of each light
def get_light_positions(angle):
    positions = []
    for i in range(NUM_LIGHTS):
        theta = (2 * math.pi / NUM_LIGHTS) * i + angle
        x = WIDTH // 2 + (WIDTH // 4) * math.cos(theta)
        y = HEIGHT // 2 + (HEIGHT // 4) * math.sin(theta)
        positions.append((x, y))
    return positions

# Main loop
angle = 0
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update and draw lights
    positions = get_light_positions(angle)
    for pos in positions:
        pygame.draw.circle(screen, WHITE, pos, RADIUS)

    # Update angle for rotation
    angle += SPEED
    if angle >= 2 * math.pi:
        angle -= 2 * math.pi

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
