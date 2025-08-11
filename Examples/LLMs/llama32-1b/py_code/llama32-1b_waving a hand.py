
import pygame
import random

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point light parameters
POINT_LIGHT_SIZE = 10
POINT_LIGHT_SPEED = 2
POINT_LIGHT_COUNT = 15

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def move(self):
        self.angle += POINT_LIGHT_SPEED
        self.x = WIDTH / 2 + int(WIDTH / 2 * math.sin(self.angle))
        self.y = HEIGHT / 2 + int(HEIGHT / 2 * math.cos(self.angle))

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
            point_light.move()
            pygame.draw.line(screen, WHITE, (point_light.x, point_light.y), (point_light.x + 1, point_light.y + 1), 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
