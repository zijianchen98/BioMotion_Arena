
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define the relative positions of each joint (relative to the center)
points_rel = [
    (0, -50),    # Head
    (-30, -40),  # Left shoulder
    (30, -40),   # Right shoulder
    (-50, -30),  # Left elbow
    (50, -30),   # Right elbow
    (-60, -20),  # Left hand
    (60, -20),   # Right hand
    (-20, 20),   # Left hip
    (20, 20),    # Right hip
    (-30, 50),   # Left knee
    (30, 50),    # Right knee
    (-20, 80),   # Left ankle
    (20, 80),    # Right ankle
    (-25, 90),   # Left foot
    (25, 90)     # Right foot
]

# Main loop variables
theta = 0  # Rotation angle
phase = 0  # Phase for limb movement
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    # Update angles and phase
    theta += 0.02  # Rotation speed
    phase += 0.05  # Limb movement speed

    # Calculate positions of all points
    points = []
    for i in range(len(points_rel)):
        x0, y0 = points_rel[i]
        dx, dy = 0, 0

        # Apply limb-specific movements
        if i == 5:  # Left hand
            dx = 10 * math.sin(phase)
        elif i == 6:  # Right hand
            dx = 10 * math.sin(phase + math.pi)
        elif i == 13:  # Left foot
            dy = 8 * math.sin(phase + math.pi)
        elif i == 14:  # Right foot
            dy = 8 * math.sin(phase)

        # Apply displacement
        x = x0 + dx
        y = y0 + dy

        # Rotate the point
        x_rot = x * math.cos(theta) - y * math.sin(theta)
        y_rot = x * math.sin(theta) + y * math.cos(theta)

        # Convert to screen coordinates
        screen_x = int(x_rot + width/2)
        screen_y = int(y_rot + height/2)
        points.append((screen_x, screen_y))

    # Draw all points
    for p in points:
        pygame.draw.circle(screen, white, p, 3)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
