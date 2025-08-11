
import numpy as np
import pygame
import math
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Running - Point-Light Stimulus")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Number of point lights
NUM_LIGHTS = 15

# Define a basic skeleton structure for a running woman
# Positions are relative to the center of the screen
# Each joint is represented by a position (x, y)
skeleton = {
    'hips': (WIDTH//2, HEIGHT*0.6),
    'left_knee': (WIDTH//2 - 100, HEIGHT*0.6 + 50),
    'left_ankle': (WIDTH//2 - 120, HEIGHT*0.6 + 100),
    'right_knee': (WIDTH//2 + 100, HEIGHT*0.6 + 50),
    'right_ankle': (WIDTH//2 + 120, HEIGHT*0.6 + 100),
    'torso': (WIDTH//2, HEIGHT*0.4),
    'left_shoulder': (WIDTH//2 - 50, HEIGHT*0.4),
    'left_elbow': (WIDTH//2 - 80, HEIGHT*0.45),
    'left_hand': (WIDTH//2 - 100, HEIGHT*0.5),
    'right_shoulder': (WIDTH//2 + 50, HEIGHT*0.4),
    'right_elbow': (WIDTH//2 + 80, HEIGHT*0.45),
    'right_hand': (WIDTH//2 + 100, HEIGHT*0.5),
    'neck': (WIDTH//2, HEIGHT*0.3),
    'head': (WIDTH//2, HEIGHT*0.25),
}

# Define joint connections
connections = [
    ('hips', 'left_knee'),
    ('left_knee', 'left_ankle'),
    ('hips', 'right_knee'),
    ('right_knee', 'right_ankle'),
    ('hips', 'torso'),
    ('torso', 'left_shoulder'),
    ('left_shoulder', 'left_elbow'),
    ('left_elbow', 'left_hand'),
    ('torso', 'right_shoulder'),
    ('right_shoulder', 'right_elbow'),
    ('right_elbow', 'right_hand'),
    ('torso', 'neck'),
    ('neck', 'head'),
]

# Define a function to calculate joint positions based on a running motion
def update_skeleton(t, phase):
    # Base positions
    base = {k: np.array(v) for k, v in skeleton.items()}
    
    # Define a sine wave for leg movement
    leg_amplitude = 30
    leg_frequency = 0.05
    leg_phase = phase + 1.0
    leg_offset = 60
    
    # Define a sine wave for arm movement
    arm_amplitude = 20
    arm_frequency = 0.05
    arm_phase = phase + 0.5
    arm_offset = 0
    
    # Update left leg
    left_knee = base['left_knee'] + np.array([0, leg_amplitude * math.sin(leg_frequency * t + leg_phase)])
    left_ankle = base['left_ankle'] + np.array([0, leg_amplitude * math.sin(leg_frequency * t + leg_phase + leg_offset)])
    
    # Update right leg
    right_knee = base['right_knee'] + np.array([0, leg_amplitude * math.sin(leg_frequency * t + leg_phase + 1.0)])
    right_ankle = base['right_ankle'] + np.array([0, leg_amplitude * math.sin(leg_frequency * t + leg_phase + 1.0 + leg_offset)])
    
    # Update arms
    left_hand = base['left_hand'] + np.array([arm_amplitude * math.sin(arm_frequency * t + arm_phase), 0])
    right_hand = base['right_hand'] + np.array([arm_amplitude * math.sin(arm_frequency * t + arm_phase + 1.0), 0])
    
    # Update torso and head for a running motion
    torso = base['torso'] + np.array([10 * math.sin(0.02 * t + phase), 0])
    neck = base['neck'] + np.array([10 * math.sin(0.02 * t + phase), 0])
    head = base['head'] + np.array([10 * math.sin(0.02 * t + phase), 0])
    
    # Update the skeleton positions
    updated_skeleton = {
        'hips': base['hips'],
        'left_knee': left_knee,
        'left_ankle': left_ankle,
        'right_knee': right_knee,
        'right_ankle': right_ankle,
        'torso': torso,
        'left_shoulder': base['left_shoulder'],
        'left_elbow': base['left_elbow'],
        'left_hand': left_hand,
        'right_shoulder': base['right_shoulder'],
        'right_elbow': base['right_elbow'],
        'right_hand': right_hand,
        'neck': neck,
        'head': head,
    }
    
    return updated_skeleton

# Generate point lights based on skeleton joints
def generate_point_lights(skeleton):
    lights = []
    for joint in skeleton:
        x = int(skeleton[joint][0])
        y = int(skeleton[joint][1])
        lights.append((x, y))
    return lights

# Main loop
running = True
t = 0.0
phase = 0.0
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update skeleton
    updated_skeleton = update_skeleton(t, phase)
    point_lights = generate_point_lights(updated_skeleton)

    # Draw background
    screen.fill(BLACK)

    # Draw point lights
    for x, y in point_lights:
        pygame.draw.circle(screen, WHITE, (x, y), 3)

    # Draw skeleton connections
    for a, b in connections:
        xa, ya = updated_skeleton[a]
        xb, yb = updated_skeleton[b]
        pygame.draw.line(screen, WHITE, (xa, ya), (xb, yb), 2)

    # Update time and phase
    t += 0.05
    phase += 0.01

    # Update display
    pygame.display.flip()

pygame.quit()
