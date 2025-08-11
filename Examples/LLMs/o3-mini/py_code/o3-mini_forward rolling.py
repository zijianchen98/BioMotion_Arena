
"""
A Python program that shows a point‐light stimulus animation representing a man performing a forward roll.
The animation uses exactly 15 white “point‐lights” (drawn as small circles) on a solid black background.
The figure smoothly transitions from an upright pose into a tucked (rolling) pose at mid‐roll and back,
while the whole figure rotates a full 360° (simulating the forward roll) and translates forward.
"""

import math
import sys
import pygame

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Forward Roll Point-Light Animation")

clock = pygame.time.Clock()
FPS = 60

# Total duration of one roll animation (in frames)
total_frames = 180  # 3 seconds per roll

# Define two sets of 15 joint coordinates (in a local coordinate system)
# Upright pose (rough approximation of a standing man)
upright = [
    (0, -50),    #  1. Head
    (0, -40),    #  2. Neck
    (-10, -35),  #  3. Left shoulder
    (10, -35),   #  4. Right shoulder
    (-20, -20),  #  5. Left elbow
    (20, -20),   #  6. Right elbow
    (-25, -5),   #  7. Left hand
    (25, -5),    #  8. Right hand
    (0, 0),      #  9. Torso
    (-10, 10),   # 10. Left hip
    (10, 10),    # 11. Right hip
    (-10, 30),   # 12. Left knee
    (10, 30),    # 13. Right knee
    (-10, 50),   # 14. Left foot
    (10, 50)     # 15. Right foot
]

# Tucked pose (approximation of the body during the roll)
# In a proper forward roll, the body tucks in considerably.
tucked = [
    (0, -20),    #  1. Head brought low
    (0, -15),    #  2. Neck
    (-5, -15),   #  3. Left shoulder (closer to center)
    (5, -15),    #  4. Right shoulder
    (-5, -5),    #  5. Left elbow (arms tucked)
    (5, -5),     #  6. Right elbow
    (-5, 0),     #  7. Left hand
    (5, 0),      #  8. Right hand
    (0, 0),      #  9. Torso (remains near center)
    (-5, 5),     # 10. Left hip (tucked)
    (5, 5),      # 11. Right hip
    (-5, 15),    # 12. Left knee (bent in)
    (5, 15),     # 13. Right knee
    (-5, 25),    # 14. Left foot (drawn in)
    (5, 25)      # 15. Right foot
]

def interpolate_points(pointsA, pointsB, factor):
    """Linearly interpolate between two sets of points (lists of (x,y))"""
    interp = []
    for (xa, ya), (xb, yb) in zip(pointsA, pointsB):
        x = (1 - factor) * xa + factor * xb
        y = (1 - factor) * ya + factor * yb
        interp.append((x, y))
    return interp

def rotate_point(point, angle):
    """Rotate a 2D point (x,y) by given angle (radians) around the origin."""
    x, y = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    x_new = x * cos_a - y * sin_a
    y_new = x * sin_a + y * cos_a
    return (x_new, y_new)

def transform_points(points, angle, translation):
    """Apply rotation and then translation to a list of points."""
    tx, ty = translation
    transformed = []
    for pt in points:
        rot_pt = rotate_point(pt, angle)
        transformed.append((rot_pt[0] + tx, rot_pt[1] + ty))
    return transformed

# Animation parameters for global translation.
# The figure will move horizontally from x=100 to x=700 and a slight vertical arch.
initial_x = 100
final_x = 700
base_y = 300   # Base vertical position for the torso
vertical_amp = 20  # Amplitude for vertical arch (rises in the middle of the roll)

frame = 0
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate normalized time (0 to 1)
    t_norm = frame / total_frames
    if t_norm > 1:
        frame = 0
        t_norm = 0

    # Compute roll rotation angle (a full 360° roll = 2*pi rad)
    angle = 2 * math.pi * t_norm

    # Use sine interpolation to smoothly change pose: f=0 at beginning and end, f=1 at middle.
    interp_factor = math.sin(math.pi * t_norm)
    current_pose = interpolate_points(upright, tucked, interp_factor)

    # Compute global translation: linear horizontal motion and vertical arch.
    current_x = initial_x + (final_x - initial_x) * t_norm
    # Vertical offset: raise the figure near the middle of roll
    current_y = base_y - vertical_amp * math.sin(2 * math.pi * t_norm)
    translation = (current_x, current_y)

    # Transform the current pose by rotating it and then translating.
    transformed_points = transform_points(current_pose, angle, translation)

    # Draw animation: clear screen, draw points.
    screen.fill((0, 0, 0))
    
    # Optionally draw a ground reference line
    ground_y = base_y + 100
    pygame.draw.line(screen, (50, 50, 50), (0, ground_y), (width, ground_y), 2)
    
    # Draw each point as a circle (radius 5)
    for pt in transformed_points:
        # Use anti-aliasing by drawing a small circle – these are the point-lights.
        pygame.draw.circle(screen, (255, 255, 255), (int(pt[0]), int(pt[1])), 5)
    
    pygame.display.flip()

    # Advance frame
    frame += 1
    clock.tick(FPS)

pygame.quit()
sys.exit()