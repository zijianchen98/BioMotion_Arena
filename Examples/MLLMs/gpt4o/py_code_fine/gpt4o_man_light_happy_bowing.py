
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion (Bowing Animation)")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Define the joint positions in hapyman figure
# Starting from head to feet (15 points)
points = [
    (0, -100),  # Head
    (-20, -80), (20, -80),  # Shoulders
    (-40, -60), (0, -60), (40, -60),  # Elbows and torso
    (-60, -40), (0, -40), (60, -40),  # Hands and torso continuation
    (-20, 0), (20, 0),  # Hips
    (-40, 40), (40, 40),  # Knees
    (-60, 80), (60, 80),  # Feet
]

# Scaling and offset to center the figure
SCALE = 4
OFFSET_X, OFFSET_Y = WIDTH // 2, HEIGHT // 2 - 50

# Bowing animation parameters
bowing_speed = 0.05  # Speed of the bowing motion
bowing_amplitude = 30  # Maximum angular displacement
bowing_angle = 0

def rotate_point(x, y, angle):
    """Rotate a point (x, y) around the origin by a given angle (in radians)."""
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    x_rot = x * cos_theta - y * sin_theta
    y_rot = x * sin_theta + y * cos_theta
    return x_rot, y_rot

def transform_points(points, angle):
    """Apply transformations to the points."""
    transformed_points = []
    for x, y in points:
        # Rotate points to simulate bowing motion
        x_rot, y_rot = rotate_point(x, y, angle)
        # Apply scaling and offset
        x_final = int(x_rot * SCALE + OFFSET_X)
        y_final = int(y_rot * SCALE + OFFSET_Y)
        transformed_points.append((x_final, y_final))
    return transformed_points

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update the bowing angle
    bowing_angle = math.sin(pygame.time.get_ticks() * bowing_speed) * math.radians(bowing_amplitude)

    # Transform points for the current animation frame
    animated_points = transform_points(points, bowing_angle)

    # Draw the 15 white points on the screen
    for point in animated_points:
        pygame.draw.circle(screen, WHITE, point, 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
