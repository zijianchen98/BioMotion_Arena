
"""
This program creates a point‐light stimulus animation on a black background
to represent a biological motion of a “sad” woman with light weight jumping forward.
It displays exactly 15 white points whose positions are computed from a basic
biomechanically-inspired dynamic model of a human body performing a jump.
Press the window close button to exit.
"""

import sys, math, pygame

# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Biological Motion Animation")
clock = pygame.time.Clock()
fps = 60

# Animation parameters
total_frames = 120        # Cycle duration for one jump cycle
frame = 0
# The forward speed (pixels per frame) and jump height in pixels
forward_speed = 3
peak_jump = 100          # Maximum jump (vertical offset) at mid-cycle

# Ground level (spine base resting position)
ground_y = 400
# Starting horizontal offset for the spine base
start_x = screen_width // 4

# Define a basic static body template: exactly 15 points representing joints.
# Coordinates are relative to a central spine base (0, 0)
# (x increases rightwards, y increases downward)
body_points = {
    0:  (0, -50),    # Head
    1:  (-15, -35),  # Left shoulder
    2:  (15, -35),   # Right shoulder
    3:  (-25, -15),  # Left elbow
    4:  (25, -15),   # Right elbow
    5:  (-30, 0),    # Left hand
    6:  (30, 0),     # Right hand
    7:  (0, -25),    # Torso (chest)
    8:  (-10, 0),    # Left hip
    9:  (10, 0),     # Right hip
    10: (-10, 25),   # Left knee
    11: (10, 25),    # Right knee
    12: (-10, 50),   # Left foot
    13: (10, 50),    # Right foot
    14: (0, -40),    # Mid-spine (additional marker)
}

# Main loop
running = True
while running:
    # Handle events (quit when window closed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen with black background
    screen.fill((0, 0, 0))

    # Compute phase in the jump cycle (0 -> 1)
    phase = (frame % total_frames) / float(total_frames)

    # Compute overall body (spine base) position:
    # Horizontal position increases steadily.
    # Vertical jump: use a parabola:  jump = -4*(phase-0.5)**2 + 1, scaled by peak_jump.
    jump_func = -4*(phase - 0.5)**2 + 1   # 0 at beginning/end, 1 at mid jump
    spine_base_x = start_x + forward_speed * frame
    spine_base_y = ground_y - (jump_func * peak_jump)

    # Pre-compute some cyclic values for smooth motion modulations.
    # These modulations add natural swing to the limbs.
    # Arm swing (sinusoidal oscillation)
    arm_swing = 5 * math.sin(2 * math.pi * phase)
    hand_swing  = 8 * math.sin(2 * math.pi * phase)
    # Head slight sway
    head_sway = 3 * math.sin(2 * math.pi * phase + math.pi/4)
    # Torso mid-spine sway
    spine_sway = 2 * math.sin(2 * math.pi * phase)
    # Leg bending: knees flex during take-off and landing.
    knee_bend = -8 * abs(math.sin(math.pi * phase))
    # Foot forward shift: small horizontal advance at mid-jump.
    foot_shift = 5 * math.cos(math.pi * phase)

    # For each of the 15 body points compute its animated position.
    for idx, (base_x, base_y) in body_points.items():
        # Start with base relative positions
        mod_x, mod_y = 0, 0

        # Apply modifications for specific joints:
        if idx == 0:   # Head: slight left/right sway.
            mod_x += head_sway
        elif idx == 3:  # Left elbow
            mod_x += -arm_swing
        elif idx == 4:  # Right elbow
            mod_x += arm_swing
        elif idx == 5:  # Left hand: extra swing outward.
            mod_x += -hand_swing
        elif idx == 6:  # Right hand: extra swing outward.
            mod_x += hand_swing
        elif idx in [10, 11]:  # Knees: bending upward when jumping.
            mod_y += knee_bend
        elif idx in [12, 13]:  # Feet: slight forward shift at mid-jump.
            # For left foot, shift left slightly; for right foot, shift right slightly.
            if idx == 12:
                mod_x += -foot_shift
            else:
                mod_x += foot_shift
        elif idx == 14:  # Mid-spine: slight vertical sway.
            mod_y += spine_sway

        # Final screen coordinates for this point
        point_x = int(spine_base_x + base_x + mod_x)
        point_y = int(spine_base_y + base_y + mod_y)

        # Draw a white circle for the point-light. Radius of 4 pixels.
        pygame.draw.circle(screen, (255, 255, 255), (point_x, point_y), 4)

    # Update display
    pygame.display.flip()
    clock.tick(fps)
    frame += 1

pygame.quit()
sys.exit()