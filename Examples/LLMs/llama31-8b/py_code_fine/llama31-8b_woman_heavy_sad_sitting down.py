
import pygame
import numpy as np

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)  # White

# Sitting down motion parameters
NUM_FRAMES = 60
FPS = 60

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, frame):
        # Sitting down motion parameters
        if frame < NUM_FRAMES // 4:
            self.y = HEIGHT // 2 - (frame * HEIGHT // (NUM_FRAMES // 4))
        elif frame < NUM_FRAMES // 2:
            self.x = WIDTH // 2 - (frame - NUM_FRAMES // 4) * 5
            self.y = HEIGHT // 2
        elif frame < 3 * NUM_FRAMES // 4:
            self.x = WIDTH // 2 + (frame - NUM_FRAMES // 2) * 5
            self.y = HEIGHT // 2
        else:
            self.y = HEIGHT // 2 + (frame - 3 * NUM_FRAMES // 4) * HEIGHT // (NUM_FRAMES // 4)

def draw_points(surface, points):
    for point in points:
        pygame.draw.circle(surface, LIGHT_COLOR, (int(point.x), int(point.y)), LIGHT_RADIUS)

def main():
    pygame.init()
    pygame.display.set_caption("Sadwoman Sitting Down")
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    points = []
    for i in range(NUM_LIGHTS):
        x = np.random.uniform(WIDTH // 2 - 100, WIDTH // 2 + 100)
        y = np.random.uniform(HEIGHT // 2 - 50, HEIGHT // 2 + 50)
        points.append(PointLight(x, y))

    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill((0, 0, 0))  # Black background

        for point in points:
            point.move(frame)
            draw_points(surface, points)

        pygame.display.flip()
        clock.tick(FPS)
        frame += 1

        if frame >= NUM_FRAMES:
            frame = 0

    pygame.quit()

if __name__ == "__main__":
    main()
