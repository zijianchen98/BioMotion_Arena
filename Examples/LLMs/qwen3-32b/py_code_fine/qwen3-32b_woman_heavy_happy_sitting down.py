
import pygame
import math
import sys
import numpy as np

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman with Heavy Weight Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
CLOCK = pygame.time.Clock()

# Joint indices for clarity
JOINTS = [
    "Head", "Left Shoulder", "Right Shoulder", "Left Elbow", "Right Elbow",
    "Left Hand", "Right Hand", "Torso", "Left Hip", "Right Hip",
    "Left Knee", "Right Knee", "Left Ankle", "Right Ankle", "Weight"
]

# Initial joint positions (relative to center)
JOINT_POSITIONS = np.array([
    [0, -100],  # Head
    [-30, -40],  # Left Shoulder
    [30, -40],  # Right Shoulder
    [-40, 10],  # Left Elbow
    [40, 10],  # Right Elbow
    [-50, 60],  # Left Hand
    [50, 60],  # Right Hand
    [0, 10],  # Torso
    [-20, 60],  # Left Hip
    [20, 60],  # Right Hip
    [-20, 120],  # Left Knee
    [20, 120],  # Right Knee
    [-20, 180],  # Left Ankle
    [20, 180],  # Right Ankle
    [0, 160]  # Weight (heavy object)
], dtype=float)

# Center of screen
CENTER = np.array([WIDTH // 2, HEIGHT // 2])

# Scaling factor
SCALE = 1.0

# Sitting down animation parameters
SITTING_PHASE = 0.0
SITTING_DURATION = 120  # frames
SITTING_AMPLITUDE = 0.8

# Function to interpolate positions for sitting motion
def animate_sitting(t, duration, amplitude):
    t /= duration
    if t > 1.0:
        t = 1.0
    # Head and shoulders move down
    head_down = amplitude * t
    shoulders_down = amplitude * t
    # Torso moves down more
    torso_down = amplitude * t * 1.2
    # Hips move down and knees bend
    hips_down = amplitude * t
    knees_bend = amplitude * t
    # Ankle movement
    ankles_down = amplitude * t
    # Weight moves down
    weight_down = amplitude * t * 1.3
    return {
        "head": head_down,
        "shoulders": shoulders_down,
        "torso": torso_down,
        "hips": hips_down,
        "knees": knees_bend,
        "ankles": ankles_down,
        "weight": weight_down
    }

# Main animation loop
running = True
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    SCREEN.fill(BLACK)

    # Update animation phase
    frame += 1
    SITTING_PHASE = min(frame, SITTING_DURATION) / SITTING_DURATION
    animation = animate_sitting(SITTING_PHASE, SITTING_DURATION, SITTING_AMPLITUDE)

    # Update joint positions
    updated_positions = JOINT_POSITIONS.copy()
    updated_positions[0, 1] += animation["head"] * 100  # Head
    updated_positions[1, 1] += animation["shoulders"] * 80  # Left Shoulder
    updated_positions[2, 1] += animation["shoulders"] * 80  # Right Shoulder
    updated_positions[3, 1] += animation["shoulders"] * 60  # Left Elbow
    updated_positions[4, 1] += animation["shoulders"] * 60  # Right Elbow
    updated_positions[5, 1] += animation["shoulders"] * 50  # Left Hand
    updated_positions[6, 1] += animation["shoulders"] * 50  # Right Hand
    updated_positions[7, 1] += animation["torso"] * 100  # Torso
    updated_positions[8, 1] += animation["hips"] * 120  # Left Hip
    updated_positions[9, 1] += animation["hips"] * 120  # Right Hip
    updated_positions[10, 1] += animation["knees"] * 100  # Left Knee
    updated_positions[11, 1] += animation["knees"] * 100  # Right Knee
    updated_positions[12, 1] += animation["ankles"] * 100  # Left Ankle
    updated_positions[13, 1] += animation["ankles"] * 100  # Right Ankle
    updated_positions[14, 1] += animation["weight"] * 100  # Weight

    # Apply scaling and centering
    updated_positions = updated_positions * SCALE + CENTER

    # Draw point lights
    for pos in updated_positions:
        pygame.draw.circle(SCREEN, WHITE, (int(pos[0]), int(pos[1])), 4)

    # Draw lines between joints for better visibility
    connections = [
        (0, 1), (0, 2), (1, 3), (3, 5), (2, 4), (4, 6),
        (1, 8), (2, 9), (8, 10), (10, 12), (9, 11), (11, 13),
        (7, 1), (7, 2), (7, 8), (7, 9), (7, 14)
    ]
    for (a, b) in connections:
        pygame.draw.line(SCREEN, WHITE, updated_positions[a], updated_positions[b], 1)

    # Update display
    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
sys.exit()
