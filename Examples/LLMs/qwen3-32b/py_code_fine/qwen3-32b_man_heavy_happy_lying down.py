
import pygame
import math
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Happyman Lying Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 30

# Define joint positions in relative coordinates (based on a 15-point biological motion model)
# We will animate a "lying down" motion with a heavy and happy posture

# Initial joint positions (relative to the body's center)
joint_positions = [
    (0, -200),  # Head
    (-50, -100), # Left shoulder
    (50, -100),  # Right shoulder
    (-80, 0),    # Left elbow
    (80, 0),     # Right elbow
    (-120, 100), # Left hand
    (120, 100),  # Right hand
    (-50, 100),  # Left hip
    (50, 100),   # Right hip
    (-80, 200),  # Left knee
    (80, 200),   # Right knee
    (-50, 300),  # Left foot
    (50, 300),   # Right foot
    (0, -100),   # Torso top
    (0, 100),    # Torso bottom
]

# Convert to actual positions (centered on screen)
center_x, center_y = WIDTH // 2, HEIGHT // 2
joint_positions = [(x + center_x, y + center_y) for x, y in joint_positions]

# Animation parameters
angle = 0
angle_increment = 0.02
amplitude = 10  # For a heavy and smooth motion

# Main loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation (lying down with a slight bounce to show happiness and weight)
    angle += angle_increment
    bounce = amplitude * math.sin(angle)

    # Apply small motion to joints to simulate lying down with a happy, heavy feel
    for i in range(len(joint_positions)):
        x, y = joint_positions[i]
        if i in [0, 1, 2, 13, 14]:  # Head, shoulders, and torso: slight vertical motion
            y += bounce * 0.5
        elif i in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:  # Limbs: subtle motion
            y += bounce * 0.2
        joint_positions[i] = (x, y)

    # Draw the points
    for pos in joint_positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
