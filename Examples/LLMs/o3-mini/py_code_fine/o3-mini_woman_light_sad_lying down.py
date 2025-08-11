
"""
This program displays an animated point‐light stimulus of a “sadwoman” lying down.
It shows exactly fifteen white “markers” (point‐lights) on a solid black background.
Each marker represents a key joint of the body and moves with a small,
cyclic (breathing‐like) oscillation that is designed to be smooth, coherent, 
and biomechanically plausible.
 
The 15 markers are assigned as follows:
  1. Head
  2. Left Shoulder 
  3. Right Shoulder 
  4. Left Elbow 
  5. Right Elbow 
  6. Left Hand 
  7. Right Hand 
  8. Spine (upper torso)
  9. Pelvis (lower torso)
 10. Left Hip 
 11. Right Hip 
 12. Left Knee 
 13. Right Knee 
 14. Left Foot 
 15. Right Foot
 
The base positions (in pixels) are chosen to represent a lying-down posture 
with the body oriented approximately horizontally. In the animation, each joint 
oscillates gently (simulating breathing and subtle shifts) using a sinusoidal function.
 
Press the window close button to exit.
"""

import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen size and settings
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sadwoman Lying Down - Point-Light Biological Motion")

clock = pygame.time.Clock()

# Define the base positions for the 15 markers.
# The coordinates are chosen so that the body’s midline is roughly horizontal.
# (These positions can be interpreted as “world coordinates” and are later drawn directly.)
# For clarity, the coordinate system here uses (x,y) where x increases to the right, y increases downward.
#
#    Legend of markers:
#      1: Head
#      2: Left Shoulder     3: Right Shoulder
#      4: Left Elbow        5: Right Elbow
#      6: Left Hand         7: Right Hand
#      8: Spine (upper central)
#      9: Pelvis (lower central)
#     10: Left Hip         11: Right Hip
#     12: Left Knee        13: Right Knee
#     14: Left Foot        15: Right Foot
#
# The body is centered roughly in the middle of the screen.
offset_x = 150  # horizontal offset to center the skeleton in the window
offset_y = 150  # vertical offset

base_points = {
    1:  (300 + offset_x, 300 + offset_y),    # Head
    2:  (340 + offset_x, 280 + offset_y),    # Left Shoulder
    3:  (360 + offset_x, 280 + offset_y),    # Right Shoulder
    4:  (325 + offset_x, 260 + offset_y),    # Left Elbow
    5:  (375 + offset_x, 260 + offset_y),    # Right Elbow
    6:  (315 + offset_x, 250 + offset_y),    # Left Hand
    7:  (385 + offset_x, 250 + offset_y),    # Right Hand
    8:  (350 + offset_x, 300 + offset_y),    # Spine (upper torso)
    9:  (370 + offset_x, 300 + offset_y),    # Pelvis (lower torso)
    10: (355 + offset_x, 310 + offset_y),    # Left Hip
    11: (365 + offset_x, 310 + offset_y),    # Right Hip
    12: (345 + offset_x, 330 + offset_y),    # Left Knee
    13: (375 + offset_x, 330 + offset_y),    # Right Knee
    14: (335 + offset_x, 350 + offset_y),    # Left Foot
    15: (385 + offset_x, 350 + offset_y),    # Right Foot
}

# Define amplitude (in pixels) for the oscillatory motion for each marker.
# Slight differences in amplitude yield a realistic "breathing" and subtle movement.
amp_table = {
    1:  (2, 2),   # Head
    2:  (2, 2),   # Left Shoulder
    3:  (2, 2),   # Right Shoulder
    4:  (3, 3),   # Left Elbow
    5:  (3, 3),   # Right Elbow
    6:  (3, 3),   # Left Hand
    7:  (3, 3),   # Right Hand
    8:  (2, 2),   # Spine
    9:  (2, 2),   # Pelvis
    10: (2, 2),   # Left Hip
    11: (2, 2),   # Right Hip
    12: (3, 3),   # Left Knee
    13: (3, 3),   # Right Knee
    14: (3, 3),   # Left Foot
    15: (3, 3),   # Right Foot
}

# Assign a phase offset (radians) for each marker (to avoid perfectly synchronous movement).
# These phases create a natural variation in the cyclical movement.
phase_table = {}
phase_step = math.pi / 8
for i in range(1, 16):
    phase_table[i] = i * phase_step

# Angular frequency (omega) of the oscillation (controls "breathing" speed)
period = 3.0  # seconds
omega = 2 * math.pi / period

# Radius for each displayed point-light
point_radius = 4

# Main loop
running = True
while running:
    # Handle events (exit on quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate time in seconds.
    t = pygame.time.get_ticks() / 1000.0

    # Clear screen to black.
    screen.fill((0, 0, 0))

    # For each marker, compute its new position and draw it.
    for idx in range(1, 16):
        base_x, base_y = base_points[idx]
        amp_x, amp_y = amp_table[idx]
        phase = phase_table[idx]
        # Compute a small oscillation using a sine function.
        offset_x_osc = amp_x * math.sin(omega * t + phase)
        offset_y_osc = amp_y * math.sin(omega * t + phase)
        # New positions.
        new_x = base_x + offset_x_osc
        new_y = base_y + offset_y_osc
        # Draw the marker as a white filled circle.
        pygame.draw.circle(screen, (255, 255, 255), (int(new_x), int(new_y)), point_radius)

    # Update the display.
    pygame.display.flip()

    # Cap the frame rate.
    clock.tick(60)

pygame.quit()
sys.exit()