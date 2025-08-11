
import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_COUNT = 15
FPS = 30
ROLL_LENGTH = 200  # Length of the forward roll

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Stimulus Animation')
clock = pygame.time.Clock()

# Create point-light positions
def get_point_positions(t):
    positions = []
    # Simple forward rolling positions in a circular motion
    for i in range(POINT_COUNT):
        angle = (t + (i * (2 * np.pi / POINT_COUNT))) % (2 * np.pi)  # Vary angles for each point
        x = WIDTH // 2 + 30 * np.cos(angle)  # Adjust radius for circle
        y = HEIGHT // 2 + (ROLL_LENGTH + 30) * np.sin(angle)  # Vertical motion
        positions.append((x, y))
    return positions

# Main loop
running = True
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BACKGROUND_COLOR)

    # Update point positions
    positions = get_point_positions(t)
    for pos in positions:
        pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), 5)

    # Update the display
    pygame.display.flip()

    # Update time variable
    t += 0.1  # Adjust speed of motion

    # Frame Rate
    clock.tick(FPS)

# Exit Pygame
pygame.quit()
