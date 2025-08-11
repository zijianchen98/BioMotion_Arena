
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Define 15 points representing key body parts of the sadman
# Initial positions in a relaxed state
points = {
    'head': [WIDTH//2, HEIGHT//4],
    'neck': [WIDTH//2, HEIGHT//3],
    'torso': [WIDTH//2, HEIGHT//2],
    'left_shoulder': [WIDTH//2 - 30, HEIGHT//3 - 10],
    'right_shoulder': [WIDTH//2 + 30, HEIGHT//3 - 10],
    'left_elbow': [WIDTH//2 - 60, HEIGHT//2],
    'right_elbow': [WIDTH//2 + 60, HEIGHT//2],
    'left_wrist': [WIDTH//2 - 80, HEIGHT//2 + 30],
    'right_wrist': [WIDTH//2 + 80, HEIGHT//2 + 30],
    'left_hip': [WIDTH//2 - 25, HEIGHT//2 + 20],
    'right_hip': [WIDTH//2 + 25, HEIGHT//2 + 20],
    'left_knee': [WIDTH//2 - 25, HEIGHT//2 + 60],
    'right_knee': [WIDTH//2 + 25, HEIGHT//2 + 60],
    'left_ankle': [WIDTH//2 - 25, HEIGHT//2 + 100],
    'right_ankle': [WIDTH//2 + 25, HEIGHT//2 + 100],
}

# Function to rotate points around the center of mass
def rotate_points(points, angle, center):
    rotated_points = {}
    for key, point in points.items():
        x, y = point
        # Translate point to origin
        x -= center[0]
        y -= center[1]
        # Rotate point
        x_new = x * math.cos(angle) - y * math.sin(angle)
        y_new = x * math.sin(angle) + y * math.cos(angle)
        # Translate point back
        rotated_points[key] = [x_new + center[0], y_new + center[1]]
    return rotated_points

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with black color
    screen.fill(BLACK)

    # Define the center of mass
    center_of_mass = [WIDTH//2, HEIGHT//2]

    # Calculate the angle of rotation based on time
    angle = (pygame.time.get_ticks() / 1000.0) * math.pi  # Rotate at 2*pi radians per second

    # Rotate the points
    rotated_points = rotate_points(points, angle, center_of_mass)

    # Draw the points
    for key, point in rotated_points.items():
        pygame.draw.circle(screen, WHITE, point, 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
