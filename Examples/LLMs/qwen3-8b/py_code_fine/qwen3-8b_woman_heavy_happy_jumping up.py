
import numpy as np
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Woman Jumping with Point-Lights")
clock = pygame.time.Clock()

# Define body parts and their positions (simplified for animation)
body_parts = {
    'hips': (400, 300),
    'left_knee': (350, 350),
    'right_knee': (450, 350),
    'left_ankle': (320, 400),
    'right_ankle': (480, 400),
    'left_shoulder': (300, 250),
    'right_shoulder': (500, 250),
    'left_elbow': (270, 280),
    'right_elbow': (530, 280),
    'left_wrist': (240, 310),
    'right_wrist': (560, 310),
    'head': (400, 200),
    'left_hand': (240, 310),
    'right_hand': (560, 310),
    'left_foot': (320, 400),
    'right_foot': (480, 400)
}

# Define point-light positions as a list of tuples
point_lights = list(body_parts.values())

# Animation parameters
jump_height = 100
jump_speed = 0.5
gravity = 0.5
current_jump = 0
is_jumping = False
frame = 0

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Jumping animation logic
    if is_jumping:
        current_jump += jump_speed
        if current_jump >= jump_height:
            current_jump = jump_height
            is_jumping = False
        elif current_jump < 0:
            current_jump = 0
            is_jumping = False
    else:
        current_jump = 0

    # Update positions based on jumping
    for part in body_parts:
        if part in ['hips', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle',
                    'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
                    'left_wrist', 'right_wrist', 'head', 'left_hand', 'right_hand',
                    'left_foot', 'right_foot']:
            x, y = body_parts[part]
            # Apply jump to hips and adjust other parts accordingly
            if part == 'hips':
                y = 300 - int(current_jump)
            elif part == 'head':
                y = 200 - int(current_jump * 0.5)
            elif part == 'left_knee' or part == 'right_knee':
                y = 350 - int(current_jump * 0.3)
            elif part == 'left_ankle' or part == 'right_ankle':
                y = 400 - int(current_jump * 0.15)
            elif part == 'left_shoulder' or part == 'right_shoulder':
                y = 250 - int(current_jump * 0.2)
            elif part == 'left_elbow' or part == 'right_elbow':
                y = 280 - int(current_jump * 0.1)
            elif part == 'left_wrist' or part == 'right_wrist':
                y = 310 - int(current_jump * 0.05)
            elif part == 'left_hand' or part == 'right_hand':
                y = 310 - int(current_jump * 0.025)
            elif part == 'left_foot' or part == 'right_foot':
                y = 400 - int(current_jump * 0.05)
            body_parts[part] = (x, y)

    # Draw point-lights
    for point in point_lights:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    # Draw limbs for clarity (optional)
    for part in body_parts:
        if part in ['hips', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle']:
            pygame.draw.line(screen, WHITE, body_parts[part], body_parts['left_ankle'], 2)
            pygame.draw.line(screen, WHITE, body_parts[part], body_parts['right_ankle'], 2)
        if part in ['left_knee', 'right_knee', 'left_ankle', 'right_ankle']:
            pygame.draw.line(screen, WHITE, body_parts[part], body_parts['left_foot'], 2)
            pygame.draw.line(screen, WHITE, body_parts[part], body_parts['right_foot'], 2)
        if part in ['left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow']:
            pygame.draw.line(screen, WHITE, body_parts[part], body_parts['left_wrist'], 2)
            pygame.draw.line(screen, WHITE, body_parts[part], body_parts['right_wrist'], 2)
        if part in ['left_elbow', 'right_elbow', 'left_wrist', 'right_wrist']:
            pygame.draw.line(screen, WHITE, body_parts[part], body_parts['left_hand'], 2)
            pygame.draw.line(screen, WHITE, body_parts[part], body_parts['right_hand'], 2)
        if part == 'head':
            pygame.draw.line(screen, WHITE, body_parts[part], body_parts['left_shoulder'], 2)
            pygame.draw.line(screen, WHITE, body_parts[part], body_parts['right_shoulder'], 2)

    # Jump trigger (spacebar)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True

    pygame.display.flip()

pygame.quit()
sys.exit()
