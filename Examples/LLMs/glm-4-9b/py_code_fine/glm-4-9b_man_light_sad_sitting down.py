
import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_COUNT = 15
FRAME_RATE = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, radius=2):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, POINT_COLOR, (int(self.x), int(self.y)), self.radius)

def update_positions(points, time):
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    radius = 150
    for i, point in enumerate(points):
        angle = 2 * math.pi * i / POINT_COUNT + time
        x = center_x + radius * math.sin(angle)
        y = center_y + radius * math.cos(angle)
        point.x = x
        point.y = y

def main():
    # Initialize points
    points = []
    for i in range(POINT_COUNT):
        angle = 2 * math.pi * i / POINT_COUNT
        x = WIDTH // 2 + 100 * math.sin(angle)
        y = HEIGHT // 2 + 100 * math.cos(angle)
        points.append(PointLight(x, y))

    time = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update positions
        update_positions(points, time)
        time += 0.02

        # Draw background
        screen.fill(BACKGROUND_COLOR)

        # Draw points
        for point in points:
            point.draw(screen)

        # Update display
        pygame.display.flip()
        clock.tick(FRAME_RATE)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
