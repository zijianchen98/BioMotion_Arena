
import pygame
import math
import sys

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 5
FPS = 60

# --- Joint Mapping and Order ---
# These are the 15 points based on the example image's structure.
# The order defines their index in the `points_pos` list.
JOINT_NAMES_ORDER = [
    "Head",          # 0
    "Shoulder_R",    # 1 (Figure's Right Shoulder)
    "Shoulder_L",    # 2 (Figure's Left Shoulder)
    "Elbow_R",       # 3
    "Elbow_L",       # 4
    "Wrist_R",       # 5
    "Wrist_L",       # 6
    "Spine_Upper",   # 7 (Chest/Sternum region)
    "Spine_Lower",   # 8 (Pelvis Center region)
    "Hip_R",         # 9
    "Hip_L",         # 10
    "Knee_R",        # 11
    "Knee_L",        # 12
    "Ankle_R",       # 13
    "Ankle_L"        # 14
]

# Map names to their indices for quick lookup
JOINT_INDICES = {name: i for i, name in enumerate(JOINT_NAMES_ORDER)}

# --- Biomechanical Model Definition ---
# Define segments as a dictionary. Each key is the child joint name.
# Value is (parent_joint_name, length, initial_relative_angle)
#
# initial_relative_angle:
# - For children of "root" (Spine_Lower), this is the segment's initial absolute world angle (from world positive X-axis).
#   e.g., math.pi/2 is straight up.
# - For other segments, this is the segment's initial angle relative to its parent's bone direction.
#   e.g., if parent bone is pointing up (world angle pi/2), and initial_relative_angle is 0,
#   then the child bone also points up. If initial_relative_angle is -math.pi/2, child bone points horizontally right.

# Segment lengths (arbitrary units, will be scaled to screen pixels)
SEGMENT_LEN_SPINE_UPPER = 40
SEGMENT_LEN_HEAD = 25
SEGMENT_LEN_TORSO_WIDTH_HALF = 20 # Half-width from spine to shoulder

SEGMENT_LEN_UPPER_ARM = 50
SEGMENT_LEN_FOREARM = 40

SEGMENT_LEN_HIP_WIDTH_HALF = 15 # Half-width from spine to hip
SEGMENT_LEN_THIGH = 60
SEGMENT_LEN_SHIN = 55

SEGMENT_DEFINITIONS = {
    "Spine_Lower":       ("root", 0, 0), # Root point, its position is the figure's origin

    # Children of "root" (Spine_Lower) - angles are initial world angles
    "Spine_Upper":       ("Spine_Lower", SEGMENT_LEN_SPINE_UPPER, math.pi/2), # Points straight up from Spine_Lower
    "Hip_R":             ("Spine_Lower", SEGMENT_LEN_HIP_WIDTH_HALF, -0.2), # Slightly down-right from Spine_Lower
    "Hip_L":             ("Spine_Lower", SEGMENT_LEN_HIP_WIDTH_HALF, math.pi + 0.2), # Slightly down-left from Spine_Lower

    # Children of other joints - angles are relative to parent's bone direction
    "Head":              ("Spine_Upper", SEGMENT_LEN_HEAD, 0), # Continues straight up from Spine_Upper
    
    "Shoulder_R":        ("Spine_Upper", SEGMENT_LEN_TORSO_WIDTH_HALF, -math.pi/2), # Relative to Spine_Upper (up), -pi/2 means horizontal right
    "Shoulder_L":        ("Spine_Upper", SEGMENT_LEN_TORSO_WIDTH_HALF, math.pi/2), # Relative to Spine_Upper (up), +pi/2 means horizontal left

    "Elbow_R":           ("Shoulder_R", SEGMENT_LEN_UPPER_ARM, -math.pi/2), # Relative to Shoulder_R bone (horizontal), -pi/2 means straight down
    "Wrist_R":           ("Elbow_R", SEGMENT_LEN_FOREARM, 0), # Relative to Elbow_R bone (down), 0 means continues straight down

    "Elbow_L":           ("Shoulder_L", SEGMENT_LEN_UPPER_ARM, -math.pi/2), # Relative to Shoulder_L bone (horizontal), -pi/2 means straight down
    "Wrist_L":           ("Elbow_L", SEGMENT_LEN_FOREARM, 0), # Relative to Elbow_L bone (down), 0 means continues straight down

    "Knee_R":            ("Hip_R", SEGMENT_LEN_THIGH, -math.pi/2), # Relative to Hip_R bone (down-right), -pi/2 means further down
    "Ankle_R":           ("Knee_R", SEGMENT_LEN_SHIN, 0), # Relative to Knee_R bone (down), 0 means continues straight down

    "Knee_L":            ("Hip_L", SEGMENT_LEN_THIGH, -math.pi/2),
    "Ankle_L":           ("Knee_L", SEGMENT_LEN_SHIN, 0),
}

# The processing order is crucial for correct Forward Kinematics (FK).
# Parent joints must be calculated before their children.
PROCESSING_ORDER = [
    "Spine_Lower", "Spine_Upper", "Head",
    "Shoulder_R", "Elbow_R", "Wrist_R",
    "Shoulder_L", "Elbow_L", "Wrist_L",
    "Hip_R", "Knee_R", "Ankle_R",
    "Hip_L", "Knee_L", "Ankle_L"
]

class Humanoid:
    def __init__(self, center_x, center_y):
        self.figure_origin = (center_x, center_y) # Screen center for Spine_Lower
        self.scale = 1.2 # Adjust overall size of the figure

        # Stores the (x,y) screen coordinates of the 15 points
        self.points_pos = [(0,0)] * 15
        # Stores the world angle (from positive X-axis) of the segment leading to each point
        self.points_world_angle = {}

        self.time = 0.0

        # Animation parameters for "waving a hand with heavy weight"
        # Slower frequency and slightly restrained amplitudes to convey "heavy weight"
        self.wave_frequency = 0.7 # Hz, cycles per second
        self.shoulder_swing_amplitude = math.radians(65) # Max swing range for upper arm (shoulder joint)
        self.elbow_bend_amplitude = math.radians(40)    # Max bend range for forearm (elbow joint)
        self.initial_elbow_bend = math.radians(20)      # Keep elbow slightly bent at rest

    def update(self, dt):
        self.time += dt

        # Reset world angles for calculation in this frame
        self.points_world_angle = {}

        # Set the root point (Spine_Lower) position and initial world angle (conceptual for its outgoing segments)
        self.points_pos[JOINT_INDICES["Spine_Lower"]] = self.figure_origin
        # Conceptually, the Spine_Lower segment itself points up, establishing world "up" for its children
        self.points_world_angle["Spine_Lower"] = math.pi / 2 

        # Calculate positions for all other points based on the kinematic chain
        for joint_name in PROCESSING_ORDER:
            if joint_name == "Spine_Lower":
                continue # Root is already handled

            parent_name, length, initial_relative_angle = SEGMENT_DEFINITIONS[joint_name]
            parent_pos = self.points_pos[JOINT_INDICES[parent_name]]
            
            # Get parent's world angle. For children of "root", parent_world_angle is effectively the figure's orientation.
            parent_world_angle = self.points_world_angle[parent_name] if parent_name != "root" else 0 # Root has no parent angle to inherit from explicitly

            # Determine the angle for the current segment relative to its parent's bone direction
            current_segment_relative_angle = initial_relative_angle
            
            # Apply animation to the Right Arm (Elbow_R and Wrist_R segments)
            if joint_name == "Elbow_R": # This segment represents the upper arm (from Shoulder_R to Elbow_R)
                # Apply shoulder flexion/extension for the waving motion
                # Wave offset added to the initial relative angle of the upper arm segment
                wave_offset = self.shoulder_swing_amplitude * math.sin(self.time * 2 * math.pi * self.wave_frequency)
                current_segment_relative_angle += wave_offset
            elif joint_name == "Wrist_R": # This segment represents the forearm (from Elbow_R to Wrist_R)
                # Apply elbow flexion/extension. Use 1 - cos for a bend-unbend motion.
                # `* 1.5` for slightly faster elbow bend relative to shoulder swing
                # `+ self.initial_elbow_bend` keeps the elbow from fully straightening
                wave_offset = self.elbow_bend_amplitude * (1 - math.cos(self.time * 2 * math.pi * self.wave_frequency * 1.5))
                current_segment_relative_angle += wave_offset + self.initial_elbow_bend

            # Calculate the world angle of the segment leading to the current joint
            # If the parent is the conceptual "root", the relative angle is already the world angle.
            # Otherwise, sum parent's world angle and current segment's relative angle.
            if parent_name == "root":
                current_segment_world_angle = current_segment_relative_angle
            else:
                current_segment_world_angle = parent_world_angle + current_segment_relative_angle
            
            # Store the calculated world angle of this segment for its children to use
            self.points_world_angle[joint_name] = current_segment_world_angle

            # Calculate the (x,y) position of the current joint
            dx = length * self.scale * math.cos(current_segment_world_angle)
            dy = length * self.scale * math.sin(current_segment_world_angle) # Pygame Y-axis is inverted (positive downwards)
            
            self.points_pos[JOINT_INDICES[joint_name]] = (
                parent_pos[0] + dx,
                parent_pos[1] - dy # Subtract dy to move upwards on the screen
            )

    def draw(self, screen):
        # Draw each of the 15 points
        for pos in self.points_pos:
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus - Waving with Heavy Weight")
clock = pygame.time.Clock()

# Create humanoid instance, placing its base (Spine_Lower) at the bottom-middle of the screen
humanoid = Humanoid(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.7) 

running = True
while running:
    dt = clock.tick(FPS) / 1000.0 # Time since last frame in seconds, for smooth, frame-rate independent animation

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    humanoid.update(dt)

    screen.fill(BLACK) # Clear the screen with a black background
    humanoid.draw(screen) # Draw the updated point-light figure
    pygame.display.flip() # Update the full display Surface to the screen

pygame.quit()
sys.exit()
