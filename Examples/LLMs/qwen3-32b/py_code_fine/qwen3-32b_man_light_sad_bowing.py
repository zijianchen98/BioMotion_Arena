
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_POINTS = 15
RADIUS = 3  # Radius of each point-light
LIGHT_SIZE = 5  # Size of each point-light
JOINT_LENGTH = 30  # Length between joints
JOINT_ANGLE_SPEED = 0.02  # Speed of motion

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Bowing - Biological Motion")
clock = pygame.time.Clock()

# Joint structure: a simple stick figure with 15 points
# We define a hierarchical structure for a simple sad man bowing
# Points are: head, neck, spine, pelvis, left shoulder, left elbow, left hand,
#              right shoulder, right elbow, right hand,
#              left hip, left knee, left foot,
#              right hip, right knee, right foot

def get_bow_position(t):
    """Compute the position of each joint during the bowing action."""
    # Base positions (static)
    base_positions = [
        [WIDTH // 2, 100],  # head
        [WIDTH // 2, 120],  # neck
        [WIDTH // 2, 150],  # spine
        [WIDTH // 2, 200],  # pelvis
        [WIDTH // 2 - 40, 140],  # left shoulder
        [WIDTH // 2 - 40, 180],  # left elbow
        [WIDTH // 2 - 40, 220],  # left hand
        [WIDTH // 2 + 40, 140],  # right shoulder
        [WIDTH // 2 + 40, 180],  # right elbow
        [WIDTH // 2 + 40, 220],  # right hand
        [WIDTH // 2 - 40, 200],  # left hip
        [WIDTH // 2 - 40, 250],  # left knee
        [WIDTH // 2 - 40, 300],  # left foot
        [WIDTH // 2 + 40, 200],  # right hip
        [WIDTH // 2 + 40, 250],  # right knee
        [WIDTH // 2 + 40, 300],  # right foot
    ]

    # Apply bowing motion to spine and head
    bend_factor = math.sin(t) * 0.5  # controls the bowing angle
    bend_factor = max(min(bend_factor, 0.5), -0.5)  # limit the bending

    # Bend the spine and head
    for i in range(3):  # head, neck, spine
        base_positions[i][0] = WIDTH // 2 + (i - 1) * (bend_factor * 50)
        base_positions[i][1] = 100 + (i * 30) - (bend_factor * 30)

    # Bend left arm and right arm
    for i in [4, 5, 6]:  # left arm
        base_positions[i][0] = WIDTH // 2 - 40 + (i - 4) * (bend_factor * 15)
        base_positions[i][1] = 140 + (i - 4) * 40 + (bend_factor * 20)

    for i in [7, 8, 9]:  # right arm
        base_positions[i][0] = WIDTH // 2 + 40 - (i - 7) * (bend_factor * 15)
        base_positions[i][1] = 140 + (i - 7) * 40 + (bend_factor * 20)

    # Bend legs
    for i in [10, 11, 12]:  # left leg
        base_positions[i][1] += bend_factor * 20

    for i in [13, 14, 15]:  # right leg
        base_positions[i][1] += bend_factor * 20

    return base_positions

def draw_point_light_stimulus(positions):
    """Draw the point-light stimulus on the screen."""
    screen.fill(BLACK)
    for x, y in positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), LIGHT_SIZE)
    pygame.display.flip()

# Main loop
t = 0  # time parameter for animation
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t += 0.05  # increment time
    positions = get_bow_position(t)
    draw_point_light_stimulus(positions)
    clock.tick(FPS)

pygame.quit()
sys.exit()
