
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define a simple biomechanical model of a running human
# Each light represents a joint or a point on the body
# We'll simulate 15 points with realistic motion

# Joint positions (approximate for a running human)
# We'll use a simplified skeleton with 15 points
joint_positions = [
    (400, 300),  # Hip
    (350, 250),  # Left thigh
    (300, 200),  # Left calf
    (250, 250),  # Left foot
    (450, 250),  # Right thigh
    (500, 200),  # Right calf
    (550, 250),  # Right foot
    (400, 350),  # Torso
    (350, 400),  # Left upper arm
    (300, 450),  # Left lower arm
    (250, 400),  # Left hand
    (450, 400),  # Right upper arm
    (500, 450),  # Right lower arm
    (550, 400),  # Right hand
    (400, 500)   # Head
]

# Motion parameters (simplified sinusoidal motion for each joint)
# These parameters simulate a running motion
motion_params = [
    (0, 0, 0),        # Hip
    (0, 0.1, 0),      # Left thigh
    (0, 0.15, 0),     # Left calf
    (0, 0.2, 0),      # Left foot
    (0, 0.1, 0),      # Right thigh
    (0, 0.15, 0),     # Right calf
    (0, 0.2, 0),      # Right foot
    (0, 0.05, 0),     # Torso
    (0, 0.1, 0),      # Left upper arm
    (0, 0.15, 0),     # Left lower arm
    (0, 0.2, 0),      # Left hand
    (0, 0.1, 0),      # Right upper arm
    (0, 0.15, 0),     # Right lower arm
    (0, 0.2, 0),      # Right hand
    (0, 0.05, 0)      # Head
]

# Animation loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Update and draw each point-light
    for i in range(len(joint_positions)):
        x, y = joint_positions[i]
        phase, amplitude, freq = motion_params[i]
        angle = math.sin(pygame.time.get_ticks() * freq * 0.001 + phase)
        dx = amplitude * angle
        dy = amplitude * angle * 0.5  # Slight vertical offset for realism
        new_x = x + dx
        new_y = y + dy

        # Ensure the point stays within the screen
        new_x = max(0, min(WIDTH, new_x))
        new_y = max(0, min(HEIGHT, new_y))

        pygame.draw.circle(screen, WHITE, (int(new_x), int(new_y)), 4)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
