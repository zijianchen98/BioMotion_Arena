
import pygame
import sys
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
NUM_POINTS = 15
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion")
clock = pygame.time.Clock()

# Point properties
points = []
trail_length = 5

for i in range(NUM_POINTS):
    angle = 2 * math.pi * i / NUM_POINTS
    x = SCREEN_WIDTH // 2 + 100 * math.sin(angle)
    y = SCREEN_HEIGHT // 2 + 100 * math.cos(angle)
    points.append((x, y))

def wave_hand(points, t):
    new_points = []
    for i, (x, y) in enumerate(points):
        angle = 2 * math.pi * i / NUM_POINTS
        x += 30 * math.sin(angle + t)
        y += 30 * math.cos(angle + t)
        new_points.append((x, y))
    return new_points

# Animation loop
t = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    t += 0.1
    animated_points = wave_hand(points, t)
    for point in animated_points:
        pygame.draw.circle(screen, WHITE, point, 3)

    pygame.display.flip()
    clock.tick(FPS)
