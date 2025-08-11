
import pygame
import math

# --- Pygame Initialization ---
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Woman Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Dot properties
DOT_RADIUS = 5

# Animation parameters
FPS = 60
ANIMATION_DURATION = 4  # seconds for one full bow cycle (down and up)
TOTAL_FRAMES = FPS * ANIMATION_DURATION
current_frame = 0

# Biomechanical Model Parameters (proportional to total figure dimensions)
PERSON_HEIGHT = SCREEN_HEIGHT * 0.6  # Make the person fill about 60% of screen height
PERSON_WIDTH = PERSON_HEIGHT * 0.3 # Approx 1:3 ratio for width to height

# Segment lengths (these determine the distances between the 15 points)
# All lengths are relative to PERSON_HEIGHT or PERSON_WIDTH.
HEAD_LENGTH = PERSON_HEIGHT * 0.08      # Top of head to base of head (for head point placement)
NECK_LENGTH = PERSON_HEIGHT * 0.05      # Neck point to top of spine (where shoulder line is)
SPINE_LENGTH = PERSON_HEIGHT * 0.25     # From pelvis to top of spine (neck base)
UPPER_ARM_LENGTH = PERSON_HEIGHT * 0.15
LOWER_ARM_LENGTH = PERSON_HEIGHT * 0.15
UPPER_LEG_LENGTH = PERSON_HEIGHT * 0.2
LOWER_LEG_LENGTH = PERSON_HEIGHT * 0.2
SHOULDER_WIDTH_HALF = PERSON_WIDTH * 0.4 # Half the distance between shoulders
HIP_WIDTH_HALF = PERSON_WIDTH * 0.3      # Half the distance between hips

# Base position for the figure's pelvis (screen coordinates).
# This point will serve as the root for our kinematic chain calculations.
PELVIS_BASE_X = SCREEN_WIDTH // 2
PELVIS_BASE_Y = SCREEN_HEIGHT * 0.5 # Mid-screen vertically for pelvis to allow full motion

class HumanSkeleton:
    def __init__(self, base_x, base_y, person_height, person_width):
        self.base_x = base_x
        self.base_y = base_y
        self.h = person_height
        self.w = person_width

        # Store segment lengths for easy access
        self.lengths = {
            "head": HEAD_LENGTH, "neck": NECK_LENGTH, "spine": SPINE_LENGTH,
            "upper_arm": UPPER_ARM_LENGTH, "lower_arm": LOWER_ARM_LENGTH,
            "upper_leg": UPPER_LEG_LENGTH, "lower_leg": LOWER_LEG_LENGTH,
            "shoulder_width_half": SHOULDER_WIDTH_HALF, "hip_width_half": HIP_WIDTH_HALF
        }

        # Dictionary to store current joint angles (in radians) and pelvis vertical offset.
        # Angles are relative to their parent segment's orientation, unless specified as global.
        # 0 radians typically means pointing straight down (positive Y direction in Pygame).
        # Positive angles indicate clockwise rotation.
        self.angles = {}
        # Dictionary to store the calculated (x, y) coordinates of each point.
        self.current_points = {}
        self.reset_pose()

    def reset_pose(self):
        # Default standing pose angles (all segments generally vertical)
        self.angles = {
            "pelvis_y_offset": 0, # Vertical displacement of the pelvis from its base_y
            "spine_rot": 0.0,       # Rotation of the spine (pelvis to neck) relative to global vertical
            "neck_rot": 0.0,        # Rotation of the head (neck to head) relative to the spine segment
            "shoulder_L_rot": math.radians(0),  # Rotation of left upper arm relative to spine segment
            "shoulder_R_rot": math.radians(0), # Symmetric for right
            "elbow_L_rot": math.radians(0), # Rotation of left lower arm relative to left upper arm
            "elbow_R_rot": math.radians(0), # Symmetric for right
            "hip_L_rot": math.radians(0),   # Rotation of left upper leg relative to global vertical
            "hip_R_rot": math.radians(0),   # Symmetric for right
            "knee_L_rot": math.radians(0),  # Rotation of left lower leg relative to left upper leg
            "knee_R_rot": math.radians(0),  # Symmetric for right
        }
        self._calculate_current_points()

    def set_pose_angles(self, pelvis_y_offset, spine_rot, neck_rot,
                        shoulder_rot, elbow_rot, hip_rot, knee_rot):
        """
        Sets all the joint angles for the skeleton and recalculates point positions.
        All angles should be in radians.
        shoulder_rot, elbow_rot, hip_rot, knee_rot are applied symmetrically for left and right.
        """
        self.angles["pelvis_y_offset"] = pelvis_y_offset
        self.angles["spine_rot"] = spine_rot
        self.angles["neck_rot"] = neck_rot
        self.angles["shoulder_L_rot"] = shoulder_rot
        self.angles["shoulder_R_rot"] = -shoulder_rot # Right arm typically mirrors left
        self.angles["elbow_L_rot"] = elbow_rot
        self.angles["elbow_R_rot"] = -elbow_rot       # Right arm typically mirrors left
        self.angles["hip_L_rot"] = hip_rot
        self.angles["hip_R_rot"] = hip_rot
        self.angles["knee_L_rot"] = knee_rot
        self.angles["knee_R_rot"] = knee_rot
        self._calculate_current_points()

    def _calculate_current_points(self):
        """
        Calculates the (x, y) coordinates for all 15 points based on current joint angles.
        Uses forward kinematics starting from the pelvis.
        """
        # 1. Pelvis point (root of the kinematic chain)
        pelvis_x = self.base_x
        pelvis_y = self.base_y + self.angles["pelvis_y_offset"]

        # 2. Leg points (Hips, Knees, Ankles)
        # Hips are offset from pelvis
        hip_L_x = pelvis_x - self.lengths["hip_width_half"]
        hip_L_y = pelvis_y

        hip_R_x = pelvis_x + self.lengths["hip_width_half"]
        hip_R_y = pelvis_y

        # Knees: Calculated from hips, using hip_L/R_rot (global angle of upper leg)
        knee_L_x = hip_L_x + self.lengths["upper_leg"] * math.sin(self.angles["hip_L_rot"])
        knee_L_y = hip_L_y + self.lengths["upper_leg"] * math.cos(self.angles["hip_L_rot"]) # Y increases down

        knee_R_x = hip_R_x + self.lengths["upper_leg"] * math.sin(self.angles["hip_R_rot"])
        knee_R_y = hip_R_y + self.lengths["upper_leg"] * math.cos(self.angles["hip_R_rot"])

        # Ankles: Calculated from knees, using knee_L/R_rot (relative to upper leg)
        # Global angle of lower leg = global angle of upper leg + relative angle of lower leg
        ankle_L_global_angle = self.angles["hip_L_rot"] + self.angles["knee_L_rot"]
        ankle_L_x = knee_L_x + self.lengths["lower_leg"] * math.sin(ankle_L_global_angle)
        ankle_L_y = knee_L_y + self.lengths["lower_leg"] * math.cos(ankle_L_global_angle)

        ankle_R_global_angle = self.angles["hip_R_rot"] + self.angles["knee_R_rot"]
        ankle_R_x = knee_R_x + self.lengths["lower_leg"] * math.sin(ankle_R_global_angle)
        ankle_R_y = knee_R_y + self.lengths["lower_leg"] * math.cos(ankle_R_global_angle)

        # 3. Torso and Head points (Neck, Head)
        # Neck: Calculated from pelvis, using spine_rot (global angle of spine)
        neck_x = pelvis_x + self.lengths["spine"] * math.sin(self.angles["spine_rot"])
        neck_y = pelvis_y - self.lengths["spine"] * math.cos(self.angles["spine_rot"]) # Y increases up the body

        # Head: Calculated from neck, using neck_rot (relative to spine segment)
        # Global angle of head = global angle of spine + relative angle of head
        head_global_angle = self.angles["spine_rot"] + self.angles["neck_rot"]
        head_x = neck_x + (self.lengths["neck"] + self.lengths["head"]/2) * math.sin(head_global_angle)
        head_y = neck_y - (self.lengths["neck"] + self.lengths["head"]/2) * math.cos(head_global_angle)

        # 4. Arm points (Shoulders, Elbows, Wrists)
        # Shoulders: Offset from neck, rotated with the spine
        # Assuming shoulder_width_half is perpendicular to the spine
        shoulder_L_x = neck_x - self.lengths["shoulder_width_half"] * math.cos(self.angles["spine_rot"])
        shoulder_L_y = neck_y - self.lengths["shoulder_width_half"] * math.sin(self.angles["spine_rot"])

        shoulder_R_x = neck_x + self.lengths["shoulder_width_half"] * math.cos(self.angles["spine_rot"])
        shoulder_R_y = neck_y + self.lengths["shoulder_width_half"] * math.sin(self.angles["spine_rot"])

        # Elbows: Calculated from shoulders, using shoulder_L/R_rot (relative to spine segment)
        # Global angle of upper arm = global angle of spine + relative angle of upper arm
        upper_arm_L_global_angle = self.angles["spine_rot"] + self.angles["shoulder_L_rot"]
        elbow_L_x = shoulder_L_x + self.lengths["upper_arm"] * math.sin(upper_arm_L_global_angle)
        elbow_L_y = shoulder_L_y + self.lengths["upper_arm"] * math.cos(upper_arm_L_global_angle)
        
        upper_arm_R_global_angle = self.angles["spine_rot"] + self.angles["shoulder_R_rot"]
        elbow_R_x = shoulder_R_x + self.lengths["upper_arm"] * math.sin(upper_arm_R_global_angle)
        elbow_R_y = shoulder_R_y + self.lengths["upper_arm"] * math.cos(upper_arm_R_global_angle)

        # Wrists: Calculated from elbows, using elbow_L/R_rot (relative to upper arm)
        # Global angle of lower arm = global angle of upper arm + relative angle of lower arm
        lower_arm_L_global_angle = upper_arm_L_global_angle + self.angles["elbow_L_rot"]
        wrist_L_x = elbow_L_x + self.lengths["lower_arm"] * math.sin(lower_arm_L_global_angle)
        wrist_L_y = elbow_L_y + self.lengths["lower_arm"] * math.cos(lower_arm_L_global_angle)

        lower_arm_R_global_angle = upper_arm_R_global_angle + self.angles["elbow_R_rot"]
        wrist_R_x = elbow_R_x + self.lengths["lower_arm"] * math.sin(lower_arm_R_global_angle)
        wrist_R_y = elbow_R_y + self.lengths["lower_arm"] * math.cos(lower_arm_R_global_angle)

        # Store all 15 points
        self.current_points = {
            "head":       [head_x, head_y],
            "neck":       [neck_x, neck_y],
            "shoulder_L": [shoulder_L_x, shoulder_L_y],
            "shoulder_R": [shoulder_R_x, shoulder_R_y],
            "elbow_L":    [elbow_L_x, elbow_L_y],
            "elbow_R":    [elbow_R_x, elbow_R_y],
            "wrist_L":    [wrist_L_x, wrist_L_y],
            "wrist_R":    [wrist_R_x, wrist_R_y],
            "pelvis":     [pelvis_x, pelvis_y],
            "hip_L":      [hip_L_x, hip_L_y],
            "hip_R":      [hip_R_x, hip_R_y],
            "knee_L":     [knee_L_x, knee_L_y],
            "knee_R":     [knee_R_x, knee_R_y],
            "ankle_L":    [ankle_L_x, ankle_L_y],
            "ankle_R":    [ankle_R_x, ankle_R_y],
        }

    def get_points(self):
        """Returns a list of (x, y) tuples for all 15 points."""
        return list(self.current_points.values())

# Instantiate skeleton model
skeleton = HumanSkeleton(PELVIS_BASE_X, PELVIS_BASE_Y, PERSON_HEIGHT, PERSON_WIDTH)

# Define key poses (start and end) for the bowing animation.
# Angles are defined in degrees for readability, and converted to radians when used.

# Pose 0: Standing, slightly slumped (initial pose of a sad woman)
POSE_STANDING_ANGLES = {
    "pelvis_y_offset": 0,
    "spine_rot": 0,             # Spine is vertical
    "neck_rot": 0,              # Head is vertical relative to spine
    "shoulder_rot": 5,          # Upper arms slightly forward from spine
    "elbow_rot": 0,             # Lower arms straight relative to upper arms
    "hip_rot": 0,               # Upper legs vertical
    "knee_rot": 0               # Lower legs straight relative to upper legs
}

# Pose 1: Bowing with heavy weight (lowest point of the bow)
# This pose implies significant forward bending, body lowering, and arms reaching down.
POSE_BOWING_ANGLES = {
    "pelvis_y_offset": PERSON_HEIGHT * 0.25, # Pelvis lowers, indicating a squat
    "spine_rot": 75,            # Spine bends significantly forward (75 degrees from vertical)
    "neck_rot": 15,             # Head looks further down relative to the bent spine
    "shoulder_rot": -65,        # Upper arms rotate backward relative to spine to point more globally vertical (75 - 65 = 10 degrees from global vertical)
    "elbow_rot": 0,             # Arms stay straight at the elbow, as if holding a rigid object
    "hip_rot": 20,              # Hips flex, upper legs move slightly forward from vertical
    "knee_rot": 50              # Knees bend significantly (50 degrees relative to upper leg)
}

# Convert all angle values in the pose dictionaries from degrees to radians
for pose in [POSE_STANDING_ANGLES, POSE_BOWING_ANGLES]:
    for key, value in pose.items():
        if "rot" in key or "angle" in key: # Identify angle parameters
            pose[key] = math.radians(value)

# Helper function for smooth interpolation (ease-in/ease-out sine wave)
def ease_in_out_sine(t):
    """
    Applies an ease-in-out effect to a linear interpolation factor t.
    t is typically between 0 and 1.
    """
    return -(math.cos(math.pi * t) - 1) / 2

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate animation progress (t goes from 0 to 1 over TOTAL_FRAMES)
    t = (current_frame % TOTAL_FRAMES) / TOTAL_FRAMES
    
    # Apply easing function for smooth motion
    eased_t = ease_in_out_sine(t)

    # Determine which phase of the animation we are in (bowing down or returning up)
    if t < 0.5: # First half: Bowing down from STANDING to BOWING pose
        interp_factor = eased_t * 2 # Scale eased_t from 0-0.5 to 0-1 for this phase
        start_pose = POSE_STANDING_ANGLES
        end_pose = POSE_BOWING_ANGLES
    else: # Second half: Returning up from BOWING to STANDING pose
        interp_factor = (eased_t - 0.5) * 2 # Scale eased_t from 0.5-1.0 to 0-1 for this phase
        start_pose = POSE_BOWING_ANGLES
        end_pose = POSE_STANDING_ANGLES

    # Interpolate all angle and offset parameters based on the current interpolation factor
    current_pelvis_offset = start_pose["pelvis_y_offset"] + (end_pose["pelvis_y_offset"] - start_pose["pelvis_y_offset"]) * interp_factor
    current_spine_rot = start_pose["spine_rot"] + (end_pose["spine_rot"] - start_pose["spine_rot"]) * interp_factor
    current_neck_rot = start_pose["neck_rot"] + (end_pose["neck_rot"] - start_pose["neck_rot"]) * interp_factor
    current_shoulder_rot = start_pose["shoulder_rot"] + (end_pose["shoulder_rot"] - start_pose["shoulder_rot"]) * interp_factor
    current_elbow_rot = start_pose["elbow_rot"] + (end_pose["elbow_rot"] - start_pose["elbow_rot"]) * interp_factor
    current_hip_rot = start_pose["hip_rot"] + (end_pose["hip_rot"] - start_pose["hip_rot"]) * interp_factor
    current_knee_rot = start_pose["knee_rot"] + (end_pose["knee_rot"] - start_pose["knee_rot"]) * interp_factor

    # Update the skeleton's pose with the interpolated angles
    skeleton.set_pose_angles(current_pelvis_offset, current_spine_rot, current_neck_rot,
                             current_shoulder_rot, current_elbow_rot, current_hip_rot,
                             current_knee_rot)

    # --- Drawing ---
    screen.fill(BLACK) # Clear the screen with black background
    
    # Draw each of the 15 white point-lights
    for point_coords in skeleton.get_points():
        pygame.draw.circle(screen, WHITE, (int(point_coords[0]), int(point_coords[1])), DOT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen

    current_frame += 1 # Advance to the next frame
    clock.tick(FPS)    # Control frame rate

pygame.quit() # Uninitialize Pygame and exit
