
import pygame
import math

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Dot properties
DOT_RADIUS = 5 # Size of the point-lights

# Animation properties
FPS = 60 # Frames per second for smooth animation
TURN_DURATION_SECONDS = 5 # How long one full 360-degree turn takes
TOTAL_FRAMES = FPS * TURN_DURATION_SECONDS # Total frames for one complete turn

# Scaling factor for 3D coordinates to screen pixels
# Adjust this value to change the overall size of the figure on the screen
SCALE = 200

# Initial relative 3D coordinates for the 15 points (x, y, z)
# The origin (0,0,0) is set approximately at the center of the hips.
# X-axis: horizontal (left/right), Y-axis: vertical (up/down), Z-axis: depth (forward/backward).
# Positive Z indicates points slightly in front of the center plane, simulating arms holding weight.
POINTS_3D_INITIAL = {
    "head":         [0.0, 0.70, 0.0],    # Top of head
    "neck":         [0.0, 0.60, 0.0],    # Base of neck
    "r_shoulder":   [-0.20, 0.50, 0.0],  # Right shoulder
    "l_shoulder":   [0.20, 0.50, 0.0],   # Left shoulder
    "r_elbow":      [-0.25, 0.25, 0.05], # Right elbow (slightly forward)
    "l_elbow":      [0.25, 0.25, 0.05],  # Left elbow (slightly forward)
    "r_wrist":      [-0.20, 0.05, 0.10], # Right wrist (more forward, implying holding weight)
    "l_wrist":      [0.20, 0.05, 0.10],  # Left wrist (more forward, implying holding weight)
    "spine":        [0.0, 0.30, 0.0],    # Mid-torso (approx T12)
    "r_hip":        [-0.10, 0.0, 0.0],   # Right hip (base)
    "l_hip":        [0.10, 0.0, 0.0],    # Left hip
    "r_knee":       [-0.10, -0.35, 0.0], # Right knee
    "l_knee":       [0.10, -0.35, 0.0],  # Left knee
    "r_ankle":      [-0.10, -0.70, 0.0], # Right ankle
    "l_ankle":      [0.10, -0.70, 0.0],  # Left ankle
}

# Ensure a consistent order of points for iteration
POINT_NAMES = list(POINTS_3D_INITIAL.keys())
initial_coords = [POINTS_3D_INITIAL[name] for name in POINT_NAMES]

# Function to rotate a 3D point (x, y, z) around the Y-axis (vertical axis) by 'angle'
# This simulates the main body turning movement.
def rotate_y(point, angle):
    x, y, z = point
    new_x = x * math.cos(angle) + z * math.sin(angle)
    new_z = -x * math.sin(angle) + z * math.cos(angle)
    return [new_x, y, new_z]

# Function to project a 3D point onto 2D screen coordinates
# This uses a simple orthographic projection, mapping 3D space to the 2D screen.
# Pygame's Y-axis increases downwards, so Y coordinates are inverted for display.
def project_to_2d(point, scale_factor):
    x, y, _ = point # Z-coordinate is used for depth calculations but not directly for 2D position in orthographic projection
    screen_x = int(CENTER_X + x * scale_factor)
    screen_y = int(CENTER_Y - y * scale_factor) # Invert Y for screen coordinates
    return (screen_x, screen_y)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Happyman Turning Around")
clock = pygame.time.Clock()

running = True
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Fill the background with black

    # Calculate the overall body rotation angle for the current frame.
    # The modulo operator ensures the animation loops smoothly from 0 to 360 degrees.
    main_rotation_angle = (frame_count % TOTAL_FRAMES) / TOTAL_FRAMES * (2 * math.pi)

    current_coords = []
    for i, point_name in enumerate(POINT_NAMES):
        # Create a mutable copy of the initial 3D point for applying local offsets.
        p_temp = list(initial_coords[i])

        # Apply subtle biomechanical adjustments to points in their *local* coordinate system.
        # These sinusoidal movements add "naturalness" and "plausibility" to the motion.
        # The frequencies (multipliers of main_rotation_angle) control the speed of these movements.

        # Head movement: small wobble (side-to-side, up-down, forward-backward)
        if point_name == "head":
            p_temp[0] += 0.01 * math.sin(main_rotation_angle * 3) # Side-to-side wobble
            p_temp[1] += 0.005 * math.cos(main_rotation_angle * 6) # Up-down bobbing
            p_temp[2] += 0.01 * math.sin(main_rotation_angle * 1.5 + math.pi/2) # Slight forward/backward movement

        # Arm movements for "light weight": subtle vertical sway and forward/backward push/pull.
        # The Z-axis offsets for wrists and elbows are positive in initial_coords, implying arms
        # are already slightly forward, consistent with holding something.
        if point_name in ["r_elbow", "l_elbow", "r_wrist", "l_wrist"]:
            # Slight up/down movement, simulating arm swing for balance or holding item
            arm_y_offset = 0.015 * math.sin(main_rotation_angle * 2)
            p_temp[1] += arm_y_offset

            # Subtle forward/backward movement, as if adjusting grip or balance
            arm_z_offset = 0.01 * math.cos(main_rotation_angle * 2.5)
            p_temp[2] += arm_z_offset

            # Small side-to-side movement, slightly opening/closing arms
            arm_x_offset = 0.005 * math.sin(main_rotation_angle * 2)
            if point_name.startswith('r_'): # Right arm moves outward/inward
                p_temp[0] -= arm_x_offset
            else: # Left arm moves inward/outward
                p_temp[0] += arm_x_offset

        # Torso (spine) movement: subtle swaying for natural body core motion
        if point_name == "spine":
            p_temp[2] += 0.01 * math.sin(main_rotation_angle * 2) # Slight forward/backward sway
            p_temp[0] += 0.005 * math.cos(main_rotation_angle * 3) # Small side-to-side sway

        # Leg movements: subtle knee bend/straighten and weight shift.
        # While the figure is "turning around" without stepping, minor leg adjustments
        # add to the biomechanical plausibility.
        if point_name in ["r_knee", "l_knee", "r_ankle", "l_ankle"]:
            # Subtle up/down movement simulating slight knee bend/straighten
            leg_y_offset = 0.015 * math.sin(main_rotation_angle * 4 + math.pi/2)
            p_temp[1] += leg_y_offset

            # Slight Z movement to simulate subtle foot placement adjustments
            leg_z_offset = 0.01 * math.cos(main_rotation_angle * 4)
            p_temp[2] += leg_z_offset

            # Side-to-side movement for weight shift between legs
            leg_x_offset = 0.01 * math.sin(main_rotation_angle * 4)
            if point_name.startswith('r_'):
                p_temp[0] -= leg_x_offset # Right leg moves slightly outward/inward
            else:
                p_temp[0] += leg_x_offset # Left leg moves slightly inward/outward

        # After applying all local biomechanical offsets, apply the overall body rotation.
        # This ensures the local movements are correctly oriented relative to the turning body.
        p_rotated = rotate_y(p_temp, main_rotation_angle)
        current_coords.append(p_rotated)

    # Draw all the transformed points on the screen
    for p_3d in current_coords:
        screen_pos = project_to_2d(p_3d, SCALE)
        pygame.draw.circle(screen, WHITE, screen_pos, DOT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen
    frame_count += 1 # Increment frame counter for animation progression
    clock.tick(FPS) # Control the frame rate to ensure smooth animation

pygame.quit() # Uninitialize Pygame modules when the loop finishes
