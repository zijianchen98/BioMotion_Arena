
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Turning Around")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# Human body point definitions (exactly 15 points)
# These are initial 3D coordinates relative to a central HIP_CENTER (0,0,0).
# Y is vertical (upwards), X is horizontal (right), Z is depth (into screen is positive).
# Values are normalized proportions, which will be scaled for screen display.
# The initial Z values are chosen to give the figure some depth,
# enhancing the visual effect of 3D rotation.
INITIAL_BODY_POINTS_3D = {
    'HEAD':          (0,   1.8, 0.05), # Top of head, slightly forward
    'NECK':          (0,   1.6, 0.05), # Base of neck/upper spine

    'R_SHOULDER':    (-0.25, 1.5, -0.05), # Right shoulder, slightly behind the central plane
    'L_SHOULDER':    (0.25, 1.5, -0.05), # Left shoulder

    'R_ELBOW':       (-0.35, 1.0, 0.05), # Right elbow, arm slightly bent forward
    'L_ELBOW':       (0.35, 1.0, 0.05), # Left elbow

    'R_WRIST':       (-0.4, 0.5, 0.1), # Right wrist, arm further forward
    'L_WRIST':       (0.4, 0.5, 0.1), # Left wrist

    'HIP_CENTER':    (0,   0,   0), # The central pivot point for the entire body's rotation
    
    'R_HIP':         (-0.15, 0,   -0.05), # Right hip joint, slightly behind
    'L_HIP':         (0.15,  0,   -0.05), # Left hip joint

    'R_KNEE':        (-0.15, -0.6, -0.02), # Right knee, slight natural bend
    'L_KNEE':        (0.15,  -0.6, -0.02), # Left knee

    'R_ANKLE':       (-0.15, -1.2, 0.05), # Right ankle, foot slightly forward
    'L_ANKLE':       (0.15,  -1.2, 0.05), # Left ankle
}

# Scaling and centering for display on the Pygame screen
SCALE_FACTOR = 150 # Adjust to control the size of the person on screen
SCREEN_CENTER_X = WIDTH // 2
SCREEN_CENTER_Y = HEIGHT // 2 + 100 # Shift slightly down to center the figure vertically on screen

# Animation parameters
FPS = 60 # Frames per second, for smooth motion
ANIMATION_DURATION_SECONDS = 4 # Time for one full 360-degree turn
TOTAL_FRAMES = ANIMATION_DURATION_SECONDS * FPS

# Function to rotate a 3D point around the Y-axis (vertical axis)
def rotate_y(point, angle):
    x, y, z = point
    # Apply rotation only to the x and z components (y remains unchanged)
    new_x = x * math.cos(angle) + z * math.sin(angle)
    new_z = -x * math.sin(angle) + z * math.cos(angle)
    return (new_x, y, new_z)

# Function to project a 3D point onto 2D screen coordinates
def project_to_2d(point_3d, scale, center_x, center_y):
    x_3d, y_3d, z_3d = point_3d
    
    # Scale and invert Y for Pygame coordinate system (Y increases downwards)
    screen_x = center_x + x_3d * scale
    screen_y = center_y - y_3d * scale # Invert Y for screen display

    return (int(screen_x), int(screen_y))

# Main animation loop
running = True
frame_count = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(BLACK) # Clear the screen with black background

    # Calculate current rotation angle for the main body.
    # It progresses smoothly from 0 to 2*PI (360 degrees) over TOTAL_FRAMES.
    current_angle = (frame_count / TOTAL_FRAMES) * (2 * math.pi)

    # Calculate and draw each of the 15 points
    for name, initial_pos in INITIAL_BODY_POINTS_3D.items():
        # Step 1: Apply the main body's 3D rotation to the point
        rotated_point = rotate_y(initial_pos, current_angle)
        
        final_x, final_y, final_z = rotated_point
        
        # Step 2: Apply subtle biomechanical adjustments for realism.
        # These are simple sinusoidal offsets to simulate non-rigid body movements,
        # such as head bob, arm swing, and slight leg shifts during a turn.
        
        # Head bob/sway: Small vertical and depth oscillation
        if name == 'HEAD':
            # Vertical bob, slightly offset phase
            final_y += 0.02 * math.sin(current_angle * 2 + math.pi/4) 
            # Depth sway (forward/back)
            final_z += 0.015 * math.cos(current_angle * 2) 

        # Arm swing: Arms swing slightly in the sagittal plane relative to the body
        # As the body turns (e.g., clockwise), the right arm swings slightly backward (-Z)
        # and the left arm swings slightly forward (+Z) for balance.
        arm_swing_magnitude = 0.07 # Max swing amplitude in Z-axis
        
        if name in ['R_ELBOW', 'R_WRIST']:
            # Right arm moves backward relative to torso during the first half of a clockwise turn
            # (i.e., its Z-coordinate decreases). `math.sin(current_angle)` is positive for 0 to pi.
            final_z -= arm_swing_magnitude * math.sin(current_angle) 
        elif name in ['L_ELBOW', 'L_WRIST']:
            # Left arm moves forward relative to torso during the first half of a clockwise turn
            # (i.e., its Z-coordinate increases).
            final_z += arm_swing_magnitude * math.sin(current_angle) 

        # Leg subtle weight shift/movement:
        # A person turning will often shift weight or make a small pivot/step.
        # This is shown as subtle lateral (X) and vertical (Y) shifts in leg points.
        leg_shift_magnitude_x = 0.015 # Max lateral shift
        leg_shift_magnitude_y = 0.01 # Max vertical shift
        
        # Phase for leg shifts, slightly faster and offset from main body turn
        leg_shift_phase_x = math.sin(current_angle * 1.5 + math.pi/4) 
        leg_shift_phase_y = math.cos(current_angle * 1.5 + math.pi/2) 
        
        if name in ['R_KNEE', 'R_ANKLE', 'R_HIP']:
            final_x += leg_shift_magnitude_x * leg_shift_phase_x
            final_y += leg_shift_magnitude_y * leg_shift_phase_y
        elif name in ['L_KNEE', 'L_ANKLE', 'L_HIP']:
            final_x -= leg_shift_magnitude_x * leg_shift_phase_x
            final_y -= leg_shift_magnitude_y * leg_shift_phase_y

        # Step 3: Project the final (adjusted) 3D point to 2D screen coordinates
        projected_pos = project_to_2d((final_x, final_y, final_z), SCALE_FACTOR, SCREEN_CENTER_X, SCREEN_CENTER_Y)
        
        # Draw the white point-light on the black background
        pygame.draw.circle(SCREEN, WHITE, projected_pos, POINT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen

    frame_count = (frame_count + 1) % TOTAL_FRAMES # Increment frame count, loop back after one full cycle
    clock.tick(FPS) # Control the animation speed

pygame.quit()
sys.exit()
