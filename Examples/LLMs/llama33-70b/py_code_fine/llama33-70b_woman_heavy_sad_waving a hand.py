
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_POINTS = 15
POINT_COLOR = (255, 255, 255)  # White
POINT_SIZE = 5

# Animation properties
FPS = 60
DURATION = 5  # seconds

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, t):
        # Update point position based on the waving motion
        self.x = self.x + math.sin(t * 2) * 10
        self.y = self.y + math.cos(t * 3) * 5

class SadWoman:
    def __init__(self):
        self.points = [
            PointLight(100, 100),  # Head
            PointLight(120, 150),  # Right shoulder
            PointLight(80, 150),   # Left shoulder
            PointLight(120, 200),  # Right elbow
            PointLight(80, 200),   # Left elbow
            PointLight(120, 250),  # Right wrist
            PointLight(80, 250),   # Left wrist
            PointLight(100, 300),  # Torso
            PointLight(120, 350),  # Right hip
            PointLight(80, 350),   # Left hip
            PointLight(120, 400),  # Right knee
            PointLight(80, 400),   # Left knee
            PointLight(120, 450),  # Right ankle
            PointLight(80, 450),   # Left ankle
            PointLight(100, 500),  # Heavy weight
        ]

    def update(self, t):
        for point in self.points:
            point.update(t)

        # Add weight movement
        self.points[-1].x = self.points[-1].x + math.sin(t * 2) * 20
        self.points[-1].y = self.points[-1].y + math.cos(t * 3) * 10

    def draw(self, screen):
        for point in self.points:
            pygame.draw.circle(screen, POINT_COLOR, (int(point.x), int(point.y)), POINT_SIZE)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    sad_woman = SadWoman()
    t = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Black background

        sad_woman.update(t)
        sad_woman.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

        t += 1 / FPS
        if t > DURATION:
            t = 0

    pygame.quit()

if __name__ == "__main__":
    main()
