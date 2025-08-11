
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light properties
POINT_LIGHT_RADIUS = 2
POINT_LIGHT_COLOR = WHITE
POINT_LIGHT_COUNT = 15

class PointLight:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def draw(self, screen):
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, (int(self.x), int(self.y)), POINT_LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Initialize point-lights
    point_lights = []
    for i in range(POINT_LIGHT_COUNT):
        x = WIDTH // 2 + math.cos(i * 2 * math.pi / POINT_LIGHT_COUNT) * 100
        y = HEIGHT // 2 + math.sin(i * 2 * math.pi / POINT_LIGHT_COUNT) * 100
        angle = i * 2 * math.pi / POINT_LIGHT_COUNT
        point_lights.append(PointLight(x, y, angle))

    # Animation parameters
    angle_step = 0.01
    angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill(BLACK)

        # Update point-lights
        for i, point_light in enumerate(point_lights):
            angle += angle_step
            point_light.angle = angle
            x = WIDTH // 2 + math.cos(point_light.angle) * 100
            y = HEIGHT // 2 + math.sin(point_light.angle) * 100
            point_light.x = x
            point_light.y = y

        # Draw point-lights
        for point_light in point_lights:
            point_light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
