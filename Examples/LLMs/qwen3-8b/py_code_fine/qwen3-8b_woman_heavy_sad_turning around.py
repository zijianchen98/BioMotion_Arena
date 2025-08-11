
import pygame
import math
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Turning Around - Point-Light Stimulus")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define joints for a human body (simplified)
JOINTS = [
    ("hips", (400, 300)),
    ("left_knee", (350, 350)),
    ("left_ankle", (300, 400)),
    ("right_knee", (450, 350)),
    ("right_ankle", (500, 400)),
    ("torso", (400, 250)),
    ("left_shoulder", (330, 200)),
    ("left_elbow", (280, 230)),
    ("left_wrist", (250, 260)),
    ("right_shoulder", (470, 200)),
    ("right_elbow", (520, 230)),
    ("right_wrist", (550, 260)),
    ("neck", (400, 180)),
    ("head", (400, 150)),
]

# Define joint connections
JOINT_CONNECTIONS = [
    ("hips", "torso"),
    ("torso", "neck"),
    ("neck", "head"),
    ("hips", "left_knee"),
    ("left_knee", "left_ankle"),
    ("hips", "right_knee"),
    ("right_knee", "right_ankle"),
    ("torso", "left_shoulder"),
    ("left_shoulder", "left_elbow"),
    ("left_elbow", "left_wrist"),
    ("torso", "right_shoulder"),
    ("right_shoulder", "right_elbow"),
    ("right_elbow", "right_wrist"),
]

# Joint movement parameters
ROTATION_SPEED = 0.005  # radians per frame
PITCH_SPEED = 0.003
YAW_SPEED = 0.003

# Initial rotation angles
rotation_angle = 0
pitch_angle = 0
yaw_angle = 0

# Create a list of point-light positions
point_lights = []

# Generate initial point-light positions based on joint positions
for joint_name, joint_pos in JOINTS:
    x, y = joint_pos
    point_lights.append((x, y))

# Function to rotate point around a center
def rotate_point(point, center, angle):
    x, y = point
    cx, cy = center
    x -= cx
    y -= cy
    x_new = x * math.cos(angle) - y * math.sin(angle)
    y_new = x * math.sin(angle) + y * math.cos(angle)
    x_new += cx
    y_new += cy
    return (x_new, y_new)

# Function to apply pitch and yaw to point
def apply_pitch_yaw(point, pitch, yaw):
    x, y = point
    # Apply yaw (rotation around Y-axis)
    x_new = x * math.cos(yaw) - z * math.sin(yaw)
    z_new = x * math.sin(yaw) + z * math.cos(yaw)
    # Apply pitch (rotation around X-axis)
    y_new = y * math.cos(pitch) - z_new * math.sin(pitch)
    z_new = y * math.sin(pitch) + z_new * math.cos(pitch)
    return (x_new, y_new)

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Update rotation angles
    rotation_angle += ROTATION_SPEED
    pitch_angle += PITCH_SPEED
    yaw_angle += YAW_SPEED

    # Update point-light positions
    for i, (joint_name, joint_pos) in enumerate(JOINTS):
        x, y = joint_pos
        # Apply rotation
        x_rot, y_rot = rotate_point((x, y), (400, 300), rotation_angle)
        # Apply pitch and yaw
        x_pitch_yaw, y_pitch_yaw = apply_pitch_yaw((x_rot, y_rot), pitch_angle, yaw_angle)
        # Update point-light position
        point_lights[i] = (x_pitch_yaw, y_pitch_yaw)

    # Draw point-lights
    for x, y in point_lights:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 3)

    # Draw joint connections
    for a, b in JOINT_CONNECTIONS:
        ax, ay = JOINTS[JOINTS.index((a, ()))][1]
        bx, by = JOINTS[JOINTS.index((b, ()))][1]
        pygame.draw.line(screen, WHITE, (int(ax), int(ay)), (int(bx), int(by)), 1)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
