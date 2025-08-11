
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define the point-light class
class PointLight:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.x += self.speed
        if self.x > WIDTH + self.radius:
            self.x = -self.radius

# Create a list of point-lights
lights = [PointLight(x, HEIGHT // 2, 10, (i + 1) / 10) for i, x in enumerate(range(0, WIDTH, 50))]

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the lights
    for light in lights:
        light.update()

    # Draw the lights
    screen.fill((0, 0, 0))
    for light in lights:
        light.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
