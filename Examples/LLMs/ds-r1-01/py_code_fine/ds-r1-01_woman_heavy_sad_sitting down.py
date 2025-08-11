
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define points with start and end positions for sitting motion
points = [
    # Head
    {'start_x': 400, 'start_y': 100, 'end_x': 400, 'end_y': 200},
    # Neck
    {'start_x': 400, 'start_y': 150, 'end_x': 400, 'end_y': 250},
    # Left shoulder
    {'start_x': 350, 'start_y': 180, 'end_x': 350, 'end_y': 280},
    # Right shoulder
    {'start_x': 450, 'start_y': 180, 'end_x': 450, 'end_y': 280},
    # Left elbow
    {'start_x': 330, 'start_y': 220, 'end_x': 330, 'end_y': 320},
    # Right elbow
    {'start_x': 470, 'start_y': 220, 'end_x': 470, 'end_y': 320},
    # Left hand
    {'start_x': 310, 'start_y': 260, 'end_x': 310, 'end_y': 360},
    # Right hand
    {'start_x': 490, 'start_y': 260, 'end_x': 490, 'end_y': 360},
    # Hip center
    {'start_x': 400, 'start_y': 250, 'end_x': 400, 'end_y': 350},
    # Left hip
    {'start_x': 380, 'start_y': 250, 'end_x': 380, 'end_y': 350},
    # Right hip
    {'start_x': 420, 'start_y': 250, 'end_x': 420, 'end_y': 350},
    # Left knee
    {'start_x': 380, 'start_y': 350, 'end_x': 400, 'end_y': 300},
    # Right knee
    {'start_x': 420, 'start_y': 350, 'end_x': 400, 'end_y': 300},
    # Left ankle
    {'start_x': 380, 'start_y': 450, 'end_x': 400, 'end_y': 400},
    # Right ankle
    {'start_x': 420, 'start_y': 450, 'end_x': 400, 'end_y': 400},
]

# Animation parameters
duration = 2  # Animation cycle duration in seconds

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate smooth progress
    time_passed = pygame.time.get_ticks() / 1000  # Convert to seconds
    linear_progress = (time_passed % duration) / duration
    progress = linear_progress ** 2 * (3 - 2 * linear_progress)  # Smoothstep easing

    # Update and draw each point
    for point in points:
        x = point['start_x'] + (point['end_x'] - point['start_x']) * progress
        y = point['start_y'] + (point['end_y'] - point['start_y']) * progress
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
sys.exit()
