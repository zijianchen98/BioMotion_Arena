
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Man Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define a class for a point-light
class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 4
        self.speed = random.uniform(0.5, 1.5)
        self.angle = random.uniform(0, 2 * math.pi)
        self.phase = random.uniform(0, 2 * math.pi)

    def update(self):
        # Simulate realistic motion based on a running gait
        self.angle += self.speed
        self.x = WIDTH / 2 + 100 * math.sin(self.angle + self.phase)
        self.y = HEIGHT / 2 + 50 * math.cos(self.angle + self.phase)

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius)

# Create 15 point-lights
point_lights = [PointLight(WIDTH / 2, HEIGHT / 2) for _ in range(15)]

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for light in point_lights:
        light.update()
        light.draw(screen)

    pygame.display.flip()

    # Quit on close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
