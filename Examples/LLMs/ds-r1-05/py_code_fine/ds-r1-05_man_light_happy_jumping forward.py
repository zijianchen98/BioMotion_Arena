
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
jump_height = 100
jump_duration = 1.5
forward_speed = 150
start_x, start_y = width // 2, height - 2 * jump_height

# Point definitions with relative positions and movement functions
points = [
    # Head
    {'dx': 0, 'dy': -50, 'dxf': lambda t: 0, 'dyf': lambda t: 0},
    # Left Shoulder
    {'dx': -20, 'dy': -30, 'dxf': lambda t: 0, 'dyf': lambda t: 0},
    # Right Shoulder
    {'dx': 20, 'dy': -30, 'dxf': lambda t: 0, 'dyf': lambda t: 0},
    # Left Elbow
    {'dx': -30, 'dy': -10, 'dxf': lambda t: 0, 'dyf': lambda t: 10*math.sin(2*math.pi*t)},
    # Right Elbow
    {'dx': 30, 'dy': -10, 'dxf': lambda t: 0, 'dyf': lambda t: 10*math.sin(2*math.pi*t)},
    # Left Hand
    {'dx': -40, 'dy': 10, 'dxf': lambda t: 0, 'dyf': lambda t: 20*math.sin(2*math.pi*t)},
    # Right Hand
    {'dx': 40, 'dy': 10, 'dxf': lambda t: 0, 'dyf': lambda t: 20*math.sin(2*math.pi*t)},
    # Left Hip
    {'dx': -15, 'dy': 0, 'dxf': lambda t: 0, 'dyf': lambda t: 0},
    # Right Hip
    {'dx': 15, 'dy': 0, 'dxf': lambda t: 0, 'dyf': lambda t: 0},
    # Left Knee
    {'dx': -15, 'dy': 30, 'dxf': lambda t: 0, 'dyf': lambda t: -20*(1-t)},
    # Right Knee
    {'dx': 15, 'dy': 30, 'dxf': lambda t: 0, 'dyf': lambda t: -20*(1-t)},
    # Left Ankle
    {'dx': -15, 'dy': 60, 'dxf': lambda t: 0, 'dyf': lambda t: 0},
    # Right Ankle
    {'dx': 15, 'dy': 60, 'dxf': lambda t: 0, 'dyf': lambda t: 0},
    # Left Foot
    {'dx': -25, 'dy': 70, 'dxf': lambda t: 0, 'dyf': lambda t: 0},
    # Right Foot
    {'dx': 25, 'dy': 70, 'dxf': lambda t: 0, 'dyf': lambda t: 0},
]

clock = pygame.time.Clock()
time_elapsed = 0.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000
    time_elapsed += dt
    t = (time_elapsed % jump_duration) / jump_duration

    # Calculate current position
    current_x = (start_x + forward_speed * time_elapsed) % width
    current_y = start_y - jump_height * 4 * t * (1 - t)

    screen.fill(BLACK)

    for point in points:
        dx = point['dx'] + point['dxf'](t)
        dy = point['dy'] + point['dyf'](t)
        x = int(current_x + dx)
        y = int(current_y + dy)
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
