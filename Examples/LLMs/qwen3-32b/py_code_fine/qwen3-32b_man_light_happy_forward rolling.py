
import pygame
import math
import sys
import time

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Happy Man Forward Rolling")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 30
clock = pygame.time.Clock()

# Number of points
NUM_POINTS = 15

# Body joint indices
JOINTS = {
    'hips': 0,
    'left_hip': 1,
    'right_hip': 2,
    'left_knee': 3,
    'right_knee': 4,
    'left_ankle': 5,
    'right_ankle': 6,
    'spine': 7,
    'left_shoulder': 8,
    'right_shoulder': 9,
    'left_elbow': 10,
    'right_elbow': 11,
    'left_wrist': 12,
    'right_wrist': 13,
    'head': 14
}

# Base joint positions (relative to hips)
BASE_JOINTS = {
    JOINTS['hips']: (0, 0),
    JOINTS['left_hip']: (-20, 20),
    JOINTS['right_hip']: (20, 20),
    JOINTS['left_knee']: (-20, 60),
    JOINTS['right_knee']: (20, 60),
    JOINTS['left_ankle']: (-20, 100),
    JOINTS['right_ankle']: (20, 100),
    JOINTS['spine']: (0, -30),
    JOINTS['left_shoulder']: (-20, -50),
    JOINTS['right_shoulder']: (20, -50),
    JOINTS['left_elbow']: (-40, -50),
    JOINTS['right_elbow']: (40, -50),
    JOINTS['left_wrist']: (-60, -50),
    JOINTS['right_wrist']: (60, -50),
    JOINTS['head']: (0, -80)
}

# Rolling motion parameters
ROLL_SPEED = 0.05  # radians per frame
ROLL_AXIS = (0, 1)  # roll around y-axis
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Rolling animation function
def rotate_point(point, angle, center):
    px, py = point
    cx, cy = center
    s = math.sin(angle)
    c = math.cos(angle)
    # Translate point to origin
    px -= cx
    py -= cy
    # Rotate
    xnew = px * c - py * s
    ynew = px * s + py * c
    # Translate back
    return (xnew + cx, ynew + cy)

# Main loop
angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate current joint positions
    points = []
    for joint_id, (x, y) in BASE_JOINTS.items():
        # Apply rolling animation
        rotated_x = x * math.cos(angle) - y * math.sin(angle)
        rotated_y = x * math.sin(angle) + y * math.cos(angle)
        px = CENTER_X + rotated_x
        py = CENTER_Y + rotated_y
        points.append((px, py))

    # Draw point lights
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    # Update the rolling angle
    angle += ROLL_SPEED
    if angle >= 2 * math.pi:
        angle = 0  # Reset for continuous motion

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
