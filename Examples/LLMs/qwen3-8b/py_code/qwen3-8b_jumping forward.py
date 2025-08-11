
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Jumping Man")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Number of point lights
NUM_LIGHTS = 15

# Define body parts and their positions relative to the center (hip)
body_parts = {
    'hip': (0, 0),
    'pelvis': (0, 0),
    'torso': (0, -50),
    'shoulder_left': (-30, -70),
    'shoulder_right': (30, -70),
    'elbow_left': (-40, -90),
    'elbow_right': (40, -90),
    'wrist_left': (-50, -110),
    'wrist_right': (50, -110),
    'hip_left': (-30, 0),
    'hip_right': (30, 0),
    'knee_left': (-30, 30),
    'knee_right': (30, 30),
    'ankle_left': (-30, 60),
    'ankle_right': (30, 60),
}

# Define joints and their connections
joints = [
    ('hip', 'pelvis'),
    ('pelvis', 'torso'),
    ('torso', 'shoulder_left'),
    ('torso', 'shoulder_right'),
    ('shoulder_left', 'elbow_left'),
    ('elbow_left', 'wrist_left'),
    ('shoulder_right', 'elbow_right'),
    ('elbow_right', 'wrist_right'),
    ('hip', 'hip_left'),
    ('hip', 'hip_right'),
    ('hip_left', 'knee_left'),
    ('knee_left', 'ankle_left'),
    ('hip_right', 'knee_right'),
    ('knee_right', 'ankle_right'),
]

# Initialize point lights
lights = []
for part in body_parts:
    x, y = body_parts[part]
    lights.append({
        'pos': (x, y),
        'radius': 3,
        'color': WHITE,
        'active': True,
    })

# Jumping parameters
gravity = 0.5
velocity = 0
jump_height = 100
jump_duration = 20
jump_timer = 0

# Animation loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Jumping logic
    if jump_timer > 0:
        jump_timer -= 1
        if jump_timer == 0:
            velocity = -15
        else:
            velocity += gravity
        y = 0
        for part in body_parts:
            x, y = body_parts[part]
            body_parts[part] = (x, y + velocity)

    # Update lights
    for light in lights:
        if light['active']:
            x, y = light['pos']
            pygame.draw.circle(screen, light['color'], (int(x), int(y)), light['radius'])

    # Draw joints
    for joint in joints:
        part1, part2 = joint
        x1, y1 = body_parts[part1]
        x2, y2 = body_parts[part2]
        pygame.draw.line(screen, WHITE, (int(x1), int(y1)), (int(x2), int(y2)), 1)

    # Update display
    pygame.display.flip()

pygame.quit()
