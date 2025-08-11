
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define the point light class
class PointLight:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

# Create a list of point lights
point_lights = [PointLight(100, 100, 5), PointLight(200, 200, 5), PointLight(300, 300, 5), PointLight(400, 400, 5), PointLight(500, 500, 5), PointLight(600, 600, 5), PointLight(700, 700, 5), PointLight(800, 800, 5), PointLight(100, 200, 5), PointLight(200, 300, 5), PointLight(300, 400, 5), PointLight(400, 500, 5), PointLight(500, 600, 5), PointLight(600, 700, 5), PointLight(700, 800, 5)]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the point lights
    for light in point_lights:
        light.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
