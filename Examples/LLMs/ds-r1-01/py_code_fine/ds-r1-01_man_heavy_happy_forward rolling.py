
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
r = 40  # Body scale radius
angular_velocity = 0.05  # Rotation speed (radians per frame)
v = r * angular_velocity  # Forward velocity (pixels per frame)

# Define 15 body points relative to center (dx, dy)
points_relative = [
    (0, -r),               # Head
    (-0.3*r, -0.7*r),      # Left shoulder
    (0.3*r, -0.7*r),       # Right shoulder
    (-0.5*r, -0.5*r),      # Left elbow
    (0.5*r, -0.5*r),       # Right elbow
    (-0.6*r, -0.3*r),      # Left hand
    (0.6*r, -0.3*r),       # Right hand
    (-0.2*r, 0),           # Left hip
    (0.2*r, 0),            # Right hip
    (-0.3*r, 0.3*r),       # Left knee
    (0.3*r, 0.3*r),        # Right knee
    (-0.2*r, 0.6*r),       # Left ankle
    (0.2*r, 0.6*r),        # Right ankle
    (-0.1*r, 0.8*r),       # Left foot
    (0.1*r, 0.8*r)         # Right foot
]

# Initial position
x_center = -100
y_center = height - 0.8*r  # Vertical position for ground contact
theta = 0  # Rotation angle

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update position and rotation
    x_center += v
    theta += angular_velocity

    # Reset position when off-screen
    if x_center - r > width:
        x_center = -100

    # Draw all body points
    for dx, dy in points_relative:
        # Apply rotation matrix
        x = x_center + dx * math.cos(theta) - dy * math.sin(theta)
        y = y_center + dx * math.sin(theta) + dy * math.cos(theta)
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
