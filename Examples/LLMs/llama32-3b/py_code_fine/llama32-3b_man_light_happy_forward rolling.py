
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PointLight:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Stimulus Animation")
    clock = pygame.time.Clock()

    point_lights = [
        PointLight(100, 100, 5),
        PointLight(150, 150, 5),
        PointLight(200, 200, 5),
        PointLight(250, 250, 5),
        PointLight(300, 300, 5),
        PointLight(350, 350, 5),
        PointLight(400, 400, 5),
        PointLight(450, 450, 5),
        PointLight(500, 500, 5),
        PointLight(550, 550, 5),
        PointLight(600, 600, 5),
        PointLight(650, 650, 5),
        PointLight(700, 700, 5),
        PointLight(750, 750, 5),
        PointLight(800, 800, 5)
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
