
import pygame
import math
import numpy as np
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Forward Roll")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light positions for a human figure in forward roll
# These will be updated to show the rolling motion
num_points = 15

# Initial positions of the point-lights around the body
def generate_body_points(radius=50, center=(WIDTH//2, HEIGHT//2), num_points=num_points):
    angles = np.linspace(0, 2*np.pi, num_points, endpoint=False)
    points = []
    for angle in angles:
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append([x, y])
    return points

body_points = generate_body_points()

# Animation parameters
amplitude = 30  # Amplitude of the oscillation
frequency = 0.5  # Frequency of the oscillation in Hz
phase_shift = 0  # Phase shift for the oscillation

# Time tracking
start_time = pygame.time.get_ticks() / 1000.0  # Convert to seconds

# Function to update point positions based on forward roll
def update_positions(points, t):
    # Create a rolling motion by shifting points along a circular path
    angle_offset = 0.5 * t  # Horizontal movement (rolling)
    radius = 50
    
    new_points = []
    center = (WIDTH//2, HEIGHT//2 + 30 * math.sin(t))  # Slight vertical movement
    
    for i, point in enumerate(points):
        # Calculate original angle of the point
        original_angle = math.atan2(point[1] - (HEIGHT//2 + 30), point[0] - (WIDTH//2))
        
        # Rotate point around the center
        new_angle = original_angle + angle_offset
        x = center[0] + radius * math.cos(new_angle)
        y = center[1] + radius * math.sin(new_angle)
        
        new_points.append([x, y])
    
    return new_points

# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Get current time
    current_time = pygame.time.get_ticks() / 1000.0  # Convert to seconds
    time_elapsed = current_time - start_time
    
    # Update positions
    body_points = update_positions(body_points, time_elapsed)
    
    # Draw points
    for point in body_points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 3)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
