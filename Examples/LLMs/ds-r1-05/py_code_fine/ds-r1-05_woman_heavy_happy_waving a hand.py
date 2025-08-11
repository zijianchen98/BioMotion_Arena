
import pygame
import math
import sys

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600
FPS = 60

# Arm configuration
AMPLITUDE = math.pi / 6  # 30 degrees in radians
OMEGA = 2 * math.pi / 1.2  # 1.2 second cycle
UPPER_ARM = 60
FOREARM = 50
TORSO_DAMPING = 6  # Torso movement coefficient

# Point definitions (relative to torso)
POINTS = [
    (0, -120),    # Head
    (0, -100),    # Neck
    (-40, -80),   # Left Shoulder
    (40, -80),    # Right Shoulder
    (-60, -40),   # Left Elbow
    (0, 0),       # Right Elbow (dynamic)
    (-60, 20),    # Left Wrist
    (0, 0),       # Right Wrist (dynamic)
    (0, 0),       # Torso
    (-25, 40),    # Left Hip
    (25, 40),     # Right Hip
    (-25, 80),    # Left Knee
    (25, 80),     # Right Knee
    (-25, 160),   # Left Ankle
    (25, 160)     # Right Ankle
]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

def calculate_positions(theta, torso_x):
    """Calculate all point positions based on arm angle and torso offset"""
    # Right arm components
    shoulder_x, shoulder_y = POINTS[3]
    elbow_rel_x = shoulder_x + UPPER_ARM * math.sin(theta)
    elbow_rel_y = shoulder_y - UPPER_ARM * math.cos(theta)
    wrist_rel_x = elbow_rel_x + FOREARM * math.cos(theta)
    wrist_rel_y = elbow_rel_y + FOREARM * math.sin(theta)

    positions = []
    for i, (rel_x, rel_y) in enumerate(POINTS):
        if i == 5:  # Right Elbow
            x, y = torso_x + elbow_rel_x, elbow_rel_y
        elif i == 7:  # Right Wrist
            x, y = torso_x + wrist_rel_x, wrist_rel_y
        else:
            x, y = torso_x + rel_x, rel_y
        positions.append((x, y))
    return positions

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time = pygame.time.get_ticks() / 1000.0
    theta = AMPLITUDE * math.sin(OMEGA * time)
    torso_x = -TORSO_DAMPING * theta

    current_points = calculate_positions(theta, torso_x)

    # Drawing
    screen.fill(BLACK)
    for x, y in current_points:
        screen_x = int(WIDTH/2 + x)
        screen_y = int(HEIGHT/2 + y)
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
