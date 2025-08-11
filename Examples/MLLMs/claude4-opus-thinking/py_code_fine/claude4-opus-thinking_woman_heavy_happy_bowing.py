
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)       # Black background
POINT_COLOR = (255, 255, 255)  # White point lights
FPS = 60  # Frames per second

# Define the points for the animation
num_points = 15
points = np.zeros((num_points, 2))

# Initial positions (example coordinates)
# Adjust these to model a woman bowing over a weight
points[:, 0] = [380, 370, 390, 410, 430, 420, 385, 395, 405, 420, 430, 440, 460, 480, 500]  # X-coordinates
points[:, 1] = [200, 220, 240, 260, 280, 300, 320, 350, 370, 390, 410, 430, 450, 460, 480]  # Y-coordinates

def bowing_motion(frame):
    """Update the points' y-positions to simulate bowing motion."""
    # Bowing effect: lower the y-coordinates over time
    for i in range(num_points):
        points[i][1] += 0.5 * (np.sin(frame / 10 + i) - 1)  # Adjust motion with a wave

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Animation")
    clock = pygame.time.Clock()
    running = True
    frame = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        # Update point positions
        bowing_motion(frame)

        # Draw point lights
        for point in points:
            pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), 5)

        pygame.display.flip()
        clock.tick(FPS)
        frame += 1

    pygame.quit()

if __name__ == "__main__":
    main()
