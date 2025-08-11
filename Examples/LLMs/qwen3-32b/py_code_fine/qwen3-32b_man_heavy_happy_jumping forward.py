
import numpy as np
import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happyman Jumping Forward")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Number of joints (points)
NUM_JOINTS = 15

# Generate joint positions for a jumping motion
# We will simulate a simple 2D jumping motion using sine waves for vertical motion
# and linear forward motion for horizontal

# Joint names (for reference)
joint_names = [
    'Head', 'Neck', 'Chest', 'Left Shoulder', 'Right Shoulder',
    'Left Elbow', 'Right Elbow', 'Left Hand', 'Right Hand',
    'Pelvis', 'Left Hip', 'Right Hip', 'Left Knee', 'Right Knee', 'Left Foot'
]

# Define joint positions (x, y, z) in a 2D plane (z is ignored for 2D animation)
# We'll create a simple forward jump with a bounce

# Initial positions
initial_x = np.array([WIDTH // 2] * NUM_JOINTS)
initial_y = np.array([
    100, 110, 120, 130, 130,
    150, 150, 170, 170,
    140, 160, 160, 180, 180, 200
])

# Joint offsets from the center
offsets = np.array([
    [0, 0], [0, 10], [0, 20], [-15, 30], [15, 30],
    [-30, 50], [30, 50], [-45, 70], [45, 70],
    [0, 40], [-20, 60], [20, 60], [-30, 80], [30, 80], [-30, 100]
])

# Convert initial positions to 2D coordinates
positions = np.zeros((NUM_JOINTS, 2))
for i in range(NUM_JOINTS):
    positions[i, 0] = initial_x[i] + offsets[i, 0]
    positions[i, 1] = initial_y[i] + offsets[i, 1]

# Animation parameters
jump_height = 100
jump_duration = 1.5  # seconds
jump_start_time = time.time()
forward_speed = 200  # pixels per second
jump_phase = 0.0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Time since jump started
    t = time.time() - jump_start_time
    t_normalized = t / jump_duration

    # Jump motion: parabolic trajectory
    if t < jump_duration:
        jump_phase = t_normalized
        y_offset = jump_height * (2 * jump_phase - 2 * jump_phase ** 2)
    else:
        # After jump is complete, reset
        jump_start_time = time.time()
        t = 0
        t_normalized = 0
        jump_phase = 0

    # Forward motion
    forward_offset = forward_speed * t

    # Update joint positions
    for i in range(NUM_JOINTS):
        positions[i, 0] = initial_x[i] + offsets[i, 0] + forward_offset
        positions[i, 1] = initial_y[i] + offsets[i, 1] - y_offset

    # Draw point-lights
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
