
import pygame
import math

# 1. Initialize Pygame
pygame.init()

# 2. Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Bowing Man")

# 3. Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 4. Point properties
POINT_RADIUS = 4
NUM_POINTS = 15 # As per requirement

# 5. Animation parameters
FPS = 60
clock = pygame.time.Clock()
ANIMATION_DURATION_SECONDS = 3 # 1.5 seconds down, 1.5 seconds up
TOTAL_FRAMES = int(FPS * ANIMATION_DURATION_SECONDS)

# Body point indices for clarity (following common conventions and image analysis)
# 0: Head
# 1: Neck base/Upper spine
# 2: Left Shoulder
# 3: Right Shoulder
# 4: Left Elbow
# 5: Right Elbow
# 6: Left Wrist
# 7: Right Wrist
# 8: Mid-torso/Pelvis center (main pivot for upper body)
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle
HEAD = 0
NECK = 1
L_SHOULDER = 2
R_SHOULDER = 3
L_ELBOW = 4
R_ELBOW = 5
L_WRIST = 6
R_WRIST = 7
PELVIS_CENTER = 8
L_HIP = 9
R_HIP = 10
L_KNEE = 11
R_KNEE = 12
L_ANKLE = 13
R_ANKLE = 14

# Segment lengths (in pixels)
# These are rough estimates scaled to fit the screen and represent a human figure
SEGMENT_LENGTHS = {}
H_BODY = 300 # Approximate total vertical span of the standing person on screen

# Spine and Head segments
SEGMENT_LENGTHS[(PELVIS_CENTER, NECK)] = H_BODY * 0.20 # From mid-pelvis (8) to neck base (1)
SEGMENT_LENGTHS[(NECK, HEAD)] = H_BODY * 0.08 # From neck base (1) to head top (0)

# Shoulders and Arms segments
SHOULDER_SPAN = H_BODY * 0.2 # Total shoulder width
SEGMENT_LENGTHS[(NECK, L_SHOULDER)] = SHOULDER_SPAN / 2 # Horizontal offset from neck (1) to shoulder (2/3)
SEGMENT_LENGTHS[(NECK, R_SHOULDER)] = SHOULDER_SPAN / 2
SEGMENT_LENGTHS[(L_SHOULDER, L_ELBOW)] = H_BODY * 0.15 # Upper arm (2 to 4)
SEGMENT_LENGTHS[(R_SHOULDER, R_ELBOW)] = H_BODY * 0.15 # (3 to 5)
SEGMENT_LENGTHS[(L_ELBOW, L_WRIST)] = H_BODY * 0.15 # Forearm (4 to 6)
SEGMENT_LENGTHS[(R_ELBOW, R_WRIST)] = H_BODY * 0.15 # (5 to 7)

# Hips and Legs segments
HIP_SPAN = H_BODY * 0.15 # Distance between hip joints (9, 10)
SEGMENT_LENGTHS[(PELVIS_CENTER, L_HIP)] = HIP_SPAN / 2 # Horizontal offset from pelvis center (8) to hip joint (9/10)
SEGMENT_LENGTHS[(L_HIP, L_KNEE)] = H_BODY * 0.23 # Thigh (9 to 11)
SEGMENT_LENGTHS[(R_HIP, R_KNEE)] = H_BODY * 0.23 # (10 to 12)
SEGMENT_LENGTHS[(L_KNEE, L_ANKLE)] = H_BODY * 0.23 # Shin (11 to 13)
SEGMENT_LENGTHS[(R_KNEE, R_ANKLE)] = H_BODY * 0.23 # (12 to 14)

# Fixed points (feet) - anchor of the skeleton
ANKLE_Y_POS = SCREEN_HEIGHT * 0.85 # Y-coordinate for the ankles (bottom of the figure)
ANKLE_X_OFFSET = SEGMENT_LENGTHS[(PELVIS_CENTER, L_HIP)] # Use hip width for ankle offset
initial_ankle_L = (SCREEN_WIDTH / 2 - ANKLE_X_OFFSET, ANKLE_Y_POS)
initial_ankle_R = (SCREEN_WIDTH / 2 + ANKLE_X_OFFSET, ANKLE_Y_POS)

# Maximum bowing angle (in radians)
MAX_BOW_ANGLE = math.radians(60) # 60 degrees forward bow

# Function to rotate a point around an origin
def rotate_point(point, origin, angle):
    ox, oy = origin
    px, py = point

    # Translate point back to origin
    translated_x, translated_y = px - ox, py - oy

    # Rotate point
    # Pygame's Y-axis increases downwards, so a positive angle (clockwise)
    # corresponds to a positive angle in a standard Cartesian system if Y were inverted.
    # For a "bowing" motion, we want to rotate forward, which is clockwise.
    rotated_x = translated_x * math.cos(angle) - translated_y * math.sin(angle)
    rotated_y = translated_x * math.sin(angle) + translated_y * math.cos(angle)

    # Translate point back to original position
    new_x, new_y = rotated_x + ox, rotated_y + oy
    return (new_x, new_y)

# Function to calculate all 15 point positions based on the current torso angle
def calculate_points(torso_angle):
    points = [None] * NUM_POINTS

    # 1. Fixed points (ankles)
    points[L_ANKLE] = initial_ankle_L
    points[R_ANKLE] = initial_ankle_R

    # 2. Legs (simplified: assume legs stay mostly straight and vertical for bowing)
    # Knees relative to ankles
    points[L_KNEE] = (points[L_ANKLE][0], points[L_ANKLE][1] - SEGMENT_LENGTHS[(L_KNEE, L_ANKLE)])
    points[R_KNEE] = (points[R_ANKLE][0], points[R_ANKLE][1] - SEGMENT_LENGTHS[(R_KNEE, R_ANKLE)])

    # Hips (L_HIP, R_HIP) relative to knees
    points[L_HIP] = (points[L_KNEE][0], points[L_KNEE][1] - SEGMENT_LENGTHS[(L_HIP, L_KNEE)])
    points[R_HIP] = (points[R_KNEE][0], points[R_KNEE][1] - SEGMENT_LENGTHS[(R_HIP, R_KNEE)])

    # 3. Main pivot for the upper body: midpoint of the hip joints (L_HIP, R_HIP).
    # Point 8 (PELVIS_CENTER) is defined at this pivot point.
    torso_pivot_x = (points[L_HIP][0] + points[R_HIP][0]) / 2
    torso_pivot_y = (points[L_HIP][1] + points[R_HIP][1]) / 2
    points[PELVIS_CENTER] = (torso_pivot_x, torso_pivot_y)

    # 4. Upper Body: Neck, Head, Shoulders, Arms
    # These points rotate around the PELVIS_CENTER (point 8).
    # Define their initial "standing" relative positions (Y is negative upwards from pivot)
    
    # Neck (1) relative to Pelvis (8)
    neck_standing_y_offset = -SEGMENT_LENGTHS[(PELVIS_CENTER, NECK)]
    points[NECK] = rotate_point(
        (points[PELVIS_CENTER][0], points[PELVIS_CENTER][1] + neck_standing_y_offset), # Standing position relative to pivot
        points[PELVIS_CENTER], # Pivot point
        torso_angle # Current torso angle
    )

    # Head (0) relative to Neck (1)
    # Head also rotates with the torso, with a small additional rotation for looking down
    head_standing_y_offset = -SEGMENT_LENGTHS[(NECK, HEAD)]
    head_additional_pitch = torso_angle * 0.1 # Small extra pitch down for head (e.g., 10% of torso angle)
    points[HEAD] = rotate_point(
        (points[NECK][0], points[NECK][1] + head_standing_y_offset), # Standing position relative to Neck
        points[NECK], # Pivot point
        torso_angle + head_additional_pitch # Total rotation for head
    )

    # Shoulders (2, 3) relative to Neck (1)
    # Shoulders rotate with the torso (same angle as neck)
    shoulder_l_standing_x_offset = -SEGMENT_LENGTHS[(NECK, L_SHOULDER)] # Left is negative X
    shoulder_r_standing_x_offset = SEGMENT_LENGTHS[(NECK, R_SHOULDER)] # Right is positive X
    shoulder_standing_y_offset = 0 # On the same Y level as neck base (initially)

    points[L_SHOULDER] = rotate_point(
        (points[NECK][0] + shoulder_l_standing_x_offset, points[NECK][1] + shoulder_standing_y_offset),
        points[NECK],
        torso_angle
    )
    points[R_SHOULDER] = rotate_point(
        (points[NECK][0] + shoulder_r_standing_x_offset, points[NECK][1] + shoulder_standing_y_offset),
        points[NECK],
        torso_angle
    )

    # Arms (Elbows and Wrists)
    # For a natural bow, arms usually hang loosely, oriented vertically downwards due to gravity.
    # This means their X coordinate remains the same as their parent (shoulder/elbow),
    # and their Y coordinate increases by the segment length (downwards).

    # Left Arm
    points[L_ELBOW] = (points[L_SHOULDER][0], points[L_SHOULDER][1] + SEGMENT_LENGTHS[(L_SHOULDER, L_ELBOW)])
    points[L_WRIST] = (points[L_ELBOW][0], points[L_ELBOW][1] + SEGMENT_LENGTHS[(L_ELBOW, L_WRIST)])

    # Right Arm
    points[R_ELBOW] = (points[R_SHOULDER][0], points[R_SHOULDER][1] + SEGMENT_LENGTHS[(R_SHOULDER, R_ELBOW)])
    points[R_WRIST] = (points[R_ELBOW][0], points[R_ELBOW][1] + SEGMENT_LENGTHS[(R_ELBOW, R_WRIST)])
    
    return points

# Main animation loop
running = True
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate current animation phase (0 to 1 over the total animation duration)
    phase = (frame_count % TOTAL_FRAMES) / TOTAL_FRAMES

    # Determine the current torso angle using an ease-in-out (cosine) function
    # The animation goes down then up.
    # Phase 0 to 0.5: bowing down (angle from 0 to MAX_BOW_ANGLE)
    # Phase 0.5 to 1.0: standing up (angle from MAX_BOW_ANGLE to 0)
    
    if phase <= 0.5:
        # Bowing down: normalize phase to 0-1 for the first half of the motion
        t_bow_down = phase * 2 
        # Cosine interpolation from 0 to 1, then scaled to MAX_BOW_ANGLE
        current_torso_angle = MAX_BOW_ANGLE * (0.5 - 0.5 * math.cos(t_bow_down * math.pi))
    else:
        # Standing up: normalize phase to 0-1 for the second half of the motion
        t_stand_up = (phase - 0.5) * 2
        # Cosine interpolation from 1 to 0, then scaled to MAX_BOW_ANGLE
        current_torso_angle = MAX_BOW_ANGLE * (0.5 + 0.5 * math.cos(t_stand_up * math.pi))

    # Calculate all point positions for the current frame
    current_points = calculate_points(current_torso_angle)

    # Drawing
    screen.fill(BLACK) # Clear the screen with black background

    # Draw each point
    for i in range(NUM_POINTS):
        x, y = int(current_points[i][0]), int(current_points[i][1])
        pygame.draw.circle(screen, WHITE, (x, y), POINT_RADIUS)

    pygame.display.flip() # Update the full display surface

    frame_count += 1
    clock.tick(FPS) # Control the animation speed

pygame.quit() # Uninitialize Pygame modules
