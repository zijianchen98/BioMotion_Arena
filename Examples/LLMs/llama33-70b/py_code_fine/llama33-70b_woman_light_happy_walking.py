
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, angle, distance, speed):
        self.x = WIDTH // 2 + math.cos(angle) * distance
        self.y = HEIGHT // 2 + math.sin(angle) * distance
        angle += speed

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Point-Light Stimulus Animation')
    clock = pygame.time.Clock()

    # Initialize point lights with different distances and speeds to simulate walking
    point_lights = [
        PointLight(WIDTH // 2, HEIGHT // 2 - 100),  # Head
        PointLight(WIDTH // 2 - 20, HEIGHT // 2 - 80),  # Left shoulder
        PointLight(WIDTH // 2 + 20, HEIGHT // 2 - 80),  # Right shoulder
        PointLight(WIDTH // 2 - 30, HEIGHT // 2 - 50),  # Left elbow
        PointLight(WIDTH // 2 + 30, HEIGHT // 2 - 50),  # Right elbow
        PointLight(WIDTH // 2 - 40, HEIGHT // 2 - 20),  # Left wrist
        PointLight(WIDTH // 2 + 40, HEIGHT // 2 - 20),  # Right wrist
        PointLight(WIDTH // 2, HEIGHT // 2 + 20),  # Hip
        PointLight(WIDTH // 2 - 20, HEIGHT // 2 + 50),  # Left knee
        PointLight(WIDTH // 2 + 20, HEIGHT // 2 + 50),  # Right knee
        PointLight(WIDTH // 2 - 30, HEIGHT // 2 + 80),  # Left ankle
        PointLight(WIDTH // 2 + 30, HEIGHT // 2 + 80),  # Right ankle
        PointLight(WIDTH // 2 - 10, HEIGHT // 2 + 100),  # Left foot
        PointLight(WIDTH // 2 + 10, HEIGHT // 2 + 100),  # Right foot
        PointLight(WIDTH // 2, HEIGHT // 2 + 120),  # Lower back
    ]

    angles = [0] * len(point_lights)
    distances = [100, 80, 80, 70, 70, 60, 60, 50, 40, 40, 30, 30, 20, 20, 10]
    speeds = [0.01, 0.02, 0.02, 0.03, 0.03, 0.04, 0.04, 0.02, 0.05, 0.05, 0.06, 0.06, 0.07, 0.07, 0.01]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for i, point_light in enumerate(point_lights):
            point_light.update(angles[i], distances[i], speeds[i])
            angles[i] += speeds[i]
            point_light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
