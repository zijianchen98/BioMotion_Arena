
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock for a smooth FPS
clock = pygame.time.Clock()

# Define the class for point-light stimulus
class PointLight:
    def __init__(self, x, y, radius, angle, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.speed = speed

    def update(self):
        self.angle += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

# Define the class for the happy man
class HappyMan:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.radius = 50
        self.angle = 0
        self.speed = 0.05

    def update(self):
        self.angle += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)
        pygame.draw.line(screen, WHITE, (int(self.x), int(self.y)), (int(self.x + 100 * math.cos(self.angle)), int(self.y + 100 * math.sin(self.angle))), 5)

# Create a list of point-lights
point_lights = [PointLight(random.randint(0, WIDTH), random.randint(0, HEIGHT), 5, 0, 0.01) for _ in range(15)]

# Create a happy man
happy_man = HappyMan()

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the point-lights and happy man
    for light in point_lights:
        light.update()
        if light.x < 0 or light.x > WIDTH:
            light.speed *= -1
        if light.y < 0 or light.y > HEIGHT:
            light.speed *= -1
    happy_man.update()

    # Draw everything
    screen.fill(BLACK)
    for light in point_lights:
        light.draw(screen)
    happy_man.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
