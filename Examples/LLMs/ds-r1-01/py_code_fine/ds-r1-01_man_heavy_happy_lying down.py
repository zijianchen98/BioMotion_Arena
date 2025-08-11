
import pygame
import math

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Define body configuration
hips_x, hips_y = 400, 250  # Center point for rotation

# Standing positions relative to hips (x, y)
standing_points_relative = [
    (0, -150),    # Head
    (0, -100),    # Neck
    (-50, -100),  # Left shoulder
    (50, -100),   # Right shoulder
    (-80, -50),   # Left elbow
    (80, -50),    # Right elbow
    (-100, 0),    # Left wrist
    (100, 0),     # Right wrist
    (-30, 50),    # Left knee
    (30, 50),     # Right knee
    (-30, 100),   # Left ankle
    (30, 100),    # Right ankle
    (0, -50),     # Torso midpoint
    (-40, -120),  # Left ear (additional point)
    (40, -120)    # Right ear (additional point)
]

# Animation parameters
theta = 0.0  # Initial angle (radians)
angular_velocity = 0.02  # Rotation speed

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Update rotation angle (lie back motion)
    theta -= angular_velocity
    if theta < -math.pi/2:  # Limit to 90 degrees backward
        theta = -math.pi/2

    # Calculate current positions
    current_points = []
    for x_rel, y_rel in standing_points_relative:
        # Apply rotation matrix
        x_rot = x_rel * math.cos(theta) - y_rel * math.sin(theta)
        y_rot = x_rel * math.sin(theta) + y_rel * math.cos(theta)
        # Convert to screen coordinates
        x = hips_x + x_rot
        y = hips_y + y_rot
        current_points.append((x, y))

    # Draw all points
    for x, y in current_points:
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
