
import pygame
import math

# --- Pygame Initialization ---
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Heavy Woman Walking")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
POINT_RADIUS = 5

# --- Biomechanical Model Parameters ---
# Base positions for the 15 points (relative to Pelvis (point 14) being at (0,0) locally).
# These coordinates define the 'skeleton' in a neutral, standing-like pose.
# They are adjusted to suggest a wider, heavier build as requested.
# Points mapping (derived from typical point-light walker models and the provided image):
# 0: Head
# 1: Left Shoulder
# 2: Right Shoulder
# 3: Torso (Mid-Chest/Upper Spine)
# 4: Left Elbow
# 5: Right Elbow
# 6: Left Wrist
# 7: Right Wrist
# 8: Left Hip
# 9: Right Hip
# 10: Left Knee
# 11: Right Knee
# 12: Left Ankle
# 13: Right Ankle
# 14: Pelvis (center of body, acts as the local origin for relative movements)
base_positions = {
    0: (0, -220),   # Head
    1: (-70, -160), # Left Shoulder (wider stance)
    2: (70, -160),  # Right Shoulder (wider stance)
    3: (0, -130),   # Torso (Upper Spine)
    4: (-85, -80),  # Left Elbow (further out from body)
    5: (85, -80),   # Right Elbow (further out from body)
    6: (-90, 0),    # Left Wrist
    7: (90, 0),     # Right Wrist
    8: (-50, 0),    # Left Hip (wider stance)
    9: (50, 0),     # Right Hip (wider stance)
    10: (-55, 80),   # Left Knee
    11: (55, 80),    # Right Knee
    12: (-60, 160),  # Left Ankle
    13: (60, 160),   # Right Ankle
    14: (0, 0)      # Pelvis (local origin)
}

# Motion parameters for each joint: (amplitude_x, phase_x, amplitude_y, phase_y)
# All oscillations are calculated as: amplitude * math.cos(time_phase + phase).
# 'time_phase = 0' is set to the moment when the Left Leg is at its mid-swing point
# (fully extended forward and at its lowest vertical point in the swing cycle),
# and the Right Leg is at its mid-stance point (under the body, supporting weight, body at highest point).
# This provides a consistent reference for setting the phases.

joint_oscillations = {
    # Pelvis (14): The primary anchor for the body's overall movement.
    # Higher vertical amplitude (25) contributes to a 'heavy' and 'happy' bouncy feel.
    # x_phase (-math.pi/2) ensures it's at zero x-offset and moving left at time_phase=0
    # (consistent with the right leg being under the body for support).
    14: (15, -math.pi/2, 25, 0), # x_amp, x_phase, y_amp, y_phase (phase in radians)

    # Head (0) & Torso (3): Generally follow the pelvis's overall movement. Head has slightly more bounce.
    0: (10, -math.pi/2, 30, 0), # Head: larger vertical amplitude for 'happy' bounce
    3: (5, -math.pi/2, 10, 0),  # Torso: less pronounced oscillation, acts as a spine anchor

    # Hips (8, 9): Control hip rotation and slight vertical movement.
    # At t=0 (Left leg forward): Left Hip (8) should be forward (x positive), Right Hip (9) backward (x negative).
    8: (15, 0, 5, math.pi/2),        # Left Hip: x positive at t=0 (forward), y starts moving down
    9: (15, math.pi, 5, -math.pi/2), # Right Hip: x negative at t=0 (backward), y starts moving up

    # Shoulders (1, 2): Counter-rotate to hips, following torso's vertical movement.
    # At t=0 (Left hip forward): Right Shoulder (2) forward, Left Shoulder (1) backward.
    1: (10, math.pi, 5, 0),       # Left Shoulder: x back, y follows torso vertical
    2: (10, 0, 5, 0),             # Right Shoulder: x forward, y follows torso vertical

    # Arms (Elbows 4, 5 & Wrists 6, 7): Swing opposite to legs.
    # At t=0 (Left leg forward): Right arm (5,7) swings forward, Left arm (4,6) swings back.
    # y_phase of pi/2 or -pi/2 ensures an elliptical path in sync with swing.
    4: (40, math.pi, 20, math.pi/2),     # Left Elbow: x back, y up/down for swing
    5: (40, 0, 20, -math.pi/2),          # Right Elbow: x forward, y up/down for swing
    6: (50, math.pi, 25, math.pi/2 + 0.2), # Left Wrist: more amplitude, slightly phase shifted for natural hang
    7: (50, 0, 25, -math.pi/2 + 0.2),      # Right Wrist

    # Legs (Knees 10, 11 & Ankles 12, 13): Elliptical motion, crucial for walking.
    # At t=0: Left Leg extended forward (max x), at lowest point of swing (min y).
    #         Right Leg extended backward (max x), at highest point (mid-stance under body).
    10: (50, 0, 60, math.pi),       # Left Knee: x forward, y lowest (extended)
    11: (50, math.pi, 60, 0),       # Right Knee: x back, y highest (under body)
    12: (55, 0, 70, math.pi + 0.3),  # Left Ankle: x forward, y lowest (slightly lagged behind knee)
    13: (55, math.pi, 70, 0 + 0.3)   # Right Ankle: x back, y highest (slightly lagged behind knee)
}

# Overall walking speed. A slightly slower value (0.07 rad/frame) contributes to the 'heavy' feel.
WALKING_SPEED = 0.07

# Character's initial screen position (centered in the window)
character_center_x = SCREEN_WIDTH // 2
character_center_y = SCREEN_HEIGHT // 2

# Game loop
running = True
frame_count = 0
clock = pygame.time.Clock()
FPS = 60 # Frames per second, controls smoothness

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate the current phase in the continuous walking cycle
    time_phase = frame_count * WALKING_SPEED

    # Calculate the current position of the pelvis (the overall moving origin for the figure).
    # This incorporates the body's primary vertical bounce and subtle horizontal sway.
    pelvis_osc_x = joint_oscillations[14][0] * math.cos(time_phase + joint_oscillations[14][1])
    pelvis_osc_y = joint_oscillations[14][2] * math.cos(time_phase + joint_oscillations[14][3])

    current_pelvis_x = character_center_x + pelvis_osc_x
    current_pelvis_y = character_center_y + pelvis_osc_y

    # Store calculated positions of all points for drawing
    current_point_positions = {}

    for i in range(15):
        base_x, base_y = base_positions[i]

        # Get oscillation parameters for the current joint from the defined dictionary
        amp_x, phase_x, amp_y, phase_y = joint_oscillations[i]

        # Calculate the joint's specific oscillation relative to its base position
        osc_x = amp_x * math.cos(time_phase + phase_x)
        osc_y = amp_y * math.cos(time_phase + phase_y)

        # Calculate the final screen position for the point:
        # It's the character's overall position (driven by the pelvis's movement),
        # plus the joint's static base offset from the pelvis,
        # plus the joint's dynamic oscillation.
        current_x = current_pelvis_x + base_x + osc_x
        current_y = current_pelvis_y + base_y + osc_y

        current_point_positions[i] = (current_x, current_y)

    # Draw each point as a white circle
    for pos in current_point_positions.values():
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Increment frame count and control frame rate
    frame_count += 1
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
