
import pygame
import math

# --- Pygame Setup ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
POINT_RADIUS = 8  # Size of the white dots
FPS = 60          # Frames per second for smooth animation

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Walking")
clock = pygame.time.Clock()

# --- Animation Parameters ---
# Overall walking speed (smaller value for a slower, 'sad' pace)
WALKING_SPEED = 0.04

# Amplitudes for movements (tuned for "sad woman, light weight")
# These values are empirical and aim for a subtle, less energetic walk.
TORSO_SWAY_AMP = 2.5  # Horizontal side-to-side torso sway
TORSO_BOB_AMP = 5     # Vertical up-down torso bob

HEAD_BOB_AMP = 3.5    # Head bob (slightly desynchronized from torso)
HEAD_SWAY_AMP = 1.5   # Head side-to-side sway

ARM_SWING_AMP_X = 20  # Horizontal arm swing (reduced for 'sad')
ARM_SWING_AMP_Y = 8   # Vertical arm swing (subtle)
ELBOW_BEND_FACTOR = 0.7 # Factor for how much the elbow bends
WRIST_OFFSET_Y_FACTOR = 0.5 # Factor for how much the wrist follows elbow bend

LEG_SWING_AMP_X = 35  # Horizontal leg swing (moderate)
LEG_SWING_AMP_Y = 12  # Vertical leg lift/drop (reduced)
KNEE_BEND_AMP = 20    # Knee bend magnitude
ANKLE_LIFT_AMP = 9    # Ankle lift magnitude during swing
FOOT_LIFT_AMP = 13    # Foot lift magnitude during swing

# Base relative positions of 15 points (adjust these to match human proportions)
# These are relative to a central hip/pelvis point (0,0).
# Adjusted for a slightly hunched/less energetic posture for 'sad woman'.
BASE_POSITIONS = {
    "head":         (0,   -170),  # Head slightly lower
    "l_shoulder":   (-60, -100),  # Shoulders slightly hunched/closer
    "r_shoulder":   (60,  -100),
    "l_elbow":      (-80, -40),   # Arms starting slightly bent
    "r_elbow":      (80,  -40),
    "l_wrist":      (-90,  10),
    "r_wrist":      (90,   10),
    "l_hip":        (-35,  0),
    "r_hip":        (35,   0),
    "l_knee":       (-45,  70),
    "r_knee":       (45,   70),
    "l_ankle":      (-40,  140),
    "r_ankle":      (40,   140),
    "l_foot":       (-50,  150), # Foot extending forward/back
    "r_foot":       (50,   150),
}

# --- Animation Logic ---
current_phase = 0.0 # This variable controls the progression through the walking cycle

def get_point_positions(phase):
    """
    Calculates the current animated positions of all 15 points based on the phase.
    """
    # Center of the person on screen (fixed for walking in place)
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2

    # Overall torso movement (subtle, representing body sway during walking)
    torso_offset_x = math.sin(phase * 0.5) * TORSO_SWAY_AMP
    torso_offset_y = math.sin(phase * 1.0) * TORSO_BOB_AMP

    # Phases for left and right legs. They are 180 degrees out of phase.
    # 'phase' 0 to 2*pi corresponds to one full walking cycle.
    # Example: phase=0 (left leg back, right leg forward), phase=pi (left leg forward, right leg back)
    left_leg_phase = phase
    right_leg_phase = phase + math.pi 

    # Phases for left and right arms. Arms swing opposite to the corresponding leg.
    # So, left arm phase is same as right leg phase, and vice-versa.
    left_arm_phase = right_leg_phase
    right_arm_phase = left_leg_phase

    # Dictionary to store the final calculated positions for drawing
    animated_points = {}

    for name, base_pos in BASE_POSITIONS.items():
        # Start with the base static position relative to torso center,
        # then add the overall torso movement.
        current_x = base_pos[0] + torso_offset_x
        current_y = base_pos[1] + torso_offset_y

        # Apply specific movements based on the joint
        if "head" in name:
            # Head has its own slight sway and bob, slightly out of sync with torso for naturalness
            current_x += math.sin(phase * 0.7) * HEAD_SWAY_AMP
            current_y += math.sin(phase * 1.2) * HEAD_BOB_AMP

        elif "shoulder" in name:
            arm_phase = left_arm_phase if "l_" in name else right_arm_phase
            # Shoulders move primarily with the torso, but also have a small component
            # linked to arm swing for more realism.
            current_x += math.sin(arm_phase) * (ARM_SWING_AMP_X * 0.1)
            current_y += math.cos(arm_phase * 2) * (ARM_SWING_AMP_Y * 0.1)

        elif "elbow" in name or "wrist" in name:
            arm_phase = left_arm_phase if "l_" in name else right_arm_phase
            
            # Base arm swing derived from the shoulder's motion.
            x_swing = math.sin(arm_phase) * ARM_SWING_AMP_X
            y_swing = math.cos(arm_phase) * ARM_SWING_AMP_Y

            current_x += x_swing
            current_y += y_swing

            # Elbow bend logic: Elbows bend more when the arm is in the middle of its swing.
            # (1 - abs(math.cos(arm_phase * 0.8))) creates a bend that peaks twice per full swing cycle.
            elbow_bend_amount = (1 - abs(math.cos(arm_phase * 0.8))) * ELBOW_BEND_FACTOR
            
            if "elbow" in name:
                # Elbow moves inward and slightly downward relative to shoulder during bend
                current_y += elbow_bend_amount * KNEE_BEND_AMP * 0.5 
                current_x += (1 if "l_" in name else -1) * elbow_bend_amount * ARM_SWING_AMP_X * 0.1
            elif "wrist" in name:
                # Wrist follows the elbow's motion, with its own slight adjustments
                current_y += elbow_bend_amount * KNEE_BEND_AMP * WRIST_OFFSET_Y_FACTOR 
                current_x += (1 if "l_" in name else -1) * elbow_bend_amount * ARM_SWING_AMP_X * 0.2

        elif "hip" in name:
            leg_phase = left_leg_phase if "l_" in name else right_leg_phase
            # Hips have slight horizontal and vertical oscillations following leg movement
            current_x += math.sin(leg_phase * 0.5) * (LEG_SWING_AMP_X * 0.1)
            current_y += math.cos(leg_phase * 1.0) * (LEG_SWING_AMP_Y * 0.2)

        elif "knee" in name or "ankle" in name or "foot" in name:
            leg_phase = left_leg_phase if "l_" in name else right_leg_phase
            
            # Horizontal leg swing (main arc motion)
            x_leg_swing = math.sin(leg_phase) * LEG_SWING_AMP_X
            current_x += x_leg_swing
            
            # Vertical leg lift/drop (less pronounced for 'sad' or 'light weight' walk)
            y_leg_swing = math.cos(leg_phase) * LEG_SWING_AMP_Y * 0.5 
            current_y += y_leg_swing

            if "knee" in name:
                # Knee bend: most bent when leg is swinging forward and off the ground.
                # (1 - math.cos(leg_phase * 2)) creates two bends per cycle, peaking at mid-swing.
                knee_bend_factor = (1 - math.cos(leg_phase * 2)) * 0.5 
                current_y += knee_bend_factor * KNEE_BEND_AMP # Bend downwards

            elif "ankle" in name:
                # Ankle lift for foot clearance during the swing phase.
                # max(0, -math.sin(leg_phase + math.pi/4)) makes it lift only when the leg is in the forward swing.
                ankle_lift_factor = max(0, -math.sin(leg_phase + math.pi/4)) 
                current_y += ankle_lift_factor * ANKLE_LIFT_AMP

            elif "foot" in name:
                # Foot lift for clearance and push-off, slightly delayed from ankle.
                foot_lift_factor = max(0, -math.sin(leg_phase + math.pi/2)) 
                current_y += foot_lift_factor * FOOT_LIFT_AMP
                # Slight horizontal adjustment for natural foot placement
                current_x += math.sin(leg_phase * 1.5) * FOOT_LIFT_AMP * 0.3

        # Add the global screen offset to center the figure and make it sway slightly
        # This keeps the figure mostly in place, but with a subtle left-right drift often seen in walking.
        final_x = int(current_x + center_x + math.sin(phase * 0.2) * 20) 
        final_y = int(current_y + center_y)
        
        animated_points[name] = (final_x, final_y)

    return animated_points

# --- Main Game Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Clear the screen with black background

    # Update animation phase for the next frame
    current_phase = (current_phase + WALKING_SPEED) % (2 * math.pi)

    # Get the current positions of all points
    current_point_positions = get_point_positions(current_phase)

    # Draw each point as a white circle
    for name, pos in current_point_positions.items():
        pygame.draw.circle(screen, WHITE, pos, POINT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen
    clock.tick(FPS)       # Control the frame rate

pygame.quit()
