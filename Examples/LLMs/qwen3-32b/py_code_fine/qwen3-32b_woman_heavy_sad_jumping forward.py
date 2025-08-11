
import pygame
import sys
import numpy as np

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Jumping Forward - Point-Light Biological Motion")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 30

# Frame rate and number of frames
total_frames = 60  # One full cycle of motion
current_frame = 0

# Joint positions over time (simplified 15 joints)
# Each joint is represented as (x, y) over time
# This is a simplified model of a sad woman jumping forward with heavy weight

# Precomputed joint positions over time
# This data is manually crafted to resemble a sad, heavy forward jump
joint_positions = []

# Create a sequence of joint positions over time
# We use a 15-joint stick figure: head, neck, torso, pelvis, left/right shoulder, elbow, wrist,
# left/right hip, knee, ankle
# All positions are relative to the center and scaled over time

for frame in range(total_frames):
    t = frame / total_frames
    sin_t = np.sin(t * np.pi)
    cos_t = np.cos(t * np.pi)

    # Base offset for movement
    x_offset = 200 * t  # Moving forward
    y_offset = 100 * (1 - np.cos(t * 2 * np.pi))  # Jumping up and down

    head = (WIDTH // 2 + x_offset, HEIGHT // 2 - 150 + y_offset)
    neck = (WIDTH // 2 + x_offset, HEIGHT // 2 - 130 + y_offset)
    torso = (WIDTH // 2 + x_offset, HEIGHT // 2 - 100 + y_offset)
    pelvis = (WIDTH // 2 + x_offset, HEIGHT // 2 - 70 + y_offset)

    left_shoulder = (WIDTH // 2 - 30 + x_offset, HEIGHT // 2 - 120 + y_offset)
    left_elbow = (WIDTH // 2 - 40 + x_offset, HEIGHT // 2 - 100 + y_offset)
    left_wrist = (WIDTH // 2 - 50 + x_offset, HEIGHT // 2 - 80 + y_offset)

    right_shoulder = (WIDTH // 2 + 30 + x_offset, HEIGHT // 2 - 120 + y_offset)
    right_elbow = (WIDTH // 2 + 40 + x_offset, HEIGHT // 2 - 100 + y_offset)
    right_wrist = (WIDTH // 2 + 50 + x_offset, HEIGHT // 2 - 80 + y_offset)

    left_hip = (WIDTH // 2 - 20 + x_offset, HEIGHT // 2 - 60 + y_offset)
    left_knee = (WIDTH // 2 - 20 + x_offset, HEIGHT // 2 - 40 + y_offset)
    left_ankle = (WIDTH // 2 - 20 + x_offset, HEIGHT // 2 - 10 + y_offset)

    right_hip = (WIDTH // 2 + 20 + x_offset, HEIGHT // 2 - 60 + y_offset)
    right_knee = (WIDTH // 2 + 20 + x_offset, HEIGHT // 2 - 40 + y_offset)
    right_ankle = (WIDTH // 2 + 20 + x_offset, HEIGHT // 2 - 10 + y_offset)

    joint_positions.append([
        head, neck, torso, pelvis,
        left_shoulder, left_elbow, left_wrist,
        right_shoulder, right_elbow, right_wrist,
        left_hip, left_knee, left_ankle,
        right_hip, right_knee, right_ankle
    ])

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw point-light stimulus
    for joint in joint_positions[current_frame]:
        pygame.draw.circle(screen, WHITE, (int(joint[0]), int(joint[1])), 5)

    pygame.display.flip()
    clock.tick(FPS)

    # Update current frame
    current_frame = (current_frame + 1) % total_frames

pygame.quit()
sys.exit()
