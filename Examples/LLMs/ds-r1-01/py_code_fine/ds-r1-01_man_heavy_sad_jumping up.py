
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point parameters
points_params = [
    # Head (1)
    {'x_offset': 0, 'y_offset': -60, 'x_osc_amp': 0, 'y_osc_amp': 0, 'phase_shift': 0},
    # Left Shoulder (2)
    {'x_offset': -30, 'y_offset': -30, 'x_osc_amp': 8, 'y_osc_amp': 5, 'phase_shift': 0.2},
    # Right Shoulder (3)
    {'x_offset': 30, 'y_offset': -30, 'x_osc_amp': 8, 'y_osc_amp': 5, 'phase_shift': 0.2},
    # Left Elbow (4)
    {'x_offset': -50, 'y_offset': 10, 'x_osc_amp': 15, 'y_osc_amp': 10, 'phase_shift': 0.4},
    # Right Elbow (5)
    {'x_offset': 50, 'y_offset': 10, 'x_osc_amp': 15, 'y_osc_amp': 10, 'phase_shift': 0.4},
    # Left Wrist (6)
    {'x_offset': -70, 'y_offset': 40, 'x_osc_amp': 20, 'y_osc_amp': 15, 'phase_shift': 0.6},
    # Right Wrist (7)
    {'x_offset': 70, 'y_offset': 40, 'x_osc_amp': 20, 'y_osc_amp': 15, 'phase_shift': 0.6},
    # Left Hip (8)
    {'x_offset': -20, 'y_offset': 0, 'x_osc_amp': 0, 'y_osc_amp': 0, 'phase_shift': 0},
    # Right Hip (9)
    {'x_offset': 20, 'y_offset': 0, 'x_osc_amp': 0, 'y_osc_amp': 0, 'phase_shift': 0},
    # Left Knee (10)
    {'x_offset': -20, 'y_offset': 50, 'x_osc_amp': 0, 'y_osc_amp': 25, 'phase_shift': 0.5},
    # Right Knee (11)
    {'x_offset': 20, 'y_offset': 50, 'x_osc_amp': 0, 'y_osc_amp': 25, 'phase_shift': 0.5},
    # Left Ankle (12)
    {'x_offset': -20, 'y_offset': 100, 'x_osc_amp': 0, 'y_osc_amp': 30, 'phase_shift': 0.7},
    # Right Ankle (13)
    {'x_offset': 20, 'y_offset': 100, 'x_osc_amp': 0, 'y_osc_amp': 30, 'phase_shift': 0.7},
    # Left Foot (14)
    {'x_offset': -25, 'y_offset': 130, 'x_osc_amp': 0, 'y_osc_amp': 15, 'phase_shift': 0.8},
    # Right Foot (15)
    {'x_offset': 25, 'y_offset': 130, 'x_osc_amp': 0, 'y_osc_amp': 15, 'phase_shift': 0.8},
]

# Animation parameters
phase = 0.0
phase_increment = 0.01  # Slower for heavier appearance
jump_height = 40  # Reduced jump for heavy weight
baseline_y = height // 2 + 100  # Lower baseline for grounded appearance
center_x = width // 2

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update phase
    phase += phase_increment
    if phase >= 1.0:
        phase -= 1.0

    # Calculate center y with parabolic motion
    center_y = baseline_y - (jump_height * 4 * (phase - 0.5)**2)

    # Update and draw points
    for params in points_params:
        x = center_x + params['x_offset'] + params['x_osc_amp'] * math.sin(2 * math.pi * (phase + params['phase_shift']))
        y = center_y + params['y_offset'] + params['y_osc_amp'] * math.sin(2 * math.pi * (phase + params['phase_shift']))
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS for smooth animation

pygame.quit()
sys.exit()
