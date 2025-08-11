
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Jumping")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Motion parameters
hip_speed = 200  # pixels per second
hip_amp = 60     # vertical movement amplitude
jump_period = 1.2  # seconds per jump cycle

# Define 15 points with relative positions and movement parameters
points_params = [
    # Head
    {'rel_x': 0, 'rel_y': -70, 'amp': 15, 'phase': 0},
    # Shoulders
    {'rel_x': -25, 'rel_y': -40, 'amp': 20, 'phase': 0.2},
    {'rel_x': 25, 'rel_y': -40, 'amp': 20, 'phase': 0.2},
    # Elbows
    {'rel_x': -50, 'rel_y': -25, 'amp': 25, 'phase': 0.4},
    {'rel_x': 50, 'rel_y': -25, 'amp': 25, 'phase': 0.4},
    # Hands
    {'rel_x': -70, 'rel_y': -10, 'amp': 30, 'phase': 0.6},
    {'rel_x': 70, 'rel_y': -10, 'amp': 30, 'phase': 0.6},
    # Hips (center point)
    {'rel_x': 0, 'rel_y': 0, 'amp': 0, 'phase': 0},
    # Knees
    {'rel_x': -20, 'rel_y': 40, 'amp': 40, 'phase': 0.8},
    {'rel_x': 20, 'rel_y': 40, 'amp': 40, 'phase': 0.8},
    # Ankles
    {'rel_x': -20, 'rel_y': 80, 'amp': 45, 'phase': 1.0},
    {'rel_x': 20, 'rel_y': 80, 'amp': 45, 'phase': 1.0},
    # Feet
    {'rel_x': -30, 'rel_y': 100, 'amp': 50, 'phase': 1.2},
    {'rel_x': 30, 'rel_y': 100, 'amp': 50, 'phase': 1.2},
    # Chest
    {'rel_x': 0, 'rel_y': -50, 'amp': 10, 'phase': 0.1},
]

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks() / 1000.0  # Get time in seconds

    # Calculate hip position
    hip_x = (hip_speed * current_time) % width
    hip_y = height/2 + hip_amp * math.sin(2 * math.pi * current_time / jump_period)

    screen.fill(black)

    # Draw all points
    for params in points_params:
        # Calculate positions
        base_x = hip_x + params['rel_x']
        vertical_offset = params['amp'] * math.sin(2 * math.pi * current_time / jump_period + params['phase'])
        y = hip_y + params['rel_y'] + vertical_offset
        
        # Wrap around screen edges
        x = base_x % width
        y = max(10, min(height-10, y))  # Keep within vertical bounds

        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
