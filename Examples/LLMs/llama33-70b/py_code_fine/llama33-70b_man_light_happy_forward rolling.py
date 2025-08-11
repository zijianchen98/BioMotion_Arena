
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_POINTS = 15
POINT_RADIUS = 5
POINT_COLOR = (255, 255, 255)  # White

# Background properties
BACKGROUND_COLOR = (0, 0, 0)  # Black

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def update(self, angle):
        self.angle = angle

    def draw(self, screen):
        pygame.draw.circle(screen, POINT_COLOR, (int(self.x), int(self.y)), POINT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Define point-light positions for a happy man with light weight
    points = [
        PointLight(0, -100),  # Head
        PointLight(-20, -50),  # Left shoulder
        PointLight(20, -50),  # Right shoulder
        PointLight(-30, 0),  # Left elbow
        PointLight(30, 0),  # Right elbow
        PointLight(-40, 50),  # Left wrist
        PointLight(40, 50),  # Right wrist
        PointLight(0, 100),  # Hips
        PointLight(-20, 150),  # Left knee
        PointLight(20, 150),  # Right knee
        PointLight(-30, 200),  # Left ankle
        PointLight(30, 200),  # Right ankle
        PointLight(-10, 250),  # Left foot
        PointLight(10, 250),  # Right foot
        PointLight(0, 300),  # Center of mass
    ]

    running = True
    angle = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Update point-light positions based on the forward rolling action
        for i, point in enumerate(points):
            if i == 0:  # Head
                point.x = WIDTH / 2 + 50 * math.sin(angle)
                point.y = HEIGHT / 2 - 50 * math.cos(angle)
            elif i == 1:  # Left shoulder
                point.x = WIDTH / 2 + 40 * math.sin(angle + math.pi / 2)
                point.y = HEIGHT / 2 - 40 * math.cos(angle + math.pi / 2)
            elif i == 2:  # Right shoulder
                point.x = WIDTH / 2 + 40 * math.sin(angle - math.pi / 2)
                point.y = HEIGHT / 2 - 40 * math.cos(angle - math.pi / 2)
            elif i == 3:  # Left elbow
                point.x = WIDTH / 2 + 30 * math.sin(angle + math.pi)
                point.y = HEIGHT / 2 - 30 * math.cos(angle + math.pi)
            elif i == 4:  # Right elbow
                point.x = WIDTH / 2 + 30 * math.sin(angle)
                point.y = HEIGHT / 2 - 30 * math.cos(angle)
            elif i == 5:  # Left wrist
                point.x = WIDTH / 2 + 20 * math.sin(angle + math.pi / 2)
                point.y = HEIGHT / 2 - 20 * math.cos(angle + math.pi / 2)
            elif i == 6:  # Right wrist
                point.x = WIDTH / 2 + 20 * math.sin(angle - math.pi / 2)
                point.y = HEIGHT / 2 - 20 * math.cos(angle - math.pi / 2)
            elif i == 7:  # Hips
                point.x = WIDTH / 2 + 50 * math.sin(angle)
                point.y = HEIGHT / 2 + 50 * math.cos(angle)
            elif i == 8:  # Left knee
                point.x = WIDTH / 2 + 40 * math.sin(angle + math.pi / 2)
                point.y = HEIGHT / 2 + 40 * math.cos(angle + math.pi / 2)
            elif i == 9:  # Right knee
                point.x = WIDTH / 2 + 40 * math.sin(angle - math.pi / 2)
                point.y = HEIGHT / 2 + 40 * math.cos(angle - math.pi / 2)
            elif i == 10:  # Left ankle
                point.x = WIDTH / 2 + 30 * math.sin(angle + math.pi)
                point.y = HEIGHT / 2 + 30 * math.cos(angle + math.pi)
            elif i == 11:  # Right ankle
                point.x = WIDTH / 2 + 30 * math.sin(angle)
                point.y = HEIGHT / 2 + 30 * math.cos(angle)
            elif i == 12:  # Left foot
                point.x = WIDTH / 2 + 20 * math.sin(angle + math.pi / 2)
                point.y = HEIGHT / 2 + 20 * math.cos(angle + math.pi / 2)
            elif i == 13:  # Right foot
                point.x = WIDTH / 2 + 20 * math.sin(angle - math.pi / 2)
                point.y = HEIGHT / 2 + 20 * math.cos(angle - math.pi / 2)
            elif i == 14:  # Center of mass
                point.x = WIDTH / 2 + 50 * math.sin(angle)
                point.y = HEIGHT / 2 + 50 * math.cos(angle)

            point.draw(screen)

        pygame.display.flip()
        angle += 0.01
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
