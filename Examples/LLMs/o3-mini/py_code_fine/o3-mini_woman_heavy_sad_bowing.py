
"""
This program displays an animated point‐light stimulus of a “sad woman with heavy weight bowing.” 
It uses exactly 15 white point‐lights on a black background. The upper‐body points (head, shoulders,
arms, torso, and belly) are rotated in a biomechanically plausible way about the hip (which remains fixed),
simulating a smooth, natural bowing motion.
  
The 15 markers are defined as follows (coordinates are in a person-centric reference frame with the hip at (0,0)
and with the y‐axis pointing upward, so that the head has a negative y coordinate):
  
  0: Head         at ( 0, -60)
  1: Left Shoulder  at (-10, -50)
  2: Right Shoulder at (10, -50)
  3: Left Elbow     at (-15, -35)
  4: Right Elbow    at (15, -35)
  5: Left Hand      at (-20, -20)
  6: Right Hand     at (20, -20)
  7: Upper Torso    at (0, -40)
  8: Lower Torso    at (0, -20)
  9: Hip            at (0, 0)
 10: Left Knee      at (-5, 20)
 11: Right Knee     at (5, 20)
 12: Left Foot      at (-5, 40)
 13: Right Foot     at (5, 40)
 14: Belly Marker   at (0, -30)
  
For the bowing motion, the “upper body” (indices 0,1,2,3,4,5,6,7,8,14) is rotated about the hip (index 9).
A sinusoidal function with a maximum rotation of 45° is used (always as a clockwise rotation) so that the 
motion is smooth, natural, and biomechanically plausible.
  
Press the window’s close button or hit ESCAPE to quit.
"""

import sys, math, pygame

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Bowing Sad Woman")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the 15 markers positions (in "body coordinates")
# Coordinate system here: x rightward; y upward.
# The hip is at (0,0), so the head is above (negative y) and feet below (positive y).
points = [
    (  0, -60),  # 0: Head
    (-10, -50),  # 1: Left Shoulder
    ( 10, -50),  # 2: Right Shoulder
    (-15, -35),  # 3: Left Elbow
    ( 15, -35),  # 4: Right Elbow
    (-20, -20),  # 5: Left Hand
    ( 20, -20),  # 6: Right Hand
    (  0, -40),  # 7: Upper Torso
    (  0, -20),  # 8: Lower Torso
    (  0,   0),  # 9: Hip (pivot)
    ( -5,  20),  # 10: Left Knee
    (  5,  20),  # 11: Right Knee
    ( -5,  40),  # 12: Left Foot
    (  5,  40),  # 13: Right Foot
    (  0, -30),  # 14: Belly Marker
]

# Indices for the points that belong to the upper body.
# These will be rotated about the hip to simulate bowing.
upper_body_indices = {0, 1, 2, 3, 4, 5, 6, 7, 8, 14}
# The remaining indices (including the hip and lower limbs) will remain fixed.
fixed_indices = set(range(15)) - upper_body_indices

# Animation parameters
FPS = 60
# Total duration (in frames) for one complete bow and return cycle.
# We use a sinusoidal function so that the bowing motion is smooth.
cycle_frames = 200  
# Maximum rotation angle in radians (clockwise bow = positive rotation).
max_angle = math.radians(45)

# To position the figure on the screen, decide on an offset.
# We want the hip (which is at (0,0)) to be at screen location pivot_screen.
pivot_screen = (WIDTH // 2, HEIGHT // 2 + 50)  # slightly lower than center

def rotate_point(point, theta):
    """Rotate a point (x, y) about the origin by angle theta (in radians)."""
    x, y = point
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x_new = x * cos_t - y * sin_t
    y_new = x * sin_t + y * cos_t
    return (x_new, y_new)

# Main animation loop
frame = 0
running = True
while running:
    # Handle events (quit on window close or ESC key)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Calculate the current rotation angle.
    # Use an absolute sine so that the rotation is always in the bowed (clockwise) direction.
    # The angle smoothly raises from 0 up to max_angle then returns to 0.
    phase = math.pi * (frame % cycle_frames) / cycle_frames
    theta = max_angle * math.fabs(math.sin(phase))

    # Clear the screen to black.
    screen.fill(BLACK)

    # Prepare a list to hold the display positions for all markers.
    display_positions = []

    # For each marker, compute its current position.
    for index, pos in enumerate(points):
        # For upper body markers, apply rotation about the hip (0,0).
        if index in upper_body_indices:
            new_pos = rotate_point(pos, theta)
        else:
            new_pos = pos  # fixed marker (hip and lower limbs)
        # Transform from body coordinates (with hip at (0,0) and y upward)
        # to screen coordinates (with pivot_screen as hip and y downward)
        x_body, y_body = new_pos
        # Invert y to account for pygame's coordinate system.
        x_screen = pivot_screen[0] + x_body
        y_screen = pivot_screen[1] - y_body
        display_positions.append((int(x_screen), int(y_screen)))

    # Draw the 15 point-lights as small circles.
    marker_radius = 5
    for pos in display_positions:
        pygame.draw.circle(screen, WHITE, pos, marker_radius)

    pygame.display.flip()
    clock.tick(FPS)
    frame += 1

pygame.quit()
sys.exit()