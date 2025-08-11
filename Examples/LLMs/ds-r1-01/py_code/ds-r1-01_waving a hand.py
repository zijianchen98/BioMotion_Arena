
import pygame
import math
import sys

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Waving Hand")
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize points with base positions and movement parameters
points = [
    # Head (0)
    {'base_x': 400, 'base_y': 100, 'amp_x': 0, 'amp_y': 2, 'freq': 0.5, 'phase': 0},
    # Neck (1)
    {'base_x': 400, 'base_y': 150, 'amp_x': 0, 'amp_y': 1, 'freq': 0.5, 'phase': 0},
    # Left Shoulder (2)
    {'base_x': 350, 'base_y': 160, 'amp_x': 1, 'amp_y': 1, 'freq': 0.3, 'phase': 0.2},
    # Left Elbow (3)
    {'base_x': 330, 'base_y': 200, 'amp_x': 1, 'amp_y': 1, 'freq': 0.3, 'phase': 0.4},
    # Left Wrist (4)
    {'base_x': 310, 'base_y': 250, 'amp_x': 1, 'amp_y': 1, 'freq': 0.3, 'phase': 0.6},
    # Right Shoulder (5)
    {'base_x': 450, 'base_y': 160, 'amp_x': 0, 'amp_y': 0, 'freq': 0, 'phase': 0},
    # Right Elbow (6)
    {'base_x': 470, 'base_y': 200, 'amp_x': 0, 'amp_y': 0, 'freq': 0, 'phase': 0},
    # Right Wrist (7)
    {'base_x': 490, 'base_y': 250, 'amp_x': 0, 'amp_y': 0, 'freq': 0, 'phase': 0},
    # Torso (8)
    {'base_x': 400, 'base_y': 200, 'amp_x': 2, 'amp_y': 1, 'freq': 0.2, 'phase': 0},
    # Left Hip (9)
    {'base_x': 380, 'base_y': 300, 'amp_x': 1, 'amp_y': 1, 'freq': 0.4, 'phase': 0.3},
    # Left Knee (10)
    {'base_x': 380, 'base_y': 400, 'amp_x': 1, 'amp_y': 1, 'freq': 0.4, 'phase': 0.6},
    # Left Ankle (11)
    {'base_x': 380, 'base_y': 500, 'amp_x': 1, 'amp_y': 1, 'freq': 0.4, 'phase': 0.9},
    # Right Hip (12)
    {'base_x': 420, 'base_y': 300, 'amp_x': 1, 'amp_y': 1, 'freq': 0.4, 'phase': 0.3},
    # Right Knee (13)
    {'base_x': 420, 'base_y': 400, 'amp_x': 1, 'amp_y': 1, 'freq': 0.4, 'phase': 0.6},
    # Right Ankle (14)
    {'base_x': 420, 'base_y': 500, 'amp_x': 1, 'amp_y': 1, 'freq': 0.4, 'phase': 0.9},
]

# Initialize current positions
for point in points:
    point['current_x'] = point['base_x']
    point['current_y'] = point['base_y']

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    current_time = pygame.time.get_ticks() / 1000  # Get current time in seconds

    # Update right arm positions
    shoulder = points[5]
    wrist = points[7]
    elbow = points[6]

    # Wrist movement parameters
    wrist_amp_x = 50
    wrist_amp_y = 30
    wrist_freq = 1.0
    angle = 2 * math.pi * wrist_freq * current_time

    # Calculate wrist position
    wrist_x = shoulder['base_x'] + wrist_amp_x * math.sin(angle)
    wrist_y = shoulder['base_y'] + wrist_amp_y * (1 + math.sin(angle + math.pi/2))

    # Calculate elbow position with biomechanical bend
    dx = wrist_x - shoulder['base_x']
    dy = wrist_y - shoulder['base_y']
    elbow_x = shoulder['base_x'] + 0.4 * dx
    elbow_y = shoulder['base_y'] + 0.4 * dy
    perp_scale = 0.5
    elbow_x += -dy * perp_scale
    elbow_y += dx * perp_scale

    # Update dynamic points
    wrist['current_x'], wrist['current_y'] = wrist_x, wrist_y
    elbow['current_x'], elbow['current_y'] = elbow_x, elbow_y

    # Update other points with subtle movements
    for i in range(len(points)):
        if i in [5, 6, 7]:
            continue  # Skip already updated points
        pt = points[i]
        t = 2 * math.pi * pt['freq'] * current_time + pt['phase']
        pt['current_x'] = pt['base_x'] + pt['amp_x'] * math.sin(t)
        pt['current_y'] = pt['base_y'] + pt['amp_y'] * math.sin(t)

    # Draw all points
    for pt in points:
        pygame.draw.circle(screen, WHITE, (int(pt['current_x']), int(pt['current_y'])), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
