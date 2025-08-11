
import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_LIGHT_COLOR = (255, 255, 255)
NUM_LIGHTS = 15
FRAMES_PER_SECOND = 30

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Define parameters for the sadman sitting down
SADMAN_SITTING_DURATION = 10  # seconds
SADMAN_SITTING_HEIGHT = 100  # pixels from bottom

# Define point-light positions for the sadman sitting down
def sadman_point_lights(t):
    """
    Generate positions of point lights representing a sitting sadman over time.
    t: Time in seconds
    """
    cycle = (t % SADMAN_SITTING_DURATION) / SADMAN_SITTING_DURATION
    # Body position changes as the sadman sits down
    if cycle < 0.5:
        body_elevation = np.sin(np.pi * cycle) * SADMAN_SITTING_HEIGHT
    else:
        body_elevation = np.cos(np.pi * (cycle - 0.5)) * SADMAN_SITTING_HEIGHT

    lights = []
    # Head position
    head_offset = np.array([0, body_elevation * 0.8])
    lights.append((WIDTH/2 + head_offset[0], HEIGHT/2 - 150 + head_offset[1]))

    # Torso position
    torso_offset = np.array([0, body_elevation * 0.6])
    lights.append((WIDTH/2 + torso_offset[0], HEIGHT/2 - 100 + torso_offset[1]))

    # Left shoulder
    left_shoulder_offset = np.array([-50, body_elevation * 0.7])
    lights.append((WIDTH/2 - 50 + left_shoulder_offset[0], HEIGHT/2 - 120 + left_shoulder_offset[1]))

    # Right shoulder
    right_shoulder_offset = np.array([50, body_elevation * 0.7])
    lights.append((WIDTH/2 + 50 + right_shoulder_offset[0], HEIGHT/2 - 120 + right_shoulder_offset[1]))

    # Left elbow
    left_elbow_offset = np.array([-80, body_elevation * 0.5])
    lights.append((WIDTH/2 - 80 + left_elbow_offset[0], HEIGHT/2 - 80 + left_elbow_offset[1]))

    # Right elbow
    right_elbow_offset = np.array([80, body_elevation * 0.5])
    lights.append((WIDTH/2 + 80 + right_elbow_offset[0], HEIGHT/2 - 80 + right_elbow_offset[1]))

    # Left hand
    left_hand_offset = np.array([-110, body_elevation * 0.3])
    lights.append((WIDTH/2 - 110 + left_hand_offset[0], HEIGHT/2 - 60 + left_hand_offset[1]))

    # Right hand
    right_hand_offset = np.array([110, body_elevation * 0.3])
    lights.append((WIDTH/2 + 110 + right_hand_offset[0], HEIGHT/2 - 60 + right_hand_offset[1]))

    # Left hip
    left_hip_offset = np.array([-40, body_elevation * 0.4])
    lights.append((WIDTH/2 - 40 + left_hip_offset[0], HEIGHT/2 + 20 + left_hip_offset[1]))

    # Right hip
    right_hip_offset = np.array([40, body_elevation * 0.4])
    lights.append((WIDTH/2 + 40 + right_hip_offset[0], HEIGHT/2 + 20 + right_hip_offset[1]))

    # Left knee
    left_knee_offset = np.array([-40, body_elevation * 0.3])
    lights.append((WIDTH/2 - 40 + left_knee_offset[0], HEIGHT/2 + 60 + left_knee_offset[1]))

    # Right knee
    right_knee_offset = np.array([40, body_elevation * 0.3])
    lights.append((WIDTH/2 + 40 + right_knee_offset[0], HEIGHT/2 + 60 + right_knee_offset[1]))

    # Left foot
    left_foot_offset = np.array([-40, body_elevation * 0.2])
    lights.append((WIDTH/2 - 40 + left_foot_offset[0], HEIGHT/2 + 100 + left_foot_offset[1]))

    # Right foot
    right_foot_offset = np.array([40, body_elevation * 0.2])
    lights.append((WIDTH/2 + 40 + right_foot_offset[0], HEIGHT/2 + 100 + right_foot_offset[1]))

    return lights

# Main loop
clock = pygame.time.Clock()
running = True
start_time = pygame.time.get_ticks() / 1000.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update time
    current_time = pygame.time.get_ticks() / 1000.0 - start_time

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw point lights for the sadman sitting down
    lights = sadman_point_lights(current_time)
    for light in lights:
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, light, 3)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FRAMES_PER_SECOND)

pygame.quit()
sys.exit()
