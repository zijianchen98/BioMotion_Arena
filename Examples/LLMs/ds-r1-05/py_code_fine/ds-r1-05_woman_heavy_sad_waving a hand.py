
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Define point-light parameters
points = [
    # Head
    {
        'base_pos': (400, 200),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 3, 'freq_y': 0.8, 'phase_y': 0
    },
    # Neck
    {
        'base_pos': (400, 240),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 2, 'freq_y': 0.8, 'phase_y': 0.5
    },
    # Left Shoulder
    {
        'base_pos': (360, 260),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 0, 'freq_y': 0, 'phase_y': 0
    },
    # Right Shoulder
    {
        'base_pos': (440, 260),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 0, 'freq_y': 0, 'phase_y': 0
    },
    # Left Elbow
    {
        'base_pos': (340, 320),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 0, 'freq_y': 0, 'phase_y': 0
    },
    # Right Elbow
    {
        'base_pos': (460, 320),
        'amp_x': 15, 'freq_x': 1.2, 'phase_x': 0,
        'amp_y': 4, 'freq_y': 2.4, 'phase_y': 0
    },
    # Left Hand
    {
        'base_pos': (320, 380),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 0, 'freq_y': 0, 'phase_y': 0
    },
    # Right Hand
    {
        'base_pos': (480, 380),
        'amp_x': 30, 'freq_x': 1.2, 'phase_x': 0,
        'amp_y': 8, 'freq_y': 2.4, 'phase_y': 0
    },
    # Left Hip
    {
        'base_pos': (380, 400),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 4, 'freq_y': 0.6, 'phase_y': 0
    },
    # Right Hip
    {
        'base_pos': (420, 400),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 4, 'freq_y': 0.6, 'phase_y': 0
    },
    # Left Knee
    {
        'base_pos': (370, 480),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 3, 'freq_y': 0.6, 'phase_y': 0.2
    },
    # Right Knee
    {
        'base_pos': (430, 480),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 3, 'freq_y': 0.6, 'phase_y': 0.2
    },
    # Left Foot
    {
        'base_pos': (360, 540),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 0, 'freq_y': 0, 'phase_y': 0
    },
    # Right Foot
    {
        'base_pos': (440, 540),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 0, 'freq_y': 0, 'phase_y': 0
    },
    # Torso
    {
        'base_pos': (400, 340),
        'amp_x': 0, 'freq_x': 0, 'phase_x': 0,
        'amp_y': 4, 'freq_y': 0.6, 'phase_y': 0
    }
]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background
    t = pygame.time.get_ticks() / 1000.0

    for point in points:
        base_x, base_y = point['base_pos']
        dx = point['amp_x'] * math.sin(2 * math.pi * point['freq_x'] * t + point['phase_x'])
        dy = point['amp_y'] * math.sin(2 * math.pi * point['freq_y'] * t + point['phase_y'])
        x, y = base_x + dx, base_y + dy
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
