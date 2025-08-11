
import pygame
import math
import random

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 2
LIGHT_SPAWN_RATE = 50  # frames
LIGHT_SPEED = 2  # pixels per frame

class PointLight:
    def __init__(self):
        self.x = random.randint(LIGHT_RADIUS, WIDTH - LIGHT_RADIUS)
        self.y = random.randint(LIGHT_RADIUS, HEIGHT - LIGHT_RADIUS)
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        self.x += math.cos(self.angle) * LIGHT_SPEED
        self.y += math.sin(self.angle) * LIGHT_SPEED

        if self.x - LIGHT_RADIUS < 0 or self.x + LIGHT_RADIUS > WIDTH:
            self.angle = math.pi - self.angle
        if self.y - LIGHT_RADIUS < 0 or self.y + LIGHT_RADIUS > HEIGHT:
            self.angle = -self.angle

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
            pygame.draw.circle(screen, WHITE, (int(light.x), int(light.y)), LIGHT_RADIUS)

        if random.randint(0, 100) < LIGHT_SPAWN_RATE:
            point_lights.append(PointLight())

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
