
import pygame
import sys
import numpy as np

# Constants
WIDTH, HEIGHT = 640, 480
FPS = 30
NUM_POINTS = 15
POINT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Define the point-light positions
initial_positions = np.array([
    [300, 100],  # Head
    [280, 140],  # Left Shoulder
    [320, 140],  # Right Shoulder
    [260, 200],  # Left Elbow
    [340, 200],  # Right Elbow
    [250, 260],  # Left Hand
    [350, 260],  # Right Hand
    [290, 220],  # Left Hip
    [310, 220],  # Right Hip
    [280, 300],  # Left Knee
    [320, 300],  # Right Knee
    [270, 360],  # Left Foot
    [330, 360],  # Right Foot
    [280, 180],  # Chest
    [300, 140],  # Neck
    [310, 230]   # Center of mass
])

def update_positions(positions, t):
    # Simple y-coordinate update simulating 'sitting down' motion
    positions[:, 1] += 0.5 * t  # Move down
    return positions

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Point-Light Animation')
    clock = pygame.time.Clock()

    t = 0  # Time variable

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update positions based on time
        point_positions = update_positions(initial_positions.copy(), t)

        screen.fill(BACKGROUND_COLOR)

        # Draw the points
        for pos in point_positions:
            pygame.draw.circle(screen, POINT_COLOR, pos.astype(int), 5)  # Draw points

        pygame.display.flip()
        t += 1 / FPS  # Increment time
        clock.tick(FPS)

if __name__ == '__main__':
    main()
