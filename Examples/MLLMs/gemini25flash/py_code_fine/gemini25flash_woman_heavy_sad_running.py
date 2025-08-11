
import pygame
import math

# --- Pygame Setup ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus - Running Sad Woman")
clock = pygame.time.Clock()

# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- Point Light Parameters ---
POINT_RADIUS = 4 # Size of the white dots
NUM_POINTS = 15 # Required number of point lights

# --- Biomechanical Model (15 points) ---
# Point mapping (approximate, based on common 15-point models used in biological motion studies):
# 0: Head
# 1: Neck/Upper Spine
# 2: Right Shoulder
# 3: Left Shoulder
# 4: Right Elbow
# 5: Left Elbow
# 6: Right Wrist
# 7: Left Wrist
# 8: Mid-Torso/Spine
# 9: Right Hip
# 10: Left Hip
# 11: Right Knee
# 12: Left Knee
# 13: Right Ankle
# 14: Left Ankle

# Base pose (relative coordinates for a canonical size). Origin (0,0) is at the hips/pelvis level.
# Y-axis is positive downwards in Pygame. So points above hips are negative Y.
# These values are designed for a 'heavy' and slightly 'sad' posture:
# Shoulders slightly slumped, head slightly lower, wider stance for hips/feet.
base_points_canonical = {
    # Head and Torso
    0: (0, -0.65),    # Head (y-coord is lower, implying a slightly bowed head)
    1: (0, -0.45),    # Neck/Upper Spine
    8: (0, -0.15),    # Mid-Torso/Spine

    # Shoulders, Arms, Wrists (relative to body center)
    2: (0.13, -0.35), # Right Shoulder (slightly wider to imply 'heavy')
    3: (-0.13, -0.35),# Left Shoulder (slightly wider to imply 'heavy')
    4: (0.22, -0.20), # Right Elbow (bent, slightly outward for relaxed/heavy)
    5: (-0.22, -0.20),# Left Elbow (bent, slightly outward for relaxed/heavy)
    6: (0.28, -0.05), # Right Wrist (more bent, closer to body for relaxed/heavy)
    7: (-0.28, -0.05),# Left Wrist (more bent, closer to body for relaxed/heavy)

    # Hips, Legs, Ankles (relative to hips origin)
    9: (0.09, 0),     # Right Hip (wider stance for 'heavy')
    10: (-0.09, 0),   # Left Hip (wider stance for 'heavy')
    11: (0.09, 0.35), # Right Knee
    12: (-0.09, 0.35),# Left Knee
    13: (0.09, 0.70), # Right Ankle
    14: (-0.09, 0.70) # Left Ankle
}

# Determine a realistic figure height in pixels. This scales the 'canonical' units.
FIGURE_HEIGHT_PX = 250 

# Convert canonical relative coordinates to actual pixel coordinates for the base pose.
# (0,0) in this system is the figure's hip center in pixels.
base_points_pixel = {k: (v[0] * FIGURE_HEIGHT_PX, v[1] * FIGURE_HEIGHT_PX) for k, v in base_points_canonical.items()}

# Screen placement variables
X_START_POS = SCREEN_WIDTH / 4 # Starting horizontal position for the figure
Y_CENTER_ANCHOR = SCREEN_HEIGHT / 2 + 50 # Vertical anchor for the figure's hips. Lower for "heavy" person.

# Animation parameters
MOTION_SPEED_FACTOR = 0.08 # Controls the speed of the gait cycle. Lower for 'heavy' person.
HORIZONTAL_RUN_SPEED = 1.5 # Pixels per frame. Slower speed for 'heavy' person.

# Overall body motion amplitudes
VERTICAL_BOB_AMPLITUDE = 10 # Smaller vertical bounce for "heavy"
HEAD_BOB_AMPLITUDE_Y = 4 # Subtle head bob
HEAD_SWAY_AMPLITUDE_X = 2 # Subtle head sway
TORSO_SWAY_AMPLITUDE_X = 4 # Subtle torso sway

# Leg kinematics (tuned for running gait)
LEG_SWING_AMPLITUDE_X = 40 # Forward/backward leg swing
LEG_SWING_AMPLITUDE_Y = 15 # Lift of foot/knee during swing (smaller for 'heavy')
KNEE_BEND_AMPLITUDE = 30 # How much knee flexes during stride
ANKLE_LIFT_AMPLITUDE = 15 # Ankle lift for ground clearance

# Arm kinematics (tuned for running)
ARM_SWING_AMPLITUDE_X = 25 # Forward/backward arm swing (reduced for 'sad'/'heavy')
ARM_SWING_AMPLITUDE_Y = 8 # Up/down arm swing
ELBOW_BEND_AMPLITUDE = 10 # Elbow flexion (less dynamic for 'sad'/'heavy')

def get_point_positions(time_factor_raw, current_character_x):
    """
    Calculates the positions of all 15 points for a given time in the animation cycle.
    `time_factor_raw` is a continuously increasing value (e.g., frame counter).
    `current_character_x` is the global horizontal position of the character's center.
    """
    positions = {}

    # Normalize time_factor to a 0-2*PI cycle for gait calculation.
    # `t` represents the phase of the right leg's stride (0 to 2*pi for one full cycle).
    t = (time_factor_raw * MOTION_SPEED_FACTOR) % (2 * math.pi)

    # --- Overall Body Motion (Torso, Head) ---
    # Vertical bob: Body is generally lowest during mid-stance (when a foot is on the ground)
    # and highest during push-off. sin(t + pi/2) ensures this timing.
    vertical_offset = math.sin(t + math.pi/2) * VERTICAL_BOB_AMPLITUDE

    # Torso sway: Side-to-side for balance, often at half the gait frequency.
    torso_x_sway = math.sin(t * 0.5) * TORSO_SWAY_AMPLITUDE_X

    # Head motion: Subtle bob and sway, slightly out of sync with torso for naturalness.
    head_y_offset = math.sin(t * 1.2 + math.pi/4) * HEAD_BOB_AMPLITUDE_Y
    head_x_offset = math.cos(t * 0.8) * HEAD_SWAY_AMPLITUDE_X

    # Apply base position and overall motion to core points (Head, Neck, Mid-Torso).
    positions[0] = (base_points_pixel[0][0] + torso_x_sway + head_x_offset,
                    base_points_pixel[0][1] + vertical_offset + head_y_offset) # Head
    positions[1] = (base_points_pixel[1][0] + torso_x_sway,
                    base_points_pixel[1][1] + vertical_offset) # Neck
    positions[8] = (base_points_pixel[8][0] + torso_x_sway,
                    base_points_pixel[8][1] + vertical_offset) # Mid-Torso

    # --- Leg Kinematics (Right and Left are out of phase by PI) ---
    for side in ['right', 'left']:
        hip_idx = 9 if side == 'right' else 10
        knee_idx = 11 if side == 'right' else 12
        ankle_idx = 13 if side == 'right' else 14
        
        # Determine specific phase for the current leg. Left leg is opposite to right.
        leg_t = t if side == 'right' else (t + math.pi) % (2 * math.pi)

        # Hip position (influenced by torso sway and general bob).
        hip_x_base = base_points_pixel[hip_idx][0] + torso_x_sway
        hip_y_base = base_points_pixel[hip_idx][1] + vertical_offset
        positions[hip_idx] = (hip_x_base, hip_y_base)

        # Leg swing (forward/backward movement). Cosine wave provides natural swing.
        leg_swing_x = math.cos(leg_t) * LEG_SWING_AMPLITUDE_X

        # Leg lift (up/down movement, primarily during swing phase).
        # abs(sin(2*leg_t)) creates two lifts per cycle (take-off and mid-swing).
        leg_lift_y = abs(math.sin(leg_t * 2)) * LEG_SWING_AMPLITUDE_Y

        # Knee bend (flexes during swing, extends at strike/push-off).
        # (0.5 - 0.5 * cos(2*leg_t)) creates a wave that goes from 0 to 1 and back.
        knee_bend_y = (0.5 - 0.5 * math.cos(leg_t * 2)) * KNEE_BEND_AMPLITUDE
        
        # Ankle lift (foot clearance from ground).
        # Offset phase to align with mid-swing.
        ankle_lift_y = (0.5 - 0.5 * math.cos(leg_t * 2 + math.pi/2)) * ANKLE_LIFT_AMPLITUDE

        # Calculate Knee position relative to hip.
        knee_x = hip_x_base + leg_swing_x * 0.5 # Knee leads/trails hip less than ankle
        knee_y = hip_y_base + base_points_pixel[knee_idx][1] + leg_lift_y + knee_bend_y
        positions[knee_idx] = (knee_x, knee_y)

        # Calculate Ankle position relative to hip.
        ankle_x = hip_x_base + leg_swing_x * 1.0
        ankle_y = hip_y_base + base_points_pixel[ankle_idx][1] + leg_lift_y * 1.5 + knee_bend_y * 0.5 + ankle_lift_y
        positions[ankle_idx] = (ankle_x, ankle_y)

    # --- Arm Kinematics (Right and Left are out of phase by PI, and opposite to same-side leg) ---
    for side in ['right', 'left']:
        shoulder_idx = 2 if side == 'right' else 3
        elbow_idx = 4 if side == 'right' else 5
        wrist_idx = 6 if side == 'right' else 7

        # Arm phase is opposite to corresponding leg (e.g., Right Arm forward when Left Leg is forward).
        # If right leg phase is `t`, then right arm phase is `t + pi`.
        arm_t = (t + math.pi) % (2 * math.pi) if side == 'right' else t

        shoulder_x_base = base_points_pixel[shoulder_idx][0] + torso_x_sway
        shoulder_y_base = base_points_pixel[shoulder_idx][1] + vertical_offset
        positions[shoulder_idx] = (shoulder_x_base, shoulder_y_base)

        # Arm swing (forward/backward).
        arm_swing_x = math.cos(arm_t) * ARM_SWING_AMPLITUDE_X

        # Arm lift (up/down).
        arm_lift_y = math.sin(arm_t) * ARM_SWING_AMPLITUDE_Y

        # Elbow bend (more bent when arm is back).
        elbow_bend_y = abs(math.sin(arm_t)) * ELBOW_BEND_AMPLITUDE

        # Calculate Elbow position relative to shoulder.
        elbow_x = shoulder_x_base + arm_swing_x
        elbow_y = shoulder_y_base + base_points_pixel[elbow_idx][1] + arm_lift_y + elbow_bend_y
        positions[elbow_idx] = (elbow_x, elbow_y)

        # Calculate Wrist position relative to shoulder.
        wrist_x = shoulder_x_base + arm_swing_x * 1.5
        wrist_y = shoulder_y_base + base_points_pixel[wrist_idx][1] + arm_lift_y * 1.5 + elbow_bend_y * 1.5
        positions[wrist_idx] = (wrist_x, wrist_y)

    # --- Apply global screen offset and horizontal movement ---
    final_positions = []
    for i in range(NUM_POINTS):
        px, py = positions[i]
        final_x = int(current_character_x + px)
        final_y = int(Y_CENTER_ANCHOR + py) # Y_CENTER_ANCHOR is the screen Y of the hips
        final_positions.append((final_x, final_y))

    return final_positions

# --- Game Loop ---
running = True
time_elapsed = 0 # Continuous time counter for animation progression
character_x = X_START_POS # Initial horizontal position of the character

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation time
    time_elapsed += 1

    # Update character's global X position to simulate running across the screen.
    # Reset character to the left side once it moves completely off the right side.
    character_x += HORIZONTAL_RUN_SPEED
    if character_x > SCREEN_WIDTH + FIGURE_HEIGHT_PX: # If figure is entirely off right
        character_x = -FIGURE_HEIGHT_PX # Reset to entirely off left

    # Get current point positions based on animation time and character's global X.
    current_point_positions = get_point_positions(time_elapsed, character_x)

    # --- Drawing ---
    screen.fill(BLACK) # Solid black background

    # Draw each point as a white circle
    for x, y in current_point_positions:
        pygame.draw.circle(screen, WHITE, (x, y), POINT_RADIUS)

    pygame.display.flip() # Update the full display surface to the screen

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
