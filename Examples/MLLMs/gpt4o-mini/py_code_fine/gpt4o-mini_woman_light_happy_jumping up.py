
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5
FPS = 60

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Jumper properties
num_points = 15
points_positions = []
initial_height = HEIGHT // 2
jump_height = 100
jump_frames = 30
fall_frames = 30

# Initial positions for the point-lights
for i in range(num_points):
    y = initial_height + (i // 3) * 20  # 3 columns
    x = WIDTH // 2 + (i % 3 - 1) * 20    # Spread across
    points_positions.append((x, y))

# Animation loop
running = True
clock = pygame.time.Clock()
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Calculate positions for jumping and falling
    if frame < jump_frames:  # Ascending
        jump_progress = frame / jump_frames
        for i in range(num_points):
            x, y = points_positions[i]
            y -= jump_height * (1 - np.cos(jump_progress * np.pi)) / 2
            points_positions[i] = (x, y)
    elif frame < jump_frames + fall_frames:  # Descending
        jump_progress = (frame - jump_frames) / fall_frames
        for i in range(num_points):
            x, y = points_positions[i]
            y += jump_height * (1 - np.cos(jump_progress * np.pi)) / 2
            points_positions[i] = (x, y)

    # Draw the points
    for x, y in points_positions:
        pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), POINT_RADIUS)

    pygame.display.flip()
    frame += 1
    clock.tick(FPS)

pygame.quit()
