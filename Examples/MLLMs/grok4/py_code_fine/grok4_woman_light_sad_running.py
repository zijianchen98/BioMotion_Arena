
import pygame
import sys
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
NUM_POINTS = 15
FPS = 60
POINT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Stimulus Animation')

# Set up clock for frame rate
clock = pygame.time.Clock()

# Example structure for points in a running motion
# Coordinates for the point-lights representing body parts
def get_running_positions(time_step):
    # Simple sinusoidal motion for running effect
    t = time_step * 0.1
    positions = []

    for i in range(NUM_POINTS):
        # Example positions for a running motion
        x = WIDTH // 2 + 50 * np.sin(t + (i * 0.5))  # Horizontal motion to depict running
        y = HEIGHT // 2 + (i * 10) - 50 + 20 * np.cos(0.5 * t)  # Vertical motion
        positions.append((x, y))

    return positions

# Main loop
time_step = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)  # Fill background

    # Get positions of the point-lights
    positions = get_running_positions(time_step)

    # Draw point-lights
    for pos in positions:
        pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), 5)

    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Maintain the frame rate
    time_step += 1  # Increase time step for motion

