
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Center of the screen
center = (width // 2, height // 2)

# Base points for a human figure (relative coordinates)
base_points = [
    (0, -100),   # Head
    (-40, -80),  # Left shoulder
    (40, -80),   # Right shoulder
    (-60, -60),  # Left elbow
    (60, -60),   # Right elbow
    (-80, -40),  # Left hand
    (80, -40),   # Right hand
    (-30, 0),    # Left hip
    (30, 0),     # Right hip
    (-40, 40),   # Left knee
    (40, 40),    # Right knee
    (-50, 80),   # Left ankle
    (50, 80),    # Right ankle
    (0, -40),    # Torso midpoint
    (0, -20)     # Weight point
]

# Phase offsets for natural movement (upper body leads)
phase_offsets = [
    0.0,   # Head
    0.15,  # Left shoulder
    0.15,  # Right shoulder
    0.15,  # Left elbow
    0.15,  # Right elbow
    0.15,  # Left hand
    0.15,  # Right hand
    -0.1,  # Left hip
    -0.1,  # Right hip
    -0.1,  # Left knee
    -0.1,  # Right knee
    -0.1,  # Left ankle
    -0.1,  # Right ankle
    0.0,   # Torso
    0.2    # Weight point
]

# Animation parameters
theta = 0
angular_speed = 0.015  # Slow rotation for heavy weight
vertical_amplitude = 8  # Reduced bounce for heavy weight
vertical_frequency = 1.2

clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Update rotation angle
    theta += angular_speed

    # Calculate vertical displacement
    vertical_shift = vertical_amplitude * math.sin(theta * vertical_frequency)

    # Draw all points
    for i, (x_base, y_base) in enumerate(base_points):
        # Apply phase offset
        current_theta = theta + phase_offsets[i]

        # Rotate point
        x_rot = x_base * math.cos(current_theta) - y_base * math.sin(current_theta)
        y_rot = x_base * math.sin(current_theta) + y_base * math.cos(current_theta)

        # Apply vertical movement
        y_rot += vertical_shift

        # Convert to screen coordinates
        x = center[0] + x_rot
        y = center[1] + y_rot

        # Draw point
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)
