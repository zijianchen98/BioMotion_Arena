
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

# Configuration parameters
scale = 3  # Scaling factor for point positions
screen_center_x = width // 2
screen_center_y = height // 2

# Initial points relative to local waist position (0, 20)
local_points = [
    (0, 50),    # Head
    (0, 45),    # Neck
    (-10, 40), (10, 40),  # Shoulders
    (-15, 35), (15, 35),  # Elbows
    (-20, 30), (20, 30),  # Hands
    (0, 30),    # Chest
    (-10, 15), (10, 15),  # Hips
    (-15, 10), (15, 10),  # Knees
    (-20, 0), (20, 0)     # Feet
]

# Scale points and convert to screen coordinates
initial_points = [(x * scale, y * scale) for (x, y) in local_points]
waist_offset_y = 20 * scale  # Local waist y-position

# Animation parameters
angular_speed = 0.03
r = 20 * scale  # Radius based on waist to feet
forward_speed = angular_speed * r
theta = 0
waist_x = screen_center_x
waist_y = screen_center_y

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update position
    waist_x += forward_speed
    theta += angular_speed

    # Reset position when off screen
    if waist_x > width + 100:
        waist_x = -100
        theta = 0

    # Draw each point
    for (x, y) in initial_points:
        dx = x  # Original x is already relative to local waist
        dy = y - waist_offset_y  # Adjust for local waist y

        # Apply clockwise rotation
        rotated_x = dx * math.cos(theta) + dy * math.sin(theta)
        rotated_y = -dx * math.sin(theta) + dy * math.cos(theta)

        # Calculate screen position
        new_x = waist_x + rotated_x
        new_y = waist_y + rotated_y

        # Draw
        pygame.draw.circle(screen, WHITE, (int(new_x), int(new_y)), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
