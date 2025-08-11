
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Running")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
SPEED_FACTOR = 0.15
BOB_AMPLITUDE = 15
ARM_AMPLITUDE = 40
LEG_AMPLITUDE = 50
HAND_AMPLITUDE = 20
FOOT_AMPLITUDE = 30

def calculate_positions(t):
    """Calculate positions for 15 body points based on time t"""
    points = []
    
    # Torso (point 0)
    torso_y = BOB_AMPLITUDE * math.sin(t * 0.8)
    points.append((0, torso_y))

    # Head (point 1)
    points.append((0, -80 + torso_y * 0.5))

    # Shoulders (points 2-3)
    shoulder_angle = math.sin(t) * 1.2
    points.append((-40 * math.cos(shoulder_angle), -30 + torso_y))
    points.append((40 * math.cos(shoulder_angle), -30 + torso_y))

    # Elbows (points 4-5)
    elbow_angle = math.sin(t + math.pi/2) * 2.5
    points.append((
        points[2][0] + ARM_AMPLITUDE * math.cos(elbow_angle),
        points[2][1] + ARM_AMPLITUDE * math.sin(elbow_angle)
    ))
    points.append((
        points[3][0] - ARM_AMPLITUDE * math.cos(elbow_angle),
        points[3][1] + ARM_AMPLITUDE * math.sin(elbow_angle)
    ))

    # Hands (points 6-7)
    hand_angle = elbow_angle * 1.2
    points.append((
        points[4][0] + HAND_AMPLITUDE * math.cos(hand_angle),
        points[4][1] + HAND_AMPLITUDE * math.sin(hand_angle)
    ))
    points.append((
        points[5][0] - HAND_AMPLITUDE * math.cos(hand_angle),
        points[5][1] + HAND_AMPLITUDE * math.sin(hand_angle)
    ))

    # Hips (points 8-9)
    hip_angle = math.sin(t + math.pi) * 0.8
    points.append((-25, 30 + torso_y))
    points.append((25, 30 + torso_y))

    # Knees (points 10-11)
    knee_angle = math.sin(t * 1.5) * 2.5
    points.append((
        points[8][0] + LEG_AMPLITUDE * math.cos(knee_angle),
        points[8][1] + LEG_AMPLITUDE * math.sin(knee_angle)
    ))
    points.append((
        points[9][0] - LEG_AMPLITUDE * math.cos(knee_angle),
        points[9][1] + LEG_AMPLITUDE * math.sin(knee_angle)
    ))

    # Ankles (points 12-13)
    ankle_angle = knee_angle * 0.8
    points.append((
        points[10][0] + FOOT_AMPLITUDE * math.cos(ankle_angle),
        points[10][1] + FOOT_AMPLITUDE * math.sin(ankle_angle)
    ))
    points.append((
        points[11][0] - FOOT_AMPLITUDE * math.cos(ankle_angle),
        points[11][1] + FOOT_AMPLITUDE * math.sin(ankle_angle)
    ))

    # Feet (points 14)
    points.append((
        (points[12][0] + points[13][0])/2,
        max(points[12][1], points[13][1]) + 10
    ))

    return points

# Main animation loop
time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Calculate positions
    body_points = calculate_positions(time)
    
    # Draw points
    center_x, center_y = width//2, height//2
    for (dx, dy) in body_points:
        x = center_x + dx
        y = center_y + dy
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 6)
    
    pygame.display.flip()
    time += SPEED_FACTOR
    clock.tick(30)

pygame.quit()
sys.exit()
