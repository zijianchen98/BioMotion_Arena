
import pygame
import math

# --- Pygame Setup ---
WIDTH, HEIGHT = 600, 800  # Screen dimensions, adjusted for a vertical figure
DOT_RADIUS = 5
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion (Running Sadman)")
clock = pygame.time.Clock()

# --- Human Body Model Parameters (Proportions and Motion Amplitudes) ---
# All units are relative to a base scale factor
SCALE = 150  # Multiplier for all relative positions to get pixel values.

# Base relative Y positions (0 is roughly the pelvis)
HIP_WIDTH_REL = 0.15 # Half-width of hips from pelvis center

TORSO_HEIGHT_REL = 0.55 # From pelvis to neck base
NECK_HEIGHT_REL = 0.1 # From neck base to top of head
HEAD_RADIUS_REL = 0.08 # For head point (used for height, not actual radius)

SHOULDER_WIDTH_REL = 0.25 # Half-width of shoulders from torso center

ARM_UPPER_LENGTH_REL = 0.25 # Shoulder to Elbow
ARM_LOWER_LENGTH_REL = 0.25 # Elbow to Wrist

LEG_UPPER_LENGTH_REL = 0.4 # Hip to Knee
LEG_LOWER_LENGTH_REL = 0.4 # Knee to Ankle

# Motion parameters
RUN_SPEED_PPS = 120 # Pixels per second for global forward movement.
CYCLE_DURATION_SEC = 1.2 # Time for one full stride cycle (e.g., a jog).

# Amplitudes for sinusoidal motions (angles in radians)
# Vertical bobbing of torso (center of mass)
TORSO_BOB_AMPLITUDE_Y = 0.03 * SCALE 

# Arm swing (angle from vertical)
ARM_SWING_ANGLE_AMPLITUDE = math.radians(25) # Max angle from vertical for arm swing
ELBOW_BEND_ANGLE_AMPLITUDE = math.radians(30) # Max additional bend at elbow

# Leg swing (angle from vertical for thigh)
HIP_SWING_ANGLE_AMPLITUDE = math.radians(35) # Max angle from vertical for thigh swing
KNEE_BEND_ANGLE_AMPLITUDE = math.radians(50) # Max additional bend at knee
ANKLE_LIFT_AMPLITUDE_Y = 0.05 * SCALE # Max vertical lift of ankle/foot when off ground

# Sadman/Light Weight specific adjustments
# These factors modify the base motion parameters to reflect the specified action.
SAD_LEAN_X = 0.02 * SCALE # Slight forward lean of the upper body
SAD_SHOULDER_DROP_Y = 0.015 * SCALE # Shoulders slightly lower (positive Y means lower)
LIGHT_BOUNCE_FACTOR = 0.7 # Reduce vertical bobbing amplitude (less bounce)
LESS_ARM_SWING_FACTOR = 0.7 # Reduce arm swing amplitude

# Global offset for the figure's base position on screen
# The figure will start off-screen left and move across.
GLOBAL_START_X = -SCALE * 2 
GLOBAL_Y_OFFSET = HEIGHT // 2 + SCALE # Lower the figure slightly on screen for better visibility

# --- Point mapping for 15 points (indices for clarity) ---
HEAD = 0
NECK = 1
R_SHOULDER = 2
L_SHOULDER = 3
R_ELBOW = 4
L_ELBOW = 5
R_WRIST = 6
L_WRIST = 7
R_HIP = 8
L_HIP = 9
PELVIS_CENTER = 10
R_KNEE = 11
L_KNEE = 12
R_ANKLE = 13
L_ANKLE = 14

# --- Functions to calculate joint positions ---

def get_point_coordinates(time_in_cycle, global_x, global_y):
    """
    Calculates the 15 point-light coordinates for a given time in the cycle.
    `time_in_cycle`: A float representing the current phase of the running cycle (0.0 to 1.0).
    `global_x, global_y`: The current center coordinates of the figure on the screen.
    """
    points = [(0, 0)] * 15 # Initialize 15 points with dummy coordinates

    # Convert time_in_cycle (0-1) to radians (0-2*pi) for sinusoidal functions
    phase = time_in_cycle * 2 * math.pi

    # --- Torso/Head ---
    # Vertical bobbing for torso (simulates center of mass movement during running).
    # Using sin(2*phase) creates two bobs per cycle, typical for a running gait.
    torso_bob_y = TORSO_BOB_AMPLITUDE_Y * LIGHT_BOUNCE_FACTOR * math.sin(phase * 2) 

    # Base pelvis position, incorporating global position and vertical bobbing
    pelvis_base_x = global_x
    pelvis_base_y = global_y + torso_bob_y
    points[PELVIS_CENTER] = (pelvis_base_x, pelvis_base_y)

    # Apply 'sadman' lean and shoulder drop to upper body points.
    # The lean is more pronounced higher up the body.
    lean_factor_head = 1.0
    lean_factor_neck = 0.7
    lean_factor_shoulder = 0.5

    points[NECK] = (pelvis_base_x + SAD_LEAN_X * lean_factor_neck, 
                    pelvis_base_y - TORSO_HEIGHT_REL * SCALE + SAD_SHOULDER_DROP_Y)
    
    points[HEAD] = (pelvis_base_x + SAD_LEAN_X * lean_factor_head, 
                    pelvis_base_y - (TORSO_HEIGHT_REL + NECK_HEIGHT_REL) * SCALE + SAD_SHOULDER_DROP_Y * 1.5)

    # Shoulders position, affected by lean, drop, and a small counter-rotation for natural look.
    shoulder_y_base = pelvis_base_y - TORSO_HEIGHT_REL * SCALE + SAD_SHOULDER_DROP_Y
    # Small horizontal swing of shoulders (opposite to hip rotation for counter-balance)
    shoulder_x_swing = SHOULDER_WIDTH_REL * SCALE * 0.1 * math.sin(phase + math.pi) 

    points[R_SHOULDER] = (pelvis_base_x - SHOULDER_WIDTH_REL * SCALE + shoulder_x_swing + SAD_LEAN_X * lean_factor_shoulder, shoulder_y_base)
    points[L_SHOULDER] = (pelvis_base_x + SHOULDER_WIDTH_REL * SCALE + shoulder_x_swing + SAD_LEAN_X * lean_factor_shoulder, shoulder_y_base)

    # --- Arms ---
    # Arm swing is typically opposite to leg swing (e.g., right arm forward when left leg forward).
    # We define angles from the vertical: positive for forward swing (right on screen), negative for backward.
    # If phase=0 corresponds to the right leg being at max forward extension:
    #   - Right arm should be at max backward extension.
    #   - Left arm should be at max forward extension.
    
    # Right Arm: Swings backward when right leg is forward. So, use `sin(phase + pi/2)` for backward.
    arm_swing_r_angle = -LESS_ARM_SWING_FACTOR * ARM_SWING_ANGLE_AMPLITUDE * math.sin(phase + math.pi/2) 
    # Elbow bend: varies from 0 to max amplitude, peaking twice per cycle (syncs with leg motion).
    elbow_bend_r_angle = ELBOW_BEND_ANGLE_AMPLITUDE * (0.5 - 0.5 * math.cos(phase * 2 + math.pi)) 

    # Left Arm: Swings forward when right leg is forward. So, use `sin(phase - pi/2)` for forward.
    arm_swing_l_angle = -LESS_ARM_SWING_FACTOR * ARM_SWING_ANGLE_AMPLITUDE * math.sin(phase - math.pi/2)
    elbow_bend_l_angle = ELBOW_BEND_ANGLE_AMPLITUDE * (0.5 - 0.5 * math.cos(phase * 2)) 
    
    # Calculate arm joint positions (shoulder -> elbow -> wrist)
    # Right arm:
    shoulder_angle_r = arm_swing_r_angle 
    upper_arm_dx_r = ARM_UPPER_LENGTH_REL * SCALE * math.sin(shoulder_angle_r)
    upper_arm_dy_r = ARM_UPPER_LENGTH_REL * SCALE * math.cos(shoulder_angle_r)
    points[R_ELBOW] = (points[R_SHOULDER][0] + upper_arm_dx_r, points[R_SHOULDER][1] + upper_arm_dy_r)
    
    lower_arm_angle_r = shoulder_angle_r + elbow_bend_r_angle # Lower arm angle relative to vertical
    lower_arm_dx_r = ARM_LOWER_LENGTH_REL * SCALE * math.sin(lower_arm_angle_r)
    lower_arm_dy_r = ARM_LOWER_LENGTH_REL * SCALE * math.cos(lower_arm_angle_r)
    points[R_WRIST] = (points[R_ELBOW][0] + lower_arm_dx_r, points[R_ELBOW][1] + lower_arm_dy_r)

    # Left arm:
    shoulder_angle_l = arm_swing_l_angle
    upper_arm_dx_l = ARM_UPPER_LENGTH_REL * SCALE * math.sin(shoulder_angle_l)
    upper_arm_dy_l = ARM_UPPER_LENGTH_REL * SCALE * math.cos(shoulder_angle_l)
    points[L_ELBOW] = (points[L_SHOULDER][0] + upper_arm_dx_l, points[L_SHOULDER][1] + upper_arm_dy_l)
    
    lower_arm_angle_l = shoulder_angle_l + elbow_bend_l_angle
    lower_arm_dx_l = ARM_LOWER_LENGTH_REL * SCALE * math.sin(lower_arm_angle_l)
    lower_arm_dy_l = ARM_LOWER_LENGTH_REL * SCALE * math.cos(lower_arm_angle_l)
    points[L_WRIST] = (points[L_ELBOW][0] + lower_arm_dx_l, points[L_ELBOW][1] + lower_arm_dy_l)
    
    # --- Legs ---
    # Hip points are slightly to the sides of the pelvis center.
    points[R_HIP] = (pelvis_base_x - HIP_WIDTH_REL * SCALE, pelvis_base_y)
    points[L_HIP] = (pelvis_base_x + HIP_WIDTH_REL * SCALE, pelvis_base_y)

    # Right Leg: max forward extension at phase = 0.
    # Thigh angle (from vertical): positive for forward swing.
    thigh_angle_r = HIP_SWING_ANGLE_AMPLITUDE * math.sin(phase + math.pi / 2)

    # Knee bend: max bend occurs twice per cycle (mid-swing and push-off).
    knee_bend_r_angle = KNEE_BEND_ANGLE_AMPLITUDE * (0.5 - 0.5 * math.cos(phase * 2))
    
    # Ankle lift: highest when leg is swinging forward and off the ground.
    # Negative Y to lift (smaller Y value on screen).
    ankle_lift_r_y = ANKLE_LIFT_AMPLITUDE_Y * (0.5 - 0.5 * math.cos(phase * 2 + math.pi/2)) 

    # Left Leg: Opposite phase to the right leg.
    thigh_angle_l = HIP_SWING_ANGLE_AMPLITUDE * math.sin(phase + math.pi / 2 + math.pi) 
    knee_bend_l_angle = KNEE_BEND_ANGLE_AMPLITUDE * (0.5 - 0.5 * math.cos(phase * 2 + math.pi))
    ankle_lift_l_y = ANKLE_LIFT_AMPLITUDE_Y * (0.5 - 0.5 * math.cos(phase * 2 + 3*math.pi/2))
    
    # Calculate leg joint positions (hip -> knee -> ankle)
    # Right Leg:
    dx_thigh_r = LEG_UPPER_LENGTH_REL * SCALE * math.sin(thigh_angle_r)
    dy_thigh_r = LEG_UPPER_LENGTH_REL * SCALE * math.cos(thigh_angle_r)
    points[R_KNEE] = (points[R_HIP][0] + dx_thigh_r, points[R_HIP][1] + dy_thigh_r)
    
    calf_angle_r = thigh_angle_r + knee_bend_r_angle # Lower leg angle relative to vertical
    dx_calf_r = LEG_LOWER_LENGTH_REL * SCALE * math.sin(calf_angle_r)
    dy_calf_r = LEG_LOWER_LENGTH_REL * SCALE * math.cos(calf_angle_r)
    points[R_ANKLE] = (points[R_KNEE][0] + dx_calf_r, points[R_KNEE][1] + dy_calf_r - ankle_lift_r_y) 

    # Left Leg:
    dx_thigh_l = LEG_UPPER_LENGTH_REL * SCALE * math.sin(thigh_angle_l)
    dy_thigh_l = LEG_LOWER_LENGTH_REL * SCALE * math.cos(thigh_angle_l)
    points[L_KNEE] = (points[L_HIP][0] + dx_thigh_l, points[L_HIP][1] + dy_thigh_l)
    
    calf_angle_l = thigh_angle_l + knee_bend_l_angle
    dx_calf_l = LEG_LOWER_LENGTH_REL * SCALE * math.sin(calf_angle_l)
    dy_calf_l = LEG_LOWER_LENGTH_REL * SCALE * math.cos(calf_angle_l)
    points[L_ANKLE] = (points[L_KNEE][0] + dx_calf_l, points[L_KNEE][1] + dy_calf_l - ankle_lift_l_y)

    return points

# --- Main Animation Loop ---
running = True
current_time_sec = 0.0 # Time elapsed since the start of the animation
global_movement_x = GLOBAL_START_X # Horizontal position of the entire figure

while running:
    dt = clock.tick(FPS) / 1000.0 # Delta time in seconds (time since last frame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Allow ESC key to quit
                running = False

    current_time_sec += dt
    
    # Update global x offset to simulate forward movement across the screen
    global_movement_x += RUN_SPEED_PPS * dt
    
    # Loop the global movement: once the figure moves completely off-screen to the right,
    # reset its position to start off-screen left, creating a continuous loop.
    if global_movement_x > WIDTH + SCALE * 2: # Move off screen by more than figure width
        global_movement_x = -SCALE * 2 # Reset to start far left

    # Calculate the current phase of the running cycle (0.0 to 1.0)
    # The modulo operator ensures the phase wraps around correctly (e.g., 1.1 becomes 0.1)
    time_in_cycle = (current_time_sec / CYCLE_DURATION_SEC) % 1.0

    # Get the coordinates for all 15 points for the current animation frame
    # figure_center_x is the global horizontal position of the pelvis_center.
    figure_center_x = global_movement_x 
    figure_center_y = GLOBAL_Y_OFFSET
    
    current_points = get_point_coordinates(time_in_cycle, figure_center_x, figure_center_y)

    # --- Drawing ---
    screen.fill(BLACK) # Clear screen to solid black

    # Draw each point as a white circle
    for point_coords in current_points:
        pygame.draw.circle(screen, WHITE, (int(point_coords[0]), int(point_coords[1])), DOT_RADIUS)

    pygame.display.flip() # Update the entire display surface to show the new frame

pygame.quit()
