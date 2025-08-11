
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light properties
POINT_LIGHT_RADIUS = 5
POINT_LIGHT_COLOR = WHITE
POINT_LIGHT_COUNT = 15

class PointLight:
    def __init__(self, x, y, angle, rotation):
        self.x = x
        self.y = y
        self.angle = angle
        self.rotation = rotation

    def update(self):
        self.angle += self.rotation
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi

    def draw(self, screen):
        x = self.x + math.cos(self.angle) * POINT_LIGHT_RADIUS
        y = self.y + math.sin(self.angle) * POINT_LIGHT_RADIUS
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, (int(x), int(y)), POINT_LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = [
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.05),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.03),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.02),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.01),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.005),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.0025),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.00125),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.000625),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.0003125),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.00015625),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.000078125),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.0000390625),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.00001953125),
        PointLight(WIDTH // 2, HEIGHT // 2, 0, 0.000009765625),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point_light in point_lights:
            point_light.update()
            point_light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
