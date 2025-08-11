
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
        self.speed = SPEED

    def update(self):
        self.angle += self.speed / 100
        self.x = WIDTH / 2 + math.cos(self.angle) * 200
        self.y = HEIGHT / 2 + math.sin(self.angle) * 150

def draw_points(screen, points):
    screen.fill(BLACK)
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    points = []
    for i in range(NUM_POINTS):
        angle = (i / NUM_POINTS) * 2 * math.pi
        x = WIDTH / 2 + math.cos(angle) * 200
        y = HEIGHT / 2 + math.sin(angle) * 150
        points.append(Point(x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for point in points:
            point.update()
            if point.x < 0 or point.x > WIDTH or point.y < 0 or point.y > HEIGHT:
                point.speed *= -1

        draw_points(screen, points)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
