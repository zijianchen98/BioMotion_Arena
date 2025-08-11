
import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class PointLight:
    def __init__(self, x, y, radius, angle, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.speed = speed

    def move(self):
        self.angle += self.speed
        if self.angle > 2 * math.pi or self.angle < 0:
            self.angle = (self.angle + math.pi) % (2 * math.pi)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

def main():
    clock = pygame.time.Clock()
    point_lights = [
        PointLight(100, 100, 10, 0, 0.01),
        PointLight(200, 200, 10, math.pi / 4, 0.01),
        PointLight(300, 300, 10, math.pi / 2, 0.01),
        PointLight(400, 400, 10, 3 * math.pi / 4, 0.01),
        PointLight(500, 500, 10, 5 * math.pi / 4, 0.01),
        PointLight(600, 600, 10, 3 * math.pi / 2, 0.01),
        PointLight(700, 100, 10, 7 * math.pi / 4, 0.01),
        PointLight(800, 200, 10, 9 * math.pi / 4, 0.01),
        PointLight(900, 300, 10, 11 * math.pi / 4, 0.01),
        PointLight(1000, 400, 10, 13 * math.pi / 4, 0.01),
        PointLight(1100, 500, 10, 15 * math.pi / 4, 0.01),
        PointLight(1200, 600, 10, 17 * math.pi / 4, 0.01),
        PointLight(1300, 100, 10, 19 * math.pi / 4, 0.01),
        PointLight(1400, 200, 10, 21 * math.pi / 4, 0.01),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point_light in point_lights:
            point_light.move()
            point_light.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
