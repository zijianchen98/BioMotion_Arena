
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus: Sad Man Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light class
class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 5)

# Create point lights positions (15 points)
point_lights = [
    PointLight(WIDTH // 2, HEIGHT // 4),  # Head
    PointLight(WIDTH // 2 - 20, HEIGHT // 3),  # Left shoulder
    PointLight(WIDTH // 2 + 20, HEIGHT // 3),  # Right shoulder
    PointLight(WIDTH // 2 - 20, HEIGHT // 2),  # Left elbow
    PointLight(WIDTH // 2 + 20, HEIGHT // 2),  # Right elbow
    PointLight(WIDTH // 2 - 40, HEIGHT // 1.5),  # Left hand
    PointLight(WIDTH // 2 + 40, HEIGHT // 1.5),  # Right hand
    PointLight(WIDTH // 2 - 10, HEIGHT // 1.8),  # Left hip
    PointLight(WIDTH // 2 + 10, HEIGHT // 1.8),  # Right hip
    PointLight(WIDTH // 2 - 30, HEIGHT // 1.2),  # Left knee
    PointLight(WIDTH // 2 + 30, HEIGHT // 1.2),  # Right knee
    PointLight(WIDTH // 2 - 10, HEIGHT // 1.1),  # Left foot
    PointLight(WIDTH // 2 + 10, HEIGHT // 1.1),  # Right foot
    PointLight(WIDTH // 2, HEIGHT // 3.5),  # Lower back
    PointLight(WIDTH // 2, HEIGHT // 2.5),  # Upper back
]

# Animation parameters
clock = pygame.time.Clock()
running = True

# Main animation loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update points to simulate bowing motion
    for i, point in enumerate(point_lights):
        if i == 0:  # Head
            point.y += 1  # Simulate slight downward movement
        elif i < 5:  # Shoulders and elbows
            point.y += 2  # Move them down
        else:
            point.y += 3  # Move down hands and legs more

    # Draw point lights
    for point in point_lights:
        point.draw(screen)

    # Refresh screen
    pygame.display.flip()

    # Frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
