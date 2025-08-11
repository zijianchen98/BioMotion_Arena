
import pygame
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_POINTS = 15
RADIUS = 5
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation of a Sad Man Turning Around")

# Function to calculate points based on rotation
def get_point_positions(angle):
    # Define basic positions of the points (body parts)
    basic_positions = [
        (WIDTH // 2, HEIGHT // 2 - 60),  # Head
        (WIDTH // 2 - 20, HEIGHT // 2 - 40),  # Left shoulder
        (WIDTH // 2 + 20, HEIGHT // 2 - 40),  # Right shoulder
        (WIDTH // 2 - 30, HEIGHT // 2 - 10),  # Left elbow
        (WIDTH // 2 + 30, HEIGHT // 2 - 10),  # Right elbow
        (WIDTH // 2 - 40, HEIGHT // 2 + 40),  # Left hand
        (WIDTH // 2 + 40, HEIGHT // 2 + 40),  # Right hand
        (WIDTH // 2 - 20, HEIGHT // 2 + 30),  # Left hip
        (WIDTH // 2 + 20, HEIGHT // 2 + 30),  # Right hip
        (WIDTH // 2 - 15, HEIGHT // 2 + 100), # Left knee
        (WIDTH // 2 + 15, HEIGHT // 2 + 100), # Right knee
        (WIDTH // 2 - 10, HEIGHT // 2 + 150), # Left foot
        (WIDTH // 2 + 10, HEIGHT // 2 + 150), # Right foot
    ]
    
    # Calculate rotation of each point around the center
    rotated_positions = []
    for (x, y) in basic_positions:
        # Rotate around center
        new_x = (x - WIDTH / 2) * math.cos(angle) - (y - HEIGHT / 2) * math.sin(angle) + WIDTH / 2
        new_y = (x - WIDTH / 2) * math.sin(angle) + (y - HEIGHT / 2) * math.cos(angle) + HEIGHT / 2
        rotated_positions.append((new_x, new_y))
    
    return rotated_positions

# Main loop
running = True
clock = pygame.time.Clock()
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update point positions
    points = get_point_positions(angle)
    
    # Draw the points
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), RADIUS)

    # Update angle for rotation
    angle += 0.05  # Adjust speed of rotation
    if angle > 2 * math.pi:  # Reset angle after a full rotation
        angle -= 2 * math.pi

    # Refresh the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
