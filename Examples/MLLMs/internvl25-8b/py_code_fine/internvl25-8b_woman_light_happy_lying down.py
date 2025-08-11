
import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
POINT_COUNT = 15
POINT_RADIUS = 10
POINT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Points positions
points = np.random.randint(0, WIDTH, size=(POINT_COUNT, 2))
velocities = np.zeros(POINT_COUNT)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Running clock
clock = pygame.time.Clock()

def run_animation():
    while True:
        screen.fill(BACKGROUND_COLOR)
        
        for i in range(POINT_COUNT):
            color = (255, 255, 255)
            pygame.draw.circle(screen, color, points[i], POINT_RADIUS)
        
        for i in range(POINT_COUNT):
            new_velocity = np.random.uniform(-1, 1, size=POINT_COUNT)
            velocities = new_velocity
            
        points += velocities

        # Ensure points are within screen bounds
        points[points < 0] = 0
        points[points > WIDTH - POINT_RADIUS] = WIDTH - POINT_RADIUS

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    run_animation()
