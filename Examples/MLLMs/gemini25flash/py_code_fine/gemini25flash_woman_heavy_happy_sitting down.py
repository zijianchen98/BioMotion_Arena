
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Dot properties
DOT_RADIUS = 5

# Animation parameters
FPS = 30
ANIMATION_DURATION_SECONDS = 3  # Time for one full sit-down or stand-up action
TOTAL_FRAMES = FPS * ANIMATION_DURATION_SECONDS

# Define joint names for the 15-point model
# This configuration allows for realistic human motion representation
JOINT_NAMES = [
    'head', 'neck',
    'shoulder_l', 'shoulder_r',
    'elbow_l', 'elbow_r',
    'wrist_l', 'wrist_r',
    'pelvis',  # Central point for the base of the spine/hips
    'hip_l', 'hip_r',
    'knee_l', 'knee_r',
    'ankle_l', 'ankle_r'
]

# Define the "standing" pose (initial pose) with relative coordinates.
# The origin (0,0) is set near the pelvis for easier calculation of body parts.
# Y-coordinates are positive upwards from the pelvis, then inverted for Pygame.
# Proportions are set to represent a human figure.
BASE_POSE = {
    'head':       (0,   180),  # Top of head
    'neck':       (0,   150),  # Base of neck
    'shoulder_l': (-40, 140),  # Left shoulder joint
    'shoulder_r': (40,  140),  # Right shoulder joint
    'elbow_l':    (-50, 80),   # Left elbow joint
    'elbow_r':    (50,  80),   # Right elbow joint
    'wrist_l':    (-60, 20),   # Left wrist joint
    'wrist_r':    (60,  20),   # Right wrist joint
    'pelvis':     (0,   0),    # Central pelvis/hip area (reference)
    'hip_l':      (-28, -10),  # Left hip joint (slightly wider for 'heavy weight')
    'hip_r':      (28,  -10),  # Right hip joint
    'knee_l':     (-28, -90),  # Left knee joint
    'knee_r':     (28,  -90),  # Right knee joint
    'ankle_l':    (-28, -170), # Left ankle joint
    'ankle_r':    (28,  -170)  # Right ankle joint
}

# Define the "seated" pose (target pose) with relative coordinates.
# Adjustments simulate sitting down action: pelvis lowers, knees bend, torso leans.
SEATED_POSE = {
    'head':       (0,   110),  # Head lowers
    'neck':       (0,   80),   # Neck lowers
    'shoulder_l': (-40, 70),   # Shoulders lower
    'shoulder_r': (40,  70),
    'elbow_l':    (-50, 20),   # Elbows lower
    'elbow_r':    (50,  20),
    'wrist_l':    (-60, -30),  # Wrists lower (arms hang more)
    'wrist_r':    (60,  -30),
    'pelvis':     (-15, -100), # Pelvis moves down and slightly back
    'hip_l':      (-40, -110), # Hips spread more when seated
    'hip_r':      (40,  -110),
    'knee_l':     (-70, -120), # Knees move forward
    'knee_r':     (70,  -120),
    'ankle_l':    (-70, -160), # Ankles adjust
    'ankle_r':    (70,  -160)
}

# Scaling and translation for screen coordinates
# SCALE can be adjusted to make the person larger/smaller
SCALE = 1.0
# OFFSET_X centers the person horizontally
OFFSET_X = SCREEN_WIDTH // 2
# OFFSET_Y places the person's 'pelvis' at this Y coordinate on screen (feet towards bottom)
OFFSET_Y = SCREEN_HEIGHT * 0.7

def get_screen_coords(relative_x, relative_y):
    """Converts relative joint coordinates to Pygame screen coordinates."""
    # Invert Y-axis to match Pygame's top-left origin (Y increases downwards)
    return int(relative_x * SCALE + OFFSET_X), int(-relative_y * SCALE + OFFSET_Y)

# Animation loop variables
current_frame = 0
direction = 1  # 1 for sitting down, -1 for standing up
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate raw animation progress (0 to 1)
    t_raw = current_frame / TOTAL_FRAMES
    
    # Easing function for smoother, more natural motion (cubic ease-in-out)
    # This makes the movement start slow, speed up, and slow down at the end.
    t_eased = t_raw * t_raw * (3 - 2 * t_raw)
    
    # Calculate current joint positions using interpolation
    current_joints = {}
    
    # Biomechanical refinement: Add a slight forward lean to the torso
    # during the middle of the sitting/standing motion for balance.
    # The lean_x_offset uses a sine wave for smooth in-out effect.
    lean_amount = 15 # Max horizontal shift for lean, in relative units
    lean_x_offset = lean_amount * math.sin(t_eased * math.pi)

    for joint_name in JOINT_NAMES:
        start_x, start_y = BASE_POSE[joint_name]
        end_x, end_y = SEATED_POSE[joint_name]

        interp_x = 0
        interp_y = 0
        
        if direction == 1: # Sitting down (interpolating from BASE_POSE to SEATED_POSE)
            interp_x = start_x + (end_x - start_x) * t_eased
            interp_y = start_y + (end_y - start_y) * t_eased
            
            # Apply forward lean to upper body parts (moves right, or 'forward' from side view)
            if joint_name in ['head', 'neck', 'shoulder_l', 'shoulder_r', 'pelvis']:
                interp_x += lean_x_offset 
        else: # Standing up (interpolating from SEATED_POSE to BASE_POSE)
            interp_x = end_x + (start_x - end_x) * t_eased
            interp_y = end_y + (start_y - end_y) * t_eased

            # Apply forward lean to upper body parts (moves left, or 'forward' from side view, then straightens)
            if joint_name in ['head', 'neck', 'shoulder_l', 'shoulder_r', 'pelvis']:
                interp_x -= lean_x_offset 

        current_joints[joint_name] = get_screen_coords(interp_x, interp_y)
    
    # Update frame counter and manage animation direction
    current_frame += direction

    # Reverse direction if animation reaches ends
    if current_frame >= TOTAL_FRAMES and direction == 1:
        direction = -1 # Finished sitting, now stand up
        current_frame = TOTAL_FRAMES # Ensure it starts from the end
    elif current_frame <= 0 and direction == -1:
        direction = 1 # Finished standing, now sit down
        current_frame = 0 # Ensure it starts from the beginning

    # Drawing
    screen.fill(BLACK) # Solid black background

    # Draw each joint as a white point-light
    for joint_name in JOINT_NAMES:
        x, y = current_joints[joint_name]
        pygame.draw.circle(screen, WHITE, (x, y), DOT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen

    clock.tick(FPS) # Control frame rate

pygame.quit()
sys.exit()
