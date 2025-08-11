
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_POINTS = 15
FPS = 30

# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation")

# Function to generate points for the happy woman sitting down
def generate_points(frame):
    # Base positions for point lights resembling a sitting figure
    base_positions = np.array([
        (WIDTH // 2, HEIGHT // 4),           # Head
        (WIDTH // 2 - 20, HEIGHT // 3),     # Left Shoulder
        (WIDTH // 2 + 20, HEIGHT // 3),     # Right Shoulder
        (WIDTH // 2 - 30, HEIGHT // 2),     # Left Elbow
        (WIDTH // 2 + 30, HEIGHT // 2),     # Right Elbow
        (WIDTH // 2 - 30, HEIGHT // 2 + 30), # Left Hand
        (WIDTH // 2 + 30, HEIGHT // 2 + 30), # Right Hand
        (WIDTH // 2 - 40, HEIGHT // 2 + 100), # Left Knee
        (WIDTH // 2 + 40, HEIGHT // 2 + 100), # Right Knee
        (WIDTH // 2 - 50, HEIGHT // 2 + 150), # Left Foot
        (WIDTH // 2 + 50, HEIGHT // 2 + 150), # Right Foot
        (WIDTH // 2 - 20, HEIGHT // 4 + 40),  # Left Eye
        (WIDTH // 2 + 20, HEIGHT // 4 + 40),  # Right Eye
        (WIDTH // 2 - 20, HEIGHT // 4 + 20),  # Mouth Left
        (WIDTH // 2 + 20, HEIGHT // 4 + 20)   # Mouth Right
    ])

    # Apply a downward motion to simulate sitting
    motion = frame * 0.5
    base_positions[:, 1] += motion

    return base_positions.astype(int)

# Main loop
running = True
clock = pygame.time.Clock()
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Generate point positions
    point_positions = generate_points(frame)

    # Draw the point lights
    for point in point_positions:
        pygame.draw.circle(screen, WHITE, (point[0], point[1]), 5)

    pygame.display.flip()
    frame += 1
    clock.tick(FPS)

pygame.quit()
