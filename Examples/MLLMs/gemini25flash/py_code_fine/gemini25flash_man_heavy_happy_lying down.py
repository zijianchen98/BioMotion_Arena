
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800  # Taller to accommodate the vertical human figure
SCREEN_CENTER_OFFSET = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point stimulus properties
POINT_RADIUS = 5  # Size of the white dots
FPS = 60          # Frames per second for smooth animation

# Define the 15 body points relative to a central origin (0,0) for the figure.
# This setup represents a person lying on their back (supine position),
# with their head at the top of the screen and feet at the bottom, performing a bench press.
# All coordinates are in pixels relative to the figure's central origin.

# 11 Fixed points (relative to MID_TORSO, which is considered at (0,0))
POINTS_DEFINITION = {
    'HEAD': (0, -180),      # Top of the head
    'SHOULDER_L': (-50, -100),  # Left shoulder joint
    'SHOULDER_R': (50, -100),   # Right shoulder joint
    'MID_TORSO': (0, 0),    # Center chest/upper abdomen (approximate sternum)
    'PELVIS': (0, 60),      # Center pelvis area (approximate sacrum)
    'HIP_L': (-40, 60),     # Left hip joint (same Y as pelvis)
    'HIP_R': (40, 60),      # Right hip joint (same Y as pelvis)
    'KNEE_L': (-60, 120),   # Left knee joint (legs bent for a stable base during press)
    'KNEE_R': (60, 120),    # Right knee joint
    'ANKLE_L': (-40, 160),  # Left ankle (foot flat on the ground)
    'ANKLE_R': (40, 160)    # Right ankle
}

# 4 Animated points (arms for the bench press motion)
# These coordinates are relative to their respective shoulder point (SHOULDER_L or SHOULDER_R).
# They define the 'UP' (arms extended) and 'DOWN' (arms at chest) poses.
ARM_POSES = {
    'UP': { # Arms fully extended upwards (simulating the top of the weight press)
        'ELBOW_L': (-10, -80),  # L-elbow: slightly out, far up from L-shoulder
        'WRIST_L': (-15, -150), # L-wrist: further up from L-elbow
        'ELBOW_R': (10, -80),   # R-elbow: slightly out, far up from R-shoulder
        'WRIST_R': (15, -150)   # R-wrist: further up from R-elbow
    },
    'DOWN': { # Arms at the bottom of the press (simulating weight at chest level)
        'ELBOW_L': (-70, -20), # L-elbow: far out, slightly down from L-shoulder
        'WRIST_L': (-50, -10), # L-wrist: somewhat in, slightly down from L-shoulder (near chest)
        'ELBOW_R': (70, -20),  # R-elbow: far out, slightly down from R-shoulder
        'WRIST_R': (50, -10)   # R-wrist: somewhat in, slightly down from R-shoulder (near chest)
    }
}

# Mapping for animated arm points to their respective shoulder anchors
ANIMATED_POINTS_MAPPING = {
    'ELBOW_L': 'SHOULDER_L',
    'WRIST_L': 'SHOULDER_L',
    'ELBOW_R': 'SHOULDER_R',
    'WRIST_R': 'SHOULDER_R'
}

# Animation timing for a single complete press cycle (down and up)
CYCLE_DURATION_MS = 2500  # 2.5 seconds per repetition to convey 'heavy weight'

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus: Bench Press")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main animation loop
running = True
start_time = pygame.time.get_ticks()  # Get initial time in milliseconds

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with black background
    screen.fill(BLACK)

    # Calculate current time relative to animation start
    current_time_ms = pygame.time.get_ticks() - start_time

    # Calculate animation phase (a value from 0 to 1 over one cycle duration)
    # This phase dictates the position within the press cycle.
    # We use a sine wave to ensure smooth, natural, and biomechanically plausible motion.
    # interp_factor_pos ranges from 1 (arms fully UP) to 0 (arms fully DOWN) and back to 1 (arms fully UP).
    # The `(1 + math.cos(angle)) / 2.0` transforms a cosine wave (which goes from 1 to -1)
    # into a normalized value from 1 to 0 (and back to 1).
    # Specifically, when `angle` is 0 or 2*pi, `interp_factor_pos` is 1 (corresponds to 'UP' pose).
    # When `angle` is pi, `interp_factor_pos` is 0 (corresponds to 'DOWN' pose).
    phase = (current_time_ms % CYCLE_DURATION_MS) / CYCLE_DURATION_MS
    angle = phase * 2 * math.pi
    interp_factor_pos = (1 + math.cos(angle)) / 2.0

    # Dictionary to hold the current (x,y) absolute positions of all 15 points
    current_points_coords = {}

    # Calculate positions for the fixed body points (head, torso, hips, legs)
    for name, pos in POINTS_DEFINITION.items():
        # Add the screen center offset to place the figure in the middle of the display
        current_points_coords[name] = (pos[0] + SCREEN_CENTER_OFFSET[0],
                                       pos[1] + SCREEN_CENTER_OFFSET[1])

    # Calculate positions for the animated arm points (elbows, wrists)
    for arm_point_name, shoulder_name in ANIMATED_POINTS_MAPPING.items():
        # Get the current absolute position of the relevant shoulder point, which acts as the pivot
        shoulder_x, shoulder_y = current_points_coords[shoulder_name]

        # Retrieve the relative offsets for the 'UP' and 'DOWN' arm poses
        up_dx, up_dy = ARM_POSES['UP'][arm_point_name]
        down_dx, down_dy = ARM_POSES['DOWN'][arm_point_name]

        # Interpolate between the 'UP' and 'DOWN' relative positions based on the `interp_factor_pos`.
        # This linear interpolation creates the smooth transition between poses.
        current_dx = up_dx * interp_factor_pos + down_dx * (1 - interp_factor_pos)
        current_dy = up_dy * interp_factor_pos + down_dy * (1 - interp_factor_pos)

        # Calculate the final absolute position of the animated arm point
        current_points_coords[arm_point_name] = (shoulder_x + current_dx, shoulder_y + current_dy)

    # Draw all 15 points on the screen as white circles
    for name, pos in current_points_coords.items():
        # Ensure coordinates are integers for Pygame's drawing functions
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

    # Update the entire display to show the new frame
    pygame.display.flip()

    # Cap the frame rate to ensure consistent animation speed
    clock.tick(FPS)

# Uninitialize Pygame and exit the program
pygame.quit()
sys.exit()
