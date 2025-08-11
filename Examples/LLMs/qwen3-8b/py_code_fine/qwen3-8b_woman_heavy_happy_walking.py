
import numpy as np
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Woman Walking with Point-Lights")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define a simple biomechanical model for a walking human
# Simplified joint positions and movement patterns

# Joint positions (in pixels) for a simple bipedal model
# These are relative to the center of the screen
JOINTS = {
    'hips': (0, 0),
    'knees': (0, -100),
    'ankles': (0, -200),
    'shoulders': (0, 100),
    'elbows': (0, 150),
    'wrists': (0, 200)
}

# Joint offsets for the body
BODY_OFFSETS = {
    'hips': (0, 0),
    'knees': (0, -100),
    'ankles': (0, -200),
    'shoulders': (0, 100),
    'elbows': (0, 150),
    'wrists': (0, 200)
}

# Define a simple walking cycle
def walk_cycle(t, speed=1.0, amplitude=100, frequency=0.05):
    return amplitude * math.sin(frequency * t * speed)

# Define a function to update joint positions based on time
def update_joints(t):
    # Simulate a walking motion
    # Hips and shoulders move horizontally
    # Knees and ankles move up and down
    # Elbows and wrists move slightly

    # Horizontal movement for hips and shoulders
    x = walk_cycle(t, speed=1.0, amplitude=50, frequency=0.05)
    # Vertical movement for knees and ankles
    y_knee = walk_cycle(t, speed=1.0, amplitude=20, frequency=0.05)
    y_ankle = walk_cycle(t, speed=1.0, amplitude=10, frequency=0.05)
    # Vertical movement for elbows and wrists
    y_elbow = walk_cycle(t, speed=1.0, amplitude=10, frequency=0.05)
    y_wrist = walk_cycle(t, speed=1.0, amplitude=5, frequency=0.05)

    # Update joint positions
    JOINTS['hips'] = (x, 0)
    JOINTS['knees'] = (x, -100 + y_knee)
    JOINTS['ankles'] = (x, -200 + y_ankle)
    JOINTS['shoulders'] = (x, 100)
    JOINTS['elbows'] = (x, 150 + y_elbow)
    JOINTS['wrists'] = (x, 200 + y_wrist)

    return JOINTS

# Define a function to compute point-light positions based on joints
def compute_point_lights(joints):
    # Define 15 point-lights based on joints and body parts
    # This is a simplified representation
    point_lights = []

    # Add lights at key joints
    for joint in joints:
        point_lights.append(joints[joint])

    # Add lights along the legs
    for i in range(1, 4):
        x = (joints['hips'][0] + joints['knees'][0]) / 2 * i
        y = (joints['hips'][1] + joints['knees'][1]) / 2 * i
        point_lights.append((x, y))

    # Add lights along the arms
    for i in range(1, 4):
        x = (joints['shoulders'][0] + joints['elbows'][0]) / 2 * i
        y = (joints['shoulders'][1] + joints['elbows'][1]) / 2 * i
        point_lights.append((x, y))

    # Add lights along the torso
    for i in range(1, 3):
        x = joints['hips'][0] + (joints['shoulders'][0] - joints['hips'][0]) * i
        y = joints['hips'][1] + (joints['shoulders'][1] - joints['hips'][1]) * i
        point_lights.append((x, y))

    # Trim to exactly 15 points
    point_lights = point_lights[:15]

    return point_lights

# Main loop
def main():
    t = 0.0
    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        # Update joint positions based on time
        joints = update_joints(t)

        # Compute point-light positions
        point_lights = compute_point_lights(joints)

        # Draw point-lights
        for x, y in point_lights:
            pygame.draw.circle(screen, WHITE, (int(x + WIDTH / 2), int(y + HEIGHT / 2)), 3)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update time
        t += 1.0 / FPS

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
