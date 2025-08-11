
import pygame
import numpy as np
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light parameters
POINT_LIGHTS = 15
POINT_LIGHT_RADIUS = 2

# H wildman model parameters
NUM_JOINTS = 8
JOINT_SPACING = 0.5
JOINT_RANGE = 0.5
JOINT_SLOPE = 0.5

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def update(self):
        self.angle += 0.01

    def draw(self, screen):
        point_x = self.x + math.cos(self.angle) * JOINT_RANGE
        point_y = self.y + math.sin(self.angle) * JOINT_RANGE
        pygame.draw.circle(screen, WHITE, (int(point_x), int(point_y)), POINT_LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = []
    for i in range(POINT_LIGHTS):
        angle = i * 2 * math.pi / POINT_LIGHTS
        x = WIDTH / 2 + math.cos(angle) * JOINT_RANGE
        y = HEIGHT / 2 + math.sin(angle) * JOINT_RANGE
        point_lights.append(PointLight(x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point_light in point_lights:
            point_light.update()
            point_light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
