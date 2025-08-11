
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Man Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 30

# Define joint positions in relative coordinates (simplified human model)
# We'll use 15 joints for the sad man jumping animation

# Joint indices (for reference)
JOINT_HEAD = 0
JOINT_TORSO = 1
JOINT_LEFT_HIP = 2
JOINT_LEFT_KNEE = 3
JOINT_LEFT_FOOT = 4
JOINT_RIGHT_HIP = 5
JOINT_RIGHT_KNEE = 6
JOINT_RIGHT_FOOT = 7
JOINT_LEFT_SHOULDER = 8
JOINT_LEFT_ELBOW = 9
JOINT_LEFT_HAND = 10
JOINT_RIGHT_SHOULDER = 11
JOINT_RIGHT_ELBOW = 12
JOINT_RIGHT_HAND = 13
JOINT_CHEST = 14

# Define a frame of joint positions (relative to center)
def get_frame(t):
    # t: time in seconds
    # We will simulate a jumping motion with a sine wave for vertical movement
    jump_height = 50
    jump_speed = 2  # jump frequency
    jump_offset = math.sin(t * jump_speed) * jump_height

    # Base positions (in local space)
    base_positions = np.array([
        # Head
        [0, -80],
        # Torso
        [0, -40],
        # Left hip
        [-30, 0],
        # Left knee
        [-30, 40],
        # Left foot
        [-30, 80],
        # Right hip
        [30, 0],
        # Right knee
        [30, 40],
        # Right foot
        [30, 80],
        # Left shoulder
        [-20, -40],
        # Left elbow
        [-20, -80],
        # Left hand
        [-20, -120],
        # Right shoulder
        [20, -40],
        # Right elbow
        [20, -80],
        # Right hand
        [20, -120],
        # Chest
        [0, -60],
    ])

    # Apply jump to the whole body (torso-based)
    base_positions[:, 1] += jump_offset

    # Add a slight slouch for the sad posture
    base_positions[JOINT_HEAD, 1] += 10  # head down
    base_positions[JOINT_TORSO, 1] += 5   # torso down
    base_positions[JOINT_CHEST, 1] += 10  # chest in

    # Add arm movement to simulate sadness
    arm_offset = math.sin(t * 1.5) * 10
    base_positions[JOINT_LEFT_ELBOW, 1] += arm_offset
    base_positions[JOINT_LEFT_HAND, 1] += arm_offset * 2
    base_positions[JOINT_RIGHT_ELBOW, 1] -= arm_offset
    base_positions[JOINT_RIGHT_HAND, 1] -= arm_offset * 2

    # Add knee flexion during jump
    knee_flex = math.sin(t * 2.5) * 10
    base_positions[JOINT_LEFT_KNEE, 1] += knee_flex
    base_positions[JOINT_RIGHT_KNEE, 1] += knee_flex

    return base_positions

# Main animation loop
def main():
    running = True
    t = 0  # time in seconds
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill(BLACK)

        # Get joint positions for this frame
        positions = get_frame(t)

        # Translate to center of screen
        center_x, center_y = WIDTH // 2, HEIGHT // 2
        translated_positions = positions + [center_x, center_y]

        # Draw each point-light joint
        for x, y in translated_positions:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

        # Update display
        pygame.display.flip()

        # Increment time
        t += 1 / FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
