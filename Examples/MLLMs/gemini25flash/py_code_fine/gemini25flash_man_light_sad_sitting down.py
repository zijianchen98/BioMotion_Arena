
import pygame
import math

# --- Pygame Initialization ---
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Dot properties
DOT_RADIUS = 4

# --- Biomechanical Model Constants (Segment Lengths, in pixels) ---
# These lengths define the proportion of the point-light figure.
HEAD_VISUAL_HEIGHT = 20  # Approximate vertical extent for the head point
NECK_LEN = 20            # Length from Center Torso to Neck
SPINE_LEN = 60           # Length from Pelvis Center to Center Torso
SHOULDER_WIDTH_HALF = 30 # Half distance between shoulders
UPPER_ARM_LEN = 55       # Length from Shoulder to Elbow
FOREARM_LEN = 50         # Length from Elbow to Wrist
THIGH_LEN = 80           # Length from Hip to Knee
SHIN_LEN = 75            # Length from Knee to Ankle
HIP_WIDTH_HALF = 35      # Half distance between hip joints (from pelvis center)

# --- Animation Parameters ---
ANIMATION_DURATION_FRAMES = 90  # Number of frames for one transition (sit down OR stand up)
STILL_PHASE_FRAMES = 60         # Frames to hold the sitting/standing pose
FPS = 60                        # Frames per second

# Initial (Standing) Joint Angles/Positions
start_params = {
    'pelvis_y': 450,             # Y-coordinate of the pelvis center (higher = standing)
    'torso_angle': math.radians(0),   # Angle of torso from vertical (0 = straight up, negative = lean forward)
    'hip_angle': math.radians(0),     # Angle of thigh from vertical (0 = straight down, positive = flex forward)
    'knee_angle': math.radians(0),    # Angle of shin relative to thigh (0 = straight, positive = flex back)
    'arm_angle': math.radians(0),     # Angle of upper arm from vertical (0 = straight down, positive = swing forward)
    'elbow_angle': math.radians(0)    # Angle of forearm relative to upper arm (0 = straight, positive = flex)
}

# Final (Sitting) Joint Angles/Positions
end_params = {
    'pelvis_y': 300,              # Y-coordinate of the pelvis center (lower = sitting)
    'torso_angle': math.radians(-15), # Slight forward lean for balance
    'hip_angle': math.radians(85),    # Thighs nearly horizontal
    'knee_angle': math.radians(95),   # Shins nearly vertical relative to thigh (total angle from vertical for shin: hip_angle + knee_angle)
    'arm_angle': math.radians(10),    # Arms slightly forward
    'elbow_angle': math.radians(10)   # Slight bend in elbow
}

# --- Utility Functions ---
def lerp(start, end, t):
    """Linear interpolation between start and end values."""
    return start + (end - start) * t

def calculate_joint_positions(params):
    """
    Calculates the (x, y) coordinates for all 15 points based on current animation parameters.
    The origin for the calculations is the Pelvis Center.
    Angles are measured clockwise from the positive Y-axis (downwards), or relative to parent segment.
    """
    center_x = WIDTH // 2
    pelvis_y = params['pelvis_y']
    torso_angle = params['torso_angle']
    hip_angle = params['hip_angle']
    knee_angle = params['knee_angle']
    arm_angle = params['arm_angle']
    elbow_angle = params['elbow_angle']

    points = {}

    # Pelvis Center (reference point for the body, not one of the 15 rendered points but used for calculation)
    P_pelvis_center = (center_x, pelvis_y)

    # Hips (R_HIP and L_HIP are points 10 and 11)
    points['R_HIP'] = (P_pelvis_center[0] + HIP_WIDTH_HALF, P_pelvis_center[1])
    points['L_HIP'] = (P_pelvis_center[0] - HIP_WIDTH_HALF, P_pelvis_center[1])

    # Legs (R_KNEE, L_KNEE, R_ANKLE, L_ANKLE are points 12, 13, 14, 15)
    # Right Leg
    # Knee: position relative to hip, based on hip_angle
    points['R_KNEE'] = (
        points['R_HIP'][0] + THIGH_LEN * math.sin(hip_angle),
        points['R_HIP'][1] - THIGH_LEN * math.cos(hip_angle)
    )
    # Ankle: position relative to knee, using hip_angle + knee_angle as the total angle from vertical
    points['R_ANKLE'] = (
        points['R_KNEE'][0] + SHIN_LEN * math.sin(hip_angle + knee_angle),
        points['R_KNEE'][1] - SHIN_LEN * math.cos(hip_angle + knee_angle)
    )

    # Left Leg (symmetrical to right leg)
    points['L_KNEE'] = (
        points['L_HIP'][0] + THIGH_LEN * math.sin(hip_angle),
        points['L_HIP'][1] - THIGH_LEN * math.cos(hip_angle)
    )
    points['L_ANKLE'] = (
        points['L_KNEE'][0] + SHIN_LEN * math.sin(hip_angle + knee_angle),
        points['L_KNEE'][1] - SHIN_LEN * math.cos(hip_angle + knee_angle)
    )

    # Torso (CENTER_TORSO is point 5)
    # Center Torso: position relative to pelvis center, based on torso_angle
    points['CENTER_TORSO'] = (
        P_pelvis_center[0] + SPINE_LEN * math.sin(torso_angle),
        P_pelvis_center[1] - SPINE_LEN * math.cos(torso_angle)
    )

    # Shoulders (R_SHOULDER, L_SHOULDER are points 3 and 4)
    # Shoulders are positioned horizontally from CENTER_TORSO and then rotated with torso_angle
    shoulder_offset_x = SHOULDER_WIDTH_HALF
    shoulder_offset_y = 0 # Shoulders are roughly at the same height as CENTER_TORSO for this model

    # Rotate the horizontal offset by torso_angle around CENTER_TORSO
    rs_rot_x = shoulder_offset_x * math.cos(torso_angle) - shoulder_offset_y * math.sin(torso_angle)
    rs_rot_y = shoulder_offset_x * math.sin(torso_angle) + shoulder_offset_y * math.cos(torso_angle)
    points['R_SHOULDER'] = (points['CENTER_TORSO'][0] + rs_rot_x, points['CENTER_TORSO'][1] + rs_rot_y)

    ls_rot_x = -shoulder_offset_x * math.cos(torso_angle) - shoulder_offset_y * math.sin(torso_angle)
    ls_rot_y = -shoulder_offset_x * math.sin(torso_angle) + shoulder_offset_y * math.cos(torso_angle)
    points['L_SHOULDER'] = (points['CENTER_TORSO'][0] + ls_rot_x, points['CENTER_TORSO'][1] + ls_rot_y)

    # Neck (NECK is point 2)
    # Neck: position relative to center torso, based on torso_angle
    neck_offset_x = NECK_LEN * math.sin(torso_angle)
    neck_offset_y = -NECK_LEN * math.cos(torso_angle)
    points['NECK'] = (points['CENTER_TORSO'][0] + neck_offset_x, points['CENTER_TORSO'][1] + neck_offset_y)

    # Head (HEAD is point 1)
    # Head: position relative to neck, based on torso_angle (simplified as directly above neck, then rotated)
    head_offset_x = 0
    head_offset_y = -HEAD_VISUAL_HEIGHT # Visual height of the head point above the neck
    
    head_rot_x = head_offset_x * math.cos(torso_angle) - head_offset_y * math.sin(torso_angle)
    head_rot_y = head_offset_x * math.sin(torso_angle) + head_offset_y * math.cos(torso_angle)
    points['HEAD'] = (points['NECK'][0] + head_rot_x, points['NECK'][1] + head_rot_y)

    # Arms (R_ELBOW, L_ELBOW, R_WRIST, L_WRIST are points 6, 7, 8, 9)
    # Elbows: position relative to shoulders, based on arm_angle
    # Right Elbow
    points['R_ELBOW'] = (
        points['R_SHOULDER'][0] + UPPER_ARM_LEN * math.sin(arm_angle),
        points['R_SHOULDER'][1] - UPPER_ARM_LEN * math.cos(arm_angle)
    )
    # Left Elbow (symmetrical)
    points['L_ELBOW'] = (
        points['L_SHOULDER'][0] + UPPER_ARM_LEN * math.sin(arm_angle),
        points['L_SHOULDER'][1] - UPPER_ARM_LEN * math.cos(arm_angle)
    )

    # Wrists: position relative to elbows, based on arm_angle + elbow_angle (total angle from vertical for forearm)
    # Right Wrist
    points['R_WRIST'] = (
        points['R_ELBOW'][0] + FOREARM_LEN * math.sin(arm_angle + elbow_angle),
        points['R_ELBOW'][1] - FOREARM_LEN * math.cos(arm_angle + elbow_angle)
    )
    # Left Wrist (symmetrical)
    points['L_WRIST'] = (
        points['L_ELBOW'][0] + FOREARM_LEN * math.sin(arm_angle + elbow_angle),
        points['L_ELBOW'][1] - FOREARM_LEN * math.cos(arm_angle + elbow_angle)
    )
    
    # Return points in a consistent order as per the 15-point model.
    # The order generally follows the image from top to bottom, then left to right for limbs.
    return [
        points['HEAD'],
        points['NECK'],
        points['R_SHOULDER'], points['L_SHOULDER'],
        points['CENTER_TORSO'],
        points['R_ELBOW'], points['L_ELBOW'],
        points['R_WRIST'], points['L_WRIST'],
        points['R_HIP'], points['L_HIP'],
        points['R_KNEE'], points['L_KNEE'],
        points['R_ANKLE'], points['L_ANKLE']
    ]

# --- Main Animation Loop ---
running = True
frame_count = 0
clock = pygame.time.Clock()

# Total frames for one full cycle (stand -> sit -> stay -> stand -> stay)
TOTAL_CYCLE_FRAMES = (ANIMATION_DURATION_FRAMES * 2) + (STILL_PHASE_FRAMES * 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(BLACK)

    # Determine current animation phase and interpolation factor (t)
    # Phase 1: Sitting Down
    if frame_count < ANIMATION_DURATION_FRAMES:
        t = frame_count / ANIMATION_DURATION_FRAMES
        current_params = {key: lerp(start_params[key], end_params[key], t) for key in start_params}
    # Phase 2: Sitting Still
    elif frame_count < ANIMATION_DURATION_FRAMES + STILL_PHASE_FRAMES:
        current_params = end_params  # Stay in sitting position
    # Phase 3: Standing Up
    elif frame_count < (ANIMATION_DURATION_FRAMES * 2) + STILL_PHASE_FRAMES:
        t = (frame_count - (ANIMATION_DURATION_FRAMES + STILL_PHASE_FRAMES)) / ANIMATION_DURATION_FRAMES
        current_params = {key: lerp(end_params[key], start_params[key], t) for key in start_params}
    # Phase 4: Standing Still (and loop reset)
    else:
        current_params = start_params # Ensure it starts from standing for the loop
        if frame_count >= TOTAL_CYCLE_FRAMES:
            frame_count = 0 # Reset frame_count to restart the animation loop

    # Calculate current joint positions for drawing
    current_joint_positions = calculate_joint_positions(current_params)

    # Draw the 15 points
    for pos in current_joint_positions:
        # Ensure positions are integers for drawing
        pygame.draw.circle(SCREEN, WHITE, (int(pos[0]), int(pos[1])), DOT_RADIUS)

    pygame.display.flip()

    frame_count += 1
    clock.tick(FPS)

pygame.quit()
