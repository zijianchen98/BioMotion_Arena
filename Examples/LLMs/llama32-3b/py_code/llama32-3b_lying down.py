
import pygame
import random
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Number of point-lights
NUM_LIGHTS = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PointLight:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(0.01, 0.1)

    def update(self):
        self.x = WIDTH // 2 + math.cos(self.angle) * random.uniform(-10, 10)
        self.y = HEIGHT // 2 + math.sin(self.angle) * random.uniform(-10, 10)
        self.angle += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = [PointLight() for _ in range(NUM_LIGHTS)]

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
