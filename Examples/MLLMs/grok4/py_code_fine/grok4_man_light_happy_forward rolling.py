
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
POINT_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
FPS = 30

# Create the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Define the points for the happy man's limbs and head
def get_point_positions(frame):
    # Define a basic structure for the happy man
    # Adjust these points for a forward roll motion
    positions = [
        (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 40),  # Head
        (SCREEN_WIDTH//2 - 15, SCREEN_HEIGHT//2 - 15),  # Left hand
        (SCREEN_WIDTH//2 + 15, SCREEN_HEIGHT//2 - 15),  # Right hand
        (SCREEN_WIDTH//2 - 10, SCREEN_HEIGHT//2 + 10),  # Left elbow
        (SCREEN_WIDTH//2 + 10, SCREEN_HEIGHT//2 + 10),  # Right elbow
        (SCREEN_WIDTH//2 - 20, SCREEN_HEIGHT//2 + 40),  # Left knee
        (SCREEN_WIDTH//2 + 20, SCREEN_HEIGHT//2 + 40),  # Right knee
        (SCREEN_WIDTH//2 - 15, SCREEN_HEIGHT//2 + 70),  # Left foot
        (SCREEN_WIDTH//2 + 15, SCREEN_HEIGHT//2 + 70),  # Right foot
    ]

    # Add forward roll motion by modifying y-positions over frames
    roll_amplitude = 30
    for i in range(len(positions)):
        y_offset = int(roll_amplitude * math.sin((frame / 10.0) + (i * 0.3)))
        positions[i] = (positions[i][0], positions[i][1] + y_offset)
        
    return positions

# Main loop
running = True
frame_count = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(BACKGROUND_COLOR)  # Fill background

    point_positions = get_point_positions(frame_count)

    # Draw all points
    for pos in point_positions:
        pygame.draw.circle(screen, POINT_COLOR, pos, POINT_RADIUS)

    pygame.display.flip()  # Update the display
    frame_count += 1
    clock.tick(FPS)  # Maintain frame rate

pygame.quit()
