
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POINT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Biomechanical Parameters ---
# These parameters are approximations for a human walking gait,
# expressed in arbitrary units and radians.
# They are tuned to produce a "happyman" walking motion.

BODY_HEIGHT_UNIT = 150  # Reference unit for scaling the figure
SCALE = SCREEN_HEIGHT / (BODY_HEIGHT_UNIT * 1.5)  # Scale to fit screen, ensures figure fits height

# Segment lengths (relative to BODY_HEIGHT_UNIT)
SEG_HEAD_NECK = 0.12 * BODY_HEIGHT_UNIT
SEG_NECK_SHOULDER = 0.05 * BODY_HEIGHT_UNIT # Distance from neck C7 to shoulder joint
SEG_SHOULDER_TORSO = 0.15 * BODY_HEIGHT_UNIT # Distance from shoulder line to sternum (mid-chest)
SEG_TORSO_PELVIS = 0.25 * BODY_HEIGHT_UNIT # Distance from sternum to hip center (mid-pelvis)
SEG_UPPER_ARM = 0.18 * BODY_HEIGHT_UNIT
SEG_LOWER_ARM = 0.15 * BODY_HEIGHT_UNIT
SEG_THIGH = 0.25 * BODY_HEIGHT_UNIT
SEG_SHIN = 0.25 * BODY_HEIGHT_UNIT
SHOULDER_WIDTH = 0.12 * BODY_HEIGHT_UNIT
HIP_WIDTH = 0.08 * BODY_HEIGHT_UNIT

# Animation speed
PHASE_SPEED = 0.1 # Radians per frame, adjusts walking speed

# Pelvis/Body center movement (slight vertical bob and horizontal sway)
PELVIS_Y_AMPLITUDE = 0.01 * BODY_HEIGHT_UNIT # Vertical bob
PELVIS_Y_PHASE_OFFSET = math.pi / 2 # Peaks when legs are extended (twice per gait cycle)
PELVIS_X_SWAY_AMPLITUDE = 0.005 * BODY_HEIGHT_UNIT # Side-to-side sway
PELVIS_X_SWAY_PHASE_OFFSET = 0 # Sway in phase with leg cycle

# Joint angle parameters (amplitudes in radians, offsets for resting angle/phase alignment)
# Angles are measured relative to the parent segment's orientation.
# For hip/shoulder, 0 rad is typically straight down. Positive angle swings forward/out.

# Hip joint angles (flexion/extension)
HIP_SWING_AMPLITUDE = math.radians(25) # Max forward/backward swing
HIP_FLEX_OFFSET = math.radians(0) # Resting angle (straight down)

# Knee joint angles (flexion only, using 0.5 * (1 + sin()) for positive only deflection)
KNEE_FLEX_AMPLITUDE = math.radians(45) # Max bend during swing
KNEE_FLEX_OFFSET = math.radians(-5) # Slight initial bend (e.g., -5 deg from anatomical straight)
KNEE_PHASE_OFFSET = -math.pi / 2 # Knee bends when leg is back (3pi/2 phase) and straightens at heel strike (0 phase)

# Ankle joint angles (dorsiflexion/plantarflexion)
ANKLE_FLEX_AMPLITUDE = math.radians(15)
ANKLE_FLEX_OFFSET = math.radians(0)
ANKLE_PHASE_OFFSET = math.pi / 2 # Ankle dorsiflexes (foot points up) at heel strike (0 phase)

# Shoulder joint angles (arm swing)
SHOULDER_SWING_AMPLITUDE = math.radians(30)
SHOULDER_FLEX_OFFSET = math.radians(0)
SHOULDER_PHASE_OFFSET = math.pi # Opposite phase to ipsilateral leg

# Elbow joint angles (slight flexion during swing)
ELBOW_FLEX_AMPLITUDE = math.radians(5) # Very slight bend
ELBOW_FLEX_OFFSET = math.radians(0)
ELBOW_PHASE_OFFSET = math.pi / 2 # Bends slightly at mid-swing

# Base coordinates for the "model"
# All calculations are relative to a conceptual hip center (pelvis_center) at (0,0) for the model.
# Then translated to screen center.
model_origin_x = SCREEN_WIDTH // 2
model_origin_y = SCREEN_HEIGHT // 2 + (BODY_HEIGHT_UNIT * SCALE / 4) # Adjust to center the full figure vertically

# Define the exact 15 points to draw (consistent with common biological motion stimuli)
POINTS_TO_DRAW_NAMES = [
    'head', 'neck', 'l_shoulder', 'r_shoulder', 'l_elbow', 'r_elbow',
    'l_wrist', 'r_wrist', 'sternum', 'l_hip', 'r_hip', 'l_knee',
    'r_knee', 'l_ankle', 'r_ankle'
]

# Function to calculate point positions based on the current phase of the walking cycle
def calculate_skeleton_coords(current_phase):
    coords = {}

    # 1. Pelvis Center (virtual origin for the body, moves slightly)
    # This point represents the center of the hips / base of spine for CoM calculation
    pelvis_x_model = PELVIS_X_SWAY_AMPLITUDE * math.sin(current_phase + PELVIS_X_SWAY_PHASE_OFFSET)
    pelvis_y_model = PELVIS_Y_AMPLITUDE * math.sin(current_phase * 2 + PELVIS_Y_PHASE_OFFSET) # Twice the frequency for vertical bob

    # 2. Hips (left and right) - these are the root of the legs
    l_hip_x, l_hip_y = pelvis_x_model - HIP_WIDTH / 2, pelvis_y_model
    r_hip_x, r_hip_y = pelvis_x_model + HIP_WIDTH / 2, pelvis_y_model
    coords['l_hip'] = (l_hip_x, l_hip_y)
    coords['r_hip'] = (r_hip_x, r_hip_y)

    # 3. Sternum (mid-chest/torso center point)
    sternum_x, sternum_y = pelvis_x_model, pelvis_y_model - SEG_TORSO_PELVIS
    coords['sternum'] = (sternum_x, sternum_y)

    # 4. Neck (C7 - base of neck)
    neck_x, neck_y = sternum_x, sternum_y - SEG_SHOULDER_TORSO # Placed above sternum
    coords['neck'] = (neck_x, neck_y)

    # 5. Head (top of head)
    # Head has slight bobbing relative to neck/torso
    head_y_offset_dynamic = HEAD_Y_AMPLITUDE * math.sin(current_phase * 2 + HEAD_Y_PHASE_OFFSET)
    head_x, head_y = neck_x, neck_y - SEG_HEAD_NECK + head_y_offset_dynamic
    coords['head'] = (head_x, head_y)

    # 6. Shoulders (left and right)
    l_shoulder_x, l_shoulder_y = neck_x - SHOULDER_WIDTH / 2, neck_y
    r_shoulder_x, r_shoulder_y = neck_x + SHOULDER_WIDTH / 2, neck_y
    coords['l_shoulder'] = (l_shoulder_x, l_shoulder_y)
    coords['r_shoulder'] = (r_shoulder_x, r_shoulder_y)

    # --- Legs ---
    # Left Leg (L_Hip is anchor)
    # Angles measured clockwise from the vertical (straight down is 0 radians)
    hip_angle_L = HIP_FLEX_OFFSET + HIP_SWING_AMPLITUDE * math.sin(current_phase)
    # Knee flexion is always positive (bending), 0.5*(1+sin) ensures range from 0 to 1
    knee_flex_L = KNEE_FLEX_OFFSET + KNEE_FLEX_AMPLITUDE * (0.5 * (1 + math.sin(current_phase * 2 + KNEE_PHASE_OFFSET)))
    ankle_flex_L = ANKLE_FLEX_OFFSET + ANKLE_FLEX_AMPLITUDE * math.sin(current_phase + ANKLE_PHASE_OFFSET)

    # L_Knee position
    l_knee_x = l_hip_x + SEG_THIGH * math.sin(hip_angle_L)
    l_knee_y = l_hip_y + SEG_THIGH * math.cos(hip_angle_L)
    coords['l_knee'] = (l_knee_x, l_knee_y)

    # L_Ankle position (angle of shin relative to global vertical)
    shin_angle_L = hip_angle_L + knee_flex_L
    l_ankle_x = l_knee_x + SEG_SHIN * math.sin(shin_angle_L)
    l_ankle_y = l_knee_y + SEG_SHIN * math.cos(shin_angle_L)
    coords['l_ankle'] = (l_ankle_x, l_ankle_y)

    # Right Leg (R_Hip is anchor) - 180 degrees out of phase from Left Leg
    hip_angle_R = HIP_FLEX_OFFSET + HIP_SWING_AMPLITUDE * math.sin(current_phase + math.pi)
    knee_flex_R = KNEE_FLEX_OFFSET + KNEE_FLEX_AMPLITUDE * (0.5 * (1 + math.sin((current_phase + math.pi) * 2 + KNEE_PHASE_OFFSET)))
    ankle_flex_R = ANKLE_FLEX_OFFSET + ANKLE_FLEX_AMPLITUDE * math.sin(current_phase + math.pi + ANKLE_PHASE_OFFSET)

    # R_Knee position
    r_knee_x = r_hip_x + SEG_THIGH * math.sin(hip_angle_R)
    r_knee_y = r_hip_y + SEG_THIGH * math.cos(hip_angle_R)
    coords['r_knee'] = (r_knee_x, r_knee_y)

    # R_Ankle position
    shin_angle_R = hip_angle_R + knee_flex_R
    r_ankle_x = r_knee_x + SEG_SHIN * math.sin(shin_angle_R)
    r_ankle_y = r_knee_y + SEG_SHIN * math.cos(shin_angle_R)
    coords['r_ankle'] = (r_ankle_x, r_ankle_y)

    # --- Arms ---
    # Left Arm (L_Shoulder is anchor) - opposite phase to left leg
    # Angle measured clockwise from vertical (hanging down is 0 radians)
    shoulder_angle_L = SHOULDER_FLEX_OFFSET + SHOULDER_SWING_AMPLITUDE * math.sin(current_phase + SHOULDER_PHASE_OFFSET)
    elbow_flex_L = ELBOW_FLEX_OFFSET + ELBOW_FLEX_AMPLITUDE * (0.5 * (1 + math.sin(current_phase + SHOULDER_PHASE_OFFSET + ELBOW_PHASE_OFFSET)))

    # L_Elbow position
    l_elbow_x = l_shoulder_x + SEG_UPPER_ARM * math.sin(shoulder_angle_L)
    l_elbow_y = l_shoulder_y + SEG_UPPER_ARM * math.cos(shoulder_angle_L)
    coords['l_elbow'] = (l_elbow_x, l_elbow_y)

    # L_Wrist position (angle of forearm relative to global vertical)
    forearm_angle_L = shoulder_angle_L + elbow_flex_L
    l_wrist_x = l_elbow_x + SEG_LOWER_ARM * math.sin(forearm_angle_L)
    l_wrist_y = l_elbow_y + SEG_LOWER_ARM * math.cos(forearm_angle_L)
    coords['l_wrist'] = (l_wrist_x, l_wrist_y)

    # Right Arm (R_Shoulder is anchor) - opposite phase to right leg
    shoulder_angle_R = SHOULDER_FLEX_OFFSET + SHOULDER_SWING_AMPLITUDE * math.sin(current_phase + SHOULDER_PHASE_OFFSET + math.pi)
    elbow_flex_R = ELBOW_FLEX_OFFSET + ELBOW_FLEX_AMPLITUDE * (0.5 * (1 + math.sin(current_phase + SHOULDER_PHASE_OFFSET + math.pi + ELBOW_PHASE_OFFSET)))

    # R_Elbow position
    r_elbow_x = r_shoulder_x + SEG_UPPER_ARM * math.sin(shoulder_angle_R)
    r_elbow_y = r_shoulder_y + SEG_UPPER_ARM * math.cos(shoulder_angle_R)
    coords['r_elbow'] = (r_elbow_x, r_elbow_y)

    # R_Wrist position
    forearm_angle_R = shoulder_angle_R + elbow_flex_R
    r_wrist_x = r_elbow_x + SEG_LOWER_ARM * math.sin(forearm_angle_R)
    r_wrist_y = r_elbow_y + SEG_LOWER_ARM * math.cos(forearm_angle_R)
    coords['r_wrist'] = (r_wrist_x, r_wrist_y)

    # Apply global transformation (scale and translate to screen coordinates)
    final_points_screen = []
    for name in POINTS_TO_DRAW_NAMES:
        x, y = coords[name]
        scaled_x = x * SCALE
        scaled_y = y * SCALE
        # Translate to screen center, and invert Y because Pygame Y increases downwards
        screen_x = int(model_origin_x + scaled_x)
        screen_y = int(model_origin_y - scaled_y) # Invert Y for typical Cartesian up-is-positive
        final_points_screen.append((screen_x, screen_y))
    
    return final_points_screen

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion (Walking Happyman)")
clock = pygame.time.Clock()

# --- Animation Loop ---
running = True
current_phase = 0.0 # Represents the phase of the walking cycle (0 to 2*pi)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen with black background
    screen.fill(BLACK)

    # Calculate the positions of the 15 point lights for the current animation phase
    points_to_draw = calculate_skeleton_coords(current_phase)

    # Draw each point light as a white circle
    for point_pos in points_to_draw:
        pygame.draw.circle(screen, WHITE, point_pos, POINT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Update the animation phase for the next frame
    current_phase += PHASE_SPEED
    # Wrap the phase around to maintain a continuous cycle (0 to 2*pi)
    if current_phase >= 2 * math.pi:
        current_phase -= 2 * math.pi

    # Cap the frame rate to ensure smooth animation
    clock.tick(FPS)

# Quit Pygame when the loop ends
pygame.quit()
