
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Turning Around")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
CLOCK = pygame.time.Clock()
FPS = 30

# Body joint indices
JOINTS = [
    "Head", "Neck", "Torso", "Left Shoulder", "Left Elbow", "Left Hand",
    "Right Shoulder", "Right Elbow", "Right Hand", "Left Hip", "Left Knee",
    "Left Foot", "Right Hip", "Right Knee", "Right Foot"
]

# Define a basic human motion sequence for a sad woman turning around
# This is a simplified, stylized 2D approximation
# Each frame is a list of (x, y) positions for each joint

# We will use a circular motion to simulate turning
# Each joint will have a position relative to the center of the body

def generate_turning_sequence(frames=60):
    sequence = []
    for i in range(frames):
        t = i / frames * 2 * math.pi
        center_x = WIDTH // 2
        center_y = HEIGHT // 2
        head_offset = (0, -100)
        neck_offset = (0, -80)
        torso_offset = (0, -50)
        left_shoulder_offset = (-20, -40)
        left_elbow_offset = (-40, -20)
        left_hand_offset = (-60, 0)
        right_shoulder_offset = (20, -40)
        right_elbow_offset = (40, -20)
        right_hand_offset = (60, 0)
        left_hip_offset = (-15, 10)
        left_knee_offset = (-30, 40)
        left_foot_offset = (-45, 70)
        right_hip_offset = (15, 10)
        right_knee_offset = (30, 40)
        right_foot_offset = (45, 70)

        # Rotate each joint around the center
        angle = t
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)

        def rotate(x, y):
            return x * cos_a - y * sin_a, x * sin_a + y * cos_a

        head = rotate(*head_offset)
        neck = rotate(*neck_offset)
        torso = rotate(*torso_offset)
        left_shoulder = rotate(*left_shoulder_offset)
        left_elbow = rotate(*left_elbow_offset)
        left_hand = rotate(*left_hand_offset)
        right_shoulder = rotate(*right_shoulder_offset)
        right_elbow = rotate(*right_elbow_offset)
        right_hand = rotate(*right_hand_offset)
        left_hip = rotate(*left_hip_offset)
        left_knee = rotate(*left_knee_offset)
        left_foot = rotate(*left_foot_offset)
        right_hip = rotate(*right_hip_offset)
        right_knee = rotate(*right_knee_offset)
        right_foot = rotate(*right_foot_offset)

        frame = [
            (center_x + head[0], center_y + head[1]),
            (center_x + neck[0], center_y + neck[1]),
            (center_x + torso[0], center_y + torso[1]),
            (center_x + left_shoulder[0], center_y + left_shoulder[1]),
            (center_x + left_elbow[0], center_y + left_elbow[1]),
            (center_x + left_hand[0], center_y + left_hand[1]),
            (center_x + right_shoulder[0], center_y + right_shoulder[1]),
            (center_x + right_elbow[0], center_y + right_elbow[1]),
            (center_x + right_hand[0], center_y + right_hand[1]),
            (center_x + left_hip[0], center_y + left_hip[1]),
            (center_x + left_knee[0], center_y + left_knee[1]),
            (center_x + left_foot[0], center_y + left_foot[1]),
            (center_x + right_hip[0], center_y + right_hip[1]),
            (center_x + right_knee[0], center_y + right_knee[1]),
            (center_x + right_foot[0], center_y + right_foot[1]),
        ]

        sequence.append(frame)
    return sequence

# Generate the turning sequence
motion_sequence = generate_turning_sequence(60)

# Main animation loop
frame_index = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    SCREEN.fill(BLACK)

    # Draw current frame
    frame = motion_sequence[frame_index]
    for x, y in frame:
        pygame.draw.circle(SCREEN, WHITE, (int(x), int(y)), 5)

    # Update display
    pygame.display.flip()

    # Next frame
    frame_index = (frame_index + 1) % len(motion_sequence)

    # Control frame rate
    CLOCK.tick(FPS)

pygame.quit()
sys.exit()
