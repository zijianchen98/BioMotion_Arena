
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Forward Roll")
clock = pygame.Clock()

# Body point configuration (relative to center in upright position)
points_relative = [
    (0, -50),    # Head
    (15, -40), (-15, -40),  # Shoulders
    (25, -30), (-25, -30),  # Elbows
    (35, -20), (-35, -20),  # Hands
    (20, 0), (-20, 0),      # Hips
    (30, 20), (-30, 20),    # Knees
    (40, 40), (-40, 40),    # Feet
    (0, -25)                # Mid-torso
]

# Verify 15 points
assert len(points_relative) == 15, "Should have exactly 15 points"

# Animation parameters
angular_velocity = 0.05
body_radius = 60
forward_velocity = angular_velocity * body_radius
center = [width//4, height//2]
angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Update position and angle
    center[0] += forward_velocity
    angle += angular_velocity

    # Reset position when off-screen
    if center[0] > width + body_radius:
        center[0] = -body_radius

    # Draw all points
    for x_rel, y_rel in points_relative:
        # Apply rotation matrix
        x_rot = x_rel * math.cos(angle) - y_rel * math.sin(angle)
        y_rot = x_rel * math.sin(angle) + y_rel * math.cos(angle)
        
        # Calculate screen position
        x = center[0] + x_rot
        y = center[1] + y_rot
        
        # Draw point
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 6)

    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()
sys.exit()
