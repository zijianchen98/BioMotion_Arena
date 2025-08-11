
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Forward Roll")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define the relative positions of the 15 points (joints) in a standing position
points_relative = [
    (0, -50),    # Head
    (-15, -40),  # Left shoulder
    (15, -40),   # Right shoulder
    (-25, -30),  # Left elbow
    (25, -30),   # Right elbow
    (-30, -20),  # Left hand
    (30, -20),   # Right hand
    (0, -30),    # Mid-torso
    (-15, -20),  # Left hip
    (15, -20),   # Right hip
    (-15, 0),    # Left knee
    (15, 0),     # Right knee
    (-15, 20),   # Left foot
    (15, 20),    # Right foot
    (0, -10)     # Mid-hips
]

# Parameters for the animation
r = 50  # Approximate radius of the body's rotation
speed_rotation = 0.05  # Radians per frame
speed_forward = r * speed_rotation  # Pixels per frame

# Initial state
theta = 0.0
center_x = 0.0
center_y = height // 2  # Vertical center
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(black)

    # Update position and rotation
    theta += speed_rotation
    center_x += speed_forward

    # Reset position when off screen to the right
    if center_x > width + 50:
        center_x = -50
        theta = 0.0

    # Draw each point
    for dx, dy in points_relative:
        # Apply rotation
        x_rot = dx * math.cos(theta) - dy * math.sin(theta)
        y_rot = dx * math.sin(theta) + dy * math.cos(theta)
        # Translate to screen coordinates
        x = center_x + x_rot
        y = center_y + y_rot
        # Draw the point
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    # Update display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
