
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light properties
LIGHT_RADIUS = 5
LIGHT_COUNT = 15
LIGHT_SPEED = 5

# Happyman properties
HAPPYMAN_RADIUS = 50
HAPPYMAN_SPEED = 5

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def update(self):
        self.angle += 0.1
        self.x = HAPPYMAN_RADIUS + math.cos(self.angle) * LIGHT_SPEED
        self.y = HAPPYMAN_RADIUS + math.sin(self.angle) * LIGHT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), LIGHT_RADIUS)

def draw_happyman(screen, x, y):
    pygame.draw.circle(screen, WHITE, (x, y), HAPPYMAN_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = [PointLight(WIDTH // 2, HEIGHT // 2) for _ in range(LIGHT_COUNT)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point_light in point_lights:
            point_light.update()
            point_light.draw(screen)

        draw_happyman(screen, WIDTH // 2, HEIGHT // 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
