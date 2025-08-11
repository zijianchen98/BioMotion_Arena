
"""
This program uses Pygame to display a point‐light biological motion animation. In this example,
15 white point‐lights represent key anatomical landmarks of a "happyman" (a heavy, cheerful man)
lying down. The markers – representing the head, shoulders, elbows, hands, chest, pelvis, hips, knees
and ankles – are drawn on a black background. Their positions are based on a biologically plausible
lying-down posture and have a subtle oscillatory (breathing/weight‐shifting) movement to enhance realism.
"""

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Lying Down Happyman")
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the base positions for 15 point-lights representing:
# 0: Head
# 1: Left Shoulder, 2: Right Shoulder
# 3: Left Elbow, 4: Right Elbow
# 5: Left Hand, 6: Right Hand
# 7: Chest (mid-torso)
# 8: Pelvis
# 9: Left Hip, 10: Right Hip
# 11: Left Knee, 12: Right Knee
# 13: Left Ankle, 14: Right Ankle
#
# These positions are defined so that the subject is lying horizontally.
# They are specified in screen coordinates.
base_points = [
    (500, 300),   # Head
    (480, 290),   # Left Shoulder
    (480, 310),   # Right Shoulder
    (460, 280),   # Left Elbow
    (460, 320),   # Right Elbow
    (440, 270),   # Left Hand
    (440, 330),   # Right Hand
    (460, 300),   # Chest (mid-torso)
    (420, 300),   # Pelvis
    (400, 290),   # Left Hip
    (400, 310),   # Right Hip
    (380, 280),   # Left Knee
    (380, 320),   # Right Knee
    (360, 270),   # Left Ankle
    (360, 330)    # Right Ankle
]

# For smooth and coherent small movements (simulating breathing and weight-shifting),
# assign each point a phase offset based on its index.
phases = [i * 0.3 for i in range(15)]

# Amplitude of the motion (in pixels). These values are small relative to the positions,
# so that the overall posture remains plausible.
AMP_X = 3  # small horizontal jitter
AMP_Y = 2  # small vertical oscillation

# Frequency of the oscillation (radians per second)
FREQ = 2 * math.pi / 2.0  # one full cycle every 2 seconds

# Radius of the drawn point-lights
POINT_RADIUS = 4

# Main animation loop
time_start = pygame.time.get_ticks() / 1000.0  # seconds

running = True
while running:
    # Time in seconds since start
    t = pygame.time.get_ticks() / 1000.0 - time_start

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(BLACK)

    # For smooth and natural oscillatory movement, update each point's position.
    for i, (base_x, base_y) in enumerate(base_points):
        # Calculate offsets using sine and cosine functions with an individual phase.
        offset_x = AMP_X * math.sin(FREQ * t + phases[i])
        offset_y = AMP_Y * math.cos(FREQ * t + phases[i])
        
        # The new (animated) position for the current point
        x = base_x + offset_x
        y = base_y + offset_y
        
        # Draw the point-light as a white circle
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

    # Update the display
    pygame.display.flip()
    
    # Limit frames per second for smooth animation
    clock.tick(60)

pygame.quit()
sys.exit()