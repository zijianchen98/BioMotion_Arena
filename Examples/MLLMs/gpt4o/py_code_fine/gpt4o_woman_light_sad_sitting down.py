
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Stimulus: Sitting Down - Sad Woman")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Skeleton configuration (approximate positions)
# Joint names: Head, Shoulders, Elbows, Wrists, Hips, Knees, Ankles
initial_positions = {
    "head": [screen_width // 2, 200],
    "left_shoulder": [screen_width // 2 - 30, 230],
    "right_shoulder": [screen_width // 2 + 30, 230],
    "left_elbow": [screen_width // 2 - 50, 260],
    "right_elbow": [screen_width // 2 + 50, 260],
    "left_wrist": [screen_width // 2 - 70, 290],
    "right_wrist": [screen_width // 2 + 70, 290],
    "left_hip": [screen_width // 2 - 30, 330],
    "right_hip": [screen_width // 2 + 30, 330],
    "left_knee": [screen_width // 2 - 40, 380],
    "right_knee": [screen_width // 2 + 40, 380],
    "left_ankle": [screen_width // 2 - 50, 430],
    "right_ankle": [screen_width // 2 + 50, 430],
}

# Animation parameters
time = 0
animation_speed = 0.1

# Function to update positions based on biomechanical plausibility
def update_motion(positions, time):
    # Simulates smooth biomechanical movement to sit down
    sitting_speed = -0.5  # Speed for downward motion
    
    for key in positions:
        if "hip" in key or "knee" in key or "ankle" in key:
            positions[key][1] += sitting_speed * np.sin(time)  # Gradually move down
        if "shoulder" in key and "elbow" in key:
            positions[key][1] += sitting_speed for coκtra weight
    
    
    
    
