
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions for the happy man
# Each point represents a joint in the body
point_lights = [
    {'x': 0, 'y': 0, 'dx': 0, 'dy': 0},  # Head
    {'x': -20, 'y': -30, 'dx': 0, 'dy': 0},  # Left shoulder
    {'x': 20, 'y': -30, 'dx': 0, 'dy': 0},  # Right shoulder
    {'x': -40, 'y': 0, 'dx': 0, 'dy': 0},  # Left elbow
    {'x': 40, 'y': 0, 'dx': 0, 'dy': 0},  # Right elbow
    {'x': -60, 'y': 30, 'dx': 0, 'dy': 0},  # Left wrist
    {'x': 60, 'y': 30, 'dx': 0, 'dy': 0},  # Right wrist
    {'x': 0, 'y': -60, 'dx': 0, 'dy': 0},  # Torso
    {'x': -20, 'y': 60, 'dx': 0, 'dy': 0},  # Left hip
    {'x': 20, 'y': 60, 'dx': 0, 'dy': 0},  # Right hip
    {'x': -40, 'y': 90, 'dx': 0, 'dy': 0},  # Left knee
    {'x': 40, 'y': 90, 'dx': 0, 'dy': 0},  # Right knee
    {'x': -60, 'y': 120, 'dx': 0, 'dy': 0},  # Left ankle
    {'x': 60, 'y': 120, 'dx': 0, 'dy': 0},  # Right ankle
    {'x': 0, 'y': 150, 'dx': 0, 'dy': 0},  # Feet
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Animation variables
jump_height = 100
jump_duration = 1000  # milliseconds
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the current time
    current_time = pygame.time.get_ticks() - start_time

    # Update point-light positions
    for point in point_lights:
        # Update x position to move forward
        point['x'] += 2

        # Update y position to simulate jumping
        if current_time < jump_duration:
            point['y'] = -jump_height * math.sin(2 * math.pi * current_time / jump_duration)
        else:
            point['y'] = 0

    # Draw everything
    screen.fill(BLACK)
    for point in point_lights:
        pygame.draw.circle(screen, WHITE, (int(WIDTH / 2 + point['x']), int(HEIGHT / 2 + point['y'])), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
