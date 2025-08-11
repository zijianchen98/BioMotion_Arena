
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
POINT_COUNT = 15
FPS = 60

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Animation")

# Function to calculate point positions
def calculate_point_positions(angle):
    positions = []
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2
    
    # Calculate positions based on angle
    for i in range(POINT_COUNT):
        # Distributing points in a circular pattern around the center
        theta = 2 * math.pi * (i / POINT_COUNT) + angle
        radius = 100 if i % 5 == 0 else 50  # Vary the radius to create a figure
        x = int(center_x + radius * math.cos(theta))
        y = int(center_y + radius * math.sin(theta))
        positions.append((x, y))
    
    return positions

# Main loop
clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill(BLACK)

    # Update angle for rotation
    angle += 0.05  # Adjust the speed of rotation

    # Calculate current positions of the points
    points = calculate_point_positions(angle)

    # Draw each point
    for point in points:
        pygame.draw.circle(screen, WHITE, point, 5)  # Draw each point as a circle

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)
