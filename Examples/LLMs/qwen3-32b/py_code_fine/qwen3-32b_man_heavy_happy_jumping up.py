
import pygame
import math
import sys
import time

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
LIGHT_RADIUS = 3
LIGHT_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)

# Joints (15 points for a human figure)
JOINTS = [
    # Main body joints
    (WIDTH // 2, HEIGHT - 100),  # Pelvis
    (WIDTH // 2 - 20, HEIGHT - 140),  # Left hip
    (WIDTH // 2 + 20, HEIGHT - 140),  # Right hip
    (WIDTH // 2 - 30, HEIGHT - 180),  # Left knee
    (WIDTH // 2 + 30, HEIGHT - 180),  # Right knee
    (WIDTH // 2 - 40, HEIGHT - 220),  # Left ankle
    (WIDTH // 2 + 40, HEIGHT - 220),  # Right ankle
    (WIDTH // 2, HEIGHT - 180),  # Spine
    (WIDTH // 2, HEIGHT - 140),  # Thorax
    (WIDTH // 2 - 25, HEIGHT - 110),  # Left shoulder
    (WIDTH // 2 + 25, HEIGHT - 110),  # Right shoulder
    (WIDTH // 2 - 40, HEIGHT - 90),  # Left elbow
    (WIDTH // 2 + 40, HEIGHT - 90),  # Right elbow
    (WIDTH // 2 - 50, HEIGHT - 70),  # Left hand
    (WIDTH // 2 + 50, HEIGHT - 70),  # Right hand
]

# Jump parameters
GRAVITY = 0.5
JUMP_HEIGHT = 100
JUMP_DURATION = 1.0  # seconds
JUMP_PHASES = 60  # number of frames for a full jump cycle
jump_frame = 0

def jump_position(t):
    """Simulate a jump with a parabolic trajectory."""
    t = t % JUMP_PHASES
    t /= JUMP_PHASES
    if t < 0.5:
        return JUMP_HEIGHT * 4 * t * t
    else:
        return JUMP_HEIGHT * (-4 * (t - 1) * (t - 1) + 1)

def update_joints(joints, jump_offset):
    updated = []
    for (x, y) in joints:
        updated.append((x, y - jump_offset))
    return updated

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happyman Jumping Animation")
clock = pygame.time.Clock()

# Main loop
running = True
start_time = time.time()

while running:
    dt = clock.tick(FPS) / 1000.0  # Time step in seconds
    screen.fill(BG_COLOR)

    # Calculate jump progress
    elapsed_time = time.time() - start_time
    jump_frame = int(elapsed_time * FPS)
    jump_offset = jump_position(jump_frame % JUMP_PHASES)

    # Update joint positions
    updated_joints = update_joints(JOINTS, jump_offset)

    # Draw point lights
    for (x, y) in updated_joints:
        pygame.draw.circle(screen, LIGHT_COLOR, (int(x), int(y)), LIGHT_RADIUS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
