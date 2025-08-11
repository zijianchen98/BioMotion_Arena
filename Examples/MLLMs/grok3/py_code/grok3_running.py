
import pygame
import numpy as np
from math import sin, cos, pi

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation of Running Man")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initial positions and motion parameters for 15 point-lights (head, torso, arms, legs, joints)
# Approximate coordinates based on a running man silhouette
base_positions = np.array([
    [200, 100],  # Head
    [200, 150],  # Neck
    [200, 200],  # Chest
    [200, 250],  # Pelvis
    [180, 150],  # Left shoulder
    [220, 150],  # Right shoulder
    [160, 200],  # Left elbow
    [240, 200],  # Right elbow
    [140, 250],  # Left hip
    [260, 250],  # Right hip
    [120, 300],  # Left knee
    [280, 300],  # Right knee
    [110, 400],  # Left ankle
    [290, 400],  # Right ankle
    [200, 350]   # Torso midpoint
])

# Motion parameters (sinusoidal for natural running motion)
amplitude = 20
frequency = 0.05
phase = 0
speed = 2

# Main loop
running = True
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update phase for animation
    phase = frame * frequency

    # Calculate new positions for each point-light
    positions = base_positions.copy()
    for i in range(len(positions)):
        if i in [0, 1, 2, 3, 14]:  # Head, neck, chest, pelvis, torso midpoint (vertical oscillation)
            positions[i][1] += amplitude * sin(phase)
        elif i in [4, 5]:  # Shoulders (horizontal arm swing)
            positions[i][0] += amplitude * cos(phase + pi/2)
            positions[i][1] += amplitude * sin(phase)
        elif i in [6, 7]:  # Elbows (follow shoulders with lag)
            positions[i][0] = positions[i-2][0] + amplitude * cos(phase + pi)
            positions[i][1] = positions[i-2][1] + amplitude * sin(phase + pi)
        elif i in [8, 9]:  # Hips (opposite leg motion)
            positions[i][0] += amplitude * cos(phase + pi)
            positions[i][1] += amplitude * sin(phase + pi/2)
        elif i in [10, 11]:  # Knees (follow hips with lag)
            positions[i][0] = positions[i-2][0] + amplitude * cos(phase + 3*pi/2)
            positions[i][1] = positions[i-2][1] + amplitude * sin(phase + pi)
        elif i in [12, 13]:  # Ankles (follow knees with lag)
            positions[i][0] = positions[i-2][0] + amplitude * cos(phase + pi)
            positions[i][1] = positions[i-2][1] + amplitude * sin(phase + 3*pi/2)

        # Ensure points stay within screen
        positions[i][0] = max(0, min(WIDTH-1, positions[i][0]))
        positions[i][1] = max(0, min(HEIGHT-1, positions[i][1]))

    # Draw point-lights
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS
    frame += 1

pygame.quit()
