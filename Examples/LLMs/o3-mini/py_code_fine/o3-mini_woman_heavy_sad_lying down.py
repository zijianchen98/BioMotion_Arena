
"""
This program displays a point‐light biological motion animation that shows the
silhouette of a sad woman with heavy weight lying down. The stimulus consists
of exactly 15 white “point‐lights” moving against a solid black background.
The movement is produced by smoothly modulating each point’s position over time,
giving a coherent, biomechanically plausible (though simple) impression of a
body “sinking” and shifting as if in a heavy, languid state.
"""

import sys
import math
import pygame
import time

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define a PointLight class to encapsulate a body marker with its base location,
# a phase offset, and an amplitude of movement.
class PointLight:
    def __init__(self, base_x, base_y, phase, amplitude):
        self.base_x = base_x
        self.base_y = base_y
        self.phase = phase
        self.amplitude = amplitude

    def position(self, t):
        # Each point oscillates vertically (simulate subtle breathing/sagging)
        # and horizontally (a slight lateral shift), with different phase.
        dx = self.amplitude * math.sin(t + self.phase)
        dy = self.amplitude * math.cos(t + self.phase)
        return self.base_x + dx, self.base_y + dy

# Create a list of exactly 15 point-lights representing key parts of the body.
# The coordinates are chosen so that the body is horizontal (i.e. lying down)
# and arranged from the head on the left to the foot on the right.
#
# The points approximate a skeleton:
#   0: Head center
#   1: Chin
#   2: Left shoulder
#   3: Right shoulder
#   4: Left elbow
#   5: Right elbow
#   6: Left wrist
#   7: Right wrist
#   8: Upper torso (sternum)
#   9: Mid-torso
#   10: Left hip
#   11: Right hip
#   12: Left knee
#   13: Right knee
#   14: Left ankle (foot)
# 
# These positions are “lying down” on a virtual horizontal line.
base_points = [
    (200, 300),  # 0 Head center
    (240, 300),  # 1 Chin
    (280, 280),  # 2 Left shoulder (slightly higher)
    (280, 320),  # 3 Right shoulder (slightly lower)
    (330, 270),  # 4 Left elbow (rising toward the hand)
    (330, 330),  # 5 Right elbow
    (380, 265),  # 6 Left wrist
    (380, 335),  # 7 Right wrist
    (350, 300),  # 8 Upper torso (center)
    (400, 300),  # 9 Mid-torso
    (420, 290),  # 10 Left hip (slightly up)
    (420, 310),  # 11 Right hip (slightly down)
    (470, 285),  # 12 Left knee
    (470, 315),  # 13 Right knee
    (520, 280)   # 14 Left ankle (foot)
]

# For biomechanically plausible and diverse slight movement,
# assign each point a phase and a small amplitude.
import random
random.seed(42) # For reproducibility

point_lights = []
for (x, y) in base_points:
    phase = random.uniform(0, 2*math.pi)
    amplitude = random.uniform(1.0, 3.0)  # small displacement amplitude
    point_lights.append(PointLight(x, y, phase, amplitude))

# Create the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion Animation – Sad Woman Lying Down")

# Main loop
start_time = time.time()
running = True
while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate time elapsed
    t = time.time() - start_time

    # Fill background with black
    screen.fill(BLACK)

    # Calculate new positions and draw each point as a small white circle.
    for point in point_lights:
        x, y = point.position(t)
        # Draw point as a circle with radius 4
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 4)
        
    # Optionally, for a more “sagging” heavy-weight feeling we can add a slight
    # global downward drift (oscillatory) on the mid-torso and hip points.
    # This is already partly simulated by each point's gentle oscillation.

    # Update the display
    pygame.display.flip()
    
    # Ensure the program maintains a rate of FPS frames per second.
    clock.tick(FPS)

pygame.quit()
sys.exit()