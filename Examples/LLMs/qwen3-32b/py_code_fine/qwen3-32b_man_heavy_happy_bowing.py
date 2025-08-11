
import pygame
import math
import sys
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_RADIUS = 4
NUM_LIGHTS = 15
JOINT_LENGTH = 20
JOINT_SPEED = 0.05
BOWING_AMPLITUDE = 15  # Reduced amplitude for "heavy" bowing
BOWING_FREQUENCY = 0.02
ACTION_DURATION = 3000  # 3 seconds for the bowing action

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Happy Man Bowing")
clock = pygame.time.Clock()

# Joint structure: Define body joints in relative coordinates
# Joints are represented as (x, y) relative to the center of the body
# This forms a simplified stick figure with 15 joints
# 0: Head
# 1: Upper chest
# 2: Lower chest
# 3: Upper right arm
# 4: Lower right arm
# 5: Upper left arm
# 6: Lower left arm
# 7: Upper right leg
# 8: Lower right leg
# 9: Upper left leg
# 10: Lower left leg
# 11: Right shoulder
# 12: Left shoulder
# 13: Right hip
# 14: Left hip
relative_joints = np.array([
    [0, -100],    # Head
    [0, -60],     # Upper chest
    [0, -20],     # Lower chest
    [20, -50],    # Upper right arm
    [40, -80],    # Lower right arm
    [-20, -50],   # Upper left arm
    [-40, -80],   # Lower left arm
    [20, 10],     # Upper right leg
    [20, 40],     # Lower right leg
    [-20, 10],    # Upper left leg
    [-20, 40],    # Lower left leg
    [20, -40],    # Right shoulder
    [-20, -40],   # Left shoulder
    [20, 0],      # Right hip
    [-20, 0],     # Left hip
])

# Convert relative joints to positions
positions = np.zeros((NUM_LIGHTS, 2))
positions[:, 0] = WIDTH // 2 + relative_joints[:, 0]
positions[:, 1] = HEIGHT // 2 + relative_joints[:, 1]

# Time-based bowing animation
def bowing_animation(elapsed_time):
    # Calculate bowing angle
    bowing_angle = BOWING_AMPLITUDE * math.sin(BOWING_FREQUENCY * elapsed_time)
    # Apply bowing to upper body joints
    head_offset = bowing_angle
    chest_offset = bowing_angle * 0.7
    arm_offset = bowing_angle * 0.5
    leg_offset = bowing_angle * 0.2
    # Update joint positions
    positions[0] = [WIDTH // 2, HEIGHT // 2 - 100 + head_offset]
    positions[1] = [WIDTH // 2, HEIGHT // 2 - 60 + chest_offset]
    positions[2] = [WIDTH // 2, HEIGHT // 2 - 20 + chest_offset]
    positions[3] = [WIDTH // 2 + 20, HEIGHT // 2 - 50 + arm_offset]
    positions[4] = [WIDTH // 2 + 40, HEIGHT // 2 - 80 + arm_offset]
    positions[5] = [WIDTH // 2 - 20, HEIGHT // 2 - 50 + arm_offset]
    positions[6] = [WIDTH // 2 - 40, HEIGHT // 2 - 80 + arm_offset]
    positions[7] = [WIDTH // 2 + 20, HEIGHT // 2 + 10 + leg_offset]
    positions[8] = [WIDTH // 2 + 20, HEIGHT // 2 + 40 + leg_offset]
    positions[9] = [WIDTH // 2 - 20, HEIGHT // 2 + 10 + leg_offset]
    positions[10] = [WIDTH // 2 - 20, HEIGHT // 2 + 40 + leg_offset]
    positions[11] = [WIDTH // 2 + 20, HEIGHT // 2 - 40 + arm_offset]
    positions[12] = [WIDTH // 2 - 20, HEIGHT // 2 - 40 + arm_offset]
    positions[13] = [WIDTH // 2 + 20, HEIGHT // 2 + 0 + leg_offset]
    positions[14] = [WIDTH // 2 - 20, HEIGHT // 2 + 0 + leg_offset]

# Main loop
start_time = pygame.time.get_ticks()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    elapsed_time = pygame.time.get_ticks() - start_time
    if elapsed_time < ACTION_DURATION:
        bowing_animation(elapsed_time)
    else:
        # After bowing, keep the character in a still position
        positions[0] = [WIDTH // 2, HEIGHT // 2 - 100]
        positions[1] = [WIDTH // 2, HEIGHT // 2 - 60]
        positions[2] = [WIDTH // 2, HEIGHT // 2 - 20]
        positions[3] = [WIDTH // 2 + 20, HEIGHT // 2 - 50]
        positions[4] = [WIDTH // 2 + 40, HEIGHT // 2 - 80]
        positions[5] = [WIDTH // 2 - 20, HEIGHT // 2 - 50]
        positions[6] = [WIDTH // 2 - 40, HEIGHT // 2 - 80]
        positions[7] = [WIDTH // 2 + 20, HEIGHT // 2 + 10]
        positions[8] = [WIDTH // 2 + 20, HEIGHT // 2 + 40]
        positions[9] = [WIDTH // 2 - 20, HEIGHT // 2 + 10]
        positions[10] = [WIDTH // 2 - 20, HEIGHT // 2 + 40]
        positions[11] = [WIDTH // 2 + 20, HEIGHT // 2 - 40]
        positions[12] = [WIDTH // 2 - 20, HEIGHT // 2 - 40]
        positions[13] = [WIDTH // 2 + 20, HEIGHT // 2 + 0]
        positions[14] = [WIDTH // 2 - 20, HEIGHT // 2 + 0]

    # Draw point lights
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), LIGHT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
