
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Center of the screen
center_x = WIDTH // 2

# Define 3D points for the figure (15 points)
points_3d = [
    # Head
    {'x3d': 0, 'y3d': 100, 'z3d': 0},
    # Shoulders
    {'x3d': 30, 'y3d': 130, 'z3d': 0},   # Right
    {'x3d': -30, 'y3d': 130, 'z3d': 0},  # Left
    # Elbows
    {'x3d': 30, 'y3d': 160, 'z3d': -20},  # Right
    {'x3d': -30, 'y3d': 160, 'z3d': -20}, # Left
    # Hands
    {'x3d': 30, 'y3d': 190, 'z3d': -40},  # Right
    {'x3d': -30, 'y3d': 190, 'z3d': -40}, # Left
    # Hips
    {'x3d': 20, 'y3d': 200, 'z3d': 0},    # Right
    {'x3d': -20, 'y3d': 200, 'z3d': 0},   # Left
    # Knees
    {'x3d': 20, 'y3d': 250, 'z3d': 0},    # Right
    {'x3d': -20, 'y3d': 250, 'z3d': 0},   # Left
    # Ankles
    {'x3d': 20, 'y3d': 300, 'z3d': 0},    # Right
    {'x3d': -20, 'y3d': 300, 'z3d': 0},   # Left
    # Torso points
    {'x3d': 0, 'y3d': 150, 'z3d': 0},     # Upper
    {'x3d': 0, 'y3d': 180, 'z3d': 0}      # Lower
]

# Animation parameters
theta = 0
angular_speed = 0.05

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    theta += angular_speed

    for point in points_3d:
        # Project 3D to 2D (Y-axis rotation)
        x_proj = point['x3d'] * math.cos(theta) - point['z3d'] * math.sin(theta)
        x = center_x + x_proj
        y = point['y3d']
        pygame.draw.circle(screen, WHITE, (int(x), y), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
