
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHTS = 15
MAX_RADIUS = 50
MIN_RADIUS = 10

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.uniform(MIN_RADIUS, MAX_RADIUS)
        self.angle = 0

    def update(self):
        self.angle += 0.01

    def draw(self):
        dx = WIDTH / 2 + math.sin(self.angle) * self.radius
        dy = HEIGHT / 2 + math.cos(self.angle) * self.radius
        pygame.draw.circle(screen, WHITE, (int(dx), int(dy)), 2)

# Create the point lights
point_lights = [PointLight(random.uniform(-WIDTH, WIDTH), random.uniform(-HEIGHT, HEIGHT)) for _ in range(POINT_LIGHTS)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.fill(BLACK)

    # Update and draw the point lights
    for light in point_lights:
        light.update()
        light.draw()

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
