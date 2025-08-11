
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define base body points (relative coordinates)
BASE_POINTS = {
    # Head and torso
    "head":       (0, -155),
    "neck":       (0, -125),
    "torso":      (0, -90),
    
    # Arms (with wider stance for heavy build)
    "l_shoulder": (-60, -115),
    "r_shoulder": (60, -115),
    "l_elbow":    (-90, -85),
    "r_elbow":    (90, -85),
    "l_wrist":    (-100, -55),
    "r_wrist":    (100, -55),
    
    # Legs (wider stance with shorter stride)
    "l_hip":      (-45, 15),
    "r_hip":      (45, 15),
    "l_knee":     (-45, 65),
    "r_knee":     (45, 65),
    "l_ankle":    (-45, 130),
    "r_ankle":    (45, 130)
}

# Biomechanical motion parameters
TIME = 0
SPEED = 0.8  # Slower speed for heavy weight
BOB_AMPLITUDE = 15  # More vertical movement for heavy build
STRIDE_WIDTH = 30   # Shorter stride for heavy weight

# Weight adjustments
KNEE_FLEX = 0.4
ANKLE_FLEX = 0.6
SHOULDER_SWAY = 0.3
ELBOW_SWAY = 0.45

# Happiness parameters
HAPPY_SWAY = 5.0     # Horizontal torso sway
HAPPY_BOUNCE = 1.2   # Extra vertical bounce

def calculate_point_positions(t):
    points = {}
    
    # Base body movements (vertical bobbing + horizontal sway)
    vertical_offset = BOB_AMPLITUDE * math.sin(t * 2 * math.pi) * HAPPY_BOUNCE
    horizontal_offset = 35 * math.sin(t * HAPPY_SWAY * math.pi)
    
    # Calculate all point positions
    for point, (base_x, base_y) in BASE_POINTS.items():
        # Adjust positions based on limb types
        if "ankle" in point:
            direction = -1 if "l_" in point else 1
            phase = 0 if "l_" in point else math.pi
            angle = t * 2 * math.pi * SPEED + phase
            points[point] = (
                base_x + direction * STRIDE_WIDTH * math.sin(angle) * ANKLE_FLEX,
                base_y + vertical_offset + 45 * abs(math.sin(angle * 2))
            )
        elif "knee" in point:
            direction = -1 if "l_" in point else 1
            phase = 0 if "l_" in point else math.pi
            angle = t * 2 * math.pi * SPEED + phase
            points[point] = (
                base_x + direction * math.sin(angle) * STRIDE_WIDTH * KNEE_FLEX,
                base_y + vertical_offset + 15 * abs(math.sin(angle * 2.5))
            )
        elif "hip" in point:
            points[point] = (base_x, base_y + vertical_offset)
        elif "wrist" in point:
            direction = -1 if "l_" in point else 1
            phase = math.pi if "l_" in point else 0
            angle = t * 2 * math.pi * SPEED + phase
            points[point] = (
                base_x + direction * math.cos(angle) * 60 * ELBOW_SWAY,
                base_y + vertical_offset
            )
        elif "shoulder" in point:
            direction = -1 if "l_" in point else 1
            angle = t * 4 * math.pi * SPEED
            points[point] = (
                base_x + direction * math.sin(angle) * 20 * SHOULDER_SWAY,
                base_y + vertical_offset
            )
        else:  # Head/neck/torso
            points[point] = (base_x + horizontal_offset, base_y + vertical_offset)
    
    return points

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Increment time
    TIME += 0.01
    
    # Get current positions
    point_positions = calculate_point_positions(TIME)
    
    # Draw all points
    for name, (x, y) in point_positions.items():
        pygame.draw.circle(
            screen, 
            WHITE, 
            (int(x) + WIDTH//2, int(y) + HEIGHT//2 + 30),  # Center on screen
            6
        )
    
    # Display update
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
