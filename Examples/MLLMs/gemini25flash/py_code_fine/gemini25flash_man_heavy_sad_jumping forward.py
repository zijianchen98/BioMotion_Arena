
import pygame
import math
import sys

# --- Pygame Setup ---
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sadman Jumping Forward")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# Animation properties
FPS = 60
clock = pygame.time.Clock()

# --- Biomechanical Model (Simplified) ---
# A dictionary to store initial relative positions for each joint.
# These are relative to a central "pelvis" point, which is considered (0,0) for these relative coordinates.
# The y-coordinates here are "upwards" relative to the pelvis.
# These values will be scaled by PERSON_HEIGHT_SCALE and PERSON_WIDTH_SCALE
# and then translated by the current pelvis screen coordinates.

# Proportional values (arbitrary scale, will be scaled to screen pixels)
# A reasonable normalized height for the person could be 0.4 of screen height.
PERSON_HEIGHT_SCALE = SCREEN_HEIGHT * 0.4
PERSON_WIDTH_SCALE = SCREEN_WIDTH * 0.15 # For lateral body width

BASE_POSE_RELATIVE = {
    'head':       (0,    0.45), # Y: 0.45 * PersonHeight above pelvis
    'neck':       (0,    0.35),
    'l_shoulder': (-0.1, 0.25),
    'r_shoulder': (0.1,  0.25),
    'l_elbow':    (-0.15, 0.05),
    'r_elbow':    (0.15,  0.05),
    'l_wrist':    (-0.18, -0.15),
    'r_wrist':    (0.18,  -0.15),
    'pelvis':     (0,    0),    # Origin for relative coordinates
    'l_hip':      (-0.08, -0.05),
    'r_hip':      (0.08,  -0.05),
    'l_knee':     (-0.08, -0.25),
    'r_knee':     (0.08,  -0.25),
    'l_ankle':    (-0.08, -0.45),
    'r_ankle':    (0.08,  -0.45),
}

# The point order for animation (matches the requirement of 15 points)
JOINT_NAMES = [
    'head', 'neck',
    'l_shoulder', 'r_shoulder',
    'l_elbow', 'r_elbow',
    'l_wrist', 'r_wrist',
    'pelvis',
    'l_hip', 'r_hip',
    'l_knee', 'r_knee',
    'l_ankle', 'r_ankle'
]

# Ensure it's exactly 15 points
assert len(JOINT_NAMES) == 15, f"Expected 15 points, but got {len(JOINT_NAMES)}"

# --- Animation Logic ---
animation_duration = 2.5 # Duration of one jump cycle in seconds
forward_speed = 100 # pixels per second
jump_height_factor = 0.7 # Multiplier for jump height (lower for heavy weight)
crouch_depth_factor = 1.1 # Multiplier for crouch depth (deeper for heavy weight prep)
sadness_factor = 0.07 # How much the figure droops (static posture adjustment)

def get_current_joint_positions(t, total_duration):
    """
    Calculates the current (x, y) screen coordinates for all 15 points based on time t.
    t: current time in seconds within the animation cycle.
    total_duration: the total duration of one animation cycle.
    """
    
    # Normalize time to a 0-1 range within the cycle
    t_norm = (t % total_duration) / total_duration

    # --- Base Pelvis Movement (overall character movement) ---
    # Horizontal motion: Continuous forward movement
    # Character starts slightly off-screen left and wraps around
    initial_offset_x = -PERSON_WIDTH_SCALE / 2
    pelvis_x_screen = (initial_offset_x + (t * forward_speed)) % (SCREEN_WIDTH + PERSON_WIDTH_SCALE)
    if pelvis_x_screen > SCREEN_WIDTH: # Make sure it fully clears before wrapping
        pelvis_x_screen -= (SCREEN_WIDTH + PERSON_WIDTH_SCALE)

    # Vertical motion (jump trajectory)
    # This simulates a "hop" or forward jump with distinct phases.
    # Phase 0.0 - 0.25: Crouch (pelvis drops)
    # Phase 0.25 - 0.50: Takeoff and Rise (pelvis rises rapidly)
    # Phase 0.50 - 0.75: Fall (pelvis drops)
    # Phase 0.75 - 1.00: Land & Recover (pelvis settles)

    # Base ground Y position for the pelvis (approx. 3/4 down the screen)
    ground_y = SCREEN_HEIGHT - (SCREEN_HEIGHT * 0.25) 
    
    jump_height = PERSON_HEIGHT_SCALE * 0.5 * jump_height_factor # Max jump height
    crouch_depth = PERSON_HEIGHT_SCALE * 0.15 * crouch_depth_factor # How much the person crouches

    pelvis_y_offset = 0 # This offset is *relative to ground_y* (positive means up)

    if t_norm < 0.25: # Crouch Phase
        t_phase = t_norm / 0.25 # 0 to 1
        pelvis_y_offset = -crouch_depth * math.sin(t_phase * math.pi / 2)
    elif t_norm < 0.5: # Takeoff and Rise Phase
        t_phase = (t_norm - 0.25) / 0.25 # 0 to 1
        pelvis_y_offset = -crouch_depth + (crouch_depth + jump_height) * math.sin(t_phase * math.pi / 2)
    elif t_norm < 0.75: # Fall Phase
        t_phase = (t_norm - 0.5) / 0.25 # 0 to 1
        pelvis_y_offset = jump_height - (jump_height + crouch_depth) * math.sin(t_phase * math.pi / 2)
    else: # Land and Recover Phase
        t_phase = (t_norm - 0.75) / 0.25 # 0 to 1
        pelvis_y_offset = -crouch_depth * (1 - math.sin(t_phase * math.pi / 2))

    # Pygame Y-axis is inverted (0 is top), so subtract offset from ground_y
    pelvis_y_screen = ground_y - pelvis_y_offset

    # --- Limb Movements (relative to pelvis) and Sadman adjustments ---
    current_positions = {}
    for joint_name, (base_x, base_y) in BASE_POSE_RELATIVE.items():
        # Apply overall scale to base relative positions
        scaled_x = base_x * PERSON_WIDTH_SCALE
        scaled_y = base_y * PERSON_HEIGHT_SCALE

        # Static "sadman with heavy weight" posture adjustment:
        # Slight forward lean, droop shoulders, slightly bent knees.
        # This is a fixed offset applied to all joints' base positions.
        sad_lean_x_offset = scaled_y * sadness_factor * 0.5 # More lean for higher joints
        sad_droop_y_offset = -scaled_y * sadness_factor * 0.5 # Higher joints droop more

        # Dynamic limb adjustments for arms and legs based on jump phase
        
        # Arm swing
        arm_swing_angle_max = math.pi / 5 # Max 36 degrees swing
        arm_angle = 0
        if t_norm < 0.25: # Crouch: arms swing back
            t_phase = t_norm / 0.25
            arm_angle = -arm_swing_angle_max * t_phase 
        elif t_norm < 0.5: # Takeoff: arms swing forward
            t_phase = (t_norm - 0.25) / 0.25
            arm_angle = -arm_swing_angle_max + (2 * arm_swing_angle_max) * t_phase 
        elif t_norm < 0.75: # Air/Landing: arms recover
            t_phase = (t_norm - 0.5) / 0.25
            arm_angle = arm_swing_angle_max * (1 - t_phase) 
        else: # Recover: arms go to neutral
            arm_angle = 0

        # Leg bend/extension (simplistic, just vertical adjustment of knee/ankle)
        knee_y_adjust = 0
        ankle_y_adjust = 0
        if t_norm < 0.25: # Crouch
            t_phase = t_norm / 0.25
            knee_y_adjust = -crouch_depth * t_phase * 0.7 # Knees drop more than ankles
            ankle_y_adjust = -crouch_depth * t_phase * 0.5 # Ankles drop less
        elif t_norm < 0.5: # Takeoff
            t_phase = (t_norm - 0.25) / 0.25
            knee_y_adjust = -crouch_depth * (1 - t_phase) * 0.7 
            ankle_y_adjust = -crouch_depth * (1 - t_phase) * 0.5 
        elif t_norm < 0.75: # Air & Landing
            t_phase = (t_norm - 0.5) / 0.25
            # Slight tuck in air, then bend for landing
            if t_phase < 0.5: # Tuck
                knee_y_adjust = -jump_height * 0.1 * math.sin(t_phase * math.pi * 2) 
                ankle_y_adjust = -jump_height * 0.1 * math.sin(t_phase * math.pi * 2)
            else: # Bend for landing
                knee_y_adjust = -crouch_depth * (t_phase - 0.5) * 2 * 0.7 
                ankle_y_adjust = -crouch_depth * (t_phase - 0.5) * 2 * 0.5 
        else: # Recover
            t_phase = (t_norm - 0.75) / 0.25
            knee_y_adjust = -crouch_depth * (1 - t_phase) * 0.7 
            ankle_y_adjust = -crouch_depth * (1 - t_phase) * 0.5 

        # Apply specific transformations to limbs
        if 'shoulder' in joint_name or 'elbow' in joint_name or 'wrist' in joint_name:
            # For simplicity, rotate all arm points around their respective shoulder's base position.
            # This is not strictly biomechanical but gives a good visual effect for point lights.
            sh_x_base, sh_y_base = BASE_POSE_RELATIVE['l_shoulder' if 'left' in joint_name else 'r_shoulder']
            
            # Calculate current position relative to its shoulder
            relative_to_shoulder_x = scaled_x - (sh_x_base * PERSON_WIDTH_SCALE)
            relative_to_shoulder_y = scaled_y - (sh_y_base * PERSON_HEIGHT_SCALE)

            # Apply arm swing angle
            current_angle = arm_angle if 'left' in joint_name else -arm_angle # Opposite swing for arms

            rot_x = relative_to_shoulder_x * math.cos(current_angle) - relative_to_shoulder_y * math.sin(current_angle)
            rot_y = relative_to_shoulder_x * math.sin(current_angle) + relative_to_shoulder_y * math.cos(current_angle)
            
            # Re-add shoulder's base position + sadness offsets
            current_x = (sh_x_base * PERSON_WIDTH_SCALE) + rot_x + sad_lean_x_offset
            current_y = (sh_y_base * PERSON_HEIGHT_SCALE) + rot_y + sad_droop_y_offset

        elif 'knee' in joint_name:
            current_x = scaled_x + sad_lean_x_offset
            current_y = scaled_y + knee_y_adjust + sad_droop_y_offset
        elif 'ankle' in joint_name:
            current_x = scaled_x + sad_lean_x_offset
            current_y = scaled_y + ankle_y_adjust + sad_droop_y_offset
        else: # Head, Neck, Pelvis, Hips (torso and upper leg base)
            current_x = scaled_x + sad_lean_x_offset
            current_y = scaled_y + sad_droop_y_offset

        # Store the current position (still relative to pelvis for now)
        current_positions[joint_name] = (current_x, current_y)

    # --- Apply Torso Lean (affecting upper body) ---
    torso_lean_angle = 0
    # Simulate a subtle forward lean for effort
    if t_norm < 0.25: # Crouch
        t_phase = t_norm / 0.25
        torso_lean_angle = math.pi / 24 * t_phase # Lean forward slightly
    elif t_norm < 0.5: # Takeoff
        t_phase = (t_norm - 0.25) / 0.25
        torso_lean_angle = math.pi / 24 * (1 - t_phase) # Straighten up from lean
    elif t_norm < 0.75: # Air/Landing
        t_phase = (t_norm - 0.5) / 0.25
        torso_lean_angle = -math.pi / 36 * t_phase # Slight backward lean then forward for landing
    else: # Recover
        t_phase = (t_norm - 0.75) / 0.25
        torso_lean_angle = -math.pi / 36 * (1-t_phase) # Straighten

    # Rotate upper body points around the pelvis point
    # We use the raw scaled x,y here (which is relative to pelvis)
    for joint_name in ['head', 'neck', 'l_shoulder', 'r_shoulder', 'l_elbow', 'r_elbow', 'l_wrist', 'r_wrist']:
        current_x, current_y = current_positions[joint_name] # These are already relative to pelvis
        
        rotated_x = current_x * math.cos(torso_lean_angle) - current_y * math.sin(torso_lean_angle)
        rotated_y = current_x * math.sin(torso_lean_angle) + current_y * math.cos(torso_lean_angle)
        
        current_positions[joint_name] = (rotated_x, rotated_y)

    # --- Final Screen Coordinates Conversion ---
    # Apply pelvis screen position and Pygame Y-axis inversion
    final_points = []
    for name in JOINT_NAMES:
        rel_x, rel_y = current_positions[name]
        screen_x = pelvis_x_screen + rel_x
        screen_y = pelvis_y_screen - rel_y # Invert Y for Pygame
        final_points.append((int(screen_x), int(screen_y)))

    return final_points


# --- Main Animation Loop ---
running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate elapsed time in seconds from animation start
    current_time_ms = pygame.time.get_ticks()
    animation_time = (current_time_ms - start_time) / 1000.0

    # Clear screen with black background
    screen.fill(BLACK)

    # Get current joint positions for drawing
    points_to_draw = get_current_joint_positions(animation_time, animation_duration)

    # Draw each point as a white circle
    for x, y in points_to_draw:
        pygame.draw.circle(screen, WHITE, (x, y), POINT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame and exit the program
pygame.quit()
sys.exit()
