
import pygame
import random
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
POINT_LIGHT_RADIUS = 5
POINT_LIGHT_COLOR = (255, 255, 255)
POINT_LIGHT_COUNT = 15

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        self.angle += 0.01

    def draw(self, screen):
        x = self.x + math.cos(self.angle) * 50
        y = self.y + math.sin(self.angle) * 50
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, (int(x), int(y)), POINT_LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = [PointLight(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(POINT_LIGHT_COUNT)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for point_light in point_lights:
            point_light.update()
            point_light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
