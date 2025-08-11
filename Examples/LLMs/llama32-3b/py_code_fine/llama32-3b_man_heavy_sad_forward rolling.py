
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHT_RADIUS = 2
POINT_LIGHT_COLOR = WHITE
POINT_LIGHT_COUNT = 15
ROLLING_SPEED = 2

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Define the class for point-light
class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def update(self):
        self.angle += ROLLING_SPEED

    def draw(self, screen):
        point_x = self.x + math.cos(self.angle) * (WIDTH / 2)
        point_y = self.y + math.sin(self.angle) * (HEIGHT / 2)
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, (int(point_x), int(point_y)), POINT_LIGHT_RADIUS)

# Create a list of point-lights
point_lights = [PointLight(WIDTH / 2 + i * 50, HEIGHT / 2) for i in range(POINT_LIGHT_COUNT)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the point-lights
    for light in point_lights:
        light.update()
        light.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
