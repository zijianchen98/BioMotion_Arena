
import pygame
import sys
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_LIGHT_COLOR = (255, 255, 255)
NUM_POINTS = 15
FPS = 30

# Point Light Positions
def get_point_positions():
    # Define the coordinates of the point lights for a lying down 'happy man'
    return [
        (WIDTH//2, HEIGHT//4),  # head
        (WIDTH//2 - 30, HEIGHT//4 + 20),  # left shoulder
        (WIDTH//2 + 30, HEIGHT//4 + 20),  # right shoulder
        (WIDTH//2 - 40, HEIGHT//4 + 60),  # left elbow
        (WIDTH//2 + 40, HEIGHT//4 + 60),  # right elbow
        (WIDTH//2 - 50, HEIGHT//4 + 100), # left wrist
        (WIDTH//2 + 50, HEIGHT//4 + 100), # right wrist
        (WIDTH//2 - 20, HEIGHT//4 + 60),  # torso
        (WIDTH//2, HEIGHT//4 + 100),      # hips
        (WIDTH//2 - 20, HEIGHT//4 + 120), # left knee
        (WIDTH//2 + 20, HEIGHT//4 + 120), # right knee
        (WIDTH//2 - 30, HEIGHT//4 + 180), # left ankle
        (WIDTH//2 + 30, HEIGHT//4 + 180), # right ankle
        (WIDTH//2 - 25, HEIGHT//4 + 140), # left foot
        (WIDTH//2 + 25, HEIGHT//4 + 140)  # right foot
    ]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Happy Man Animation')
clock = pygame.time.Clock()

# Main Animation Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    # Draw the point-lights
    for pos in get_point_positions():
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, pos, 5)

    pygame.display.flip()
    clock.tick(FPS)
