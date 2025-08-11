
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Forward Rolling")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point radius
POINT_RADIUS = 5

# Initial relative positions for 15 points (approximate based on a standing human skeleton)
# (x, y) where positive y is up, positive x is right relative to the PELVIS (index 8).
# The PELVIS (0,0) serves as the body's local origin.
initial_points_relative = [
    (0, 80),   # 0 Head
    (-15, 60), # 1 Shoulder L
    (15, 60),  # 2 Shoulder R
    (-25, 40), # 3 Elbow L
    (25, 40),  # 4 Elbow R
    (-30, 20), # 5 Wrist L
    (30, 20),  # 6 Wrist R
    (0, 50),   # 7 Upper Torso (Chest)
    (0, 0),    # 8 Lower Torso (Pelvis) - Local origin
    (-10, -10),# 9 Hip L
    (10, -10), # 10 Hip R
    (-15, -40),# 11 Knee L
    (15, -40), # 12 Knee R
    (-15, -70),# 13 Ankle L
    (15, -70)  # 14 Ankle R
]

# Mapping point indices for easier access and readability
HEAD = 0
SHOULDER_L, SHOULDER_R = 1, 2
ELBOW_L, ELBOW_R = 3, 4
WRIST_L, WRIST_R = 5, 6
CHEST = 7
PELVIS = 8
HIP_L, HIP_R = 9, 10
KNEE_L, KNEE_R = 11, 12
ANKLE_L, ANKLE_R = 13, 14


# Parameters for animation
FPS = 60
animation_speed = 0.05  # Radians per frame, controls speed of roll (smaller = slower)
roll_radius_estimate = 40  # Estimated effective radius of the body when curled for rolling
# Horizontal distance covered per full roll cycle. Adjust for desired ground coverage.
total_horizontal_distance_per_cycle = 2 * math.pi * roll_radius_estimate * 1.5 

# Global body properties for screen placement and movement
body_initial_x_screen = WIDTH // 4  # Starting X position of the pelvis on screen
pelvis_avg_y_screen = HEIGHT - 100  # Average Y position of the pelvis on screen (screen coordinates)
vertical_dip_amplitude = 50  # How much the pelvis dips below its average height during the roll

# Animation state variables
current_roll_angle = 0.0  # Accumulative angle of the entire body's rotation (radians)

# Game loop control
running = True
clock = pygame.time.Clock()

def rotate_point(x, y, angle):
    """Rotates a point (x, y) around the origin by 'angle' radians."""
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    new_x = x * cos_angle - y * sin_angle
    new_y = x * sin_angle + y * cos_angle
    return new_x, new_y

def apply_curl(initial_points, curl_factor):
    """
    Applies a curling transformation to limb points based on a curl_factor.
    Returns a NEW list of points, not modifying the original `initial_points`.
    curl_factor: 0 (no curl/fully extended) to 1 (max curl/fully tucked).
    The 'sad' and 'heavy' aspects are subtly implied by relatively compact and lower movements.
    """
    curled_points = [list(p) for p in initial_points] # Create a mutable copy

    # Head tucks towards chest
    head_orig = initial_points[HEAD]
    chest_orig = initial_points[CHEST]
    dx_head = head_orig[0] - chest_orig[0]
    dy_head = head_orig[1] - chest_orig[1]
    curled_points[HEAD][0] = chest_orig[0] + dx_head * (1 - curl_factor * 0.5)
    curled_points[HEAD][1] = chest_orig[1] + dy_head * (1 - curl_factor * 0.6)

    # Arms tuck in (Elbows and Wrists)
    for arm_side in [("L", SHOULDER_L, ELBOW_L, WRIST_L), ("R", SHOULDER_R, ELBOW_R, WRIST_R)]:
        _, shoulder_idx, elbow_idx, wrist_idx = arm_side
        
        shoulder_orig = initial_points[shoulder_idx]
        elbow_orig = initial_points[elbow_idx]
        wrist_orig = initial_points[wrist_idx]

        # Elbow relative to Shoulder
        dx_elbow = elbow_orig[0] - shoulder_orig[0]
        dy_elbow = elbow_orig[1] - shoulder_orig[1]
        curled_points[elbow_idx][0] = shoulder_orig[0] + dx_elbow * (1 - curl_factor * 0.7)
        curled_points[elbow_idx][1] = shoulder_orig[1] + dy_elbow * (1 - curl_factor * 0.7) + 15 * curl_factor # Bend arm upwards
        
        # Wrist relative to (initial) Elbow point, then shifted by current elbow position
        dx_wrist = wrist_orig[0] - elbow_orig[0] 
        dy_wrist = wrist_orig[1] - elbow_orig[1]
        curled_points[wrist_idx][0] = curled_points[elbow_idx][0] + dx_wrist * (1 - curl_factor * 0.8)
        curled_points[wrist_idx][1] = curled_points[elbow_idx][1] + dy_wrist * (1 - curl_factor * 0.8) + 20 * curl_factor

    # Legs tuck in (Knees and Ankles)
    for leg_side in [("L", HIP_L, KNEE_L, ANKLE_L), ("R", HIP_R, KNEE_R, ANKLE_R)]:
        _, hip_idx, knee_idx, ankle_idx = leg_side

        hip_orig = initial_points[hip_idx]
        knee_orig = initial_points[knee_idx]
        ankle_orig = initial_points[ankle_idx]

        # Knee relative to Hip
        dx_knee = knee_orig[0] - hip_orig[0]
        dy_knee = knee_orig[1] - hip_orig[1]
        curled_points[knee_idx][0] = hip_orig[0] + dx_knee * (1 - curl_factor * 0.7)
        curled_points[knee_idx][1] = hip_orig[1] + dy_knee * (1 - curl_factor * 0.7) - 20 * curl_factor # Bend leg upwards (less negative Y)

        # Ankle relative to (initial) Knee point, then shifted by current knee position
        dx_ankle = ankle_orig[0] - knee_orig[0]
        dy_ankle = ankle_orig[1] - knee_orig[1]
        curled_points[ankle_idx][0] = curled_points[knee_idx][0] + dx_ankle * (1 - curl_factor * 0.8)
        curled_points[ankle_idx][1] = curled_points[knee_idx][1] + dy_ankle * (1 - curl_factor * 0.8) - 15 * curl_factor

    return curled_points

# Main animation loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update animation state
    current_roll_angle += animation_speed
    
    # Normalize roll angle to [0, 1] for one cycle (2*PI radians) to control curl and vertical dip
    roll_angle_normalized = (current_roll_angle % (2 * math.pi)) / (2 * math.pi)

    # Horizontal translation (continuous progress for continuous roll)
    # The person moves horizontally based on total accumulated angle.
    horizontal_offset_total = (current_roll_angle / (2 * math.pi)) * total_horizontal_distance_per_cycle
    
    # Vertical movement (pelvis dips and rises during the roll)
    # Uses a cosine wave: 0 at 0 and 2PI radians (start/end of cycle), max_dip at PI radians (middle of cycle).
    # This means the pelvis is highest at the start/end of the roll cycle, and lowest (dips) in the middle.
    pelvis_vertical_offset = vertical_dip_amplitude * (0.5 - 0.5 * math.cos(roll_angle_normalized * 2 * math.pi))
    
    # Calculate global Y position of the pelvis: average Y + vertical offset (offset is positive for downward movement)
    current_pelvis_y_screen = pelvis_avg_y_screen + pelvis_vertical_offset

    # Calculate curl factor for limbs (0 to 1 and back to 0 over the 2*PI cycle)
    # The body tucks in, stays tucked, then extends, mimicking a forward roll.
    # Stages: 0 to 0.25 (tuck in), 0.25 to 0.75 (stay tucked), 0.75 to 1.0 (uncurl)
    tuck_in_end_normalized = 0.25 
    stay_tucked_end_normalized = 0.75 

    current_curl_factor = 0.0
    if roll_angle_normalized <= tuck_in_end_normalized:
        current_curl_factor = roll_angle_normalized / tuck_in_end_normalized
    elif roll_angle_normalized <= stay_tucked_end_normalized:
        current_curl_factor = 1.0
    else: 
        current_curl_factor = 1.0 - (roll_angle_normalized - stay_tucked_end_normalized) / (1.0 - stay_tucked_end_normalized)

    # Apply a smoothstep function for smoother transitions of the curl factor
    current_curl_factor = max(0.0, min(1.0, current_curl_factor)) 
    current_curl_factor = current_curl_factor * current_curl_factor * (3 - 2 * current_curl_factor)

    # Get the points' relative positions after applying the curling transformation
    curled_relative_points = apply_curl(initial_points_relative, current_curl_factor)

    # Calculate and draw absolute screen positions for each point
    for i, (rel_x, rel_y) in enumerate(curled_relative_points):
        # Step 1: Rotate the point around the body's local origin (pelvis at (0,0) in relative coords)
        rotated_x, rotated_y = rotate_point(rel_x, rel_y, current_roll_angle)
        
        # Step 2: Translate to global screen coordinates
        # X-coordinate: Add initial X + total horizontal offset + rotated_x. Then wrap around screen.
        # Y-coordinate: Add current global pelvis Y - rotated_y (because Pygame's Y-axis is inverted).
        abs_x = int((body_initial_x_screen + horizontal_offset_total + rotated_x) % WIDTH)
        abs_y = int(current_pelvis_y_screen - rotated_y) 

        # Draw the point-light
        pygame.draw.circle(screen, WHITE, (abs_x, abs_y), POINT_RADIUS)

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
