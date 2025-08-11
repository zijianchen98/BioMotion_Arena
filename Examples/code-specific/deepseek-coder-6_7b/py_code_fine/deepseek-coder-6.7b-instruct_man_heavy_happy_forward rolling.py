
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Define a class for the point light
class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), 5)

# Create a list of point lights
point_lights = [PointLight(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(15)]

# Game loop
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill the screen with black
    win.fill((0, 0, 0))

    # Draw the point lights
    for light in point_lights:
        light.draw(win)

    # Update the display
    pygame.display.update()

pygame.quit()
