
import pygame
import numpy as np
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
POINTS_COUNT = 15
POINT_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)    # Black
POINT_COLOR = (255, 255, 255)    # White

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation")
clock = pygame.time.Clock()

# Function to create point-light positions representing the joints of the happy man
def create_joint_positions(t):
    # Example joint positions for a waving action
    positions = np.array([
        [WIDTH // 2, HEIGHT // 4],               # Head
        [WIDTH // 2, HEIGHT // 3],                # Neck
        [WIDTH // 2 - 30, HEIGHT // 3 + 30],      # Left shoulder
        [WIDTH // 2 + 30, HEIGHT // 3 + 30],     # Right shoulder
        [WIDTH // 2 - 30, HEIGHT // 3 + 80],      # Left elbow
        [WIDTH // 2 + 30, HEIGHT // 3 + 80],     # Right elbow
        [WIDTH // 2 - 30, HEIGHT // 3 + 120],     # Left hand
        [WIDTH // 2 + 30, HEIGHT // 3 + 120],    # Right hand
        [WIDTH // 2 - 50, HEIGHT // 2],          # Left hip
        [WIDTH // 2 + 50, HEIGHT // 2],          # Right hip
        [WIDTH // 2 - 50, HEIGHT // 2 + 40],     # Left knee
        [WIDTH // 2 + 50, HEIGHT // 2 + 40],     # Right knee
        [WIDTH // 2 - 50, HEIGHT // 2 + 80],     # Left foot
        [WIDTH // 2 + 50, HEIGHT // 2 + 80],     # Right foot
        [WIDTH // 2 - 15, HEIGHT // 3 + 30 - 20 * np.sin(2 * np.pi * t)]  # Waving hand
    ])
    return positions

# Main animation loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear screen
        screen.fill(BACKGROUND_COLOR)

        # Get the current time normalized between 0 and 1
        t = (pygame.time.get_ticks() / 1000) % 1
        
        # Update joint positions
        joint_positions = create_joint_positions(t)

        # Draw the points (joints)
        for pos in joint_positions:
            pygame.draw.circle(screen, POINT_COLOR, pos.astype(int), POINT_RADIUS)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
