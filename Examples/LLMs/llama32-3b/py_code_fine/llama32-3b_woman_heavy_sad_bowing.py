
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
POINT_LIGHT_COUNT = 15

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        self.angle += 0.01

    def draw(self, screen):
        end_x = self.x + math.cos(self.angle) * POINT_LIGHT_RADIUS
        end_y = self.y + math.sin(self.angle) * POINT_LIGHT_RADIUS
        pygame.draw.circle(screen, WHITE, (int(end_x), int(end_y)), POINT_LIGHT_RADIUS)

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
            point_light.update()
            point_light.draw(screen)

        # Create the illusion of movement by moving the point lights away from the center
        for point_light in point_lights:
            point_light.x += math.cos(point_light.angle) * 0.1
            point_light.y += math.sin(point_light.angle) * 0.1

        # Keep the point lights within the window
        for point_light in point_lights:
            if point_light.x < 0:
                point_light.x = WIDTH
            elif point_light.x > WIDTH:
                point_light.x = 0
            if point_light.y < 0:
                point_light.y = HEIGHT
            elif point_light.y > HEIGHT:
                point_light.y = 0

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
