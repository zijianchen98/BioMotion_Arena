
import numpy as np
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define body parts for a sad man with a waving hand
body_parts = {
    "head": (400, 100),
    "torso": (400, 200),
    "left_shoulder": (320, 250),
    "right_shoulder": (480, 250),
    "left_hand": (300, 300),
    "right_hand": (500, 300),
    "left_knee": (320, 400),
    "right_knee": (480, 400),
    "left_ankle": (320, 500),
    "right_ankle": (480, 500),
    "left_elbow": (260, 350),
    "right_elbow": (540, 350),
    "left_wrist": (240, 400),
    "right_wrist": (560, 400)
}

# Define joint connections
joint_connections = [
    ("head", "torso"),
    ("torso", "left_shoulder"),
    ("torso", "right_shoulder"),
    ("left_shoulder", "left_elbow"),
    ("left_elbow", "left_wrist"),
    ("left_wrist", "left_hand"),
    ("right_shoulder", "right_elbow"),
    ("right_elbow", "right_wrist"),
    ("right_wrist", "right_hand"),
    ("torso", "left_knee"),
    ("left_knee", "left_ankle"),
    ("torso", "right_knee"),
    ("right_knee", "right_ankle")
]

# Define body part movement parameters
body_part_positions = {
    "head": np.array([400, 100]),
    "torso": np.array([400, 200]),
    "left_shoulder": np.array([320, 250]),
    "right_shoulder": np.array([480, 250]),
    "left_hand": np.array([300, 300]),
    "right_hand": np.array([500, 300]),
    "left_knee": np.array([320, 400]),
    "right_knee": np.array([480, 400]),
    "left_ankle": np.array([320, 500]),
    "right_ankle": np.array([480, 500]),
    "left_elbow": np.array([260, 350]),
    "right_elbow": np.array([540, 350]),
    "left_wrist": np.array([240, 400]),
    "right_wrist": np.array([560, 400])
}

# Define motion parameters
# Head and torso: slight up and down movement
head_motion = np.array([0, 0.5])
torso_motion = np.array([0, 0.3])

# Left shoulder: slight up and down
left_shoulder_motion = np.array([0, 0.3])

# Right shoulder: slight up and down
right_shoulder_motion = np.array([0, 0.3])

# Left hand: waving motion
left_hand_motion = np.array([0, 0.5])

# Right hand: slight up and down
right_hand_motion = np.array([0, 0.2])

# Left knee: slight up and down
left_knee_motion = np.array([0, 0.2])

# Right knee: slight up and down
right_knee_motion = np.array([0, 0.2])

# Left elbow: slight up and down
left_elbow_motion = np.array([0, 0.2])

# Right elbow: slight up and down
right_elbow_motion = np.array([0, 0.2])

# Left wrist: slight up and down
left_wrist_motion = np.array([0, 0.2])

# Right wrist: slight up and down
right_wrist_motion = np.array([0, 0.2])

# Animation loop
running = True
frame = 0
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Update positions based on motion
    body_part_positions["head"] += head_motion
    body_part_positions["torso"] += torso_motion
    body_part_positions["left_shoulder"] += left_shoulder_motion
    body_part_positions["right_shoulder"] += right_shoulder_motion
    body_part_positions["left_hand"] += left_hand_motion
    body_part_positions["right_hand"] += right_hand_motion
    body_part_positions["left_knee"] += left_knee_motion
    body_part_positions["right_knee"] += right_knee_motion
    body_part_positions["left_elbow"] += left_elbow_motion
    body_part_positions["right_elbow"] += right_elbow_motion
    body_part_positions["left_wrist"] += left_wrist_motion
    body_part_positions["right_wrist"] += right_wrist_motion

    # Reset motion for periodic movement
    if frame % 60 == 0:
        head_motion[1] = np.random.uniform(-0.5, 0.5)
        torso_motion[1] = np.random.uniform(-0.3, 0.3)
        left_shoulder_motion[1] = np.random.uniform(-0.3, 0.3)
        right_shoulder_motion[1] = np.random.uniform(-0.3, 0.3)
        left_hand_motion[1] = np.random.uniform(-0.5, 0.5)
        right_hand_motion[1] = np.random.uniform(-0.2, 0.2)
        left_knee_motion[1] = np.random.uniform(-0.2, 0.2)
        right_knee_motion[1] = np.random.uniform(-0.2, 0.2)
        left_elbow_motion[1] = np.random.uniform(-0.2, 0.2)
        right_elbow_motion[1] = np.random.uniform(-0.2, 0.2)
        left_wrist_motion[1] = np.random.uniform(-0.2, 0.2)
        right_wrist_motion[1] = np.random.uniform(-0.2, 0.2)

    # Draw body parts as point lights
    for part in body_parts:
        x, y = body_part_positions[part]
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    # Draw joint connections
    for a, b in joint_connections:
        x1, y1 = body_part_positions[a]
        x2, y2 = body_part_positions[b]
        pygame.draw.line(screen, WHITE, (int(x1), int(y1)), (int(x2), int(y2)), 2)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    frame += 1

pygame.quit()
