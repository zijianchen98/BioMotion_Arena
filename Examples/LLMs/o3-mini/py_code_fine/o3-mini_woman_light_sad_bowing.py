
"""
A Python program that animates a point‐light stimulus representing a sad woman bowing.
The animation shows 15 white point-lights on a black background. The figure is divided into an “upper body” (head, neck, shoulders, elbows, wrists, and a spine point)
that bows forward about the hip center, while the “lower body” (hips, knees, and ankles) remains stable.
The bowing motion is biomechanically plausible and executed smoothly.
"""

import sys
import math
import pygame

# Initialize pygame
pygame.init()

# Screen configuration
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Bowing Sad Woman")

clock = pygame.time.Clock()
FPS = 60

# Scale and offset for drawing: our figure coordinates (in arbitrary units) will be scaled and offset for good display.
SCALE = 2.0
OFFSET_X = 150
OFFSET_Y = 20

# Define the 15 key points of the figure in the upright posture (2D coordinates, y increasing downward).
# The coordinate system here is chosen in arbitrary units.
# Points:
# 0. Head top: (10, 50)
# 1. Neck: (10, 70)
# 2. Spine (mid): (10, 80)
# 3. Left shoulder: (0, 70)
# 4. Right shoulder: (20, 70)
# 5. Left elbow: (-5, 90)
# 6. Right elbow: (25, 90)
# 7. Left wrist: (-10, 110)
# 8. Right wrist: (30, 110)
# 9. Left hip: (5, 100)
# 10. Right hip: (15, 100)
# 11. Left knee: (5, 150)
# 12. Right knee: (15, 150)
# 13. Left ankle: (5, 200)
# 14. Right ankle: (15, 200)
points = [
    (10, 50),   # 0: Head top
    (10, 70),   # 1: Neck
    (10, 80),   # 2: Spine mid
    (0, 70),    # 3: Left shoulder
    (20, 70),   # 4: Right shoulder
    (-5, 90),   # 5: Left elbow
    (25, 90),   # 6: Right elbow
    (-10, 110), # 7: Left wrist
    (30, 110),  # 8: Right wrist
    (5, 100),   # 9: Left hip
    (15, 100),  # 10: Right hip
    (5, 150),   # 11: Left knee
    (15, 150),  # 12: Right knee
    (5, 200),   # 13: Left ankle
    (15, 200)   # 14: Right ankle
]

# Define indices for the upper body and lower body.
# We will transform the upper body to simulate a bowing movement.
upper_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
lower_indices = [9, 10, 11, 12, 13, 14]

# Pivot point for bowing is taken as the hip center: the average of the left and right hip.
hip_center = ( (points[9][0] + points[10][0]) / 2, (points[9][1] + points[10][1]) / 2 )  # (10, 100)

def rotate_point(p, angle, pivot):
    """Rotate point p (tuple) around pivot by angle (radians)."""
    dx = p[0] - pivot[0]
    dy = p[1] - pivot[1]
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    rx = pivot[0] + dx * cos_a - dy * sin_a
    ry = pivot[1] + dx * sin_a + dy * cos_a
    return (rx, ry)

def transform_points(points, angle):
    """Apply bowing transformation to upper body points; lower body remains unchanged."""
    transformed = []
    # Process each point based on its index.
    for i, pt in enumerate(points):
        if i in upper_indices:
            # Rotate this upper body point about the hip center.
            new_pt = rotate_point(pt, angle, hip_center)
        else:
            # Lower body remains the same.
            new_pt = pt
        transformed.append(new_pt)
    return transformed

def to_screen_coords(pt):
    """Convert figure coordinates to screen pixel coordinates, applying scaling and offset."""
    x = pt[0] * SCALE + OFFSET_X
    y = pt[1] * SCALE + OFFSET_Y
    return (int(x), int(y))

# Animation parameters:
# The bowing motion oscillates from upright (angle = 0) to a maximum bow.
MAX_BOW_ANGLE = math.radians(30)  # maximum bowing angle in radians (30 deg)
BOW_PERIOD = 4.0  # seconds for full cycle (bow down and come back)

start_ticks = pygame.time.get_ticks()

running = True
while running:
    # Event handling: allow exit on quit or ESC key.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Calculate elapsed time in seconds.
    elapsed = (pygame.time.get_ticks() - start_ticks) / 1000.0

    # Compute the current bowing angle using a sine wave oscillation.
    # The sine goes from -1 to 1; we take its absolute value (or use a cosine shifted to have 0 mean)
    # so that the figure bows forward and then returns upright.
    # We'll use: angle = MAX_BOW_ANGLE * sin(pi * t / period)
    # To ensure a smooth bow and return, we use half a period for bowing down.
    angle = MAX_BOW_ANGLE * math.sin(math.pi * (elapsed % BOW_PERIOD) / BOW_PERIOD)
    
    # Get transformed points for current frame.
    transformed_points = transform_points(points, angle)
    
    # Clear screen with black background.
    screen.fill((0, 0, 0))
    
    # Draw each point as a white circle.
    for pt in transformed_points:
        # Scale and offset the point to screen coordinates.
        x, y = to_screen_coords(pt)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 4)
    
    # Update the display.
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()