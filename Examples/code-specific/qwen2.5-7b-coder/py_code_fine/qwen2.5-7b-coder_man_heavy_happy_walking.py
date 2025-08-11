
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
LAMP_RADIUS = 5
LAMP_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happyman Walking with Heavy Weight")

# Define lamp class
class Lamp:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(screen, LAMP_COLOR, (int(self.x), int(self.y)), LAMP_RADIUS)

# Create lamps
lamps = [Lamp() for _ in range(NUM_LIGHTS)]

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update lamps
    for lamp in lamps:
        lamp.update()

    # Draw lamps
    for lamp in lamps:
        lamp.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
