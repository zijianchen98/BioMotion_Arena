
import pygame
import numpy as np
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set background and point color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Define the coordinates for point-lights (Biomechanical model for a jumping sadwoman)
# These coordinates are placeholders for the human figure's joints (15 key points)
# We use numpy array to allow manipulation for animation
points = np.array([
    [400, 200],  # Head
    [380, 220], [420, 220],  # Shoulders
    [370, 260], [430, 260],  # Elbows
    [360, 300], [440, 300],  # Hands
    [390, 280], [410, 280],  # Hips
    [380, 340], [420, 340],  # Knees
    [370, 380], [430, 380],  # Ankles
    [360, 420], [440, 420]   # Feet
], dtype=float)

# Define motion parameters for the "jumping" action
def update_motion(frame):
    """Update point coordinates for jumping animation."""
    # Vertical sinusoidal movement for jumping
    jump_amplitude = 60  # Height of jump
    frequency = 2 * np.pi * (frame / FPS) * 0.5  # Frequency of jump
    displacement = jump_amplitude * np.abs(np.sin(frequency))

    # Move whole body up and down
    points[:, 1] = original_positions[:, 1] - displacement

    # Add biomechanical details for natural motion
    # For legs: Move knees and ankles more on jump
    points[9:11, 1] -= displacement * 0.2  # Knees
    points[11:13, 1] -= displacement * 0.3  # Ankles
    # For hands: Slight upward movement during jump
    points[5:7, 1] -= displacement * 0.1

# Store original positions to reset later if needed
original_positions = np.copy(points)

# Main animation loop
running = True
frame = 0
while running:
    screen.fill(BLACK)  # Clear screen with black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update motion for current frame
    update_motion(frame)

    # Draw the point-lights
    for point in points:
        pygame.draw.circle(screen, WHITE, point.astype(int), 5)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

    # Increment frame count
    frame += 1

pygame.quit()
sys.exit()
