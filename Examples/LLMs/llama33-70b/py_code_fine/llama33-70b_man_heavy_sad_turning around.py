
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_COLOR = (255, 255, 255)  # White
LIGHT_RADIUS = 5

# Sadman properties
SADMAN_HEIGHT = 200
SADMAN_WEIGHT_HEIGHT = 50
SADMAN_WEIGHT_WIDTH = 20

# Animation properties
TURNING_SPEED = 0.05  # radians per frame
FRAME_RATE = 60

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, angle):
        # Update position based on angle
        self.x = WIDTH // 2 + math.cos(angle) * (SADMAN_HEIGHT // 2)
        self.y = HEIGHT // 2 + math.sin(angle) * (SADMAN_HEIGHT // 2)

    def draw(self, screen):
        pygame.draw.circle(screen, LIGHT_COLOR, (int(self.x), int(self.y)), LIGHT_RADIUS)

class Sadman:
    def __init__(self):
        self.lights = [
            PointLight(WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 2),  # Head
            PointLight(WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 4),  # Upper body
            PointLight(WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 8),  # Upper arm
            PointLight(WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 16),  # Forearm
            PointLight(WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 32),  # Hand
            PointLight(WIDTH // 2, HEIGHT // 2),  # Hip
            PointLight(WIDTH // 2, HEIGHT // 2 + SADMAN_HEIGHT // 4),  # Upper leg
            PointLight(WIDTH // 2, HEIGHT // 2 + SADMAN_HEIGHT // 8),  # Lower leg
            PointLight(WIDTH // 2, HEIGHT // 2 + SADMAN_HEIGHT // 16),  # Foot
            PointLight(WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 2 + SADMAN_WEIGHT_HEIGHT // 2),  # Weight
            PointLight(WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 2 + SADMAN_WEIGHT_HEIGHT // 2 + SADMAN_WEIGHT_WIDTH // 2),  # Weight
            PointLight(WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 2 + SADMAN_WEIGHT_HEIGHT // 2 - SADMAN_WEIGHT_WIDTH // 2),  # Weight
            PointLight(WIDTH // 2 - SADMAN_WEIGHT_WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 2 + SADMAN_WEIGHT_HEIGHT // 2),  # Weight
            PointLight(WIDTH // 2 + SADMAN_WEIGHT_WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 2 + SADMAN_WEIGHT_HEIGHT // 2),  # Weight
            PointLight(WIDTH // 2, HEIGHT // 2 - SADMAN_HEIGHT // 2 + SADMAN_WEIGHT_HEIGHT // 2 + SADMAN_WEIGHT_WIDTH),  # Weight
        ]

    def update(self, angle):
        for light in self.lights:
            light.update(angle)

    def draw(self, screen):
        for light in self.lights:
            light.draw(screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    sadman = Sadman()
    angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Black background
        sadman.update(angle)
        sadman.draw(screen)
        angle += TURNING_SPEED

        pygame.display.flip()
        clock.tick(FRAME_RATE)

    pygame.quit()

if __name__ == "__main__":
    main()
