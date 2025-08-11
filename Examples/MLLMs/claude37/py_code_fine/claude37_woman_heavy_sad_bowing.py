
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Animation: Sad Woman Bowing')

# Point-light positions for initial state
points = np.array([
    [400, 200],  # Head
    [370, 250], [400, 250], [430, 250],  # Shoulders
    [350, 300], [400, 300], [450, 300],  # Upper body
    [320, 350], [400, 350], [480, 350],  # Lower body
    [300, 400], [400, 400], [500, 400],  # Legs
    [400, 500],  # Foot
])

# Bowing action parameters
bowing_angle = np.linspace(0, np.pi/3, 60)  # 60 frames bowing
bow_duration = 60
frame_counter = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update the position of point-lights for bowing
    if frame_counter < bow_duration:
        # Bowing motion
        angle = bowing_angle[frame_counter]
        points[0, 1] += 5 * (np.sin(angle) - 0.5)  # Move head down
        points[1:, 1] += 3 * (np.sin(angle) - 0.5)  # Lower body follows
        frame_counter += 1
    else:
        # Reset position after bowing
        points[:, 1] = points[:, 1] - points[0, 1] + 200
        frame_counter = 0

    # Draw point-lights
    for pos in points:
        pygame.draw.circle(screen, WHITE, pos.astype(int), 5)

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()
