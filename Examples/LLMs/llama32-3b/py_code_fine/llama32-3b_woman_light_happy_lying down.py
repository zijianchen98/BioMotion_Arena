
import pygame
import random
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 2
LIGHT_SPEED = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PointLight:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        self.x += LIGHT_SPEED * math.cos(self.angle)
        self.y += LIGHT_SPEED * math.sin(self.angle)
        if self.x < 0 or self.x > WIDTH:
            self.angle += math.pi
        if self.y < 0 or self.y > HEIGHT:
            self.angle -= math.pi

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    lights = [PointLight() for _ in range(NUM_LIGHTS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for light in lights:
            light.update()
            light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
