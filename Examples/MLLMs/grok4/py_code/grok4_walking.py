
import pygame
import numpy as np
import sys

# Constants
WIDTH, HEIGHT = 800, 600
NUM_POINTS = 15
FPS = 30

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Walking Point-Light Animation')
clock = pygame.time.Clock()

# Function to create a walking skeleton
def get_walking_positions(frame):
    # Simple walking animation over 50 frames
    phase = frame % 50
    if phase < 25:
        offset = phase * 5
    else:
        offset = (50 - phase) * 5

    # Define the positions for 15 points (simplified stride)
    base_y = HEIGHT // 2
    positions = [
        (WIDTH // 2 - 15, base_y - 50 + offset),  # Head
        (WIDTH // 2 + 15, base_y - 50 + offset),  # Head
        (WIDTH // 2 - 25, base_y - 25 + offset),  # Left shoulder
        (WIDTH // 2 + 25, base_y - 25 + offset),  # Right shoulder
        (WIDTH // 2 - 25, base_y + 25 + offset),  # Left elbow
        (WIDTH // 2 + 25, base_y + 25 + offset),  # Right elbow
        (WIDTH // 2 - 50, base_y + 50 + offset),  # Left hand
        (WIDTH // 2 + 50, base_y + 50 + offset),  # Right hand
        (WIDTH // 2 - 15, base_y + 75 + offset),  # Left hip
        (WIDTH // 2 + 15, base_y + 75 + offset),  # Right hip
        (WIDTH // 2 - 25, base_y + 100 + offset), # Left knee
        (WIDTH // 2 + 25, base_y + 100 + offset), # Right knee
        (WIDTH // 2 - 35, base_y + 130 + offset), # Left foot
        (WIDTH // 2 + 35, base_y + 130 + offset), # Right foot
        (WIDTH // 2, base_y - 10 + offset),       # Center of Mass
        (WIDTH // 2, base_y)                       # Bottom
    ]
    return positions

def main():
    # Main loop
    frame = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Get the positions of the point-lights for this frame
        positions = get_walking_positions(frame)
        
        # Draw the point lights
        for pos in positions:
            pygame.draw.circle(screen, (255, 255, 255), pos, 5)  # White circles

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Limit to FPS frame rate
        frame += 1

if __name__ == "__main__":
    main()
