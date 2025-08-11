
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30  # Frames per second

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Walking Animation")

# Define the point-light structure
class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), 5)

# Create point-lights representing the body joints
point_lights = [
    PointLight(WIDTH // 2, HEIGHT // 3),   # Head
    PointLight(WIDTH // 2 - 20, HEIGHT // 2), # Left shoulder
    PointLight(WIDTH // 2 + 20, HEIGHT // 2), # Right shoulder
    PointLight(WIDTH // 2 - 40, HEIGHT // 2 + 40), # Left elbow
    PointLight(WIDTH // 2 + 40, HEIGHT // 2 + 40), # Right elbow
    PointLight(WIDTH // 2 - 60, HEIGHT // 2 + 80), # Left wrist
    PointLight(WIDTH // 2 + 60, HEIGHT // 2 + 80), # Right wrist
    PointLight(WIDTH // 2 - 20, HEIGHT // 2 + 100), # Left hip
    PointLight(WIDTH // 2 + 20, HEIGHT // 2 + 100), # Right hip
    PointLight(WIDTH // 2 - 30, HEIGHT // 2 + 160), # Left knee
    PointLight(WIDTH // 2 + 30, HEIGHT // 2 + 160), # Right knee
    PointLight(WIDTH // 2 - 20, HEIGHT // 2 + 200), # Left ankle
    PointLight(WIDTH // 2 + 20, HEIGHT // 2 + 200), # Right ankle
    PointLight(WIDTH // 2 - 10, HEIGHT // 2 + 100), # Left hand carrying weight
    PointLight(WIDTH // 2 + 10, HEIGHT // 2 + 100), # Right hand carrying weight
]

# Movement parameters
dx = 2
dy = 0

# Animation loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the point lights to simulate walking
    for i in range(len(point_lights)):
        point_lights[i].move(dx, dy)
        
        # Add dynamics for front and back legs, simulating walking
        if i % 2 == 0:  # Left side lights
            point_lights[i].y += 2 * math.sin(pygame.time.get_ticks() / 200 + i)  
        else:  # Right side lights
            point_lights[i].y += 2 * math.sin(pygame.time.get_ticks() / 200 + i + math.pi)  

    # Fill screen with black
    screen.fill(BLACK)

    # Draw point-lights
    for point_light in point_lights:
        point_light.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
