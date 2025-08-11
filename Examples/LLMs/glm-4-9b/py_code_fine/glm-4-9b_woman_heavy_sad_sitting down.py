
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of point-lights
NUM_LIGHTS = 15

# Point-light class
class PointLight:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.angle = 0
    
    def update(self, time):
        # Calculate new position based on time and action (sitting down)
        self.angle += 0.02
        if time > 300:
            # After some time, simulate sitting down
            self.y += 0.5
        
        # Add some randomness to positions for natural movement
        self.x += np.sin(self.angle) * 0.5
        self.y += np.cos(self.angle) * 0.2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Initialize point-lights for a sad woman sitting down
point_lights = []
for i in range(NUM_LIGHTS):
    angle = 2 * math.pi * i / NUM_LIGHTS
    # Initial positions in a human-like shape
    x = WIDTH // 2 + int(math.cos(angle) * 100)
    y = HEIGHT // 2 + int(math.sin(angle) * 50)
    point_lights.append(PointLight(x, y, 5, WHITE))

# Main loop
running = True
clock = pygame.time.Clock()
time_counter = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    # Update and draw point-lights
    for light in point_lights:
        light.update(time_counter)
        light.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    time_counter += 1

pygame.quit()
