
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Bowing with Heavy Weight")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point radius
POINT_RADIUS = 4

# Animation parameters
FPS = 60
ANIMATION_DURATION_SECONDS = 4  # Total duration of one cycle (bow down and up)
TOTAL_FRAMES = FPS * ANIMATION_DURATION_SECONDS

# Body segment lengths (in pixels) - adjusted for a typical human figure scale
# These are relative proportions, scaled to fit the screen.
SCALE_FACTOR = HEIGHT / 450 

SEGMENTS = {
    'NECK_LENGTH': 20 * SCALE_FACTOR,
    'SHOULDER_WIDTH': 25 * SCALE_FACTOR, # Half width from center axis
    'TORSO_UPPER_LENGTH': 60 * SCALE_FACTOR, # Chest to Neck
    'TORSO_LOWER_LENGTH': 70 * SCALE_FACTOR, # Pelvis to Chest
    'UPPER_ARM_LENGTH': 80 * SCALE_FACTOR,
    'FOREARM_LENGTH': 70 * SCALE_FACTOR,
    'THIGH_LENGTH': 100 * SCALE_FACTOR,
    'SHANK_LENGTH': 100 * SCALE_FACTOR,
    'FOOT_OFFSET_X': 20 * SCALE_FACTOR, # Horizontal offset from feet_base to ankle
    'FOOT_OFFSET_Y': 10 * SCALE_FACTOR, # Vertical offset from feet_base to ankle
    'HIP_WIDTH': 30 * SCALE_FACTOR # Half width from pelvis center
}

# Base position (feet on the ground, center of body)
BASE_X = WIDTH // 2
BASE_Y = HEIGHT * 0.85 # The Y coordinate of the lowest point (FEET_BASE)

# Dictionary to hold current positions of points
points_coords = {}

# Function to calculate point positions based on frame
def calculate_points(frame):
    t = (frame % TOTAL_FRAMES) / TOTAL_FRAMES # Normalized time [0, 1)

    # Use a smooth interpolation for the bowing motion (0 to 1 and back to 0)
    # This creates a natural ease-in/ease-out effect.
    animation_progress = (1 - math.cos(t * 2 * math.pi)) / 2

    # Animation Angles (all in radians)
    # Angle convention: 0 is vertical UP, positive is clockwise (forward bend/right)

    # 1. Torso Angle (from vertical) - Primary bowing motion
    MAX_TORSO_BEND_DEG = 70 # Max forward bend from upright
    torso_angle_from_vertical = math.radians(MAX_TORSO_BEND_DEG) * animation_progress

    # 2. Knee Flexion (relative to straight leg, 0 is straight) - Slight squat for stability/weight
    MAX_KNEE_BEND_DEG = 20
    knee_flexion_rad = math.radians(MAX_KNEE_BEND_DEG) * animation_progress

    # 3. Arm Swing (forward from hanging straight down from shoulder, relative to torso line)
    # Simulates reaching down or holding/lifting heavy object
    MAX_ARM_SWING_DEG = 45 
    arm_swing_rad = math.radians(MAX_ARM_SWING_DEG) * animation_progress

    # 4. Elbow Flexion (relative to straight arm, 0 is straight) - Arms bend as if gripping
    MAX_ELBOW_BEND_DEG = 30 
    elbow_flexion_rad = math.radians(MAX_ELBOW_BEND_DEG) * animation_progress

    # --- Kinematic Chain Calculations (Bottom-up approach) ---

    # 15. FEET_BASE (fixed point on the ground)
    points_coords['FEET_BASE'] = (BASE_X, BASE_Y)

    # Legs Lean Angle: The entire leg assembly leans forward less than the torso.
    leg_lean_angle = torso_angle_from_vertical / 2

    # Ankles (relative to FEET_BASE)
    # Ankle is slightly forward (X) and up (Y) from the FEET_BASE.
    # The offset also rotates with the overall leg lean.
    ankle_x_base = BASE_X + SEGMENTS['FOOT_OFFSET_X'] * math.sin(leg_lean_angle)
    ankle_y_base = BASE_Y - SEGMENTS['FOOT_OFFSET_Y'] * math.cos(leg_lean_angle)
    
    # Left and Right ankles are slightly offset horizontally for visual separation
    points_coords['LEFT_ANKLE'] = (ankle_x_base - SEGMENTS['HIP_WIDTH']/4, ankle_y_base) 
    points_coords['RIGHT_ANKLE'] = (ankle_x_base + SEGMENTS['HIP_WIDTH']/4, ankle_y_base)

    # Knees (relative to Ankles)
    # Shank segment angle from vertical UP. Knee flexion bends shank backward relative to thigh/leg axis.
    shank_segment_angle = leg_lean_angle - knee_flexion_rad 
    
    for prefix in ['LEFT_', 'RIGHT_']:
        ankle_pos = points_coords[f'{prefix}ANKLE']
        knee_x = ankle_pos[0] + SEGMENTS['SHANK_LENGTH'] * math.sin(shank_segment_angle)
        knee_y = ankle_pos[1] - SEGMENTS['SHANK_LENGTH'] * math.cos(shank_segment_angle) # Knee is above ankle
        points_coords[f'{prefix}KNEE'] = (knee_x, knee_y)

    # Hips (relative to Knees)
    # Thigh segment angle from vertical UP (aligned with overall leg lean).
    thigh_segment_angle = leg_lean_angle 
    
    for prefix in ['LEFT_', 'RIGHT_']:
        knee_pos = points_coords[f'{prefix}KNEE']
        hip_x = knee_pos[0] + SEGMENTS['THIGH_LENGTH'] * math.sin(thigh_segment_angle)
        hip_y = knee_pos[1] - SEGMENTS['THIGH_LENGTH'] * math.cos(thigh_segment_angle) # Hip is above knee
        points_coords[f'{prefix}HIP'] = (hip_x, hip_y)

    # 8. PELVIS (center of Hips)
    avg_hip_x = (points_coords['LEFT_HIP'][0] + points_coords['RIGHT_HIP'][0]) / 2
    avg_hip_y = (points_coords['LEFT_HIP'][1] + points_coords['RIGHT_HIP'][1]) / 2
    points_coords['PELVIS'] = (avg_hip_x, avg_hip_y)


    # Torso & Head (from Pelvis up)
    # Torso segments rotate with `torso_angle_from_vertical`

    # 5. CHEST point (mid-torso)
    chest_x = points_coords['PELVIS'][0] + SEGMENTS['TORSO_LOWER_LENGTH'] * math.sin(torso_angle_from_vertical)
    chest_y = points_coords['PELVIS'][1] - SEGMENTS['TORSO_LOWER_LENGTH'] * math.cos(torso_angle_from_vertical) # Chest is above pelvis
    points_coords['CHEST'] = (chest_x, chest_y)

    # 2. NECK point
    neck_x = points_coords['CHEST'][0] + SEGMENTS['TORSO_UPPER_LENGTH'] * math.sin(torso_angle_from_vertical)
    neck_y = points_coords['CHEST'][1] - SEGMENTS['TORSO_UPPER_LENGTH'] * math.cos(torso_angle_from_vertical) # Neck is above chest
    points_coords['NECK'] = (neck_x, neck_y)

    # 1. HEAD point (top of head)
    head_x = points_coords['NECK'][0] + SEGMENTS['NECK_LENGTH'] * math.sin(torso_angle_from_vertical)
    head_y = points_coords['NECK'][1] - SEGMENTS['NECK_LENGTH'] * math.cos(torso_angle_from_vertical) # Head is above neck
    points_coords['HEAD'] = (head_x, head_y)

    # Shoulders (relative to Neck)
    # Shoulders are offset horizontally from the neck, rotating with the torso.
    shoulder_offset_x = SEGMENTS['SHOULDER_WIDTH'] * math.cos(torso_angle_from_vertical)
    shoulder_offset_y = SEGMENTS['SHOULDER_WIDTH'] * math.sin(torso_angle_from_vertical)

    # 3. LEFT_SHOULDER and 4. RIGHT_SHOULDER
    points_coords['LEFT_SHOULDER'] = (neck_x - shoulder_offset_x, neck_y - shoulder_offset_y)
    points_coords['RIGHT_SHOULDER'] = (neck_x + shoulder_offset_x, neck_y - shoulder_offset_y)

    # Arms (from Shoulders down)
    # Upper arm angle from vertical: A sum of torso angle (base), pi (for hanging down), and arm swing.
    # arm_swing_rad (positive) adds to the clockwise rotation.
    upper_arm_angle_from_vertical = torso_angle_from_vertical + math.pi + arm_swing_rad
    
    for prefix in ['LEFT_', 'RIGHT_']:
        shoulder_pos = points_coords[f'{prefix}SHOULDER']
        
        # 6. LEFT_ELBOW and 7. RIGHT_ELBOW
        elbow_x = shoulder_pos[0] + SEGMENTS['UPPER_ARM_LENGTH'] * math.sin(upper_arm_angle_from_vertical)
        elbow_y = shoulder_pos[1] + SEGMENTS['UPPER_ARM_LENGTH'] * math.cos(upper_arm_angle_from_vertical) # Elbow is below shoulder
        points_coords[f'{prefix}ELBOW'] = (elbow_x, elbow_y)
        
        # Wrists (relative to Elbows)
        # Forearm angle from vertical: Elbow flexion bends forearm *backward* (counter-clockwise)
        forearm_angle_from_vertical = upper_arm_angle_from_vertical - elbow_flexion_rad
        
        # Corresponding to points 6 and 7 in a typical 15-point configuration for hands
        # The prompt says 15 points. Image has 2 elbows, 2 wrists. So these should be wrists.
        # But my numbering is 1-15 for the joints. Let's make sure I'm using correct point names.
        # Image points list:
        # 1. Head
        # 2. Neck
        # 3. Left Shoulder
        # 4. Right Shoulder
        # 5. Chest (Mid-spine/Chest)
        # 6. Left Elbow
        # 7. Right Elbow
        # 8. Pelvis (Pelvis center)
        # 9. Left Hip
        # 10. Right Hip
        # 11. Left Knee
        # 12. Right Knee
        # 13. Left Ankle
        # 14. Right Ankle
        # 15. FEET_BASE (Ground contact point)
        # This means wrists are not explicitly defined in the final 15 point list.
        # However, the cropped images show points that would be elbows and then hands/wrists.
        # Let's adjust to match the visual example of 15 points if wrists are truly excluded.
        # The original image's 15 points:
        # Row 1: 1 (Head)
        # Row 2: 3 (L Shoulder, Neck, R Shoulder)
        # Row 3: 3 (L Elbow, Mid Spine/Chest, R Elbow)
        # Row 4: 3 (L Hip, Pelvis Center, R Hip)
        # Row 5: 2 (L Knee, R Knee)
        # Row 6: 2 (L Ankle, R Ankle)
        # Row 7: 1 (Feet Base)
        # This interpretation means WRIST points should *not* be in the final drawing.
        # So I only need to calculate them if they are an intermediate step to get other points.
        # My current code calculates them but only draws the explicitly listed 15 points. This is correct.

    return points_coords

# Animation loop
running = True
clock = pygame.time.Clock()
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate points for the current frame
    current_points = calculate_points(frame_count)

    # Draw the points
    # Explicitly list the 15 points to ensure correct drawing based on the image's structure.
    points_to_draw = [
        'HEAD', 'NECK', 'LEFT_SHOULDER', 'RIGHT_SHOULDER', 'CHEST',
        'LEFT_ELBOW', 'RIGHT_ELBOW', 'PELVIS', 'LEFT_HIP', 'RIGHT_HIP',
        'LEFT_KNEE', 'RIGHT_KNEE', 'LEFT_ANKLE', 'RIGHT_ANKLE', 'FEET_BASE'
    ]

    for name in points_to_draw:
        pos = current_points.get(name)
        if pos: # Ensure point exists
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

    pygame.display.flip()

    frame_count += 1
    clock.tick(FPS)

pygame.quit()
