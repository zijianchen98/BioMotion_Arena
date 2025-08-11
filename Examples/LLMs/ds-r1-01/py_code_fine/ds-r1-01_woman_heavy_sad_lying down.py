
import pygame
import sys
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define points with start (standing) and end (lying) positions
points = [
    # Head
    ((400, 100), (300, 300)),
    # Neck
    ((400, 150), (350, 300)),
    # Left Shoulder
    ((350, 180), (300, 280)),
    # Right Shoulder
    ((450, 180), (300, 320)),
    # Left Elbow
    ((330, 220), (250, 280)),
    # Right Elbow
    ((470, 220), (250, 320)),
    # Left Hand
    ((310, 260), (200, 280)),
    # Right Hand
    ((490, 260), (200, 320)),
    # Torso
    ((400, 210), (400, 300)),
    # Left Hip
    ((370, 300), (500, 300)),
    # Right Hip
    ((430, 300), (500, 300)),
    # Left Knee
    ((370, 380), (600, 300)),
    # Right Knee
    ((430, 380), (600, 300)),
    # Left Ankle
    ((370, 460), (700, 300)),
    # Right Ankle
    ((430, 460), (700, 300))
]

# Animation parameters
duration = 3.0  # seconds
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed = (current_time - start_time) / 1000  # Convert to seconds

    # Calculate progress with sinusoidal easing
    progress = (elapsed % duration) / duration
    eased_progress = (1 - math.cos(progress * math.pi * 2)) / 2  # Full sine cycle for smooth loop

    # Interpolate positions
    current_positions = []
    for start, end in points:
        x = start[0] + (end[0] - start[0]) * eased_progress
        y = start[1] + (end[1] - start[1]) * eased_progress
        current_positions.append((int(x), int(y)))

    # Draw frame
    screen.fill(BLACK)
    for pos in current_positions:
        pygame.draw.circle(screen, WHITE, pos, 5)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
sys.exit()
