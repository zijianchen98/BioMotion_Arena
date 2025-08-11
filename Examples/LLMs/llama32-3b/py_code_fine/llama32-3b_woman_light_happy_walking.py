
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light properties
POINT_LIGHT_RADIUS = 5
POINT_LIGHT_COLOR = WHITE
POINT_LIGHT_COUNT = 15

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        self.angle += 0.01

    def draw(self, screen):
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, (int(self.x), int(self.y)), POINT_LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = []
    for i in range(POINT_LIGHT_COUNT):
        x = random.uniform(0, WIDTH)
        y = random.uniform(0, HEIGHT)
        point_lights.append(PointLight(x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point_light in point_lights:
            point_light.update()
            point_light.x = math.cos(point_light.angle) * 200 + WIDTH / 2
            point_light.y = math.sin(point_light.angle) * 200 + HEIGHT / 2
            point_light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
