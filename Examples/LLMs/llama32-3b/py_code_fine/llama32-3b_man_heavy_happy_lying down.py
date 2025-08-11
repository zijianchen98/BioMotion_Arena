
import pygame
import random
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light properties
POINT_LIGHT_RADIUS = 5
POINT_LIGHT_COUNT = 15

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.angle += 0.05
        self.speed_x += random.uniform(-0.01, 0.01)
        self.speed_y += random.uniform(-0.01, 0.01)

        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), POINT_LIGHT_RADIUS)

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

        for light in point_lights:
            light.update()
            light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
