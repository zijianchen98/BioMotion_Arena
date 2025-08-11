
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_COUNT = 15
FPS = 30

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Walking Animation')

# Point light positions: Positions correspond to a simplified walking animation
def get_positions(frame):
    # Define positions of point lights (head, arms, legs, etc.)
    positions = [
        (WIDTH // 2, HEIGHT // 3),                               # Head
        (WIDTH // 2 - 20, HEIGHT // 3 + 25 + math.sin(frame / 10) * 5),  # Left shoulder
        (WIDTH // 2 + 20, HEIGHT // 3 + 25 + math.sin(frame / 10) * 5),  # Right shoulder
        (WIDTH // 2 - 20, HEIGHT // 3 + 80),                    # Left hand
        (WIDTH // 2 + 20, HEIGHT // 3 + 80),                    # Right hand
        (WIDTH // 2 - 15, HEIGHT // 3 + 100 + math.sin((frame + 5) / 10) * 10), # Left hip
        (WIDTH // 2 + 15, HEIGHT // 3 + 100 + math.sin((frame + 5) / 10) * 10), # Right hip
        (WIDTH // 2 - 15, HEIGHT // 3 + 140),                   # Left knee
        (WIDTH // 2 + 15, HEIGHT // 3 + 140),                   # Right knee
        (WIDTH // 2 - 15, HEIGHT // 3 + 180 + math.sin(frame / 10) * 5), # Left foot
        (WIDTH // 2 + 15, HEIGHT // 3 + 180 + math.sin(frame / 10) * 5), # Right foot
        (WIDTH // 2 - 30, HEIGHT // 3 + 60),                    # Left elbow
        (WIDTH // 2 + 30, HEIGHT // 3 + 60),                    # Right elbow
        (WIDTH // 2 - 10, HEIGHT // 3 + 160),                   # Left thigh
        (WIDTH // 2 + 10, HEIGHT // 3 + 160)                    # Right thigh
    ]
    return positions

# Main loop
clock = pygame.time.Clock()
frame = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)
    
    positions = get_positions(frame)

    # Draw point lights
    for pos in positions:
        pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), 5)
    
    pygame.display.flip()
    frame += 1
    clock.tick(FPS)
