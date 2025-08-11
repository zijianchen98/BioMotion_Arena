
import pygame
import math
import sys

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of points
NUM_POINTS = 15

# Point properties
RADIUS = 5
SPEED = 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def move(self):
        self.angle += 0.05
        self.x = 50 + math.cos(self.angle) * 100
        self.y = 300 + math.sin(self.angle) * 50

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    points = [
        Point(50, 200),
        Point(100, 220),
        Point(150, 240),
        Point(200, 260),
        Point(250, 280),
        Point(300, 300),
        Point(350, 320),
        Point(400, 340),
        Point(450, 360),
        Point(500, 380),
        Point(550, 400),
        Point(600, 420),
        Point(650, 440),
        Point(700, 460),
        Point(750, 480)
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point in points:
            point.move()
            point.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
