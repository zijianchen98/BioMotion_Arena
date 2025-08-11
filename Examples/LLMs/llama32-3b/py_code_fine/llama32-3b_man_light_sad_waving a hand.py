
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHTS = 15
POINT_LIGHT_RADIUS = 2

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class PointLight:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = random.uniform(0.5, 2.0)
        self.target_angle = angle

    def update(self):
        self.target_angle += self.speed
        self.angle += (self.target_angle - self.angle) / 10
        self.x = WIDTH / 2 + math.cos(self.angle) * 200
        self.y = HEIGHT / 2 + math.sin(self.angle) * 200

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), POINT_LIGHT_RADIUS)

def main():
    clock = pygame.time.Clock()
    point_lights = [PointLight(random.uniform(-WIDTH / 2, WIDTH / 2), random.uniform(-HEIGHT / 2, HEIGHT / 2), random.uniform(0, 2 * math.pi)) for _ in range(POINT_LIGHTS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point_light in point_lights:
            point_light.update()
            point_light.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
