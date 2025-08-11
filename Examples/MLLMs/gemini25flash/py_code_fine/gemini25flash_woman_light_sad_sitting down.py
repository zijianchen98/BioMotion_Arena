
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# Animation parameters
ANIMATION_DURATION = 3000  # milliseconds for one phase (sitting down or standing up)
FRAME_RATE = 60

# Human body dimensions (normalized ratios, scaled later to screen height)
# These values are approximate and designed to look natural on screen.
# All segment lengths are relative to the 'person_height_on_screen' for scaling.
person_height_on_screen = SCREEN_HEIGHT * 0.7  # The overall height of the standing figure

HEAD_HEIGHT = person_height_on_screen * 0.125      # Approx 1/8 of body height
TORSO_LENGTH = person_height_on_screen * 0.375     # Approx 3/8 of body height (Neck to Pelvis)
LEG_LENGTH = person_height_on_screen * 0.5         # Approx 1/2 of body height (Pelvis to Ankle)

HEAD_NECK_LENGTH = HEAD_HEIGHT * 0.8               # Distance from top of head to neck base
NECK_SHOULDER_WIDTH = person_height_on_screen * 0.08 # Half width between shoulders
HIP_WIDTH = person_height_on_screen * 0.1          # Half width between hips

SHOULDER_ELBOW_LENGTH = person_height_on_screen * 0.18 # Shoulder to elbow
ELBOW_WRIST_LENGTH = person_height_on_screen * 0.18    # Elbow to wrist

HIP_KNEE_LENGTH = LEG_LENGTH * 0.5                 # Hip to knee
KNEE_ANKLE_LENGTH = LEG_LENGTH * 0.5               # Knee to ankle

# Point indices for clarity and consistency (15 points)
HEAD = 0
NECK = 1
L_SHOULDER = 2
R_SHOULDER = 3
L_ELBOW = 4
R_ELBOW = 5
L_WRIST = 6
R_WRIST = 7
L_HIP = 8
R_HIP = 9
PELVIS = 10  # Central point between hips
L_KNEE = 11
R_KNEE = 12
L_ANKLE = 13
R_ANKLE = 14

def get_point_positions(progress):
    """
    Calculates the 15 point positions based on animation progress (0.0 to 1.0).
    The returned coordinates are relative to the *horizontal center* and *lowest point* of the figure.
    
    `progress`: 0.0 (standing) to 1.0 (fully sitting).
    """
    
    # Use an easing function for smooth animation (ease-in-out sine wave)
    eased_progress = (1 - math.cos(progress * math.pi)) / 2

    # --- Define key pose parameters for standing (eased_progress=0) and sitting (eased_progress=1) ---
    
    # 1. Pelvis Y-position (relative to standing ankle at y=0)
    # Standing: pelvis is at `LEG_LENGTH` from the floor.
    # Sitting: pelvis drops significantly. Sitting height is roughly half of standing height.
    standing_pelvis_y_rel = LEG_LENGTH 
    sitting_pelvis_y_rel = standing_pelvis_y_rel - (person_height_on_screen * 0.45) # Drop pelvis by approx 45% of total height

    current_pelvis_y_rel = standing_pelvis_y_rel - eased_progress * (standing_pelvis_y_rel - sitting_pelvis_y_rel)

    # 2. Pelvis X-position (relative to horizontal center x=0)
    # Sitting often involves a slight backward shift of the hips for balance.
    standing_pelvis_x_rel = 0
    sitting_pelvis_x_rel = -person_height_on_screen * 0.05 # Move pelvis slightly backward (negative x)
    current_pelvis_x_rel = standing_pelvis_x_rel + eased_progress * (sitting_pelvis_x_rel - standing_pelvis_x_rel)

    # 3. Knee bend angle (angle from hip-knee line to knee-ankle line)
    # 0 degrees bend (straight leg) to 90 degrees bend (pi/2 radians)
    standing_knee_bend_rad = 0
    sitting_knee_bend_rad = math.pi / 2 
    current_knee_bend_rad = standing_knee_bend_rad + eased_progress * (sitting_knee_bend_rad - standing_knee_bend_rad)

    # 4. Thigh angle (angle of hip-knee segment from vertical)
    # 0 degrees (vertical leg) to 90 degrees (horizontal thigh)
    standing_thigh_angle_rad = 0
    sitting_thigh_angle_rad = math.pi / 2 
    current_thigh_angle_rad = standing_thigh_angle_rad + eased_progress * (sitting_thigh_angle_rad - standing_thigh_angle_rad)

    # 5. Torso lean (angle from vertical)
    # 0 degrees (upright torso) to slight forward lean for balance
    standing_torso_lean_rad = 0
    sitting_torso_lean_rad = math.pi / 10 # Approx 18 degrees forward lean
    current_torso_lean_rad = standing_torso_lean_rad + eased_progress * (sitting_torso_lean_rad - standing_torso_lean_rad)

    # 6. Arm angle (relative to torso, hanging)
    # Arms typically hang down. When sitting, they might rest on lap or hang beside.
    # We'll make them hang mostly vertically but slightly forward/inward if sitting.
    standing_arm_angle_rad = 0 # Straight down from shoulder relative to torso
    sitting_arm_angle_rad = math.pi / 8 # Slight bend forward/inward
    current_arm_angle_rad = standing_arm_angle_rad + eased_progress * (sitting_arm_angle_rad - standing_arm_angle_rad)
    
    # --- Calculate point positions relative to (current_pelvis_x_rel, current_pelvis_y_rel) ---
    
    body_points = {}

    # Pelvis is the central reference point for the lower body
    body_points[PELVIS] = (current_pelvis_x_rel, current_pelvis_y_rel)

    # Hips (left and right) relative to pelvis
    body_points[L_HIP] = (current_pelvis_x_rel - HIP_WIDTH, current_pelvis_y_rel)
    body_points[R_HIP] = (current_pelvis_x_rel + HIP_WIDTH, current_pelvis_y_rel)

    # Legs: Hip -> Knee -> Ankle
    # Angles for segments are measured clockwise from the positive Y-axis (downwards).
    
    # Right Leg
    rk_x = body_points[R_HIP][0] + HIP_KNEE_LENGTH * math.sin(current_thigh_angle_rad)
    rk_y = body_points[R_HIP][1] + HIP_KNEE_LENGTH * math.cos(current_thigh_angle_rad)
    body_points[R_KNEE] = (rk_x, rk_y)

    ra_x = body_points[R_KNEE][0] + KNEE_ANKLE_LENGTH * math.sin(current_thigh_angle_rad + current_knee_bend_rad)
    ra_y = body_points[R_KNEE][1] + KNEE_ANKLE_LENGTH * math.cos(current_thigh_angle_rad + current_knee_bend_rad)
    body_points[R_ANKLE] = (ra_x, ra_y)

    # Left Leg (symmetric to right, so x-components of vectors are negated)
    lk_x = body_points[L_HIP][0] - HIP_KNEE_LENGTH * math.sin(current_thigh_angle_rad)
    lk_y = body_points[L_HIP][1] + HIP_KNEE_LENGTH * math.cos(current_thigh_angle_rad)
    body_points[L_KNEE] = (lk_x, lk_y)

    la_x = body_points[L_KNEE][0] - KNEE_ANKLE_LENGTH * math.sin(current_thigh_angle_rad + current_knee_bend_rad)
    la_y = body_points[L_KNEE][1] + KNEE_ANKLE_LENGTH * math.cos(current_thigh_angle_rad + current_knee_bend_rad)
    body_points[L_ANKLE] = (la_x, la_y)

    # Torso and Head (relative to pelvis)
    # The torso rotates forward, so the angle is negative when Y-axis points down.
    torso_global_angle_rad = -current_torso_lean_rad 

    # Neck position (base of neck/upper spine)
    neck_x = body_points[PELVIS][0] + TORSO_LENGTH * math.sin(torso_global_angle_rad)
    neck_y = body_points[PELVIS][1] - TORSO_LENGTH * math.cos(torso_global_angle_rad) # Y decreases going up
    body_points[NECK] = (neck_x, neck_y)

    # Head position (above neck)
    head_x = body_points[NECK][0] + HEAD_NECK_LENGTH * math.sin(torso_global_angle_rad)
    head_y = body_points[NECK][1] - HEAD_NECK_LENGTH * math.cos(torso_global_angle_rad)
    body_points[HEAD] = (head_x, head_y)

    # Shoulders (relative to Neck, rotated with torso)
    # Shoulders are perpendicular to the spine.
    # If torso_global_angle_rad is 0, shoulders are at (neck_x +/- NECK_SHOULDER_WIDTH, neck_y).
    # If torso leans forward (negative angle), shoulders move slightly back horizontally and up/down vertically.
    
    # Left Shoulder
    ls_rel_x = -NECK_SHOULDER_WIDTH * math.cos(torso_global_angle_rad) 
    ls_rel_y = -NECK_SHOULDER_WIDTH * math.sin(torso_global_angle_rad) # Should be 0 if horizontal
    # Corrected shoulder calculation to rotate around neck point
    # X and Y components of vector from neck to shoulder for a vertical torso: (-NECK_SHOULDER_WIDTH, 0)
    # Rotate this vector by `torso_global_angle_rad`
    ls_rotated_x = (-NECK_SHOULDER_WIDTH * math.cos(torso_global_angle_rad)) - (0 * math.sin(torso_global_angle_rad))
    ls_rotated_y = (-NECK_SHOULDER_WIDTH * math.sin(torso_global_angle_rad)) + (0 * math.cos(torso_global_angle_rad))
    body_points[L_SHOULDER] = (body_points[NECK][0] + ls_rotated_x, body_points[NECK][1] + ls_rotated_y)

    # Right Shoulder
    rs_rotated_x = (NECK_SHOULDER_WIDTH * math.cos(torso_global_angle_rad)) - (0 * math.sin(torso_global_angle_rad))
    rs_rotated_y = (NECK_SHOULDER_WIDTH * math.sin(torso_global_angle_rad)) + (0 * math.cos(torso_global_angle_rad))
    body_points[R_SHOULDER] = (body_points[NECK][0] + rs_rotated_x, body_points[NECK][1] + rs_rotated_y)

    # Arms: Shoulder -> Elbow -> Wrist
    # Arm angle relative to the global Y-axis (down), influenced by torso lean and arm swing.
    arm_global_angle_rad = torso_global_angle_rad + current_arm_angle_rad 

    # Right Arm
    re_x = body_points[R_SHOULDER][0] + SHOULDER_ELBOW_LENGTH * math.sin(arm_global_angle_rad)
    re_y = body_points[R_SHOULDER][1] + SHOULDER_ELBOW_LENGTH * math.cos(arm_global_angle_rad)
    body_points[R_ELBOW] = (re_x, re_y)

    rw_x = body_points[R_ELBOW][0] + ELBOW_WRIST_LENGTH * math.sin(arm_global_angle_rad)
    rw_y = body_points[R_ELBOW][1] + ELBOW_WRIST_LENGTH * math.cos(arm_global_angle_rad)
    body_points[R_WRIST] = (rw_x, rw_y)

    # Left Arm (symmetric to right)
    le_x = body_points[L_SHOULDER][0] - SHOULDER_ELBOW_LENGTH * math.sin(arm_global_angle_rad)
    le_y = body_points[L_SHOULDER][1] + SHOULDER_ELBOW_LENGTH * math.cos(arm_global_angle_rad)
    body_points[L_ELBOW] = (le_x, le_y)

    lw_x = body_points[L_ELBOW][0] - ELBOW_WRIST_LENGTH * math.sin(arm_global_angle_rad)
    lw_y = body_points[L_ELBOW][1] + ELBOW_WRIST_LENGTH * math.cos(arm_global_angle_rad)
    body_points[L_WRIST] = (lw_x, lw_y)

    # Convert dictionary to a list in numerical order of indices (0-14)
    ordered_points = [None] * 15
    for idx, (x, y) in body_points.items():
        ordered_points[idx] = (x, y)
    
    return ordered_points

# Main animation loop
running = True
clock = pygame.time.Clock()

# Calculate where the ground line should be on the screen
ground_y = SCREEN_HEIGHT - 50 # 50 pixels from the bottom of the screen

# Get the initial lowest Y-coordinate of the standing figure (progress=0)
standing_points_rel = get_point_positions(0)
initial_lowest_y_rel = min(p[1] for p in standing_points_rel)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Allow ESC to quit
                running = False

    screen.fill(BLACK)

    # Animation progress over a full cycle (sit down then stand up)
    # The total cycle duration is 2 * ANIMATION_DURATION
    animation_elapsed_time = (pygame.time.get_ticks() % (2 * ANIMATION_DURATION))
    
    if animation_elapsed_time < ANIMATION_DURATION:
        # First half: Sitting down (progress from 0.0 to 1.0)
        progress = animation_elapsed_time / ANIMATION_DURATION
    else:
        # Second half: Standing up (progress from 1.0 to 0.0)
        progress = 1.0 - ((animation_elapsed_time - ANIMATION_DURATION) / ANIMATION_DURATION)

    # Get the relative coordinates for the current animation progress
    current_points_rel = get_point_positions(progress)

    # Find the lowest Y-coordinate of the figure in its current pose
    current_lowest_y_rel = min(p[1] for p in current_points_rel)

    # Calculate the translation needed to keep the lowest point (feet) on the ground_y line
    # The figure's horizontal center will be SCREEN_WIDTH // 2
    center_x = SCREEN_WIDTH // 2
    
    # Apply translation to screen coordinates
    translated_points = []
    for x_rel, y_rel in current_points_rel:
        # Translate X relative to the figure's horizontal center to screen center
        translated_x = center_x + x_rel
        
        # Translate Y such that the current lowest point of the figure aligns with `ground_y`
        # This makes the figure appear to sit down onto a surface at `ground_y`
        translated_y = ground_y + (y_rel - current_lowest_y_rel) 
        
        translated_points.append((translated_x, translated_y))

    # Draw points
    for x, y in translated_points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

    pygame.display.flip()
    clock.tick(FRAME_RATE)

pygame.quit()
sys.exit()
