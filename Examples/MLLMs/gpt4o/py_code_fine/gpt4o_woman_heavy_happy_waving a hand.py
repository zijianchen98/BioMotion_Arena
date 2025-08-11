
import pygame
import numpy as np
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
FPS = 60

# Point-light color and size
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_RADIUS = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Waving Hand")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to generate joint positions for a simple biomechanically plausible waving motion
def generate_joint_positions(frame):
    """
    Generate the 15 joints of a humanoid figure, with biomechanically plausible movement.
    `frame` determines the point in time of the wave animation (periodic).
    """
    # Base positions (standing still)
    base_positions = np.array([
        [0, -200],  # Head
        [-30, -160], [30, -160],  # Shoulders
        [-60, -100], [60, -100],  # Elbows
        [-30, -50], [30, -50],    # Hands
        [0, 0],                   # Hip
        [-30, 50], [30, 50],      # Knees
        [-30, 120], [30, 120],    # Feet
        [0, -200],  # Waving hand joint (same as head initially for symmetry)
        [0, 0],     # Left Arm Anchor
        [0, 0],     # Loop back
    ])
    time = frame / FPS  # Convert frame to time in seconds
    wave_amplitude = 60
    wave_speed = 2 * np.pi * 1  # 1 Hz frequency
