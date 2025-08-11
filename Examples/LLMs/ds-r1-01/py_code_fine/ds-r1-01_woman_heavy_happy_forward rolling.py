
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light configuration
points_relative = [
    (0, -50),    # head
    (-15, -40),  # left shoulder
    (15, -40),   # right shoulder
    (-25, -30),  # left elbow
    (25, -30),   # right elbow
    (-35, -20),  # left hand
    (35, -20),   # right hand
    (0, -30),    # upper torso
    (0, -10),    # mid torso
    (0, 10),     # lower torso/hips
    (-15, 20),   # left knee
    (15, 20),    # right knee
    (-25, 40),   # left foot
    (25, 40),    # right foot
    (0, 0)       # center (belly)
]

# Animation parameters
angular_speed = 0.02
radius = 50  # maximum distance from center to a point
speed = radius * angular_speed
ground_y = 500  # Ground level

# Initial positions
cx = 100
cy = 300
theta = 0

# Main animation loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update position and rotation
    theta += angular_speed
    cx += speed
    if cx > WIDTH:
        cx = 100  # Reset position when reaching screen edge

    # Calculate rotated points and find lowest point
    rotated_points = []
    for (px, py) in points_relative:
        rx = px * math.cos(theta) - py * math.sin(theta)
        ry = px * math.sin(theta) + py * math.cos(theta)
        rotated_points.append((rx, ry))

    # Adjust vertical position to maintain ground contact
    max_ry = max(ry for (rx, ry) in rotated_points)
    current_cy = ground_y - max_ry

    # Draw all points
    for (rx, ry) in rotated_points:
        pos_x = int(cx + rx)
        pos_y = int(current_cy + ry)
        pygame.draw.circle(screen, WHITE, (pos_x, pos_y), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
