
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Running")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Number of joints (points)
NUM_JOINTS = 15

# Joint indices for limbs (for drawing lines)
JOINT_PAIRS = [
    (0, 1), (1, 2), (2, 3), (3, 4),  # Left leg
    (0, 5), (5, 6), (6, 7), (7, 8),  # Right leg
    (4, 9), (8, 9), (9, 10), (10, 11),  # Torso and head
    (11, 12), (11, 13), (12, 14), (13, 14)  # Arms
]

# Base joint positions (relative to center)
JOINT_RELATIVE = np.array([
    [0, 0],           # Center (pelvis)
    [-40, 0],         # Left hip
    [-40, -60],       # Left knee
    [-40, -100],      # Left ankle
    [-40, -120],      # Left foot

    [40, 0],          # Right hip
    [40, -60],        # Right knee
    [40, -100],       # Right ankle
    [40, -120],       # Right foot

    [-20, -40],       # Left shoulder
    [0, -40],         # Spine top
    [20, -40],        # Right shoulder
    [-40, -80],       # Left hand
    [40, -80],        # Right hand
    [0, -100]         # Head
])

# Animation parameters
AMPLITUDE = 20
FREQUENCY = 0.1
TIME = 0

# Main loop
def run_animation():
    global TIME
    while True:
        screen.fill(BLACK)
        TIME += 0.1

        # Compute joint positions based on time
        joints = JOINT_RELATIVE.copy()
        for i in range(NUM_JOINTS):
            # Apply sine wave to simulate motion (running)
            joints[i][1] += AMPLITUDE * math.sin(FREQUENCY * i + TIME)

        # Convert to screen coordinates
        center_x, center_y = WIDTH // 2, HEIGHT // 2
        joint_positions = [(int(center_x + x), int(center_y + y)) for x, y in joints]

        # Draw points
        for x, y in joint_positions:
            pygame.draw.circle(screen, WHITE, (x, y), 5)

        # Draw limbs
        for j1, j2 in JOINT_PAIRS:
            pygame.draw.line(screen, WHITE, joint_positions[j1], joint_positions[j2], 2)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    run_animation()
