
import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define constants
T = 60  # Period in frames
V_X = 2  # Horizontal velocity in pixels per frame
Y0 = 400  # Base y position
A = 100   # Amplitude of jump

# Bone lengths
L_PELVIS_TO_HIP = 20
L_HIP_TO_KNEE = 80
L_KNEE_TO_ANKLE = 80
L_PELVIS_TO_TORSO = 30
L_TORSO_TO_NECK = 30
L_NECK_TO_HEAD = 30
L_TORSO_TO_SHOULDER = 30
L_SHOULDER_TO_ELBOW = 40
L_ELBOW_TO_WRIST = 40

# Angle functions for joint movements
def get_theta_left_hip(t):
    return 5  # Slight forward tilt

def get_theta_right_hip(t):
    return 5

def get_theta_left_knee(t):
    return 30 if 10 <= t % T < 30 else 0  # Bend knees during airborne phase

def get_theta_right_knee(t):
    return get_theta_left_knee(t)

def get_theta_left_shoulder(t):
    return -30 * math.sin(2 * math.pi * t / T)  # Arms swing to convey happiness

def get_theta_right_shoulder(t):
    return get_theta_left_shoulder(t)

def get_theta_left_elbow(t):
    return 0  # Keep elbows straight for simplicity

def get_theta_right_elbow(t):
    return 0

# Helper functions for position calculations
def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def rotate(v, theta):
    c, s = math.cos(theta), math.sin(theta)
    return (c * v[0] - s * v[1], s * v[0] + c * v[1])

# Main animation loop
t = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    t += 1

    # Compute root (pelvis) position
    x_root = (100 + V_X * t) % 800  # Move forward, wrap around screen
    y_root = Y0 - A * (math.sin(math.pi * (t % T) / T) ** 2)  # Smooth jump motion
    root_pos = (x_root, y_root)

    # Calculate joint positions using skeletal hierarchy
    pos_left_hip = add(root_pos, (-L_PELVIS_TO_HIP, 0))
    pos_right_hip = add(root_pos, (L_PELVIS_TO_HIP, 0))

    theta_left_hip_rad = math.radians(get_theta_left_hip(t))
    theta_right_hip_rad = math.radians(get_theta_right_hip(t))
    pos_left_knee = add(pos_left_hip, rotate((0, L_HIP_TO_KNEE), theta_left_hip_rad))
    pos_right_knee = add(pos_right_hip, rotate((0, L_HIP_TO_KNEE), theta_right_hip_rad))

    theta_left_knee_rad = math.radians(get_theta_left_knee(t))
    theta_right_knee_rad = math.radians(get_theta_right_knee(t))
    pos_left_ankle = add(pos_left_knee, rotate((0, L_KNEE_TO_ANKLE), theta_left_hip_rad + theta_left_knee_rad))
    pos_right_ankle = add(pos_right_knee, rotate((0, L_KNEE_TO_ANKLE), theta_right_hip_rad + theta_right_knee_rad))

    pos_torso = add(root_pos, (0, -L_PELVIS_TO_TORSO))
    pos_neck = add(pos_torso, (0, -L_TORSO_TO_NECK))
    pos_head = add(pos_neck, (0, -L_NECK_TO_HEAD))

    theta_left_shoulder_rad = math.radians(get_theta_left_shoulder(t))
    theta_right_shoulder_rad = math.radians(get_theta_right_shoulder(t))
    pos_left_shoulder = add(pos_torso, rotate((-L_TORSO_TO_SHOULDER, 0), theta_left_shoulder_rad))
    pos_right_shoulder = add(pos_torso, rotate((L_TORSO_TO_SHOULDER, 0), theta_right_shoulder_rad))

    theta_left_elbow_rad = math.radians(get_theta_left_elbow(t))
    theta_right_elbow_rad = math.radians(get_theta_right_elbow(t))
    pos_left_elbow = add(pos_left_shoulder, rotate((0, L_SHOULDER_TO_ELBOW), theta_left_shoulder_rad))
    pos_right_elbow = add(pos_right_shoulder, rotate((0, L_SHOULDER_TO_ELBOW), theta_right_shoulder_rad))

    pos_left_wrist = add(pos_left_elbow, rotate((0, L_ELBOW_TO_WRIST), theta_left_shoulder_rad + theta_left_elbow_rad))
    pos_right_wrist = add(pos_right_elbow, rotate((0, L_ELBOW_TO_WRIST), theta_right_shoulder_rad + theta_right_elbow_rad))

    # Clear the screen
    screen.fill(BLACK)

    # List of all 15 points to draw
    points = [
        pos_left_hip, pos_right_hip,
        pos_left_knee, pos_right_knee,
        pos_left_ankle, pos_right_ankle,
        pos_torso, pos_neck, pos_head,
        pos_left_shoulder, pos_right_shoulder,
        pos_left_elbow, pos_right_elbow,
        pos_left_wrist, pos_right_wrist
    ]

    # Draw each point as a white dot
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    # Update the display
    pygame.display.flip()

    # Control frame rate for smooth animation
    clock.tick(60)

# Clean up and exit
pygame.quit()
