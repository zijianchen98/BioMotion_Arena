
import pygame
import math
import random

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Number of point-lights
NUM_LIGHTS = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.uniform(-1, 1)
        self.radius = random.uniform(1, 3)

    def update(self):
        self.y += self.speed
        if self.y < 0 or self.y > HEIGHT:
            self.speed *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), int(self.radius))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = [PointLight(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_LIGHTS)]

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
