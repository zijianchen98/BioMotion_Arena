
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

# Body parameters
L1 = 60  # Upper arm length (shoulder to elbow)
L2 = 60  # Lower arm length (elbow to hand)
amplitude = 80  # Arm movement amplitude
speed = 0.05  # Animation speed

def compute_elbow(S, H, L1, L2):
    """Calculate elbow position using inverse kinematics"""
    x0, y0 = S
    x3, y3 = H
    dx = x3 - x0
    dy = y3 - y0
    d = math.hypot(dx, dy)
    
    if d > L1 + L2 or d < abs(L1 - L2) or d == 0:
        return None  # No solution
    
    a = (L1**2 - L2**2 + d**2) / (2 * d)
    h = math.sqrt(L1**2 - a**2)
    
    x2 = x0 + a * dx / d
    y2 = y0 + a * dy / d
    
    # Return both possible solutions
    return [
        (x2 + h * dy / d, y2 - h * dx / d),
        (x2 - h * dy / d, y2 + h * dx / d)
    ]

# Initial body points (relative to center)
points = [
    # Head (0)
    {'pos': (0, -120), 'base': (0, -120)},
    # Right Shoulder (1)
    {'pos': (50, -90), 'base': (50, -90)},
    # Left Shoulder (2)
    {'pos': (-50, -90), 'base': (-50, -90)},
    # Right Elbow (3)
    {'pos': (50, -30), 'base': (50, -30)},
    # Left Elbow (4)
    {'pos': (-50, -30), 'base': (-50, -30)},
    # Right Wrist (5)
    {'pos': (50, 30), 'base': (50, 30)},
    # Left Wrist (6)
    {'pos': (-50, 30), 'base': (-50, 30)},
    # Right Hand (7)
    {'pos': (50, 90), 'base': (50, 90)},
    # Left Hand (8)
    {'pos': (-50, 90), 'base': (-50, 90)},
    # Hips (9,10)
    {'pos': (40, 30), 'base': (40, 30)},
    {'pos': (-40, 30), 'base': (-40, 30)},
    # Knees (11,12)
    {'pos': (40, 90), 'base': (40, 90)},
    {'pos': (-40, 90), 'base': (-40, 90)},
    # Ankles (13,14)
    {'pos': (40, 150), 'base': (40, 150)},
    {'pos': (-40, 150), 'base': (-40, 150)}
]

clock = pygame.time.Clock()
time = 0

def translate_coords(point, screen_width, screen_height):
    """Convert mathematical coordinates to pygame screen coordinates"""
    return (int(point[0]) + screen_width//2, int(-point[1]) + screen_height//2)

# Main animation
running = True
prev_elbow = points[3]['pos']
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Update right arm motion
    shoulder = points[1]['base']
    hand_base_x = points[7]['base'][0]
    hand_base_y = points[7]['base'][1]
    
    # Animate hand in circular pattern
    angle = time * 2
    hand_x = hand_base_x + amplitude * math.cos(angle)
    hand_y = hand_base_y + amplitude * 1.2 * math.sin(angle)
    
    # Calculate elbow positions
    solutions = compute_elbow(shoulder, (hand_x, hand_y), L1, L2)
    if solutions:
        # Choose solution closest to previous position
        d1 = math.hypot(solutions[0][0]-prev_elbow[0], solutions[0][1]-prev_elbow[1])
        d2 = math.hypot(solutions[1][0]-prev_elbow[0], solutions[1][1]-prev_elbow[1])
        elbow_pos = solutions[0] if d1 < d2 else solutions[1]
        prev_elbow = elbow_pos
    else:
        elbow_pos = prev_elbow

    # Update points
    points[3]['pos'] = elbow_pos
    points[5]['pos'] = (
        (elbow_pos[0] * 0.3 + hand_x * 0.7),
        (elbow_pos[1] * 0.3 + hand_y * 0.7)
    )
    points[7]['pos'] = (hand_x, hand_y)

    # Add secondary body motion
    body_sway = 10 * math.sin(time)
    points[0]['pos'] = (points[0]['base'][0] + body_sway/2, points[0]['base'][1])
    points[9]['pos'] = (points[9]['base'][0] + body_sway, points[9]['base'][1])
    points[10]['pos'] = (points[10]['base'][0] - body_sway, points[10]['base'][1])

    # Draw all points
    for point in points:
        screen_pos = translate_coords(point['pos'], width, height)
        pygame.draw.circle(screen, WHITE, screen_pos, 8)

    pygame.display.flip()
    time += speed
    clock.tick(30)

pygame.quit()
sys.exit()
