
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point settings
CENTER = (WIDTH//2, HEIGHT//2)
POINT_RADIUS = 4
NUM_POINTS = 15

# Define initial relative positions for a human figure (x, y)
points_base = [
    (0, -50),    # Head
    (0, -40),    # Neck
    (-30, -30),  # Left shoulder
    (30, -30),   # Right shoulder
    (-40, -10),  # Left elbow
    (40, -10),   # Right elbow
    (-50, 10),   # Left hand
    (50, 10),    # Right hand
    (0, -15),    # Torso
    (-20, 0),    # Left hip
    (20, 0),     # Right hip
    (-25, 30),   # Left knee
    (25, 30),    # Right knee
    (-20, 60),   # Left ankle
    (20, 60)     # Right ankle
]

# Animation parameters
angle = 0
angular_speed = 0.03
phase_offset = 0.5  # For arm/leg movement

clock = pygame.time.Clock()

def rotate_point(x, y, theta):
    """Rotate a point around the origin by theta radians"""
    return (x * math.cos(theta) - y * math.sin(theta),
            x * math.sin(theta) + y * math.cos(theta))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Update points with rotation and dynamic movement
    updated_points = []
    for i, (x, y) in enumerate(points_base):
        # Add subtle vertical movement for arms and legs
        if i in [6, 7]:  # Hands
            dy_mod = 5 * math.sin(angle * 2 + phase_offset)
            y += dy_mod
        elif i in [12, 13, 14]:  # Knees and ankles
            dy_mod = 3 * math.sin(angle * 2)
            y += dy_mod
            
        # Rotate point
        rx, ry = rotate_point(x, y, angle)
        px = int(CENTER[0] + rx)
        py = int(CENTER[1] + ry)
        pygame.draw.circle(screen, WHITE, (px, py), POINT_RADIUS)
    
    # Update rotation angle
    angle += angular_speed
    if angle >= 2 * math.pi:
        angle = 0

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
