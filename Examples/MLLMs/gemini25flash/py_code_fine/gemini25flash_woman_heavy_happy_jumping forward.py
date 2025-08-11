
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DOT_RADIUS = 5

# Ground level for the character (Y-coordinate for the base of the feet when standing)
GROUND_LEVEL_Y = SCREEN_HEIGHT - 100

# Base X position for the character (will move forward from here)
BASE_X_START = SCREEN_WIDTH // 4

# Forward movement speed in pixels per frame
FORWARD_SPEED_PIXELS_PER_FRAME = 2.0 

# --- Joint Names (exactly 15 points) ---
# These names correspond to typical major joints used in biological motion studies.
JOINT_NAMES = [
    'head', 'neck',
    'r_shoulder', 'r_elbow', 'r_wrist',
    'l_shoulder', 'l_elbow', 'l_wrist',
    'hips_center',
    'r_hip', 'r_knee', 'r_ankle',
    'l_hip', 'l_knee', 'l_ankle'
]

# --- Keyframes ---
# Each keyframe defines the relative (x, y) coordinates for all 15 joints.
# The 'x' coordinate is relative to the character's horizontal center line.
# The 'y' coordinate is relative to GROUND_LEVEL_Y, where 0 means the point is at the ground,
# and negative values mean the point is above the ground.
# These values are designed to represent a "heavy woman jumping forward", focusing on biomechanical
# plausibility with a robust, but not overly high, jump and a noticeable landing.

KEYFRAMES = {
    "stand": {
        'r_ankle':   (15, 0),    'l_ankle':   (-15, 0), # Feet on ground
        'r_knee':    (15, -70),  'l_knee':    (-15, -70), # Knees straight
        'r_hip':     (15, -140), 'l_hip':     (-15, -140), # Hips position
        'hips_center': (0, -140), # Center of mass/hips reference
        'neck':      (0, -230),  'head':      (0, -250), # Head top at 250 units above ground
        'r_shoulder':(25, -210), 'l_shoulder':(-25, -210), # Shoulders
        'r_elbow':   (35, -160), 'l_elbow':   (-35, -160), # Elbows slightly bent
        'r_wrist':   (40, -110), 'l_wrist':   (-40, -110), # Wrists, arms hanging naturally
    },
    "crouch": {
        # Preparation for jump: body lowers, knees bend, arms swing back.
        'r_ankle':   (15, 0),    'l_ankle':   (-15, 0), # Feet remain on ground
        'r_knee':    (20, -40),  'l_knee':    (-20, -40), # Knees deeply bent, slightly forward
        'r_hip':     (15, -100), 'l_hip':     (-15, -100), # Hips lowered (40 units below standing)
        'hips_center': (0, -100), 
        'neck':      (5, -190),  'head':      (5, -210), # Body leans slightly forward
        'r_shoulder':(20, -170), 'l_shoulder':(-20, -170),
        'r_elbow':   (10, -130), 'l_elbow':   (-10, -130), # Arms swung back for momentum
        'r_wrist':   (0, -90),   'l_wrist':   (0, -90),
    },
    "push_off": {
        # Propelling upwards: legs extend, body straightens, arms swing forward/up.
        'r_ankle':   (10, -20),  'l_ankle':   (-10, -20), # Feet just lifting off ground
        'r_knee':    (10, -50),  'l_knee':    (-10, -50), # Legs rapidly extending
        'r_hip':     (15, -100), 'l_hip':     (-15, -100), 
        'hips_center': (0, -100), # Hips rising from crouch depth
        'neck':      (10, -230), 'head':      (10, -250), # Head rising back towards standing height
        'r_shoulder':(30, -220), 'l_shoulder':(-30, -220),
        'r_elbow':   (45, -170), 'l_elbow':   (-45, -170), # Arms swinging powerfully upwards
        'r_wrist':   (50, -120), 'l_wrist':   (-50, -120),
    },
    "apex": {
        # Peak of jump: body is airborne, legs slightly tucked, arms up for balance.
        'r_ankle':   (10, -100), 'l_ankle':   (-10, -100), # Feet at highest point, tucked
        'r_knee':    (20, -100), 'l_knee':    (-20, -100), # Knees bent for mid-air pose
        'r_hip':     (10, -150), 'l_hip':     (-10, -150),
        'hips_center': (0, -150), # Overall highest point for hips (10 units higher than standing)
        'neck':      (15, -250), 'head':      (15, -270), # Max height for head (270 units above ground)
        'r_shoulder':(35, -230), 'l_shoulder':(-35, -230),
        'r_elbow':   (50, -180), 'l_elbow':   (-50, -180),
        'r_wrist':   (55, -130), 'l_wrist':   (-55, -130), # Arms remain elevated
    },
    "land": {
        # Landing: feet impact ground, body lowers to absorb impact, arms move forward for balance.
        'r_ankle':   (15, 0),    'l_ankle':   (-15, 0), # Feet back on ground (Y=0)
        'r_knee':    (25, -30),  'l_knee':    (-25, -30), # Deep squat to absorb impact (Y-30)
        'r_hip':     (15, -90),  'l_hip':     (-15, -90),
        'hips_center': (0, -90), # Hips lowest point after impact (50 units below standing)
        'neck':      (5, -180),  'head':      (5, -200),
        'r_shoulder':(20, -160), 'l_shoulder':(-20, -160),
        'r_elbow':   (30, -100), 'l_elbow':   (-30, -100), # Arms swing forward for balance
        'r_wrist':   (35, -50),  'l_wrist':   (-35, -50),
    }
}

# --- Animation Control ---
# Defines the sequence of poses and how long each transition/hold lasts in frames.
ANIMATION_SEQUENCE = [
    ("stand", 30),        # Initial standing phase
    ("crouch", 30),       # Transition to crouch (preparation)
    ("push_off", 30),     # Transition to push-off (propulsion)
    ("apex", 40),         # Hold at apex of jump
    ("land", 30),         # Transition to landing pose (impact absorption)
    ("stand", 30)         # Recover back to standing (transition)
]

TOTAL_ANIMATION_FRAMES = sum(duration for _, duration in ANIMATION_SEQUENCE)

# --- Helper Functions ---

def interpolate_points(pose1, pose2, t):
    """
    Linearly interpolates between two poses.
    't' is the interpolation factor, from 0.0 (pose1) to 1.0 (pose2).
    """
    interpolated_pose = {}
    for joint in JOINT_NAMES:
        x1, y1 = pose1[joint]
        x2, y2 = pose2[joint]
        interp_x = x1 * (1 - t) + x2 * t
        interp_y = y1 * (1 - t) + y2 * t
        interpolated_pose[joint] = (interp_x, interp_y)
    return interpolated_pose

def ease_in_out_quad(t):
    """
    Quadratic easing function for smooth transitions (slow-fast-slow).
    't' goes from 0.0 to 1.0.
    """
    return 2 * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 2) / 2

def get_current_pose(frame_num):
    """
    Determines the current interpolated pose based on the animation sequence and current frame number.
    """
    current_time_in_cycle = frame_num % TOTAL_ANIMATION_FRAMES
    
    accumulated_frames = 0
    for i, (pose_name, duration) in enumerate(ANIMATION_SEQUENCE):
        if accumulated_frames <= current_time_in_cycle < accumulated_frames + duration:
            # Calculate 't' (0.0 to 1.0) within the current phase
            t_in_phase = (current_time_in_cycle - accumulated_frames) / duration
            
            current_target_pose = KEYFRAMES[pose_name]
            
            # Determine the previous pose for interpolation.
            # If at the very start of the sequence, interpolate from the last pose of the previous cycle.
            if i == 0:
                # If the first phase is 'stand', and we loop, the previous 'stand' is itself, or the last of the full cycle.
                # Here, we treat 'stand' as the initial and final point of the cycle.
                previous_pose_name, _ = ANIMATION_SEQUENCE[-1] # Last phase of previous cycle
            else:
                previous_pose_name, _ = ANIMATION_SEQUENCE[i-1]
            previous_pose = KEYFRAMES[previous_pose_name]

            # Apply easing for smoother transitions
            eased_t = ease_in_out_quad(t_in_phase)
            return interpolate_points(previous_pose, current_target_pose, eased_t)
        accumulated_frames += duration

    # Fallback to the initial stand pose if logic error occurs (should not happen with modulo)
    return KEYFRAMES["stand"]

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Jumping Forward")
clock = pygame.time.Clock()

# --- Main Animation Loop ---
current_frame_idx = 0
char_global_x_offset = 0 # Character's overall X offset from BASE_X_START
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update frame index for animation cycle
    current_frame_idx += 1
    
    # Get the current interpolated pose data (relative x, y coordinates for each joint)
    current_pose_data = get_current_pose(current_frame_idx)
    
    # Update character's global X position for forward movement
    char_global_x_offset += FORWARD_SPEED_PIXELS_PER_FRAME

    # Loop the character's horizontal movement when it goes off screen to the right.
    # Reset it to appear from the left side, maintaining a continuous animation.
    # The 'SCREEN_WIDTH + 100' ensures the entire character leaves the screen before reset.
    if BASE_X_START + char_global_x_offset > SCREEN_WIDTH + 100: 
        char_global_x_offset = -SCREEN_WIDTH // 2 # Reset to left of screen

    # Clear the screen with a black background
    screen.fill(BLACK) 

    # Draw each point-light for the current pose
    for joint_name in JOINT_NAMES:
        rel_x, rel_y = current_pose_data[joint_name]
        
        # Calculate absolute screen coordinates for the point
        # Add BASE_X_START for initial position, char_global_x_offset for continuous forward movement
        # Add GROUND_LEVEL_Y for vertical positioning based on ground, then add relative Y from keyframe
        absolute_x = int(BASE_X_START + char_global_x_offset + rel_x)
        absolute_y = int(GROUND_LEVEL_Y + rel_y) # rel_y is negative for points above ground

        # Draw the white point-light (circle)
        pygame.draw.circle(screen, WHITE, (absolute_x, absolute_y), DOT_RADIUS)

    # Update the full display surface
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame when the loop ends
pygame.quit()
