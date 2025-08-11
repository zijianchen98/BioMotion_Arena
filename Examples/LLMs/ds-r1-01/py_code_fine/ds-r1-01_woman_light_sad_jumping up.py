
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Woman Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 30
JUMP_CYCLE = 2.5  # Seconds per jump
MAX_JUMP_HEIGHT = 80
GRAVITY = 0.5

# Point-light configuration (15 points representing major joints and body parts)
points = [
    {'name': 'head', 'base_y': -120, 'phase': 0.0, 'sway': 0},
    {'name': 'neck', 'base_y': -90, 'phase': 0.05, 'sway': 2},
    {'name': 'l_shoulder', 'base_y': -80, 'phase': 0.1, 'sway': 15},
    {'name': 'r_shoulder', 'base_y': -80, 'phase': 0.1, 'sway': -15},
    {'name': 'l_elbow', 'base_y': -50, 'phase': 0.2, 'sway': 30},
    {'name': 'r_elbow', 'base_y': -50, 'phase': 0.2, 'sway': -30},
    {'name': 'l_wrist', 'base_y': -20, 'phase': 0.3, 'sway': 40},
    {'name': 'r_wrist', 'base_y': -20, 'phase': 0.3, 'sway': -40},
    {'name': 'torso', 'base_y': -60, 'phase': 0.0, 'sway': 0},
    {'name': 'l_hip', 'base_y': 0, 'phase': 0.4, 'sway': 10},
    {'name': 'r_hip', 'base_y': 0, 'phase': 0.4, 'sway': -10},
    {'name': 'l_knee', 'base_y': 40, 'phase': 0.5, 'sway': 20},
    {'name': 'r_knee', 'base_y': 40, 'phase': 0.5, 'sway': -20},
    {'name': 'l_ankle', 'base_y': 80, 'phase': 0.6, 'sway': 30},
    {'name': 'r_ankle', 'base_y': 80, 'phase': 0.6, 'sway': -30},
]

def calculate_position(point, time):
    """Calculate vertical position with biomechanical constraints"""
    phase_time = (time + point['phase']) % 1.0
    
    # Vertical motion: Parabolic jump with arm swing modulation
    vertical = MAX_JUMP_HEIGHT * (1 - (2*phase_time - 1)**2)
    y = HEIGHT//2 + point['base_y'] - vertical + 10*math.sin(4*math.pi*phase_time)
    
    # Horizontal motion: Gentle sway with phase offset
    x = WIDTH//2 + point['sway'] * math.sin(2*math.pi*phase_time + point['phase'])
    
    return int(x), int(y)

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    current_time = (pygame.time.get_ticks() - start_time) / 1000
    phase = (current_time % JUMP_CYCLE) / JUMP_CYCLE

    for point in points:
        x, y = calculate_position(point, phase)
        pygame.draw.circle(screen, WHITE, (x, y), 6)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
