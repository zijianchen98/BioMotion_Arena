
import numpy as np
import pygame
import sys
import math
import time

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happyman Jumping")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Skeleton structure (15 joints)
# Define joints as relative positions to a center point (body center)
# Each joint is [x, y], in relative units (will be scaled)
skeleton = [
    [0, -0.4],   # 0 - Center (hips)
    [0, -0.2],   # 1 - Mid body
    [0, 0],      # 2 - Chest
    [0.1, 0.1],  # 3 - Right shoulder
    [-0.1, 0.1], # 4 - Left shoulder
    [0.15, 0.3], # 5 - Right elbow
    [-0.15, 0.3],# 6 - Left elbow
    [0.2, 0.5],  # 7 - Right hand
    [-0.2, 0.5], # 8 - Left hand
    [0.1, -0.2], # 9 - Right hip
    [-0.1, -0.2],#10 - Left hip
    [0.15, -0.4],#11 - Right knee
    [-0.15, -0.4],#12 - Left knee
    [0.1, -0.6], #13 - Right foot
    [-0.1, -0.6], #14 - Left foot
]

# Convert skeleton to numpy array for easier manipulation
skeleton = np.array(skeleton, dtype=np.float32)

# Animation parameters
jump_height = 0.5  # relative jump height
jump_duration = 1.0  # in seconds
jump_cycle = 2.0    # total cycle time (jump up and down)
frame_rate = 60
frames_per_cycle = int(jump_cycle * frame_rate)

# Scaling factor for display
scale = 150
offset_x = WIDTH // 2
offset_y = HEIGHT // 2

# Animation function for jumping motion
def get_jump_phase(t):
    t = t % jump_cycle
    if t < jump_duration:
        # Going up
        phase = t / jump_duration
        return jump_height * (1 - phase**2)
    else:
        # Going down
        phase = (t - jump_duration) / (jump_cycle - jump_duration)
        return jump_height * phase**2

# Limb motion functions (add slight rotation and swing for realism)
def limb_swing(t, amplitude=0.05, freq=2):
    return amplitude * math.sin(freq * 2 * math.pi * (t % 1))

def limb_rotation(t, amplitude=0.1, freq=2):
    return amplitude * math.sin(freq * 2 * math.pi * (t % 1))

# Main loop
running = True
start_time = time.time()
while running:
    screen.fill(BLACK)

    current_time = time.time()
    t = (current_time - start_time) % jump_cycle

    # Calculate jump height
    y_offset = get_jump_phase(t)

    # Draw point lights
    for i, (x, y) in enumerate(skeleton):
        # Apply jump
        y += y_offset
        # Apply limb swing or rotation
        if i in [9, 11, 13]:  # Right leg
            x += limb_swing(t, 0.03, 1.5)
            y += limb_rotation(t, 0.02, 1.5)
        elif i in [10, 12, 14]:  # Left leg
            x -= limb_swing(t, 0.03, 1.5)
            y -= limb_rotation(t, 0.02, 1.5)
        elif i in [3, 5, 7]:  # Right arm
            x += limb_swing(t, 0.04, 1.5)
            y -= limb_rotation(t, 0.02, 1.5)
        elif i in [4, 6, 8]:  # Left arm
            x -= limb_swing(t, 0.04, 1.5)
            y -= limb_rotation(t, 0.02, 1.5)

        # Scale and translate to screen coordinates
        px = int(x * scale + offset_x)
        py = int(y * scale + offset_y)
        pygame.draw.circle(screen, WHITE, (px, py), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()
sys.exit()
