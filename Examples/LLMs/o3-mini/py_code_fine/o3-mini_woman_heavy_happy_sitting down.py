
"""
This program creates a point‐light stimulus animation of a “happy woman with heavy weight
sitting down” using 15 white point‐lights on a black background. The 15 points represent
key anatomical landmarks (e.g., head, shoulders, elbows, hands, torso, hips, knees, ankles, and mid‐torso).
The animation linearly (with smooth easing) interpolates between a standing pose (initial)
and a sitting pose (final). The poses have been manually designed to be biomechanically plausible.
"""

import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Window dimensions and colors
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30  # frames per second

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Sitting Down")

clock = pygame.time.Clock()

# Define initial (standing) positions for 15 points.
# Coordinates are chosen so that the figure is roughly centered.
# 1. Head, 2. Left shoulder, 3. Right shoulder,
# 4. Left elbow, 5. Right elbow, 6. Left hand, 7. Right hand,
# 8. Torso top, 9. Left hip, 10. Right hip,
# 11. Left knee, 12. Right knee, 13. Left ankle, 14. Right ankle,
# 15. Belly (mid-torso)

start_points = [
    (300, 100),  # 1. Head
    (250, 150),  # 2. Left shoulder
    (350, 150),  # 3. Right shoulder
    (230, 200),  # 4. Left elbow
    (370, 200),  # 5. Right elbow
    (220, 240),  # 6. Left hand
    (380, 240),  # 7. Right hand
    (300, 150),  # 8. Torso top
    (270, 250),  # 9. Left hip
    (330, 250),  # 10. Right hip
    (260, 350),  # 11. Left knee
    (340, 350),  # 12. Right knee
    (250, 450),  # 13. Left ankle
    (350, 450),  # 14. Right ankle
    (300, 200)   # 15. Belly (mid-torso)
]

# Define final (sitting) positions for the points.
# The sitting pose shifts the body downward and brings the knees and hips forward.
final_points = [
    (300, 150),  # 1. Head moves downward
    (240, 200),  # 2. Left shoulder, slightly left and down
    (360, 200),  # 3. Right shoulder
    (230, 250),  # 4. Left elbow moves down
    (370, 250),  # 5. Right elbow
    (220, 300),  # 6. Left hand moves down more
    (380, 300),  # 7. Right hand
    (300, 200),  # 8. Torso top downward
    (290, 300),  # 9. Left hip moves down and slightly right
    (310, 300),  # 10. Right hip
    (290, 400),  # 11. Left knee forward and down
    (310, 400),  # 12. Right knee
    (280, 450),  # 13. Left ankle
    (320, 450),  # 14. Right ankle
    (300, 230)   # 15. Belly shifts downward a bit further
]

# Total animation frames and duration
total_frames = 200

# Easing function for smooth motion (sinusoidal easing in-out)
def ease(t):
    # t between 0 and 1. 
    # Easing: (1 - cos(pi*t)) / 2 gives a smooth start and end.
    return (1 - math.cos(math.pi * t)) / 2

# Main animation loop
frame = 0
running = True
while running:
    # Check for quit events (so window can be closed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen to black
    screen.fill(BLACK)

    # Compute interpolation factor using easing.
    t = min(frame / total_frames, 1)
    f = ease(t)

    # Interpolate positions for each point and draw them.
    for (start, end) in zip(start_points, final_points):
        x = start[0] + (end[0] - start[0]) * f
        y = start[1] + (end[1] - start[1]) * f
        # Draw a white circle (point-light) of radius 5 pixels.
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(FPS)

    # Increment frame until reaching end of animation
    if frame < total_frames:
        frame += 1

# Pause briefly before quitting (so last frame remains visible)
pygame.time.delay(2000)
pygame.quit()
sys.exit()