
import pygame
import numpy as np
import math

# --- Constants ---
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 6
FPS = 60

# --- Animation Parameters ---
# Duration of the bowing down and rising up phases (in seconds)
MOTION_DURATION = 2.0
# Duration of the pause at the lowest and highest points (in seconds)
PAUSE_DURATION = 1.0
# Maximum angle of the bow in degrees
MAX_BOW_ANGLE_DEGREES = 50

# --- Skeleton Definition ---
# A 15-point skeleton defined in a standard upright pose.
# The coordinate system is centered at the 'torso' point, with Y-axis pointing up.
# Units are arbitrary pixels, defining the figure's proportions.
SKELETON_DATA = {
    # Central Body
    'torso': np.array([0., 0.]),
    'neck': np.array([0., 90.]),
    'head': np.array([0., 125.]),

    # Hips and Legs
    'l_hip': np.array([-30., -10.]),
    'r_hip': np.array([30., -10.]),
    'l_knee': np.array([-30., -90.]),
    'r_knee': np.array([30., -90.]),
    'l_ankle': np.array([-30., -170.]),
    'r_ankle': np.array([30., -170.]),

    # Shoulders and Arms
    'l_shoulder': np.array([-45., 90.]),
    'r_shoulder': np.array([45., 90.]),
    'l_elbow': np.array([-45., 20.]),
    'r_elbow': np.array([45., 20.]),
    'l_wrist': np.array([-45., -50.]),
    'r_wrist': np.array([45., -50.]),
}

# --- Main Program ---
def main():
    """
    Initializes pygame and runs the main animation loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Bowing")
    clock = pygame.time.Clock()

    # Define which parts of the body move during the bow
    upper_body_keys = [
        'torso', 'neck', 'head', 'l_shoulder', 'r_shoulder',
        'l_elbow', 'r_elbow', 'l_wrist', 'r_wrist'
    ]
    lower_body_keys = [
        'l_hip', 'r_hip', 'l_knee', 'r_knee', 'l_ankle', 'r_ankle'
    ]

    # The pivot point for the bow is the center of the hips
    pivot_point = (SKELETON_DATA['l_hip'] + SKELETON_DATA['r_hip']) / 2.0
    
    # Convert angle to radians for math functions
    max_bow_angle_rad = math.radians(MAX_BOW_ANGLE_DEGREES)

    start_time = pygame.time.get_ticks()
    running = True

    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # --- Animation Timing ---
        total_cycle_duration = (MOTION_DURATION * 2) + (PAUSE_DURATION * 2)
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0
        cycle_time = elapsed_time % total_cycle_duration

        # Determine the current phase of the animation cycle
        current_angle = 0.0
        if cycle_time < MOTION_DURATION:
            # Phase 1: Bowing down
            progress = cycle_time / MOTION_DURATION
            # Use a sinusoidal easing function for smooth start and end
            t = 0.5 * (1 - math.cos(math.pi * progress))
            current_angle = t * max_bow_angle_rad
        elif cycle_time < MOTION_DURATION + PAUSE_DURATION:
            # Phase 2: Paused at the bottom of the bow
            current_angle = max_bow_angle_rad
        elif cycle_time < (MOTION_DURATION * 2) + PAUSE_DURATION:
            # Phase 3: Rising up
            progress = (cycle_time - (MOTION_DURATION + PAUSE_DURATION)) / MOTION_DURATION
            t = 0.5 * (1 - math.cos(math.pi * progress))
            current_angle = (1 - t) * max_bow_angle_rad
        else:
            # Phase 4: Paused standing upright
            current_angle = 0.0

        # --- Calculate Point Positions ---
        # Create the 2D rotation matrix for a clockwise rotation (forward bow)
        cos_a = math.cos(current_angle)
        sin_a = math.sin(current_angle)
        rotation_matrix = np.array([[cos_a, sin_a], [-sin_a, cos_a]])

        current_points = {}
        
        # Lower body points remain static relative to the origin
        for key in lower_body_keys:
            current_points[key] = SKELETON_DATA[key]

        # Upper body points rotate around the pivot point
        for key in upper_body_keys:
            # Get original position vector from the data
            original_pos = SKELETON_DATA[key]
            # Create a vector from the pivot to the point
            vec_to_rotate = original_pos - pivot_point
            # Apply the rotation
            rotated_vec = rotation_matrix @ vec_to_rotate
            # Add the pivot back to get the final position
            current_points[key] = rotated_vec + pivot_point

        # --- Drawing ---
        screen.fill(BACKGROUND_COLOR)
        
        # Define the center of the screen for drawing the figure
        screen_center = np.array([WIDTH / 2, HEIGHT / 2 + 120])

        for point_pos in current_points.values():
            # Translate model coordinates to screen coordinates
            # Flip the Y-axis because pygame's Y is inverted
            screen_pos = screen_center + np.array([point_pos[0], -point_pos[1]])
            pygame.draw.circle(screen, POINT_COLOR, screen_pos.astype(int), POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
