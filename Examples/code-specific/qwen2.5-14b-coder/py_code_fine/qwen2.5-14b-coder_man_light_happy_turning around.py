
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Happyman model (simplified representation)
# Define key points of the body
body_points = [
    (400, 300),  # Center of mass
    (350, 250),  # Left shoulder
    (450, 250),  # Right shoulder
    (300, 350),  # Left hip
    (500, 350),  # Right hip
    (250, 400),  # Left knee
    (550, 400),  # Right knee
    (200, 450),  # Left ankle
    (600, 450)   # Right ankle
]

# Function to rotate a point around another point
def rotate_point(point, origin, angle):
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

# Main loop
clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Rotate the body points
    rotated_body_points = [rotate_point(p, (400, 300), angle) for p in body_points]

    # Calculate positions of the point-lights
    light_positions = []
    for i in range(NUM_LIGHTS):
        # Distribute lights across the body points
        light_x = rotated_body_points[i % len(rotated_body_points)][0]
        light_y = rotated_body_points[i % len(rotated_body_points)][1]
        light_positions.append((light_x, light_y))

    # Draw the point-lights
    for pos in light_positions:
        pygame.draw.circle(screen, WHITE, pos, 5)

    # Update the display
    pygame.display.flip()

    # Increment the angle for rotation
    angle += 0.05

    # Cap the frame rate
    clock.tick(FPS)
