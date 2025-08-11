
import pygame
import math

# --- Pygame Setup ---
SCREEN_WIDTH = 1000  # Width of the display window
SCREEN_HEIGHT = 700  # Height of the display window
FPS = 60             # Frames per second
POINT_RADIUS = 5     # Radius of each white point-light
WHITE = (255, 255, 255) # Color of the point-lights
BLACK = (0, 0, 0)       # Background color

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Forward Roll Stimulus")
clock = pygame.time.Clock()

# --- Body Parameters (relative units, will be scaled to pixels) ---
SCALE = 180  # Conversion factor from relative units to pixels. Adjust to change figure size.
# Y-coordinate for the body's center of rotation (mid-hip). Placed lower to allow full roll.
BODY_CENTER_Y = SCREEN_HEIGHT * 0.6 

# Segment lengths (in relative units, proportions based on common human ratios)
# These define the 'bone' lengths of the stick figure.
LEN_HEAD_NECK = 0.08
LEN_NECK_SHOULDER = 0.05 
LEN_UPPER_ARM = 0.20
LEN_LOWER_ARM = 0.20
LEN_TORSO_VERTICAL = 0.25 # Vertical distance from hip line to shoulder line
LEN_UPPER_LEG = 0.30
LEN_LOWER_LEG = 0.25
LEN_FOOT = 0.08

# Widths (half-widths for Left/Right separation of points)
HALF_SHOULDER_WIDTH = 0.18
HALF_HIP_WIDTH = 0.12

# --- Animation Parameters ---
roll_speed = 0.08  # Radians per frame for global rotation. Higher value means faster roll.
current_roll_angle = 0.0 # Global rotation angle of the entire body
current_body_x = SCREEN_WIDTH * 0.1 # Starting X position of the body's center

# --- Define initial and tucked joint angles (in radians) ---
# These define the range of motion for each joint.
# Angles are relative to parent segment, or a fixed axis (e.g., vertical for hip).

# Hip angle: relative to vertical (0=straight down). Positive bends leg forward/up.
# Initial pose: Slightly bent forward, ready to roll.
INITIAL_HIP_ANGLE = math.radians(10)   
# Tucked pose: Legs pulled up high towards the chest.
TUCKED_HIP_ANGLE = math.radians(130)   

# Knee angle: relative to upper leg (0=straight). Positive bends knee back.
INITIAL_KNEE_ANGLE = math.radians(10)  # Slightly bent
TUCKED_KNEE_ANGLE = math.radians(160)  # Deeply bent for a compact shape

# Shoulder arm angle: relative to horizontal from shoulder (0=straight out, pi/2=straight down).
# For tucking, arms move forward and wrap around the body.
INITIAL_SHOULDER_ARM_ANGLE = math.radians(90) # Arms hanging straight down
TUCKED_SHOULDER_ARM_ANGLE = math.radians(20)  # Arms moved forward and slightly up/out to wrap

# Elbow angle: relative to upper arm (0=straight). Positive bends elbow.
INITIAL_ELBOW_ANGLE = math.radians(0)    # Arms straight
TUCKED_ELBOW_ANGLE = math.radians(150)   # Elbows deeply bent

# Head vertical offset from neck/shoulder base. This controls how much the head 'tucks in'.
# Positive offset means head is higher relative to shoulder line.
INITIAL_HEAD_VERTICAL_OFFSET = LEN_HEAD_NECK + LEN_NECK_SHOULDER # Standard head height
TUCKED_HEAD_VERTICAL_OFFSET = LEN_NECK_SHOULDER / 2 # Head comes down significantly closer to torso

def interpolate(val1, val2, factor):
    """Linear interpolation between two values."""
    return val1 + (val2 - val1) * factor

def get_body_points(tuck_amount, roll_angle):
    """
    Calculates the 15 body points for the current frame in a local coordinate system
    where the body's center of rotation (mid-hip) is (0,0).

    Args:
        tuck_amount (float): How tucked the body is (0 = initial pose, 1 = fully tucked pose).
        roll_angle (float): The global rotation angle of the entire body (in radians).

    Returns:
        list: A list of (x, y) tuples representing the 15 body points in relative coordinates.
    """
    points = [None] * 15 # Initialize list to hold (x, y) coordinates for each point

    # Interpolate joint angles and head offset based on the current tuck_amount
    hip_angle = interpolate(INITIAL_HIP_ANGLE, TUCKED_HIP_ANGLE, tuck_amount)
    knee_angle = interpolate(INITIAL_KNEE_ANGLE, TUCKED_KNEE_ANGLE, tuck_amount)
    shoulder_arm_angle = interpolate(INITIAL_SHOULDER_ARM_ANGLE, TUCKED_SHOULDER_ARM_ANGLE, tuck_amount)
    elbow_angle = interpolate(INITIAL_ELBOW_ANGLE, TUCKED_ELBOW_ANGLE, tuck_amount)
    head_vertical_offset = interpolate(INITIAL_HEAD_VERTICAL_OFFSET, TUCKED_HEAD_VERTICAL_OFFSET, tuck_amount)

    # --- Calculate relative positions of joints from the body's central origin (mid-hip) ---
    # The origin for rotation is considered the mid-hip point (0,0) in the local system.
    origin_x, origin_y = 0, 0

    # 7: Left Hip, 8: Right Hip
    points[7] = (origin_x - HALF_HIP_WIDTH, origin_y) 
    points[8] = (origin_x + HALF_HIP_WIDTH, origin_y) 
    lh_x, lh_y = points[7]
    rh_x, rh_y = points[8]

    # 1: Left Shoulder, 2: Right Shoulder (relative to hip line, upwards)
    points[1] = (origin_x - HALF_SHOULDER_WIDTH, origin_y + LEN_TORSO_VERTICAL) 
    points[2] = (origin_x + HALF_SHOULDER_WIDTH, origin_y + LEN_TORSO_VERTICAL) 
    ls_x, ls_y = points[1]
    rs_x, rs_y = points[2]

    # 0: Head (relative to midpoint of shoulders, adjusted for tucking)
    head_base_x = origin_x
    head_base_y = origin_y + LEN_TORSO_VERTICAL # Y-coordinate of shoulder line (mid-shoulder)
    points[0] = (head_base_x, head_base_y + head_vertical_offset) 

    # Legs (angles are relative to vertical, 0=down, positive=forward/up)
    # Left Leg (9: Knee, 11: Ankle, 13: Foot)
    lk_x = lh_x + LEN_UPPER_LEG * math.sin(hip_angle)
    lk_y = lh_y - LEN_UPPER_LEG * math.cos(hip_angle)
    points[9] = (lk_x, lk_y) 

    la_x = lk_x + LEN_LOWER_LEG * math.sin(hip_angle + knee_angle)
    la_y = lk_y - LEN_LOWER_LEG * math.cos(hip_angle + knee_angle)
    points[11] = (la_x, la_y) 

    # Adding a slight foot angle for a more natural look during tucking
    lf_x = la_x + LEN_FOOT * math.sin(hip_angle + knee_angle + math.radians(20)) 
    lf_y = la_y - LEN_FOOT * math.cos(hip_angle + knee_angle + math.radians(20))
    points[13] = (lf_x, lf_y) 

    # Right Leg (mirror of left) (10: Knee, 12: Ankle, 14: Foot)
    rk_x = rh_x - LEN_UPPER_LEG * math.sin(hip_angle) 
    rk_y = rh_y - LEN_UPPER_LEG * math.cos(hip_angle)
    points[10] = (rk_x, rk_y) 

    ra_x = rk_x - LEN_LOWER_LEG * math.sin(hip_angle + knee_angle)
    ra_y = rk_y - LEN_LOWER_LEG * math.cos(hip_angle + knee_angle)
    points[12] = (ra_x, ra_y) 

    rf_x = ra_x - LEN_FOOT * math.sin(hip_angle + knee_angle + math.radians(20))
    rf_y = ra_y - LEN_FOOT * math.cos(hip_angle + knee_angle + math.radians(20))
    points[14] = (rf_x, rf_y) 

    # Arms (angles are relative to horizontal from shoulder, 0=straight out, positive=down/forward)
    # Left Arm (3: Elbow, 5: Wrist)
    le_x = ls_x + LEN_UPPER_ARM * math.cos(shoulder_arm_angle)
    le_y = ls_y + LEN_UPPER_ARM * math.sin(shoulder_arm_angle)
    points[3] = (le_x, le_y) 

    lw_x = le_x + LEN_LOWER_ARM * math.cos(shoulder_arm_angle + elbow_angle)
    lw_y = le_y + LEN_LOWER_ARM * math.sin(shoulder_arm_angle + elbow_angle)
    points[5] = (lw_x, lw_y) 

    # Right Arm (mirror of left, assuming symmetric arm movement for tucking)
    # (4: Elbow, 6: Wrist)
    re_x = rs_x - LEN_UPPER_ARM * math.cos(shoulder_arm_angle) 
    re_y = rs_y + LEN_UPPER_ARM * math.sin(shoulder_arm_angle)
    points[4] = (re_x, re_y) 

    rw_x = re_x - LEN_LOWER_ARM * math.cos(shoulder_arm_angle + elbow_angle)
    rw_y = re_y + LEN_LOWER_ARM * math.sin(shoulder_arm_angle + elbow_angle)
    points[6] = (rw_x, rw_y) 

    # Apply global rotation to all points around the body's origin (0,0)
    rotated_points = []
    for px, py in points:
        rotated_px = px * math.cos(roll_angle) - py * math.sin(roll_angle)
        rotated_py = px * math.sin(roll_angle) + py * math.cos(roll_angle)
        rotated_points.append((rotated_px, rotated_py))
    
    return rotated_points

# --- Main Animation Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen for next frame
    screen.fill(BLACK)

    # --- Update animation state ---
    # Continuously increase the global rotation angle
    current_roll_angle += roll_speed 
    
    # Calculate horizontal speed based on the roll speed for natural-looking movement.
    # This tries to approximate the horizontal distance covered per rotation.
    roll_circumference_factor = 0.5 # A factor representing effective radius of tucked body
    horizontal_speed = roll_speed * roll_circumference_factor * SCALE / (2 * math.pi) * 2 # Adjusted for natural feel
    current_body_x += horizontal_speed
    
    # Reset body position to the left side once it moves off the right side of the screen
    if current_body_x > SCREEN_WIDTH + SCALE * 2: 
        current_body_x = -SCALE * 2 

    # Calculate tuck_amount based on global rotation phase.
    # For a continuous forward roll, the body generally stays quite compact.
    # This uses a sine wave to create subtle variations in tucking, making it more dynamic.
    # `abs(math.sin(current_roll_angle))` provides a value that is 0 when upright/inverted,
    # and 1 when on its side, simulating a slight compression and expansion.
    base_tuck = 0.85 # The body is generally 85% tucked
    tuck_variation = 0.15 # Max variation is 15% (e.g., from 85% to 100% tuck)
    dynamic_tuck_factor = abs(math.sin(current_roll_angle)) 
    tuck_amount = base_tuck + tuck_variation * dynamic_tuck_factor

    # Get the calculated (rotated) positions of the 15 points in relative coordinates
    relative_points = get_body_points(tuck_amount, current_roll_angle)

    # --- Draw points ---
    for i, (rx, ry) in enumerate(relative_points):
        # Scale the relative coordinates and translate them to screen coordinates
        screen_x = int(rx * SCALE + current_body_x)
        screen_y = int(ry * SCALE + BODY_CENTER_Y)
        
        # Draw each point as a white circle
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), POINT_RADIUS)

    # Update the full display surface to the screen
    pygame.display.flip()

    # Cap the frame rate to ensure consistent animation speed
    clock.tick(FPS)

# Quit Pygame when the loop finishes
pygame.quit()
