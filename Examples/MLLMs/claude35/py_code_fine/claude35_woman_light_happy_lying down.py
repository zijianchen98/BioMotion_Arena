
import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 600, 800
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
NUM_POINTS = 15
FPS = 30

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Happy Woman Lying Down")

# Define point-light positions (assumed positions for a plausible lying woman animation)
positions = [
    (WIDTH // 2, HEIGHT // 4),  # Head
    (WIDTH // 2 - 15, HEIGHT // 4 + 30),  # Left Shoulder
    (WIDTH // 2 + 15, HEIGHT // 4 + 30),  # Right Shoulder
    (WIDTH // 2 - 30, HEIGHT // 4 + 100), # Left Elbow
    (WIDTH // 2 + 30, HEIGHT // 4 + 100), # Right Elbow
    (WIDTH // 2 - 50, HEIGHT // 4 + 200), # Left Hand
    (WIDTH // 2 + 50, HEIGHT // 4 + 200), # Right Hand
    (WIDTH // 2 - 15, HEIGHT // 4 + 150), # Left Hip
    (WIDTH // 2 + 15, HEIGHT // 4 + 150), # Right Hip
    (WIDTH // 2 - 30, HEIGHT // 4 + 300), # Left Knee
    (WIDTH // 2 + 30, HEIGHT // 4 + 300), # Right Knee
    (WIDTH // 2 - 20, HEIGHT // 4 + 390), # Left Foot
    (WIDTH // 2 + 20, HEIGHT // 4 + 390), # Right Foot
    (WIDTH // 2, HEIGHT // 4 + 320),       # Center of Body 
    (WIDTH // 2, HEIGHT // 4 + 50),        # Center of Happiness (Chest)
]

# Function to animate points
def animate():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Draw points
        for pos in positions:
            pygame.draw.circle(screen, POINT_COLOR, pos, 5)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    animate()
