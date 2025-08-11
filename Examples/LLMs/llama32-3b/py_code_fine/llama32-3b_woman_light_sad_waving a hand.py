
import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_RADIUS = 5
LIGHT_COUNT = 15
ACTION_DURATION = 10  # seconds

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Define the class for a point-light
class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)
        self.velocity = random.uniform(-0.1, 0.1)

    def update(self):
        self.angle += self.velocity
        self.x = WIDTH / 2 + math.sin(self.angle) * 200
        self.y = HEIGHT / 2 + math.cos(self.angle) * 200

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), LIGHT_RADIUS)

# Create the point-lights
point_lights = [PointLight(random.uniform(-200, 200), random.uniform(-200, 200)) for _ in range(LIGHT_COUNT)]

# Set up the action
action_start_time = 0
action_duration = ACTION_DURATION

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update and draw the point-lights
    for point_light in point_lights:
        point_light.update()
        point_light.draw(screen)

    # Check if the action has started
    if action_start_time == 0:
        action_start_time = pygame.time.get_ticks()

    # Check if the action has ended
    if pygame.time.get_ticks() - action_start_time >= action_duration * 1000:
        running = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
