
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_SPEED = 2

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def update(self):
        self.angle += LIGHT_SPEED

    def draw(self):
        dx = LIGHT_RADIUS * math.cos(self.angle)
        dy = LIGHT_RADIUS * math.sin(self.angle)
        pygame.draw.circle(screen, WHITE, (int(self.x + dx), int(self.y + dy)), LIGHT_RADIUS)

# Create a list of point lights
lights = [PointLight(WIDTH // 2, HEIGHT // 2) for _ in range(NUM_LIGHTS)]

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.fill(BLACK)

    # Update and draw each light
    for light in lights:
        light.update()
        light.draw()

    # Ensure lights don't move off the screen
    for light in lights:
        if light.x - LIGHT_RADIUS < 0 or light.x + LIGHT_RADIUS > WIDTH:
            light.x = WIDTH // 2
        if light.y - LIGHT_RADIUS < 0 or light.y + LIGHT_RADIUS > HEIGHT:
            light.y = HEIGHT // 2

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
