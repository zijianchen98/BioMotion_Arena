
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 30
clock = pygame.time.Clock()

# Joint structure for a human figure in point-light format (15 joints)
# We define positions relative to a central joint (torso center)
JOINTS = [
    (0, -200),   # Head
    (0, -120),   # Neck
    (0, 0),      # Torso center
    (-40, 60),   # Left shoulder
    (40, 60),    # Right shoulder
    (-40, 120),  # Left elbow
    (40, 120),   # Right elbow
    (-40, 180),  # Left hand
    (40, 180),   # Right hand
    (-30, 40),   # Left hip
    (30, 40),    # Right hip
    (-30, 100),  # Left knee
    (30, 100),   # Right knee
    (-30, 160),  # Left foot
    (30, 160),   # Right foot
]

# Convert to numpy array for easier manipulation
JOINTS = np.array(JOINTS, dtype=float)

# Animation parameters
bowing_angle = 0.0
bowing_speed = 0.05
max_bow = math.radians(30)

# Main animation loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Animate bowing motion
    bowing_angle += bowing_speed
    if bowing_angle > max_bow:
        bowing_speed = -abs(bowing_speed)
    elif bowing_angle < -max_bow:
        bowing_speed = abs(bowing_speed)

    # Apply bowing motion: tilt the upper body forward
    upper_body = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in upper_body:
        x, y = JOINTS[i]
        # Rotate around torso center (index 2)
        dx = x - JOINTS[2][0]
        dy = y - JOINTS[2][1]
        # Apply rotation
        new_x = dx * math.cos(bowing_angle) - dy * math.sin(bowing_angle)
        new_y = dx * math.sin(bowing_angle) + dy * math.cos(bowing_angle)
        JOINTS[i][0] = JOINTS[2][0] + new_x
        JOINTS[i][1] = JOINTS[2][1] + new_y

    # Draw the joints
    for x, y in JOINTS:
        pygame.draw.circle(screen, WHITE, (int(x + WIDTH/2), int(y + HEIGHT/2)), 5)

    # Draw the limbs (connect the joints)
    limbs = [
        (0, 1), (1, 2), (2, 9), (2, 10),
        (3, 4), (3, 5), (4, 6), (5, 7), (6, 8),
        (9, 11), (10, 12), (11, 13), (12, 14)
    ]
    for a, b in limbs:
        pygame.draw.line(screen, WHITE, 
                         (int(JOINTS[a][0] + WIDTH/2), int(JOINTS[a][1] + HEIGHT/2)),
                         (int(JOINTS[b][0] + WIDTH/2), int(JOINTS[b][1] + HEIGHT/2)), 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
