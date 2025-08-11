
import numpy as np
import pygame
import math
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman with Heavy Weight Lying Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define body parts as points (approximate coordinates)
body_parts = {
    'head': np.array([350, 100]),
    'neck': np.array([350, 150]),
    'torso': np.array([350, 200]),
    'pelvis': np.array([350, 300]),
    'left_hip': np.array([300, 300]),
    'right_hip': np.array([400, 300]),
    'left_knee': np.array([280, 350]),
    'right_knee': np.array([370, 350]),
    'left_ankle': np.array([250, 400]),
    'right_ankle': np.array([380, 400]),
    'left_shoulder': np.array([300, 150]),
    'right_shoulder': np.array([400, 150]),
    'left_elbow': np.array([280, 200]),
    'right_elbow': np.array([370, 200]),
    'left_wrist': np.array([250, 250]),
    'right_wrist': np.array([380, 250]),
    'left_hand': np.array([240, 300]),
    'right_hand': np.array([390, 300]),
    'left_foot': np.array([230, 450]),
    'right_foot': np.array([390, 450]),
}

# Define point-light positions as a list of body parts
point_lights = list(body_parts.values())

# Define animation parameters
frame_count = 0
total_frames = 120
amplitude = 50
frequency = 0.01
phase_shift = 0

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Update positions based on sine wave motion
    for i, point in enumerate(point_lights):
        angle = frequency * frame_count + phase_shift + i * 0.1
        offset = amplitude * np.sin(angle)
        new_point = point + np.array([0, offset])
        point_lights[i] = new_point

    # Draw point lights
    for point in point_lights:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    # Draw body structure (optional for visualization)
    for part in body_parts.values():
        pygame.draw.circle(screen, (100, 100, 100), (int(part[0]), int(part[1])), 3)

    # Draw ground
    pygame.draw.line(screen, (50, 50, 50), (0, 500), (800, 500), 2)

    # Draw heavy weight (simulated by lower body movement)
    pygame.draw.circle(screen, (200, 0, 0), (int(point_lights[18][0]), int(point_lights[18][1])), 10)

    # Update display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame_count += 1
    if frame_count >= total_frames:
        frame_count = 0

pygame.quit()
sys.exit()
