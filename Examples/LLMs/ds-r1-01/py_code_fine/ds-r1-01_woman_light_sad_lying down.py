
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Lying Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define 15 points with start (standing) and end (lying) positions, and phase offsets
points = [
    # Head, Neck, Shoulders
    {'start': (400, 100), 'end': (300, 500), 'phase': 0.0},
    {'start': (400, 150), 'end': (350, 500), 'phase': 0.2},
    {'start': (350, 180), 'end': (250, 500), 'phase': 0.4},
    {'start': (450, 180), 'end': (450, 500), 'phase': 0.6},
    # Arms
    {'start': (330, 220), 'end': (200, 500), 'phase': 0.8},
    {'start': (470, 220), 'end': (500, 500), 'phase': 1.0},
    {'start': (310, 250), 'end': (150, 500), 'phase': 1.2},
    {'start': (490, 250), 'end': (550, 500), 'phase': 1.4},
    # Torso and Hips
    {'start': (400, 200), 'end': (350, 500), 'phase': 1.6},
    {'start': (400, 300), 'end': (400, 500), 'phase': 1.8},
    # Legs
    {'start': (370, 400), 'end': (300, 500), 'phase': 2.0},
    {'start': (430, 400), 'end': (500, 500), 'phase': 2.2},
    {'start': (370, 500), 'end': (250, 500), 'phase': 2.4},
    {'start': (430, 500), 'end': (550, 500), 'phase': 2.6},
    # Mid-torso
    {'start': (400, 250), 'end': (375, 500), 'phase': 2.8}
]

# Animation parameters
speed = 0.5
radius = 5
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    time_var = pygame.time.get_ticks() / 1000  # Current time in seconds

    for point in points:
        # Calculate smooth progress with phase offset
        progress = (math.sin(time_var * speed - point['phase']) + 1) / 2
        x = point['start'][0] + (point['end'][0] - point['start'][0]) * progress
        y = point['start'][1] + (point['end'][1] - point['start'][1]) * progress
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), radius)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
