
import pygame
import math
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Happy Man Walking")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 30

# Define joint positions relative to a central body
# This is a simplified model of 15 joints for a walking human

def get_joints(phase):
    # phase is a float between 0 and 1, representing the walking cycle
    # We'll create a simple walking gait with 15 joints

    # Parameters
    walk_speed = 0.005  # controls how fast the walking cycle progresses
    step_height = 40    # how high the feet lift
    step_length = 60    # how far the legs move forward
    arm_swing = 20      # how much arms move

    # Calculate positions for each joint
    joints = []

    # Pelvis (center of body)
    pelvis_x = WIDTH // 2 + phase * step_length * 2
    pelvis_y = HEIGHT // 2
    joints.append((pelvis_x, pelvis_y))

    # Spine
    spine_x = pelvis_x
    spine_y = pelvis_y - 40
    joints.append((spine_x, spine_y))

    # Head
    head_x = spine_x
    head_y = spine_y - 40
    joints.append((head_x, head_y))

    # Left shoulder
    left_shoulder_x = spine_x - 20
    left_shoulder_y = spine_y
    joints.append((left_shoulder_x, left_shoulder_y))

    # Right shoulder
    right_shoulder_x = spine_x + 20
    right_shoulder_y = spine_y
    joints.append((right_shoulder_x, right_shoulder_y))

    # Left elbow
    left_elbow_x = left_shoulder_x - 30 * math.sin(2 * math.pi * (phase - 0.25))
    left_elbow_y = left_shoulder_y + 30 * math.cos(2 * math.pi * (phase - 0.25))
    joints.append((left_elbow_x, left_elbow_y))

    # Right elbow
    right_elbow_x = right_shoulder_x + 30 * math.sin(2 * math.pi * (phase - 0.25))
    right_elbow_y = right_shoulder_y + 30 * math.cos(2 * math.pi * (phase - 0.25))
    joints.append((right_elbow_x, right_elbow_y))

    # Left hand
    left_hand_x = left_elbow_x - 30 * math.sin(2 * math.pi * (phase - 0.5))
    left_hand_y = left_elbow_y + 30 * math.cos(2 * math.pi * (phase - 0.5))
    joints.append((left_hand_x, left_hand_y))

    # Right hand
    right_hand_x = right_elbow_x + 30 * math.sin(2 * math.pi * (phase - 0.5))
    right_hand_y = right_elbow_y + 30 * math.cos(2 * math.pi * (phase - 0.5))
    joints.append((right_hand_x, right_hand_y))

    # Left hip
    left_hip_x = pelvis_x - 20
    left_hip_y = pelvis_y
    joints.append((left_hip_x, left_hip_y))

    # Right hip
    right_hip_x = pelvis_x + 20
    right_hip_y = pelvis_y
    joints.append((right_hip_x, right_hip_y))

    # Left knee
    left_knee_x = left_hip_x + step_length * math.sin(2 * math.pi * (phase - 0.5))
    left_knee_y = left_hip_y - step_height * math.sin(2 * math.pi * (phase - 0.5)) - 30
    joints.append((left_knee_x, left_knee_y))

    # Right knee
    right_knee_x = right_hip_x + step_length * math.sin(2 * math.pi * (phase + 0.5))
    right_knee_y = right_hip_y - step_height * math.sin(2 * math.pi * (phase + 0.5)) - 30
    joints.append((right_knee_x, right_knee_y))

    # Left foot
    left_foot_x = left_knee_x + step_length * math.sin(2 * math.pi * (phase - 0.5))
    left_foot_y = left_knee_y - step_height * math.sin(2 * math.pi * (phase - 0.5)) - 30
    joints.append((left_foot_x, left_foot_y))

    # Right foot
    right_foot_x = right_knee_x + step_length * math.sin(2 * math.pi * (phase + 0.5))
    right_foot_y = right_knee_y - step_height * math.sin(2 * math.pi * (phase + 0.5)) - 30
    joints.append((right_foot_x, right_foot_y))

    return joints

def draw_joints(joints):
    for x, y in joints:
        pygame.draw.circle(SCREEN, WHITE, (int(x), int(y)), 5)

def main():
    phase = 0.0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill(BLACK)

        joints = get_joints(phase)
        draw_joints(joints)

        phase += 0.01
        if phase >= 1.0:
            phase = 0.0

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
