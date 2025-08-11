
import pygame
import math
import sys

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 4
FPS = 30
JUMP_DURATION = 1.5
PEAK_HEIGHT = 120
GROUND_LEVEL = HEIGHT - 100

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Jumping")
clock = pygame.time.Clock()

# Point configuration: 15 points with movement parameters
points_params = [
    # Head
    {'base_dx': 0, 'base_dy': -60, 'amp_x': 0, 'amp_y': 3, 'freq': 1.2, 'phase': 0},
    # Left shoulder
    {'base_dx': -25, 'base_dy': -30, 'amp_x': 4, 'amp_y': 8, 'freq': 2.0, 'phase': 0.2},
    # Right shoulder
    {'base_dx': 25, 'base_dy': -30, 'amp_x': 4, 'amp_y': 8, 'freq': 2.0, 'phase': 0.3},
    # Left elbow
    {'base_dx': -50, 'base_dy': 10, 'amp_x': 15, 'amp_y': 12, 'freq': 2.0, 'phase': 0.5},
    # Right elbow
    {'base_dx': 50, 'base_dy': 10, 'amp_x': 15, 'amp_y': 12, 'freq': 2.0, 'phase': 0.6},
    # Left hand
    {'base_dx': -70, 'base_dy': 50, 'amp_x': 20, 'amp_y': 15, 'freq': 2.0, 'phase': 0.7},
    # Right hand
    {'base_dx': 70, 'base_dy': 50, 'amp_x': 20, 'amp_y': 15, 'freq': 2.0, 'phase': 0.8},
    # Left hip
    {'base_dx': -20, 'base_dy': 20, 'amp_x': 5, 'amp_y': 5, 'freq': 1.0, 'phase': 0.1},
    # Right hip
    {'base_dx': 20, 'base_dy': 20, 'amp_x': 5, 'amp_y': 5, 'freq': 1.0, 'phase': 0.2},
    # Left knee
    {'base_dx': -30, 'base_dy': 60, 'amp_x': 8, 'amp_y': 25, 'freq': 1.5, 'phase': 0.3},
    # Right knee
    {'base_dx': 30, 'base_dy': 60, 'amp_x': 8, 'amp_y': 25, 'freq': 1.5, 'phase': 0.4},
    # Left ankle
    {'base_dx': -40, 'base_dy': 100, 'amp_x': 10, 'amp_y': 30, 'freq': 1.5, 'phase': 0.5},
    # Right ankle
    {'base_dx': 40, 'base_dy': 100, 'amp_x': 10, 'amp_y': 30, 'freq': 1.5, 'phase': 0.6},
    # Torso
    {'base_dx': 0, 'base_dy': -10, 'amp_x': 0, 'amp_y': 4, 'freq': 1.0, 'phase': 0},
    # Mid-hip
    {'base_dx': 0, 'base_dy': 30, 'amp_x': 0, 'amp_y': 5, 'freq': 1.0, 'phase': 0},
]

def get_center_position(t):
    t_in_jump = t % JUMP_DURATION
    x = 100 + (WIDTH - 200) * (t_in_jump / JUMP_DURATION)
    y = GROUND_LEVEL - (4 * PEAK_HEIGHT / (JUMP_DURATION**2)) * t_in_jump * (JUMP_DURATION - t_in_jump)
    return x, int(y)

# Main loop
running = True
start_time = pygame.time.get_ticks() / 1000.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    current_time = pygame.time.get_ticks() / 1000.0 - start_time
    center_x, center_y = get_center_position(current_time)

    for params in points_params:
        dx = params['amp_x'] * math.sin(2 * math.pi * params['freq'] * current_time + params['phase'])
        dy = params['amp_y'] * math.sin(2 * math.pi * params['freq'] * current_time + params['phase'])
        x = center_x + params['base_dx'] + dx
        y = center_y + params['base_dy'] + dy
        pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), POINT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
