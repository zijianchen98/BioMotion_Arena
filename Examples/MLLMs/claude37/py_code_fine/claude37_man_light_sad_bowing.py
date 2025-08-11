
import pygame
import sys
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0) # Black
POINT_COLOR = (255, 255, 255) # White
POINT_RADIUS = 5
NUM_POINTS = 15

# Point locations for the sad man bowing
# These will represent joint positions as a simple 2D "stick figure"
positions = [
    (400, 100), # Head
    (380, 150), (420, 150), # Shoulders
    (370, 200), (430, 200), # Elbows
    (350, 250), (450, 250), # Hands
    (400, 200), # Body
    (390, 300), (410, 300), # Hips
    (370, 400), (430, 400), # Knees
    (350, 500), (450, 500)  # Feet
]

# Animation function
def animate():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Point-Light Stimulus: Sad Man Bowing')
    clock = pygame.time.Clock()

    # Bowing motion parameters
    # Modify these to create a smooth up and down bowing motion
    step = 1
    bow_depth = 20

    while True:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Update positions for bowing effect
        for i in range(len(positions)):
            x, y = positions[i]
            # Adjust y position to simulate bowing
            if i == 0:  # Head, bow down
                positions[i] = (x, y + step * np.sin(pygame.time.get_ticks() / 500.0))
            else:  # Adjust other points for biomechanical plausibility
                positions[i] = (x, y + (step // 2) * np.sin(pygame.time.get_ticks() / 500.0))

            # Draw the point
            pygame.draw.circle(screen, POINT_COLOR, (int(positions[i][0]), int(positions[i][1])), POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    animate()
