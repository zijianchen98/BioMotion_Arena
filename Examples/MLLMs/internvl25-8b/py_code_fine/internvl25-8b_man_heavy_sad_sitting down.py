
import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a clock for controlling the frame rate
clock = pygame.time.Clock()

# Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

# Number of points
POINT_COUNT = 15

# Radius of each point
RADIUS = 10

# List for storing point positions
points_positions = [(WIDTH // 2, HEIGHT // 2) for _ in range(POINT_COUNT)]

# Function to draw each point
def draw_point(screen, pos):
    pygame.draw.circle(screen, WHITE, pos, RADIUS)

# Function to calculate the new positions of the points
def calculate_motion_steps(positions, steps):
    new_positions = []
    for i, pos in enumerate(positions):
        d = math.sqrt((i // POINT_COUNT) * 2)
        angle = -90 + (i // 15) * 180 / POINT_COUNT
        new_x = pos[0] + d * math.cos(math.radians(angle))
        new_y = pos[1] + d * math.sin(math.radians(angle))
        new_positions.append((int(new_x), int(new_y)))
    return new_positions

# Main animation loop
frame_step = 0.05  # Time in seconds to reach the next motion step
steps = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    new_positions = calculate_motion_steps(points_positions, steps)
    positions_shifted = [
        (new_x + pos[0], new_y + pos[1])
        for new_x, new_y, pos in zip(*zip(*[positions_shifted + new_positions[i] for i, _ in enumerate(points_positions)]))
    ]

    frame_step += clock.tick(40) / 1000.0
    steps = int(round(frame_step * 60 / frame_step))

    # Ensure the steps don't exceed the number of total frames
    steps = steps % int((frame_step * 1 / frame_step) + 1)

    for pos in positions_shifted:
        draw_point(screen, pos)

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
