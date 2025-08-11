
import pygame
import numpy as np
import sys

# --- Constants ---
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
ANIMATION_DURATION_S = 2.5
TOTAL_FRAMES = int(ANIMATION_DURATION_S * FPS)
POINT_RADIUS = 5

# --- Body Proportions ---
# Scaled to screen height for a responsive animation
SCALE = HEIGHT / 5.5
TORSO_LEN = 0.3 * SCALE
HEAD_VEC_LEN = 0.22 * SCALE
UPPER_ARM_LEN = 0.25 * SCALE
LOWER_ARM_LEN = 0.22 * SCALE
UPPER_LEG_LEN = 0.28 * SCALE
LOWER_LEG_LEN = 0.26 * SCALE
SHOULDER_WIDTH = 0.26 * SCALE
HIP_WIDTH = 0.15 * SCALE

def rotate(point, angle):
    """Rotates a 2D point (numpy array) around the origin."""
    c, s = np.cos(angle), np.sin(angle)
    rotation_matrix = np.array([[c, -s], [s, c]])
    return rotation_matrix.dot(point)

def get_animation_frame(t):
    """
    Calculates the 15 point coordinates for a given time t (0 to 1).
    The model simulates a forward roll, starting from a squat, rolling,
    and returning to a squat.
    """
    # --- Global Motion Control ---
    # `roll_progress` maps the main rolling action to a 0-1 scale
    roll_progress = max(0, min(1, (t - 0.1) / 0.8))
    
    # Body rotates a full 360 degrees (2*pi radians) during the roll
    body_angle = -2 * np.pi * roll_progress  # Negative for clockwise (forward) roll

    # Horizontal and vertical translation of the whole body (pelvis)
    x_translation = -WIDTH * 0.45 + WIDTH * 0.9 * t
    pelvis_y_base = -HEIGHT * 0.18
    roll_height = HEIGHT * 0.25
    pelvis_y_offset = roll_height * np.sin(np.pi * roll_progress)
    
    # Add a small bounce at the end for an energetic landing
    bounce = 0
    if t > 0.9:
        t_end = (t - 0.9) / 0.1
        bounce = 15 * np.sin(2 * np.pi * t_end) * np.exp(-4 * t_end)

    pelvis_y = pelvis_y_base + pelvis_y_offset + bounce
    pelvis_pos = np.array([x_translation, pelvis_y])

    # --- Spine Calculation (Pelvis -> Sternum -> Head) ---
    sternum_pos = pelvis_pos + rotate(np.array([0, TORSO_LEN]), body_angle)
    head_pos = sternum_pos + rotate(np.array([0, HEAD_VEC_LEN]), body_angle)

    # --- Leg Calculation (Tucked, with push-off/landing extension) ---
    l_hip_pos = pelvis_pos + rotate(np.array([-HIP_WIDTH / 2, 0]), body_angle)
    r_hip_pos = pelvis_pos + rotate(np.array([HIP_WIDTH / 2, 0]), body_angle)

    # Extension for push-off (at start of roll) and landing (at end)
    extension_factor = np.exp(-30 * (roll_progress - 0.05)**2) + np.exp(-30 * (roll_progress - 0.95)**2)
    hip_angle_rel = np.pi * 0.70 - np.pi * 0.2 * extension_factor
    knee_angle_rel = -np.pi * 0.70 + np.pi * 0.6 * extension_factor

    l_knee_pos = l_hip_pos + rotate(np.array([0, -UPPER_LEG_LEN]), body_angle + hip_angle_rel)
    l_ankle_pos = l_knee_pos + rotate(np.array([0, -LOWER_LEG_LEN]), body_angle + hip_angle_rel + knee_angle_rel)
    r_knee_pos = r_hip_pos + rotate(np.array([0, -UPPER_LEG_LEN]), body_angle - hip_angle_rel)
    r_ankle_pos = r_knee_pos + rotate(np.array([0, -LOWER_LEG_LEN]), body_angle - hip_angle_rel - knee_angle_rel)
    
    # --- Arm Calculation (Reaching forward, then tucking overhead) ---
    l_shoulder_pos = sternum_pos + rotate(np.array([-SHOULDER_WIDTH / 2, 0]), body_angle)
    r_shoulder_pos = sternum_pos + rotate(np.array([SHOULDER_WIDTH / 2, 0]), body_angle)

    # Arms swing from forward (pi/2) to overhead (-pi/2) and back
    shoulder_angle_rel = (np.pi / 2.2) * np.cos(np.pi * roll_progress)
    elbow_angle_rel = np.pi * 0.35  # Arms stay bent

    l_elbow_pos = l_shoulder_pos + rotate(np.array([0, -UPPER_ARM_LEN]), body_angle + shoulder_angle_rel)
    l_wrist_pos = l_elbow_pos + rotate(np.array([0, -LOWER_ARM_LEN]), body_angle + shoulder_angle_rel + elbow_angle_rel)
    r_elbow_pos = r_shoulder_pos + rotate(np.array([0, -UPPER_ARM_LEN]), body_angle - shoulder_angle_rel)
    r_wrist_pos = r_elbow_pos + rotate(np.array([0, -LOWER_ARM_LEN]), body_angle - shoulder_angle_rel - elbow_angle_rel)

    # --- Collect 15 points ---
    points = [
        head_pos, l_shoulder_pos, r_shoulder_pos, l_elbow_pos, r_elbow_pos,
        l_wrist_pos, r_wrist_pos, sternum_pos, pelvis_pos, l_hip_pos, r_hip_pos,
        l_knee_pos, r_knee_pos, l_ankle_pos, r_ankle_pos
    ]
    
    # --- Transform to Screen Coordinates ---
    # (0,0) is top-left in Pygame, so we shift and invert the Y-axis
    transformed_points = []
    for p in points:
        screen_x = p[0] + WIDTH / 2
        screen_y = HEIGHT / 2 - p[1]
        transformed_points.append((screen_x, screen_y))
        
    return transformed_points

def main():
    """Main function to run the Pygame animation."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Forward Roll")
    clock = pygame.time.Clock()

    frame_count = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Calculate animation time `t` from 0 to 1, looping
        t = (frame_count % TOTAL_FRAMES) / TOTAL_FRAMES

        # Get the coordinates for the current frame
        points = get_animation_frame(t)

        # Drawing
        screen.fill(BLACK)
        for pos in points:
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)
        
        pygame.display.flip()
        clock.tick(FPS)
        frame_count += 1

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
