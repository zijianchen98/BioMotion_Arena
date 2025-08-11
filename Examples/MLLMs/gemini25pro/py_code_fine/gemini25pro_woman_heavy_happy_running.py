
import pygame
import math

# --- Constants ---
# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light stimulus properties
POINT_RADIUS = 6
NUM_POINTS = 15

# --- Biomechanical Parameters for a "Heavy, Happy Woman Running" ---

# Body Proportions (in pixels)
HEAD_SIZE = 15
NECK_LENGTH = 15
TORSO_LENGTH = 80
SHOULDER_WIDTH = 85
UPPER_ARM_LENGTH = 65
FOREARM_LENGTH = 60
HIP_WIDTH = 70
THIGH_LENGTH = 85
CALF_LENGTH = 75

# Motion Parameters
CYCLE_DURATION_MS = 1200  # Slower cadence for heavy feel
FORWARD_LEAN = 0.25       # Radians, lean into the run

# Torso Motion (Core of the movement)
TORSO_Y_BASE = SCREEN_HEIGHT / 2 + 40
TORSO_Y_AMP = 6           # Reduced vertical bounce for weight
TORSO_SWAY_AMP = 8        # Increased side-to-side sway for weight

# Leg Motion
STRIDE_AMP = 1.1          # Radians, how far legs swing back and forth
KNEE_BEND_SWING = 2.0     # Radians, how much knee bends during swing phase
KNEE_BEND_IMPACT = 0.35   # Radians, extra bend to absorb impact (heavy feel)

# Arm Motion
ARM_SWING_AMP = 1.0       # Radians, how far arms swing
ARM_ABDUCTION = 0.3       # Radians, arms held away from body for balance
ELBOW_BEND = 1.3          # Radians, base elbow bend

# "Happy" Modifier
HEAD_TILT = -0.15         # Radians, slight upward tilt for a happy expression

# --- Main Program ---

def update_points(time_ms):
    """
    Calculates the 2D coordinates of the 15 joints for a given time.
    The model uses forward kinematics, starting from the torso and calculating
    limb positions based on angles and bone lengths.
    """
    
    # --- Time and Phase Calculation ---
    t_cycle = (time_ms % CYCLE_DURATION_MS) / CYCLE_DURATION_MS
    phase = t_cycle * 2 * math.pi
    
    # --- Torso and Core Body Motion ---
    # The torso is the root of all other movements. It sways and bounces.
    
    # Vertical bounce (two bounces per full cycle)
    torso_y = TORSO_Y_BASE - TORSO_Y_AMP * abs(math.sin(phase))
    # Side-to-side sway (one sway per cycle)
    torso_x = SCREEN_WIDTH / 2 + TORSO_SWAY_AMP * math.sin(phase)

    # Calculate core points with a forward lean
    # [3] Center Torso (mid-spine)
    p_torso = (torso_x, torso_y)
    
    # [2] Neck (base of the head)
    p_neck = (p_torso[0] + NECK_LENGTH * math.sin(FORWARD_LEAN),
              p_torso[1] - NECK_LENGTH * math.cos(FORWARD_LEAN))
              
    # [1] Head (with a "happy" upward tilt)
    p_head = (p_neck[0] + HEAD_SIZE * math.sin(FORWARD_LEAN + HEAD_TILT),
              p_neck[1] - HEAD_SIZE * math.cos(FORWARD_LEAN + HEAD_TILT))

    # --- Shoulders and Hips ---
    # These joints are attached to the torso and have their own slight rotational sway.
    shoulder_sway = 0.1 * math.sin(phase)
    hip_sway = -0.18 * math.sin(phase) # Pelvic tilt is opposite to shoulder sway

    # Shoulder positions
    p_l_shoulder = (p_neck[0] - (SHOULDER_WIDTH/2) * math.cos(FORWARD_LEAN - shoulder_sway),
                    p_neck[1] - (SHOULDER_WIDTH/2) * math.sin(FORWARD_LEAN - shoulder_sway))
    p_r_shoulder = (p_neck[0] + (SHOULDER_WIDTH/2) * math.cos(FORWARD_LEAN + shoulder_sway),
                    p_neck[1] + (SHOULDER_WIDTH/2) * math.sin(FORWARD_LEAN + shoulder_sway))

    # Hip positions
    hip_base_y = p_torso[1] + TORSO_LENGTH * math.cos(FORWARD_LEAN)
    hip_base_x = p_torso[0] + TORSO_LENGTH * math.sin(FORWARD_LEAN)
    
    p_l_hip = (hip_base_x - (HIP_WIDTH/2) * math.cos(FORWARD_LEAN + hip_sway),
               hip_base_y - (HIP_WIDTH/2) * math.sin(FORWARD_LEAN + hip_sway))
    p_r_hip = (hip_base_x + (HIP_WIDTH/2) * math.cos(FORWARD_LEAN - hip_sway),
               hip_base_y + (HIP_WIDTH/2) * math.sin(FORWARD_LEAN - hip_sway))

    # --- Limb Calculation ---
    # A helper function to compute positions for arms and legs to avoid repetition.
    def calculate_limb(p_base, limb_phase, upper_len, lower_len, is_leg):
        if is_leg:
            # Leg kinematics
            swing_factor = (math.cos(limb_phase) + 1) / 2 # 0 for back, 1 for forward
            stance_factor = 1 - swing_factor
            
            # Primary swing motion of the thigh
            thigh_angle = FORWARD_LEAN - STRIDE_AMP * math.sin(limb_phase)
            
            # Knee bends significantly during swing and absorbs impact during stance
            impact_effect = math.exp(-8 * stance_factor) # Sharp effect on landing
            knee_angle = KNEE_BEND_SWING * swing_factor + KNEE_BEND_IMPACT * impact_effect

            # Calculate joint positions
            p_knee = (p_base[0] + thigh_len * math.sin(thigh_angle),
                      p_base[1] + thigh_len * math.cos(thigh_angle))
            p_ankle = (p_knee[0] + lower_len * math.sin(thigh_angle - knee_angle),
                       p_knee[1] + lower_len * math.cos(thigh_angle - knee_angle))
            return p_knee, p_ankle
        else:
            # Arm kinematics (contralateral motion)
            arm_phase = limb_phase + math.pi
            
            # Arms swing from the shoulder and are held out for balance (abduction)
            shoulder_angle = FORWARD_LEAN + ARM_SWING_AMP * math.sin(arm_phase)
            
            # Elbow has a fixed bend
            elbow_angle = ELBOW_BEND

            # Calculate joint positions with abduction
            p_elbow = (p_base[0] + upper_len * math.sin(shoulder_angle) - upper_len * ARM_ABDUCTION * math.cos(shoulder_angle),
                       p_base[1] + upper_len * math.cos(shoulder_angle) + upper_len * ARM_ABDUCTION * math.sin(shoulder_angle))
            p_wrist = (p_elbow[0] + lower_len * math.sin(shoulder_angle - elbow_angle) - lower_len * ARM_ABDUCTION * math.cos(shoulder_angle),
                       p_elbow[1] + lower_len * math.cos(shoulder_angle - elbow_angle) + lower_len * ARM_ABDUCTION * math.sin(shoulder_angle))
            return p_elbow, p_wrist
            
    # Calculate all limb points
    # Legs (right leg follows main phase, left is opposite)
    thigh_len, calf_len = THIGH_LENGTH, CALF_LENGTH
    p_r_knee, p_r_ankle = calculate_limb(p_r_hip, phase, thigh_len, calf_len, is_leg=True)
    p_l_knee, p_l_ankle = calculate_limb(p_l_hip, phase + math.pi, thigh_len, calf_len, is_leg=True)

    # Arms
    upper_arm_len, forearm_len = UPPER_ARM_LENGTH, FOREARM_LENGTH
    p_r_elbow, p_r_wrist = calculate_limb(p_r_shoulder, phase, upper_arm_len, forearm_len, is_leg=False)
    p_l_elbow, p_l_wrist = calculate_limb(p_l_shoulder, phase + math.pi, upper_arm_len, forearm_len, is_leg=False)
                                          
    # Assemble the final list of 15 points
    return [
        p_head, p_neck, p_torso,
        p_l_shoulder, p_r_shoulder,
        p_l_elbow, p_r_elbow,
        p_l_wrist, p_r_wrist,
        p_l_hip, p_r_hip,
        p_l_knee, p_r_knee,
        p_l_ankle, p_r_ankle
    ]

def main():
    """
    Initializes Pygame, runs the main animation loop, and handles events.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Running")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        time_ms = pygame.time.get_ticks()
        points = update_points(time_ms)
        
        # --- Drawing ---
        screen.fill(BLACK)
        for point in points:
            # Cast to integers for Pygame's drawing functions
            int_point = (int(point[0]), int(point[1]))
            pygame.draw.circle(screen, WHITE, int_point, POINT_RADIUS)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
