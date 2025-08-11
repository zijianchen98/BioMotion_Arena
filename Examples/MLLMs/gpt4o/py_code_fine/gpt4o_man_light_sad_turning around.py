
import pygame
import math

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Point-light positions for a sadman (15 points)
# Defining initial static 2D positions for representative points
sadman_structure = [
    (0, -200),  # Head
    (-30, -180), (30, -180),  # Shoulders (left, right)
    (-50, -140), (50, -140),  # Upper arms
    (-30, -60), (30, -60),  # Elbows
    (0, -20),  # Torso
    (-20, 40), (20, 40),  # Hips
    (-40, 120), (40, 120),  # Knees
    (-25, 200), (25, 200),  # Feet
    (0, -100)  # Weight representation
]

# Scale and center settings
CENTER = (WIDTH // 2, HEIGHT // 2)
SCALE = 1.5

# Rotation parameters
ROTATION_SPEED = 1  # Rotation speed in degrees per frame
current_angle = 0


def rotate_point(point, angle):
    """Rotate a point around the origin by a given angle."""
    x, y = point
    radians = math.radians(angle)
    cos_a, sin_a = math.cos(radians), math.sin(radians)
    return x * cos_a - y * sin_a, x * sin_a + y * cos_a


def transform_and_rotate(points, angle, center, scale):
    """Transform points: rotate them, scale, and shift to center."""
    transformed = []
    for p in points:
        rotated_point = rotate_point(p, angle)
        scaled_point = (rotated_point[0] * scale, rotated_point[1] * scale)
        centered_point = (center[0] + scaled_point[0], center[1] + scaled_point[1])
        transformed.append(centered_point)
    return transformed


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update animation state
    current_angle += ROTATION_SPEED
    current_angle %= 360  # Keep angle within range for clarity
    transformed_points = transform_and_rotate(sadman_structure, current_angle, CENTER, SCALE)

    # Render point lights as white circles
    for point in transformed_points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
