
import pygame
import math
import random

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light properties
POINT_LIGHT_RADIUS = 2
POINT_LIGHT_COLOR = WHITE
POINT_LIGHT_COUNT = 15

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self, dt):
        self.angle += 0.05 * dt

    def draw(self, screen):
        dx = math.cos(self.angle) * 50
        dy = math.sin(self.angle) * 50
        end_x = self.x + dx
        end_y = self.y + dy
        pygame.draw.line(screen, POINT_LIGHT_COLOR, (self.x, self.y), (end_x, end_y), POINT_LIGHT_RADIUS)

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

        screen.fill(BLACK)

        for point_light in point_lights:
            point_light.update(1 / 60)  # 60 FPS
            point_light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
