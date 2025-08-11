
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Forward Roll")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 30
POINT_RADIUS = 4
NUM_POINTS = 15
BODY_RADIUS = 50
ANGULAR_SPEED = 0.08  # Radians per frame
FORWARD_SPEED = ANGULAR_SPEED * BODY_RADIUS

# Biomechanical point configuration (relative to center)
points_relative = [
    (0, -45),    # Head
    (-15, -40),  # Left shoulder
    (15, -40),   # Right shoulder
    (-25, -30),  # Left elbow
    (25, -30),   # Right elbow
    (-35, -20),  # Left hand
    (35, -20),   # Right hand
    (-20, 0),    # Left hip
    (20, 0),     # Right hip
    (-25, 15),   # Left knee
    (25, 15),    # Right knee
    (-30, 30),   # Left foot
    (30, 30),    # Right foot
    (0, -20),    # Torso
    (0, -35)     # Neck
]

# Initialize motion state
center_x = -BODY_RADIUS
center_y = height // 2
angle = 0

clock = pygame.time.Clock()

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Update position and rotation
    center_x += FORWARD_SPEED
    angle = (angle + ANGULAR_SPEED) % (2 * math.pi)
    
    # Reset position when off-screen
    if center_x > width + BODY_RADIUS:
        center_x = -BODY_RADIUS

    # Draw all points
    for dx, dy in points_relative:
        # Apply rotation matrix
        x_rot = dx * math.cos(angle) - dy * math.sin(angle)
        y_rot = dx * math.sin(angle) + dy * math.cos(angle)
        
        # Calculate screen position
        pos_x = int(center_x + x_rot)
        pos_y = int(center_y + y_rot)
        
        pygame.draw.circle(screen, WHITE, (pos_x, pos_y), POINT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
