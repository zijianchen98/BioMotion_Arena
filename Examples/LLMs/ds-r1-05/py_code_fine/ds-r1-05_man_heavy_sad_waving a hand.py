
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Arm parameters
amplitude = math.pi / 3  # Swing range
frequency = 1.2  # Wave speed
L1 = 40  # Upper arm length
L2 = 30  # Forearm length
phi = math.pi / 2  # Elbow bend

# Initialize body points with positions and motion functions
points = [
    # Head (0)
    {'pos': (400, 100), 'motion': lambda t: (400, 100 + 4 * math.sin(2 * t))},
    # Left Shoulder (1)
    {'pos': (350, 150), 'motion': None},
    # Right Shoulder (2)
    {'pos': (450, 150), 'motion': None},
    # Left Elbow (3)
    {'pos': (310, 190), 'motion': None},
    # Right Elbow (4) - dynamic
    {'pos': (0, 0), 'motion': None},
    # Left Hand (5)
    {'pos': (280, 190), 'motion': None},
    # Right Hand (6) - dynamic
    {'pos': (0, 0), 'motion': None},
    # Torso (7)
    {'pos': (400, 200), 'motion': lambda t: (400, 200 + 3 * math.sin(t * 1.5))},
    # Left Hip (8)
    {'pos': (370, 300), 'motion': lambda t: (370 + 4 * math.sin(t), 300)},
    # Right Hip (9)
    {'pos': (430, 300), 'motion': lambda t: (430 + 4 * math.sin(t), 300)},
    # Left Knee (10)
    {'pos': (370, 400), 'motion': lambda t: (370, 400 + 4 * math.sin(t * 2))},
    # Right Knee (11)
    {'pos': (430, 400), 'motion': lambda t: (430, 400 + 4 * math.sin(t * 2))},
    # Left Foot (12)
    {'pos': (370, 500), 'motion': None},
    # Right Foot (13)
    {'pos': (430, 500), 'motion': None},
    # Mid Hip (14)
    {'pos': (400, 300), 'motion': lambda t: (400 + 3 * math.sin(t), 300 + 2 * math.sin(t * 0.8))},
]

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    current_time = pygame.time.get_ticks() / 1000  # Current time in seconds

    # Calculate arm dynamics
    theta = amplitude * math.sin(2 * math.pi * frequency * current_time)
    rs_x, rs_y = points[2]['pos']
    
    # Update right arm positions
    re_x = rs_x + L1 * math.cos(theta)
    re_y = rs_y + L1 * math.sin(theta)
    rh_x = re_x + L2 * math.cos(theta + phi)
    rh_y = re_y + L2 * math.sin(theta + phi)

    points[4]['pos'] = (re_x, re_y)
    points[6]['pos'] = (rh_x, rh_y)

    # Update other points' positions
    for i in range(len(points)):
        if callable(points[i].get('motion')):
            t = current_time
            new_x, new_y = points[i]['motion'](t)
            points[i]['pos'] = (new_x, new_y)

    # Draw all points
    for point in points:
        x, y = point['pos']
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
