
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHT_RADIUS = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def update(self):
        self.angle += 0.01

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), POINT_LIGHT_RADIUS)

def main():
    point_lights = [
        PointLight(100, 100),
        PointLight(200, 100),
        PointLight(300, 100),
        PointLight(400, 100),
        PointLight(500, 100),
        PointLight(600, 100),
        PointLight(700, 100),
        PointLight(100, 200),
        PointLight(200, 200),
        PointLight(300, 200),
        PointLight(400, 200),
        PointLight(500, 200),
        PointLight(600, 200),
        PointLight(700, 200),
        PointLight(100, 300)
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for light in point_lights:
            light.update()
            light.draw(screen)

            # Calculate the angle of the light based on its position
            # We want the lights to move in a smooth, natural motion
            # So we use a sinusoidal function to calculate the angle
            # The angle is also affected by the light's position
            light.x = WIDTH / 2 + math.sin(light.angle) * 200
            light.y = HEIGHT / 2 + math.cos(light.angle) * 200

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
