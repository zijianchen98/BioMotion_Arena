
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
POINT_COUNT = 15
FPS = 30
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Set up positions for 15 point-lights representing a lying down form
# These coordinates can be adjusted to better represent the desired action
points = np.array([
    [400, 200], [375, 250], [425, 250], # Head
    [350, 300], [450, 300],             # Shoulders
    [325, 350], [475, 350],             # Elbows
    [300, 400], [500, 400],             # Hands
    [275, 450], [525, 450],             # Hips
    [250, 500], [550, 500],             # Knees
    [225, 550], [575, 550],             # Feet
])

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    # Simulate motion slightly by shifting points down and side to side
    # Adding a wave-like motion for realism
    for i in range(POINT_COUNT):
        points[i][1] += np.sin(pygame.time.get_ticks() / 100 + i) * 0.5  # Vertical motion
        points[i][0] += np.cos(pygame.time.get_ticks() / 100 + i) * 0.5  # Horizontal motion
        pygame.draw.circle(screen, POINT_COLOR, (int(points[i][0]), int(points[i][1])), POINT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
