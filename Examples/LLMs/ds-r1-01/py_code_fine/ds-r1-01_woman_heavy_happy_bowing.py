
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point parameters
point_radius = 5

# Define initial relative positions of points (hip-centered)
points = [
    (0, -100),    # Head (0)
    (-40, -80), (40, -80),  # Shoulders (1, 2)
    (-60, -60), (60, -60),  # Elbows (3,4)
    (-80, -40), (80, -40),  # Hands (5,6)
    (0, -60),     # Torso (7)
    (-20, 0), (20, 0),      # Hips (8,9)
    (-30, 40), (30, 40),    # Knees (10,11)
    (-40, 80), (40, 80),    # Feet (12,13)
    (0, -20)      # Spine (14)
]

# Indices of upper body points
upper_body = [0, 1, 2, 3, 4, 5, 6, 7, 14]

# Animation parameters
max_angle = math.radians(30)  # Max 30 degrees bow
speed = 0.05
time = 0

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate current angle
    angle = max_angle * math.sin(time)
    time += 0.05

    center_x, center_y = width // 2, height // 2

    for i, (x, y) in enumerate(points):
        if i in upper_body:
            # Rotate upper body points
            x_rot = x * math.cos(angle) + y * math.sin(angle)
            y_rot = -x * math.sin(angle) + y * math.cos(angle)
        elif i in [10, 11]:  # Knees bending
            y_offset = 15 * math.sin(angle)
            x_rot, y_rot = x, y + y_offset
        else:
            x_rot, y_rot = x, y

        # Convert to screen coordinates and draw
        pos = (int(center_x + x_rot), int(center_y + y_rot))
        pygame.draw.circle(screen, WHITE, pos, point_radius)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
