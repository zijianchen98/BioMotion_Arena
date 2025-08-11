
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
POINT_LIGHT_COLOR = (255, 255, 255)  # White
POINT_LIGHT_RADIUS = 5

# Animation properties
FPS = 60
JUMP_HEIGHT = 200
JUMP_DURATION = 1  # seconds

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, time):
        # Update point-light position based on the jumping motion
        self.y = HEIGHT // 2 - JUMP_HEIGHT * math.sin(2 * math.pi * time / JUMP_DURATION)

class Human:
    def __init__(self):
        # Define 15 point-lights to represent the happy woman
        self.point_lights = [
            PointLight(WIDTH // 2, HEIGHT // 2),  # Head
            PointLight(WIDTH // 2 - 20, HEIGHT // 2 - 50),  # Left shoulder
            PointLight(WIDTH // 2 + 20, HEIGHT // 2 - 50),  # Right shoulder
            PointLight(WIDTH // 2 - 30, HEIGHT // 2 - 100),  # Left elbow
            PointLight(WIDTH // 2 + 30, HEIGHT // 2 - 100),  # Right elbow
            PointLight(WIDTH // 2 - 40, HEIGHT // 2 - 150),  # Left wrist
            PointLight(WIDTH // 2 + 40, HEIGHT // 2 - 150),  # Right wrist
            PointLight(WIDTH // 2, HEIGHT // 2 + 50),  # Hip
            PointLight(WIDTH // 2 - 20, HEIGHT // 2 + 100),  # Left knee
            PointLight(WIDTH // 2 + 20, HEIGHT // 2 + 100),  # Right knee
            PointLight(WIDTH // 2 - 30, HEIGHT // 2 + 150),  # Left ankle
            PointLight(WIDTH // 2 + 30, HEIGHT // 2 + 150),  # Right ankle
            PointLight(WIDTH // 2 - 10, HEIGHT // 2 - 20),  # Left breast
            PointLight(WIDTH // 2 + 10, HEIGHT // 2 - 20),  # Right breast
            PointLight(WIDTH // 2, HEIGHT // 2 + 20),  # Belly button
        ]

    def update(self, time):
        for point_light in self.point_lights:
            point_light.update(time)

    def draw(self, screen):
        for point_light in self.point_lights:
            pygame.draw.circle(screen, POINT_LIGHT_COLOR, (int(point_light.x), int(point_light.y)), POINT_LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    human = Human()
    time = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black

        human.update(time)
        human.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

        time += 1 / FPS
        if time > JUMP_DURATION:
            time = 0

    pygame.quit()

if __name__ == "__main__":
    main()
