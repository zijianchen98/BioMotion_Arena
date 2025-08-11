
import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
POINT_LIGHTS = 15
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Biological Motion - Sad Man Sitting Down')

# Function to calculate positions of the point-lights
def get_sitting_down_positions(frame):
    # Base positions for a static configuration
    base_positions = np.array([
        [400, 50],   # Head
        [380, 100],  # Left Shoulder
        [420, 100],  # Right Shoulder
        [360, 150],  # Left Elbow
        [440, 150],  # Right Elbow
        [340, 250],  # Left Hand
        [460, 250],  # Right Hand
        [390, 200],  # Chest
        [380, 300],  # Left Hip
        [420, 300],  # Right Hip
        [370, 400],  # Left Knee
        [430, 400],  # Right Knee
        [360, 500],  # Left Foot
        [440, 500],  # Right Foot
        [400, 350],  # Pelvis
        [400, 450],  # Center of mass
    ])
    
    # Motion parameters
    sitting_motion = np.array([
        [0, -0.1 * frame],  # Head moves slightly down
        [0, -0.1 * frame],  # Shoulders move more down
        [0, -0.1 * frame],
        [0, -0.1 * frame],
        [0, -0.1 * frame],
        [0, -0.2 * frame],  # Hands drop down
        [0, -0.2 * frame],
        [0, -0.2 * frame],
        [0, -0.2 * frame],
        [0, -0.2 * frame],
        [0, -0.2 * frame],
        [0, -0.2 * frame],
        [0, -0.2 * frame],
        [0, -0.2 * frame],
        [0, 0]  # Center of mass stays fixed for this position
    ])
    
    # Updating positions
    current_positions = base_positions + sitting_motion
    return current_positions.astype(int)

# Main Animation Loop
clock = pygame.time.Clock()
frame = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Get the point light positions for the current frame
    positions = get_sitting_down_positions(frame)

    # Draw the point lights
    for pos in positions:
        pygame.draw.circle(screen, LIGHT_COLOR, pos, 5)

    pygame.display.flip()
    frame += 1
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
