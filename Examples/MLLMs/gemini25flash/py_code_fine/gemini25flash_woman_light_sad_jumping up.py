
import pygame
import math
import numpy as np

# --- Pygame Setup ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POINT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Jumping Up (Sadwoman with light weight)")
clock = pygame.time.Clock()

# --- Human Model Joint Names ---
# These 15 joints correspond to the example image structure
JOINT_NAMES = [
    "head", "neck",
    "right_shoulder", "left_shoulder",
    "right_elbow", "left_elbow",
    "right_wrist", "left_wrist",
    "pelvis_center",
    "right_hip", "left_hip",
    "right_knee", "left_knee",
    "right_ankle", "left_ankle"
]

class HumanFigure:
    def __init__(self, scale=1.0):
        self.scale = scale
        # current_joint_coords_relative stores interpolated joint positions,
        # where pelvis_center for the current pose is always (0,0) in this local frame.
        self.current_joint_coords_relative = {} 
        
        # Pose definitions:
        # Each pose defines:
        # 1. "pelvis_offset_y_from_standing": How much the pelvis_center moves vertically from its
        #    standing Y position *due to body shape change* (e.g., crouching lowers pelvis).
        #    Positive value means pelvis moves DOWN (towards positive Y in local frame).
        # 2. "joint_coords": Dictionary of (x,y) for each joint, RELATIVE to the pelvis_center (0,0)
        #    of this specific pose. Y-coords are negative for points above pelvis_center, positive for below.
        
        # Pose 1: Stand (relaxed and slightly slumped for 'sad' effect)
        self.pose_stand = {
            "pelvis_offset_y_from_standing": 0.0,
            "joint_coords": {
                "pelvis_center": (0.0, 0.0),
                "neck": (0.0, -0.15),
                "head": (0.0, -0.22),
                "right_shoulder": (-0.06, -0.17), "left_shoulder": (0.06, -0.17),
                "right_elbow": (-0.08, -0.05), "left_elbow": (0.08, -0.05),
                "right_wrist": (-0.09, 0.05), "left_wrist": (0.09, 0.05),
                "right_hip": (-0.05, 0.01), "left_hip": (0.05, 0.01),
                "right_knee": (-0.05, 0.2), "left_knee": (0.05, 0.2),
                "right_ankle": (-0.05, 0.4), "left_ankle": (0.05, 0.4)
            }
        }

        # Pose 2: Crouch (prepare for jump - deep bend, arms back)
        self.pose_crouch = {
            "pelvis_offset_y_from_standing": 0.15, # Pelvis moves down
            "joint_coords": {
                "pelvis_center": (0.0, 0.0), 
                "neck": (0.0, -0.10), # Torso slightly forward
                "head": (0.0, -0.17),
                "right_shoulder": (-0.07, -0.12), "left_shoulder": (0.07, -0.12),
                "right_elbow": (-0.12, -0.05), "left_elbow": (0.12, -0.05),
                "right_wrist": (-0.15, 0.05), "left_wrist": (0.15, 0.05),
                "right_hip": (-0.05, 0.02), "left_hip": (0.05, 0.02),
                "right_knee": (-0.04, 0.15), # Deep bend
                "left_knee": (0.04, 0.15),
                "right_ankle": (-0.03, 0.3),
                "left_ankle": (0.03, 0.3)
            }
        }

        # Pose 3: Take-off / Propulsion (legs extending, arms swinging up)
        self.pose_takeoff = {
            "pelvis_offset_y_from_standing": 0.05, # Pelvis slightly down, but rising fast
            "joint_coords": {
                "pelvis_center": (0.0, 0.0),
                "neck": (0.0, -0.15),
                "head": (0.0, -0.22),
                "right_shoulder": (-0.06, -0.20), "left_shoulder": (0.06, -0.20), # Arms swinging up
                "right_elbow": (-0.08, -0.10), "left_elbow": (0.08, -0.10),
                "right_wrist": (-0.09, -0.0), "left_wrist": (0.09, -0.0),
                "right_hip": (-0.05, 0.01), "left_hip": (0.05, 0.01),
                "right_knee": (-0.05, 0.1), # Legs extending
                "left_knee": (0.05, 0.1),
                "right_ankle": (-0.05, 0.2), # On toes
                "left_ankle": (0.05, 0.2)
            }
        }

        # Pose 4: Apex (at peak of jump, body relatively stretched and floating)
        self.pose_apex = {
            "pelvis_offset_y_from_standing": 0.0, # Pelvis returns to its 'standing' height relative to its *own feet*
            "joint_coords": {
                "pelvis_center": (0.0, 0.0),
                "neck": (0.0, -0.18),
                "head": (0.0, -0.25),
                "right_shoulder": (-0.06, -0.25), "left_shoulder": (0.06, -0.25), # Arms up
                "right_hip": (-0.05, 0.00), "left_hip": (0.05, 0.00),
                "right_elbow": (-0.06, -0.15), "left_elbow": (0.06, -0.15),
                "right_wrist": (-0.06, -0.05), "left_wrist": (0.06, -0.05),
                "right_knee": (-0.05, 0.1), "left_knee": (0.05, 0.1),
                "right_ankle": (-0.05, 0.25), "left_ankle": (0.05, 0.25)
            }
        }

        # Pose 5: Landing (body preparing for impact, similar to crouch)
        self.pose_landing = {
            "pelvis_offset_y_from_standing": 0.10, # Pelvis moves down, absorbing impact
            "joint_coords": {
                "pelvis_center": (0.0, 0.0),
                "neck": (0.0, -0.10),
                "head": (0.0, -0.17),
                "right_shoulder": (-0.06, -0.15), "left_shoulder": (0.06, -0.15), # Arms coming down
                "right_hip": (-0.05, 0.02), "left_hip": (0.05, 0.02),
                "right_elbow": (-0.08, -0.05), "left_elbow": (0.08, -0.05),
                "right_wrist": (-0.09, 0.05), "left_wrist": (0.09, 0.05),
                "right_knee": (-0.04, 0.18), # Deep bend
                "left_knee": (0.04, 0.18),
                "right_ankle": (-0.03, 0.35),
                "left_ankle": (0.03, 0.35)
            }
        }
        
        # Calculate the Y distance from pelvis_center to the lowest point of the feet
        # for the standing pose. This helps anchor the figure to the ground.
        # Assuming ankle is the lowest point.
        self.standing_pelvis_to_feet_y_dist_rel = \
            max(self.pose_stand["joint_coords"]["right_ankle"][1], self.pose_stand["joint_coords"]["left_ankle"][1]) - \
            self.pose_stand["joint_coords"]["pelvis_center"][1]
        
        # This variable will store the global vertical displacement of the *feet* from the ground.
        # 0 means feet are on ground. Positive value means jumping up.
        self.figure_global_vertical_offset_rel = 0.0 

        # Initialize current pose to the standing pose
        self.set_current_pose(self.pose_stand, self.pose_stand, 0.0)

    def set_current_pose(self, pose1, pose2, alpha):
        """
        Interpolates body shape and pelvis_center vertical offset between two poses.
        alpha = 0 means pose1, alpha = 1 means pose2.
        """
        # Interpolate pelvis_center's vertical offset due to body bending/straightening.
        self.current_pelvis_body_offset_y_rel = (1 - alpha) * pose1["pelvis_offset_y_from_standing"] + \
                                                  alpha * pose2["pelvis_offset_y_from_standing"]
        
        # Interpolate coordinates for all joints, relative to their pose's pelvis_center (0,0).
        for joint_name in JOINT_NAMES:
            x1, y1 = pose1["joint_coords"][joint_name]
            x2, y2 = pose2["joint_coords"][joint_name]
            
            interpolated_x = (1 - alpha) * x1 + alpha * x2
            interpolated_y = (1 - alpha) * y1 + alpha * y2
            
            self.current_joint_coords_relative[joint_name] = np.array([interpolated_x, interpolated_y])

    def get_screen_coords(self):
        """
        Calculates and returns a list of (x, y) tuples for all 15 joints,
        converted to Pygame screen coordinates.
        """
        screen_coords = []
        
        # 1. Determine the Pygame Y coordinate of the "pelvis center when standing".
        # This anchors the figure relative to the GROUND_LEVEL.
        # `GROUND_LEVEL` is the bottom of the feet. `standing_pelvis_to_feet_y_dist_rel` is the distance UP from feet to pelvis.
        pelvis_y_standing_on_screen_px = GROUND_LEVEL - (self.standing_pelvis_to_feet_y_dist_rel * self.scale)
        
        # 2. Calculate the actual Pygame Y coordinate of the current pelvis_center.
        # This accounts for:
        #    a) its "standing" base Y position,
        #    b) its displacement due to body shape changes (e.g., crouching),
        #    c) its global jump height (figure's overall vertical movement).
        
        # Pygame Y-axis increases downwards.
        # - `current_pelvis_body_offset_y_rel`: Positive when pelvis moves DOWN (crouch), so ADD to Y.
        # - `figure_global_vertical_offset_rel`: Positive when figure moves UP (jump), so SUBTRACT from Y.
        
        current_pelvis_center_y_px = pelvis_y_standing_on_screen_px + \
                                     (self.current_pelvis_body_offset_y_rel * self.scale) - \
                                     (self.figure_global_vertical_offset_rel * self.scale)
        
        # Pelvis center X (constant for a jump in place)
        current_pelvis_center_x_px = SCREEN_WIDTH / 2
        
        # Calculate absolute screen coordinates for all joints based on the current pelvis_center.
        for joint_name in JOINT_NAMES:
            x_rel, y_rel = self.current_joint_coords_relative[joint_name]
            
            screen_x = current_pelvis_center_x_px + (x_rel * self.scale)
            screen_y = current_pelvis_center_y_px + (y_rel * self.scale) 

            screen_coords.append((int(screen_x), int(screen_y)))
        return screen_coords

# --- Animation Control Parameters ---
FIGURE_SCALE = SCREEN_HEIGHT / 2.5 # Make figure about 40% of screen height
GROUND_LEVEL = SCREEN_HEIGHT * 0.8 # The Y-coordinate where the character's feet touch the ground

human_figure = HumanFigure(scale=FIGURE_SCALE)

# Define durations for each animation phase (in frames at 60 FPS)
PHASE_DURATIONS = {
    "stand_to_crouch": 20,      # Initial stand to deep crouch
    "crouch_to_takeoff": 15,    # Deep crouch to just before leaving ground
    "takeoff_to_apex": 20,      # Leaving ground to peak height
    "apex_to_landing": 20,      # Peak height to landing impact
    "landing_to_stand": 15,     # Absorb impact to recover to stand
    "pause_at_stand": 30        # A short pause before next jump cycle
}

# Define the sequence of poses for the animation
animation_phases = [
    ("stand_to_crouch", human_figure.pose_stand, human_figure.pose_crouch),
    ("crouch_to_takeoff", human_figure.pose_crouch, human_figure.pose_takeoff),
    ("takeoff_to_apex", human_figure.pose_takeoff, human_figure.pose_apex),
    ("apex_to_landing", human_figure.pose_apex, human_figure.pose_landing),
    ("landing_to_stand", human_figure.pose_landing, human_figure.pose_stand),
    ("pause_at_stand", human_figure.pose_stand, human_figure.pose_stand) # Effectively a pause
]

current_phase_idx = 0
frame_in_phase = 0

# Maximum jump height for the entire figure, relative to FIGURE_SCALE
MAX_JUMP_HEIGHT_REL = 0.35 # Slightly higher for "light weight" feel

def ease_in_out_cubic(t):
    """Cubic easing function for smooth interpolation."""
    return t * t * (3 - 2 * t)

def get_parabolic_height(progress):
    """
    Calculates height based on a parabolic trajectory.
    progress: 0 (start of arc) to 1 (end of arc)
    Returns height (0 at ends, max at 0.5)
    """
    # Simple parabola: y = -4x(x-1) for x in [0,1]
    return -4 * progress * (progress - 1)

# --- Main Animation Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current phase details
    current_phase_name, pose_start, pose_end = animation_phases[current_phase_idx]
    duration = PHASE_DURATIONS[current_phase_name]

    # Calculate alpha for pose interpolation, applying easing for smoother transitions
    alpha_raw = frame_in_phase / duration if duration > 0 else 1.0
    alpha_eased = ease_in_out_cubic(alpha_raw)
    
    # Update the human figure's internal body pose
    human_figure.set_current_pose(pose_start, pose_end, alpha_eased)

    # Update the global vertical offset (jump height) for the entire figure
    if current_phase_name == "takeoff_to_apex":
        # First half of the parabolic arc (ascending)
        progress_in_air = alpha_raw # 0 to 1
        human_figure.figure_global_vertical_offset_rel = get_parabolic_height(progress_in_air) * MAX_JUMP_HEIGHT_REL
    elif current_phase_name == "apex_to_landing":
        # Second half of the parabolic arc (descending)
        progress_in_air = 1.0 - alpha_raw # 1 to 0 (reversed progress for descent)
        human_figure.figure_global_vertical_offset_rel = get_parabolic_height(progress_in_air) * MAX_JUMP_HEIGHT_REL
    else:
        # Grounded phases - no global vertical jump offset
        human_figure.figure_global_vertical_offset_rel = 0.0

    # Advance frame and transition to the next phase if current one is complete
    frame_in_phase += 1
    if frame_in_phase >= duration:
        frame_in_phase = 0
        current_phase_idx = (current_phase_idx + 1) % len(animation_phases)

    # --- Drawing ---
    screen.fill(BLACK) # Solid black background

    # Get the calculated joint positions in screen coordinates
    joint_screen_coords = human_figure.get_screen_coords()

    # Draw each point (white circles)
    for x, y in joint_screen_coords:
        pygame.draw.circle(screen, WHITE, (x, y), POINT_RADIUS)

    pygame.display.flip() # Update the entire display Surface to the screen

    clock.tick(FPS) # Control the frame rate

pygame.quit()
