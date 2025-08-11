
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Define the point light class
class PointLight:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

# Create a list to hold the point lights
point_lights = []

# Create the point lights
for i in range(15):
    point_lights.append(PointLight(50 + i*50, 300, (255, 255, 255)))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the point lights
    for light in point_lights:
        light.draw()

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)
