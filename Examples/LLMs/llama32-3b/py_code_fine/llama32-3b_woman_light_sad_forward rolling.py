
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light properties
POINT_LIGHT_RADIUS = 5
POINT_LIGHT_SPAWN_RATE = 10

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        self.angle += 0.01

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), POINT_LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = [PointLight(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(15)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point_light in point_lights:
            point_light.update()
            point_light.x = WIDTH / 2 + math.cos(point_light.angle) * 200
            point_light.y = HEIGHT / 2 + math.sin(point_light.angle) * 200
            point_light.draw(screen)

        # Spawn new point-lights
        if random.randint(0, POINT_LIGHT_SPAWN_RATE) == 0:
            point_lights.append(PointLight(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
