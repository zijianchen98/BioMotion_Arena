
"""
This program shows a point‐light stimulus animation representing a human figure “lying down”. 
It simulates 15 white point‐lights (each representing a body joint) moving on a solid black background.
The figure morphs smoothly from an initial standing posture into a final lying posture (obtained by
rotating the body about the torso center) and then back again in a continuous loop.
"""

import sys
import math
import pygame

# Window settings
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the 15 points for the standing posture of the man.
# Joint indices (0 to 14):
#  0: Head top
#  1: Neck
#  2: Left shoulder
#  3: Right shoulder
#  4: Left elbow
#  5: Right elbow
#  6: Left wrist
#  7: Right wrist
#  8: Torso middle
#  9: Left hip
# 10: Right hip
# 11: Left knee
# 12: Right knee
# 13: Left ankle
# 14: Right ankle

standing = [
    (400, 100),  # Head top
    (400, 130),  # Neck
    (360, 140),  # Left shoulder
    (440, 140),  # Right shoulder
    (340, 180),  # Left elbow
    (460, 180),  # Right elbow
    (330, 220),  # Left wrist
    (470, 220),  # Right wrist
    (400, 210),  # Torso middle
    (380, 240),  # Left hip
    (420, 240),  # Right hip
    (370, 300),  # Left knee
    (430, 300),  # Right knee
    (360, 360),  # Left ankle
    (440, 360)   # Right ankle
]

# We compute the final (lying) posture by rotating the standing posture by -90° (clockwise)
# about the torso middle (point index 8). This gives a biomechanically plausible lying posture.
def compute_lying_posture(points, pivot):
    lying = []
    cx, cy = pivot
    for (x, y) in points:
        # Difference from the pivot.
        dx = x - cx
        dy = y - cy
        # Rotate by -90 degrees: (dx, dy) -> (dy, -dx)
        rx = dy
        ry = -dx
        # New point
        lying.append((cx + rx, cy + ry))
    return lying

pivot = standing[8]  # torso middle used as pivot
lying = compute_lying_posture(standing, pivot)

# Interpolation helper: linear interpolation between two points.
def lerp_point(p1, p2, t):
    return (p1[0] + (p2[0] - p1[0]) * t,
            p1[1] + (p2[1] - p1[1]) * t)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion (Lying Down)")
    clock = pygame.time.Clock()

    # Duration (in seconds) for one morph from standing to lying.
    DURATION = 3.0

    # Timer for interpolation. We'll use a ping-pong mode: 0 -> 1 and then 1 -> 0.
    t = 0.0
    direction = 1  # 1 for standing->lying, -1 for lying->standing

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # seconds elapsed since last frame

        # Process events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update interpolation factor.
        t += direction * (dt / DURATION)
        if t >= 1.0:
            t = 1.0
            direction = -1
        elif t <= 0.0:
            t = 0.0
            direction = 1

        # Compute the current positions for each of the 15 points.
        current_points = [lerp_point(standing[i], lying[i], t) for i in range(len(standing))]

        # Draw the scene.
        screen.fill(BLACK)
        for point in current_points:
            # draw a small white circle for each point-light
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()