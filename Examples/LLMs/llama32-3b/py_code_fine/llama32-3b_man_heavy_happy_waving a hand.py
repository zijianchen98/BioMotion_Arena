
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PointLight:
    def __init__(self, x, y, radius, angle, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.speed = speed

    def update(self):
        self.angle += self.speed
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = [
        PointLight(100, 100, 5, 0, 0.05),
        PointLight(200, 100, 5, math.pi / 4, 0.05),
        PointLight(300, 100, 5, math.pi / 2, 0.05),
        PointLight(400, 100, 5, 3 * math.pi / 4, 0.05),
        PointLight(500, 100, 5, 5 * math.pi / 4, 0.05),
        PointLight(600, 100, 5, 3 * math.pi / 2, 0.05),
        PointLight(700, 100, 5, 7 * math.pi / 4, 0.05),
        PointLight(800, 100, 5, math.pi, 0.05),
        PointLight(100, 200, 5, 0, 0.05),
        PointLight(200, 200, 5, math.pi / 4, 0.05),
        PointLight(300, 200, 5, math.pi / 2, 0.05),
        PointLight(400, 200, 5, 3 * math.pi / 4, 0.05),
        PointLight(500, 200, 5, 5 * math.pi / 4, 0.05),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for light in point_lights:
            light.update()
            light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
