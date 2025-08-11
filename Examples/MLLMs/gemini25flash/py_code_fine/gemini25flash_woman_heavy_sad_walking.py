
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
POINT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# --- Animation Parameters for "sad woman, heavy weight walking" ---
# Overall gait parameters
# Slower speed and reduced amplitudes contribute to the impression of "sad" and "heavy weight"
WALK_SPEED = 0.04  # Radians per frame (a lower value, e.g., 0.04-0.06, results in a slower, heavier gait)
BODY_Y_BOB_AMPLITUDE = 5  # Vertical bob of the entire figure (less for heavy, typical range 5-10 pixels)
BODY_X_SWAY_AMPLITUDE = 0 # Overall side-to-side sway of the torso (set to 0 for a straight front view walk)

# Initial relative positions for the 15 points
# These coordinates define the "standing" pose of the figure, relative to its center.
# The selection of points generally follows standard biomechanical models for point-light walkers.
# The order is consistent with the `point_names` list for easy indexing.
initial_positions = [
    (0,   -180), # 1. Head (topmost point)
    (-40, -100), # 2. Left Shoulder
    (40,  -100), # 3. Right Shoulder
    (-60, -40),  # 4. Left Elbow
    (60,  -40),  # 5. Right Elbow
    (-70, 20),   # 6. Left Wrist
    (70,  20),   # 7. Right Wrist
    (-25, 0),    # 8. Left Hip (approximate location of hip joint relative to torso center)
    (25,  0),    # 9. Right Hip
    (-35, 70),   # 10. Left Knee
    (35,  70),   # 11. Right Knee
    (-25, 140),  # 12. Left Ankle
    (25,  140),  # 13. Right Ankle
    (-35, 160),  # 14. Left Foot (representing the toe/ball of the foot)
    (35,  160),  # 15. Right Foot
]
assert len(initial_positions) == 15, "The number of initial positions must be exactly 15."

# Motion parameters for each point, defining their oscillation during the walk cycle.
# Format: (amplitude_x, amplitude_y, phase_offset_x, phase_offset_y, base_phase_modifier)
# - amplitude_x, amplitude_y: Max displacement from the point's base position in X and Y.
#   Reduced amplitudes contribute to the "heavy weight" and "sad" impression.
# - phase_offset_x, phase_offset_y: Shifts the sine wave for X and Y motion relative to `effective_phase`.
# - base_phase_modifier: Determines if the limb moves with the left leg's cycle (0) or
#   the right leg's cycle (math.pi, 180 degrees out of phase). This creates natural arm-leg
#   counter-swing.
motion_profiles = {
    "head":        (2,   4,  math.pi/2, math.pi/2, 0), # Slight bobbing and subtle forward/back sway
    
    "L_shoulder":  (10,  3,  0,         math.pi/2, math.pi), # Left shoulder swings forward with Right leg (phase pi)
    "R_shoulder":  (10,  3,  0,         math.pi/2, 0),       # Right shoulder swings forward with Left leg (phase 0)

    "L_elbow":     (18,  5,  0,         math.pi/2, math.pi), # Left arm swings (slightly more amplitude than shoulder)
    "R_elbow":     (18,  5,  0,         math.pi/2, 0),       # Right arm swings
    "L_wrist":     (22,  7,  0,         math.pi/2, math.pi), # Wrist swings with more amplitude than elbow
    "R_wrist":     (22,  7,  0,         math.pi/2, 0),

    "L_hip":       (5,   2,  math.pi/2, math.pi/2, 0), # Left hip moves slightly with Left leg
    "R_hip":       (5,   2, -math.pi/2, math.pi/2, 0), # Right hip moves slightly opposite to Left hip (via phase_offset_x)

    "L_knee":      (40,  20, 0,         math.pi/4, 0), # Left knee swings forward and bends (Y-movement)
    "R_knee":      (40,  20, 0,         math.pi/4, math.pi), # Right knee is out of phase with Left knee
    "L_ankle":     (45,  25, 0,         math.pi/8, 0), # Left ankle trails knee, with more vertical movement for foot clearance
    "R_ankle":     (45,  25, 0,         math.pi/8, math.pi), # Right ankle is out of phase
    "L_foot":      (50,  30, 0,         math.pi/2, 0), # Left foot swings widely, lifts during mid-swing
    "R_foot":      (50,  30, 0,         math.pi/2, math.pi), # Right foot is out of phase
}

# The names of the points in the exact order they appear in `initial_positions`
point_names = [
    "head", "L_shoulder", "R_shoulder", "L_elbow", "R_elbow", "L_wrist", "R_wrist",
    "L_hip", "R_hip", "L_knee", "R_knee", "L_ankle", "R_ankle", "L_foot", "R_foot"
]

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman with Heavy Weight Walking")
    clock = pygame.time.Clock()

    running = True
    walk_cycle_phase = 0.0 # Represents the current phase of the walking cycle, from 0 to 2*pi

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK) # Clear the screen with black background

        # Calculate overall body bobbing (vertical displacement of the entire figure)
        # This uses a cosine wave with double frequency (2 * walk_cycle_phase) to create two bob peaks
        # per full walk cycle (typically corresponding to the mid-stance/double support phases).
        # (1 - math.cos(...)) ensures the bobbing motion is always downwards from a baseline, then upwards.
        body_y_offset = BODY_Y_BOB_AMPLITUDE * (1 - math.cos(walk_cycle_phase * 2))

        # Calculate overall body side-to-side sway (minimal for straight walking)
        body_x_offset = BODY_X_SWAY_AMPLITUDE * math.sin(walk_cycle_phase)

        current_points = []
        for i, name in enumerate(point_names):
            base_x, base_y = initial_positions[i]
            amp_x, amp_y, phase_offset_x, phase_offset_y, base_phase_modifier = motion_profiles[name]

            # Determine the effective phase for this specific point's oscillation.
            # This incorporates the `base_phase_modifier` to ensure limbs move in/out of phase correctly.
            effective_phase = walk_cycle_phase + base_phase_modifier

            # Calculate individual point oscillations using sine waves.
            # `math.sin` is used for both X (forward/backward motion) and Y (up/down motion, e.g., knee bend, foot lift).
            offset_x = amp_x * math.sin(effective_phase + phase_offset_x)
            offset_y = amp_y * math.sin(effective_phase + phase_offset_y)

            # Combine the initial static position, the overall body movement, and the limb-specific oscillation
            # to get the final position for the current frame.
            final_x = SCREEN_WIDTH // 2 + base_x + body_x_offset + offset_x
            final_y = SCREEN_HEIGHT // 2 + base_y + body_y_offset + offset_y
            
            current_points.append((int(final_x), int(final_y)))

        # Draw all 15 points as white circles
        for point_pos in current_points:
            pygame.draw.circle(screen, WHITE, point_pos, POINT_RADIUS)

        pygame.display.flip() # Update the full display Surface to the screen

        # Update walk cycle phase for the next frame, wrapping around at 2*pi (a full cycle)
        walk_cycle_phase = (walk_cycle_phase + WALK_SPEED) % (2 * math.pi)
        clock.tick(FPS) # Control the frame rate

    pygame.quit() # Uninitialize pygame modules

if __name__ == "__main__":
    main()
