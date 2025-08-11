
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Happy Woman Forward Rolling Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation settings
num_points = 15
point_radius = 3
clock = pygame.time.Clock()
fps = 60
animation_duration = 5 * fps  # 5 seconds
angle_step = 2 * math.pi / num_points

# Point light positions (simplified stick figure)
points = [
    (screen_width // 2, screen_height // 2),  # Center
    (screen_width // 2 + 50, screen_height // 2 - 50),  # Right arm
    (screen_width // 2 - 50, screen_height // 2 - 50),  # Left arm
    (screen_width // 2 + 70, screen_height // 2 + 50),  # Right leg
    (screen_width // 2 - 70, screen_height // 2 + 50),  # Left leg
]

# Animation loop
for frame in range(animation_duration):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    screen.fill(BLACK)

    # Update point positions for forward rolling motion
    angle = frame / fps * math.pi / 4  # Change this to control the rolling speed
    new_points = []
    for point in points:
        x, y = point
        new_x = x + math.cos(angle) * 50  # Modify the amplitude for different parts of the body
        new_y = y + math.sin(angle) * 50
        new_points.append((new_x, new_y))

    # Draw point lights
    for i, point in enumerate(new_points):
        pygame.draw.circle(screen, WHITE, point, point_radius)

    # Update the display
    pygame.display.flip()
    clock.tick(fps)

# Quit Pygame
pygame.quit()
