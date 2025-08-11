
import pygame
import math

# --- Constants ---
# Window settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAPTION = "Biological Motion: Running"
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light stimulus properties
POINT_RADIUS = 5

# --- Kinematic Model Parameters ---
# These parameters define the structure and movement of the point-light figure.
# They have been tuned to create a plausible running motion.

# Body proportions (in pixels)
HEAD_OFFSET = 30
SPINE_LENGTH = 150
SHOULDER_WIDTH = 90
UPPER_ARM_LENGTH = 75
LOWER_ARM_LENGTH = 70
PELVIS_WIDTH = 60
THIGH_LENGTH = 95
SHIN_LENGTH = 90

# Animation cycle speed
ANIMATION_SPEED = 0.06

def get_stimulus_points(t):
    """
    Calculates the 15 point positions for a given time 't' in the animation cycle.
    The model is based on sinusoidal oscillations of limbs and a bobbing torso,
    creating a biomechanically plausible running gait.

    Args:
        t (float): A float representing the current phase of the animation cycle.

    Returns:
        list: A list of 15 (x, y) tuples representing the joint positions.
    """
    
    # --- Central Body Movement ---
    # The main reference point for the figure
    center_x = SCREEN_WIDTH / 2
    # The body bobs up and down twice per cycle (once per footfall)
    y_bob = 10 * math.cos(2 * t)
    center_y = SCREEN_HEIGHT / 2 - 40 + y_bob
    
    # The torso has a slight forward lean
    torso_lean = math.radians(8)

    # --- Torso Points (3 points) ---
    # The torso is represented by two points: upper (at the shoulders) and lower (at the hips).
    # A head point is positioned above the upper torso.
    upper_torso_y = center_y - (SPINE_LENGTH / 2) * math.cos(torso_lean)
    upper_torso_x = center_x + (SPINE_LENGTH / 2) * math.sin(torso_lean)
    
    lower_torso_y = center_y + (SPINE_LENGTH / 2) * math.cos(torso_lean)
    lower_torso_x = center_x - (SPINE_LENGTH / 2) * math.sin(torso_lean)

    # Point 1: Head
    head_pos = (upper_torso_x, upper_torso_y - HEAD_OFFSET)
    # Point 2: Upper Torso (clavicle/shoulder center)
    upper_torso_pos = (upper_torso_x, upper_torso_y)
    # Point 3: Lower Torso (pelvis)
    lower_torso_pos = (lower_torso_x, lower_torso_y)

    # --- Arms (Contralateral movement: left arm swings with right leg) ---
    # Phase for right leg and left arm
    phase1 = t
    # Phase for left leg and right arm (pi radians out of phase)
    phase2 = t + math.pi

    # Left Arm
    shoulder_l_angle = torso_lean + math.radians(55) * math.cos(phase1)
    elbow_l_angle = shoulder_l_angle + math.radians(80) + math.radians(40) * (math.cos(phase1) + 1) / 2
    
    # Point 4: Left Shoulder
    shoulder_l_pos = (upper_torso_pos[0] - SHOULDER_WIDTH / 2, upper_torso_pos[1])
    # Point 6: Left Elbow
    elbow_l_pos = (shoulder_l_pos[0] + UPPER_ARM_LENGTH * math.sin(shoulder_l_angle),
                   shoulder_l_pos[1] + UPPER_ARM_LENGTH * math.cos(shoulder_l_angle))
    # Point 8: Left Wrist
    wrist_l_pos = (elbow_l_pos[0] + LOWER_ARM_LENGTH * math.sin(elbow_l_angle),
                   elbow_l_pos[1] + LOWER_ARM_LENGTH * math.cos(elbow_l_angle))

    # Right Arm
    shoulder_r_angle = torso_lean + math.radians(55) * math.cos(phase2)
    elbow_r_angle = shoulder_r_angle + math.radians(80) + math.radians(40) * (math.cos(phase2) + 1) / 2
    
    # Point 5: Right Shoulder
    shoulder_r_pos = (upper_torso_pos[0] + SHOULDER_WIDTH / 2, upper_torso_pos[1])
    # Point 7: Right Elbow
    elbow_r_pos = (shoulder_r_pos[0] + UPPER_ARM_LENGTH * math.sin(shoulder_r_angle),
                   shoulder_r_pos[1] + UPPER_ARM_LENGTH * math.cos(shoulder_r_angle))
    # Point 9: Right Wrist
    wrist_r_pos = (elbow_r_pos[0] + LOWER_ARM_LENGTH * math.sin(elbow_r_angle),
                   elbow_r_pos[1] + LOWER_ARM_LENGTH * math.cos(elbow_r_angle))

    # --- Legs ---
    # Right Leg
    hip_r_angle = torso_lean + math.radians(50) * math.cos(phase1)
    # The knee bends significantly when the leg is in the recovery (back) phase
    knee_r_bend = math.radians(100) * (math.sin(phase1 - math.pi / 2) + 1) / 2
    knee_r_angle = hip_r_angle + knee_r_bend
    
    # Point 11: Right Hip
    hip_r_pos = (lower_torso_pos[0] + PELVIS_WIDTH / 2, lower_torso_pos[1])
    # Point 13: Right Knee
    knee_r_pos = (hip_r_pos[0] + THIGH_LENGTH * math.sin(hip_r_angle),
                  hip_r_pos[1] + THIGH_LENGTH * math.cos(hip_r_angle))
    # Point 15: Right Ankle
    ankle_r_pos = (knee_r_pos[0] + SHIN_LENGTH * math.sin(knee_r_angle),
                   knee_r_pos[1] + SHIN_LENGTH * math.cos(knee_r_angle))

    # Left Leg
    hip_l_angle = torso_lean + math.radians(50) * math.cos(phase2)
    knee_l_bend = math.radians(100) * (math.sin(phase2 - math.pi / 2) + 1) / 2
    knee_l_angle = hip_l_angle + knee_l_bend

    # Point 10: Left Hip
    hip_l_pos = (lower_torso_pos[0] - PELVIS_WIDTH / 2, lower_torso_pos[1])
    # Point 12: Left Knee
    knee_l_pos = (hip_l_pos[0] + THIGH_LENGTH * math.sin(hip_l_angle),
                  hip_l_pos[1] + THIGH_LENGTH * math.cos(hip_l_angle))
    # Point 14: Left Ankle
    ankle_l_pos = (knee_l_pos[0] + SHIN_LENGTH * math.sin(knee_l_angle),
                   knee_l_pos[1] + SHIN_LENGTH * math.cos(knee_l_angle))

    # Assemble the 15 points in a consistent order
    points = [
        head_pos, upper_torso_pos, lower_torso_pos,
        shoulder_l_pos, shoulder_r_pos,
        elbow_l_pos, elbow_r_pos,
        wrist_l_pos, wrist_r_pos,
        hip_l_pos, hip_r_pos,
        knee_l_pos, knee_r_pos,
        ankle_l_pos, ankle_r_pos
    ]
    
    return points

def main():
    """
    Initializes Pygame and runs the main animation loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()

    time_step = 0  # This variable will increment to drive the animation
    is_running = True

    while is_running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False

        # --- Update State ---
        time_step += ANIMATION_SPEED

        # --- Drawing ---
        screen.fill(BLACK)
        
        # Get and draw the stimulus points for the current frame
        stimulus_points = get_stimulus_points(time_step)
        for point in stimulus_points:
            # Ensure coordinates are integers for drawing
            pos_x, pos_y = int(point[0]), int(point[1])
            pygame.draw.circle(screen, WHITE, (pos_x, pos_y), POINT_RADIUS)

        # --- Display Update ---
        pygame.display.flip()

        # --- Frame Rate Control ---
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
