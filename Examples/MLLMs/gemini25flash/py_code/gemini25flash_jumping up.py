
import pygame
import math
import numpy as np

# Screen dimensions
WIDTH, HEIGHT = 800, 600
DOT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Scaling factor for the human model relative to screen height
PERSON_SCALE = HEIGHT * 0.4 
# Ground Y-coordinate in Pygame screen space (bottom of the screen is HEIGHT)
GROUND_Y_SCREEN = HEIGHT * 0.8 

# Define relative joint positions for a human body.
# All coordinates are relative to the 'c_hip' (center hip) joint, which is set at (0.0, 0.0).
# Y-axis is positive upwards in this model, facilitating biomechanical interpretation.
# These values will be scaled by PERSON_SCALE and then translated to screen coordinates.
BODY_STRUCTURE = {
    "c_hip": (0.0, 0.0), # Reference point for the model
    "l_hip": (-0.05, 0.0),
    "r_hip": (0.05, 0.0),

    "l_knee": (-0.05, -0.3),  # Relative to c_hip. Y is negative as knees are below hips.
    "r_knee": (0.05, -0.3),
    "l_ankle": (-0.05, -0.6), # Relative to c_hip. Y is negative as ankles are below hips.
    "r_ankle": (0.05, -0.6),

    "chest": (0.0, 0.25),   # Relative to c_hip. Y is positive as chest is above hip.
    "head": (0.0, 0.5),     # Relative to c_hip.

    "l_shoulder": (-0.15, 0.2), # Relative to c_hip.
    "r_shoulder": (0.15, 0.2),
    "l_elbow": (-0.2, 0.0),     # Relative to c_hip.
    "r_elbow": (0.2, 0.0),
    "l_wrist": (-0.25, -0.2),   # Relative to c_hip.
    "r_wrist": (0.25, -0.2),
}

# Ensure the drawing order is consistent for clarity, though not strictly necessary for points.
JOINT_NAMES = [
    "head", "chest",
    "l_shoulder", "r_shoulder",
    "l_elbow", "r_elbow",
    "l_wrist", "r_wrist",
    "c_hip", "l_hip", "r_hip",
    "l_knee", "r_knee",
    "l_ankle", "r_ankle"
]

def rotate_point(origin, point, angle):
    """
    Rotate a point (px, py) around an origin (ox, oy) by an angle (radians).
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def get_current_pose(t):
    """
    Returns a dictionary of (x,y) coordinates for each joint based on time t.
    t goes from 0.0 to 1.0 for one full jump cycle.
    Animation parameters (body_y_offset, knee_bend, arm_angle, torso_lean)
    are interpolated over time using keyframes.
    """
    # Key times (normalized 0-1) for control points of the animation
    times = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    # 1. Body vertical offset (relative to standing ground level of c_hip = 0)
    # Negative means lower, positive means higher. Values are factors of PERSON_SCALE.
    crouch_depth = -0.15
    jump_peak_height = 0.5
    landing_sink_depth = -0.05

    body_y_offsets_keyframes = [
        0.0,  # 0.0s: Stand
        0.0,  # 0.1s: Start crouch
        crouch_depth, # 0.2s: Max crouch
        crouch_depth, # 0.3s: Start push-off (still at crouch depth)
        jump_peak_height * 0.5, # 0.4s: Mid-air ascent
        jump_peak_height, # 0.5s: Apex
        jump_peak_height * 0.5, # 0.6s: Mid-air descent
        landing_sink_depth, # 0.7s: Landing impact (knees bent, body dips slightly below standing)
        landing_sink_depth, # 0.8s: Landing impact (hold)
        0.0,  # 0.9s: Recovery back to stand
        0.0   # 1.0s: Stand (loop back)
    ]
    body_y_offset_val = np.interp(t, times, body_y_offsets_keyframes)

    # 2. Knee bend factor (0=straight, 1=max bend)
    knee_bend_factors_keyframes = [
        0.0,  # 0.0s: Stand
        0.0,  # 0.1s: Start crouch
        1.0,  # 0.2s: Max crouch
        1.0,  # 0.3s: Start push-off
        0.0,  # 0.4s: Knees extend for jump
        0.0,  # 0.5s: Apex (legs straight)
        0.0,  # 0.6s: Descent (legs straight)
        1.0,  # 0.7s: Landing impact
        0.5,  # 0.8s: Landing recovery
        0.0,  # 0.9s: Recovery back to stand
        0.0   # 1.0s: Stand
    ]
    knee_bend_factor_val = np.interp(t, times, knee_bend_factors_keyframes)

    # 3. Arm angle (radians, 0=arms down, positive=forward/up, negative=backward)
    arm_angles_rad_keyframes = [
        0.0,         # 0.0s: Stand (arms down)
        0.0,         # 0.1s: Start crouch
        -math.pi/4,  # 0.2s: Arms swing back for crouch
        -math.pi/4,  # 0.3s: Start push-off
        math.pi/2,   # 0.4s: Arms swing up for jump
        math.pi/2,   # 0.5s: Apex (arms up)
        math.pi/4,   # 0.6s: Arms start coming down
        0.0,         # 0.7s: Arms return to neutral
        0.0,         # 0.8s: Landing recovery
        0.0,         # 0.9s: Recovery back to stand
        0.0          # 1.0s: Stand
    ]
    arm_angle_rad_val = np.interp(t, times, arm_angles_rad_keyframes)

    # 4. Torso lean (radians, 0=upright, positive=forward lean)
    torso_leans_rad_keyframes = [
        0.0,         # 0.0s: Stand
        0.0,         # 0.1s: Start crouch
        math.pi/12,  # 0.2s: Slight forward lean for crouch
        math.pi/12,  # 0.3s: Start push-off
        0.0,         # 0.4s: Straighten up
        0.0,         # 0.5s: Apex
        0.0,         # 0.6s: Descent
        0.0,         # 0.7s: Landing impact
        0.0,         # 0.8s: Landing recovery
        0.0,         # 0.9s: Recovery back to stand
        0.0          # 1.0s: Stand
    ]
    torso_lean_rad_val = np.interp(t, times, torso_leans_rad_keyframes)

    # Calculate current absolute screen position of the 'c_hip' (center hip) joint.
    # The 'ground' is at GROUND_Y_SCREEN. The lowest points (ankles) in the model are at rel_y = -0.6.
    # So, when body_y_offset_val is 0 (standing), the c_hip's Y position in screen space is:
    # GROUND_Y_SCREEN - (relative Y of ankle * PERSON_SCALE)
    # The relative Y of the ankle from c_hip is -0.6. So, `GROUND_Y_SCREEN - (-0.6 * PERSON_SCALE)`.
    base_c_hip_screen_y = GROUND_Y_SCREEN - (BODY_STRUCTURE["l_ankle"][1] * PERSON_SCALE)

    # Apply the overall vertical jump offset to the c_hip's base Y position.
    # Subtract because positive body_y_offset_val means moving up, which is a smaller Y in Pygame.
    c_hip_screen_y = base_c_hip_screen_y - (body_y_offset_val * PERSON_SCALE)
    c_hip_screen_x = WIDTH // 2

    current_frame_pose = {}
    
    for joint_name, (rel_x_orig, rel_y_orig) in BODY_STRUCTURE.items():
        # Start with original relative coordinates for transformation
        x, y = rel_x_orig, rel_y_orig 

        # Apply torso lean to upper body and hip points
        # These joints pivot around the c_hip
        if joint_name in ["head", "chest", "l_shoulder", "r_shoulder", "c_hip", "l_hip", "r_hip"]:
            x, y = rotate_point(BODY_STRUCTURE["c_hip"], (rel_x_orig, rel_y_orig), torso_lean_rad_val)
        
        # Apply knee bend: simply adjust Y and X position for a bending appearance.
        # This is a simplification and not true inverse kinematics.
        if "knee" in joint_name:
            x_shift = 0.05 * knee_bend_factor_val * (1 if joint_name.startswith('l') else -1)
            y_shift = -0.15 * knee_bend_factor_val
            x += x_shift
            y += y_shift
        elif "ankle" in joint_name:
            x_shift = 0.08 * knee_bend_factor_val * (1 if joint_name.startswith('l') else -1)
            y_shift = -0.25 * knee_bend_factor_val
            x += x_shift
            y += y_shift

        # Apply arm swing (rotate around the respective shoulder)
        if joint_name in ["l_elbow", "r_elbow", "l_wrist", "r_wrist"]:
            shoulder_key = "l_shoulder" if joint_name.startswith('l') else "r_shoulder"
            
            # Get the current position of the shoulder (which might have been affected by torso lean)
            rotated_shoulder_rel_x, rotated_shoulder_rel_y = rotate_point(
                BODY_STRUCTURE["c_hip"], BODY_STRUCTURE[shoulder_key], torso_lean_rad_val
            )

            # Calculate the position of the current joint relative to its (potentially leaned) shoulder
            point_rel_to_shoulder_x = x - rotated_shoulder_rel_x
            point_rel_to_shoulder_y = y - rotated_shoulder_rel_y
            
            # Apply arm rotation around the shoulder
            rotated_arm_x = math.cos(arm_angle_rad_val) * point_rel_to_shoulder_x - math.sin(arm_angle_rad_val) * point_rel_to_shoulder_y
            rotated_arm_y = math.sin(arm_angle_rad_val) * point_rel_to_shoulder_x + math.cos(arm_angle_rad_val) * point_rel_to_shoulder_y
            
            # Add back the rotated shoulder position to get the final relative position
            x = rotated_shoulder_rel_x + rotated_arm_x
            y = rotated_shoulder_rel_y + rotated_arm_y
        
        # Final transformation to Pygame screen coordinates: scale and translate.
        # X: Add to center X. Y: Subtract from calculated c_hip Y (because Pygame Y increases downwards)
        screen_x = c_hip_screen_x + (x * PERSON_SCALE)
        screen_y = c_hip_screen_y - (y * PERSON_SCALE) 

        current_frame_pose[joint_name] = (int(screen_x), int(screen_y))

    return current_frame_pose

# Main Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Jumping Man")
clock = pygame.time.Clock()

running = True
frame_count = 0
animation_duration = 2.0 # Total seconds for one full jump cycle
total_frames = int(animation_duration * FPS)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Clear screen with black background

    # Calculate animation progress (normalized 0.0 to 1.0)
    t = (frame_count % total_frames) / total_frames

    # Get the current pose for all joints
    current_pose = get_current_pose(t)

    # Draw each point as a white circle
    for joint_name in JOINT_NAMES:
        x, y = current_pose[joint_name]
        pygame.draw.circle(screen, WHITE, (x, y), DOT_RADIUS)

    pygame.display.flip() # Update the full display surface
    frame_count += 1
    clock.tick(FPS) # Control frame rate

pygame.quit()
