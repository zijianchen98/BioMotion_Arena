
import pygame
import math
import numpy as np

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_SPEED = 2

# Rotation angles
START_ANGLE = 0
END_ANGLE = 360
ROTATION_SPEED = 1

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, angle):
        self.x = WIDTH // 2 + 100 * math.cos(math.radians(angle))
        self.y = HEIGHT // 2 + 100 * math.sin(math.radians(angle))

def draw_points(screen, points):
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    points = []
    for i in range(NUM_LIGHTS):
        angle = START_ANGLE + (END_ANGLE - START_ANGLE) * i / (NUM_LIGHTS - 1)
        x = WIDTH // 2 + 100 * math.cos(math.radians(angle))
        y = HEIGHT // 2 + 100 * math.sin(math.radians(angle))
        points.append(PointLight(x, y))

    running = True
    angle = START_ANGLE
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point in points:
            point.update(angle)
            draw_points(screen, points)

        angle = (angle + ROTATION_SPEED) % 360

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
