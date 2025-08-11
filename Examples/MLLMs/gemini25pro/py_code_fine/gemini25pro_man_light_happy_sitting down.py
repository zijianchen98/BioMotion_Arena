
import pygame
import numpy as np
import sys

# --- Constants ---
WIDTH, HEIGHT = 800, 800
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DOT_RADIUS = 7
ANIMATION_FRAMES = 180  # Slower motion to represent "heavy weight"

# --- Body Proportions (in pixels) ---
TORSO_LENGTH = 110
UPPER_ARM_LENGTH = 60
FOREARM_LENGTH = 65
THIGH_LENGTH = 75
SHIN_LENGTH = 70
HEAD_OFFSET = 25
SHOULDER_WIDTH = 80
HIP_WIDTH = 60

# --- Keyframe Definitions (Absolute Angles in degrees and Positions) ---
# Angles use a standard mathematical convention: 0 is right, 90 is up.
# The rendering function will handle the inverted Y-axis of the screen.
START_POSE = {
    'pelvis_pos': np.array([WIDTH / 2, HEIGHT / 2]),
    'torso_angle': 88.0,
    # Arms held forward and slightly bent
    'l_up_arm_angle': 220.0,
    'r_up_arm_angle': 320.0,
    'l_lo_arm_angle': 200.0,
    'r_lo_arm_angle': 340.0,
    # Legs almost straight
    'l_up_leg_angle': 265.0,
    'r_up_leg_angle': 275.0,
    'l_lo_leg_angle': 265.0,
    'r_lo_leg_angle': 275.0,
}

END_POSE = {
    'pelvis_pos': np.array([WIDTH / 2 - 40, HEIGHT / 2 + 70]),
    'torso_angle': 55.0,
    # Arms adjust with torso, maintaining hold
    'l_up_arm_angle': 190.0,
    'r_up_arm_angle': 300.0,
    'l_lo_arm_angle': 180.0,
    'r_lo_arm_angle': 310.0,
    # Legs bent in a seated position
    'l_up_leg_angle': 225.0,
    'r_up_leg_angle': 315.0,
    'l_lo_leg_angle': 275.0,
    'r_lo_leg_angle': 265.0,
}


def lerp(v0, v1, t):
    """Linear interpolation for both scalars and numpy arrays."""
    return v0 * (1 - t) + v1 * t

def get_vec(angle_deg, length):
    """Calculates a vector from an angle (in degrees) and length."""
    rad = np.deg2rad(angle_deg)
    # The y-component is negative to convert from math coordinates (y-up)
    # to screen coordinates (y-down).
    return np.array([np.cos(rad), -np.sin(rad)]) * length

def calculate_all_joints(params):
    """
    Calculates the 15 joint positions using absolute angles from the params dict.
    This is a direct Forward Kinematics implementation.
    """
    points = {}
    
    # Torso and Pelvis are central
    points['pelvis'] = params['pelvis_pos']
    torso_vec = get_vec(params['torso_angle'], TORSO_LENGTH)
    points['upper_torso'] = points['pelvis'] + torso_vec

    # Head is offset from the upper torso
    points['head'] = points['upper_torso'] + get_vec(params['torso_angle'], HEAD_OFFSET)

    # Shoulders are perpendicular to the torso line
    shoulder_perp_vec = get_vec(params['torso_angle'] + 90, SHOULDER_WIDTH / 2)
    points['l_shoulder'] = points['upper_torso'] + shoulder_perp_vec
    points['r_shoulder'] = points['upper_torso'] - shoulder_perp_vec

    # Hips are perpendicular to the torso line, at the pelvis
    hip_perp_vec = get_vec(params['torso_angle'] + 90, HIP_WIDTH / 2)
    points['l_hip'] = points['pelvis'] + hip_perp_vec
    points['r_hip'] = points['pelvis'] - hip_perp_vec

    # Arms
    points['l_elbow'] = points['l_shoulder'] + get_vec(params['l_up_arm_angle'], UPPER_ARM_LENGTH)
    points['r_elbow'] = points['r_shoulder'] + get_vec(params['r_up_arm_angle'], UPPER_ARM_LENGTH)
    points['l_wrist'] = points['l_elbow'] + get_vec(params['l_lo_arm_angle'], FOREARM_LENGTH)
    points['r_wrist'] = points['r_elbow'] + get_vec(params['r_lo_arm_angle'], FOREARM_LENGTH)

    # Legs
    points['l_knee'] = points['l_hip'] + get_vec(params['l_up_leg_angle'], THIGH_LENGTH)
    points['r_knee'] = points['r_hip'] + get_vec(params['r_up_leg_angle'], THIGH_LENGTH)
    points['l_ankle'] = points['l_knee'] + get_vec(params['l_lo_leg_angle'], SHIN_LENGTH)
    points['r_ankle'] = points['r_knee'] + get_vec(params['r_lo_leg_angle'], SHIN_LENGTH)

    # Return the 15 points in the specified order for biological motion stimuli
    return [
        points['head'], points['upper_torso'], points['pelvis'],
        points['l_shoulder'], points['r_shoulder'],
        points['l_elbow'], points['r_elbow'],
        points['l_wrist'], points['r_wrist'],
        points['l_hip'], points['r_hip'],
        points['l_knee'], points['r_knee'],
        points['l_ankle'], points['r_ankle']
    ]

def main():
    """Main function to run the Pygame animation."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Sitting Down with Heavy Weight")
    clock = pygame.time.Clock()

    frame_count = 0
    initial_ankle_y = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # --- Animation and Interpolation ---
        # Calculate progress and apply an ease-in-out function for smooth motion
        progress = (frame_count % ANIMATION_FRAMES) / (ANIMATION_FRAMES - 1)
        t = 0.5 * (1 - np.cos(progress * np.pi))

        # Interpolate all parameters between the start and end poses
        current_params = {}
        for key in START_POSE:
            current_params[key] = lerp(START_POSE[key], END_POSE[key], t)
        
        # Calculate joint positions for the current frame
        points = calculate_all_joints(current_params)

        # --- Foot-Slip Correction ---
        # This keeps the feet planted on the "ground" for realism.
        current_ankle_y = (points[-1][1] + points[-2][1]) / 2  # Average Y of both ankles
        if initial_ankle_y is None:
            initial_ankle_y = current_ankle_y
        
        y_offset = initial_ankle_y - current_ankle_y
        
        # Apply the correction to all points
        corrected_points = [p + np.array([0, y_offset]) for p in points]

        # --- Drawing ---
        screen.fill(BLACK)
        for point in corrected_points:
            pygame.draw.circle(screen, WHITE, point.astype(int), DOT_RADIUS)
        
        pygame.display.flip()

        frame_count += 1
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
