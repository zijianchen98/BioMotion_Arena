
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PointLight:
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.radius = 5

    def update(self):
        self.angle += self.speed

    def draw(self, screen):
        x = self.x + math.cos(self.angle) * 100
        y = self.y + math.sin(self.angle) * 100
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    lights = [
        PointLight(100, 100, 0, 0.1),
        PointLight(200, 100, 0, 0.1),
        PointLight(300, 100, 0, 0.1),
        PointLight(400, 100, 0, 0.1),
        PointLight(100, 200, 0, 0.1),
        PointLight(200, 200, 0, 0.1),
        PointLight(300, 200, 0, 0.1),
        PointLight(400, 200, 0, 0.1),
        PointLight(100, 300, 0, 0.1),
        PointLight(200, 300, 0, 0.1),
        PointLight(300, 300, 0, 0.1),
        PointLight(400, 300, 0, 0.1),
        PointLight(100, 400, 0, 0.1),
        PointLight(200, 400, 0, 0.1),
        PointLight(300, 400, 0, 0.1),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for light in lights:
            light.update()
            light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
