
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the light source class
class LightSource:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = 5
        self.speed = 2

    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

# Create a list of light sources
lights = [LightSource() for _ in range(15)]

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the light sources
    for light in lights:
        light.move()

    # Draw the lights
    screen.fill((0, 0, 0))
    for light in lights:
        light.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
