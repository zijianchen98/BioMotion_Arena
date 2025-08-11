
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
point_lights = [PointLight(100, 100, 50), PointLight(200, 200, 50), PointLight(300, 300, 50), PointLight(400, 400, 50), PointLight(500, 500, 50), PointLight(600, 600, 50), PointLight(700, 700, 50), PointLight(800, 800, 50), PointLight(900, 900, 50), PointLight(1000, 1000, 50), PointLight(1100, 1100, 50), PointLight(1200, 1200, 50), PointLight(1300, 1300, 50), PointLight(1400, 1400, 50), PointLight(1500, 1500, 50)]

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
