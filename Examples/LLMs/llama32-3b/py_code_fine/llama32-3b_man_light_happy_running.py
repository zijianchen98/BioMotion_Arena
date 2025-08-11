
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHTS = 15

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class PointLight:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def update(self, frame):
        if frame % 30 == 0:
            self.x = (self.x + 1) % WIDTH
        elif frame % 30 == 15:
            self.x = (self.x - 1) % WIDTH
        self.y = HEIGHT // 2

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

def main():
    clock = pygame.time.Clock()
    point_lights = [PointLight(WIDTH // 2 + i * 50, HEIGHT // 2, 5) for i in range(POINT_LIGHTS)]

    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for light in point_lights:
            light.update(frame)
            light.draw(screen)

        frame += 1

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
