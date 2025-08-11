
import pygame
import math
import sys

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light properties
NUM_POINTS = 15
POINT_RADIUS = 2
POINT_COLOR = WHITE

# Animation properties
FPS = 60
ANIMATION_DURATION = 2  # seconds
ACTION_DURATION = 1.5  # seconds
BOWING_AMPLITUDE = 50
BOWING_FREQUENCY = 2  # Hz

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def update(self, time):
        self.angle = math.pi * BOWING_FREQUENCY * time
        self.x = WIDTH / 2 + math.cos(self.angle) * BOWING_AMPLITUDE
        self.y = HEIGHT / 2 + math.sin(self.angle) * BOWING_AMPLITUDE

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    points = []
    for i in range(NUM_POINTS):
        angle = 2 * math.pi * i / NUM_POINTS
        x = WIDTH / 2 + math.cos(angle) * 100
        y = HEIGHT / 2 + math.sin(angle) * 100
        points.append(Point(x, y))

    running = True
    start_time = pygame.time.get_ticks()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = (pygame.time.get_ticks() - start_time) / 1000
        if current_time < ACTION_DURATION:
            for point in points:
                point.update(current_time)
        else:
            for point in points:
                point.update(current_time - ACTION_DURATION)

        screen.fill(BLACK)
        for point in points:
            pygame.draw.circle(screen, POINT_COLOR, (int(point.x), int(point.y)), POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

        if current_time > ANIMATION_DURATION:
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
