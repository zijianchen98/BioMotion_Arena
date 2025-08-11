
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
FPS = 60
NUM_POINTS = 15

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Stimulus Animation')

# Define the points for the sad woman
# These coordinates should be adjusted for realism based on the human form
points = [
    (WIDTH // 2, HEIGHT // 2 - 50),  # Head
    (WIDTH // 2 - 15, HEIGHT // 2 - 30),  # Left Shoulder
    (WIDTH // 2 + 15, HEIGHT // 2 - 30),  # Right Shoulder
    (WIDTH // 2 - 35, HEIGHT // 2 + 10),  # Left Elbow
    (WIDTH // 2 + 35, HEIGHT // 2 + 10),  # Right Elbow
    (WIDTH // 2 - 25, HEIGHT // 2 + 60),  # Left Hand
    (WIDTH // 2 + 25, HEIGHT // 2 + 60),  # Right Hand
    (WIDTH // 2 - 30, HEIGHT // 2 + 90),  # Left Hip
    (WIDTH // 2 + 30, HEIGHT // 2 + 90),  # Right Hip
    (WIDTH // 2 - 25, HEIGHT // 2 + 160),  # Left Knee
    (WIDTH // 2 + 25, HEIGHT // 2 + 160),  # Right Knee
    (WIDTH // 2 - 15, HEIGHT // 2 + 220),  # Left Foot
    (WIDTH // 2 + 15, HEIGHT // 2 + 220),  # Right Foot
    (WIDTH // 2 - 10, HEIGHT // 2 - 100),  # Back
    (WIDTH // 2 + 10, HEIGHT // 2 - 100),  # Back
]

# Animation loop
clock = pygame.time.Clock()
running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Calculate the new positions of the points
    new_points = []
    for i, (x, y) in enumerate(points):
        # Apply a simple rotation transformation
        radius = 30  # Adjust radius for turning effect
        new_x = WIDTH // 2 + radius * math.cos(math.radians(angle + i * (360 / NUM_POINTS)))
        new_y = HEIGHT // 2 + radius * math.sin(math.radians(angle + i * (360 / NUM_POINTS)))
        new_points.append((new_x, new_y))

    # Draw the points
    for point in new_points:
        pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), 5)

    # Update the display
    pygame.display.flip()
    
    # Update the angle for rotation
    angle += 2  # Adjust the speed of rotation
    angle %= 360

    # Maintain the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
