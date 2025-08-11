
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60
POINT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Body Segment Lengths (in pixels, adjusted by GLOBAL_SCALE) ---
# These lengths define the proportion of the figure.
GLOBAL_SCALE = 100 # Adjust for overall size of the figure on screen

TORSO_LOWER_LEN = 0.3 * GLOBAL_SCALE  # From pelvis_root to lower_torso
TORSO_UPPER_LEN = 0.5 * GLOBAL_SCALE  # From lower_torso to upper_torso
HEAD_LEN = 0.2 * GLOBAL_SCALE         # Length of head itself
NECK_OFFSET = 0.05 * GLOBAL_SCALE     # Small gap/segment for neck from upper_torso to head

SHOULDER_WIDTH_HALF = 0.2 * GLOBAL_SCALE # Half width from upper_torso center to shoulder
HIP_WIDTH_HALF = 0.15 * GLOBAL_SCALE     # Half width from pelvis_root center to hip

UPPER_ARM_LEN = 0.35 * GLOBAL_SCALE # From shoulder to elbow
FOREARM_LEN = 0.35 * GLOBAL_SCALE   # From elbow to wrist

THIGH_LEN = 0.45 * GLOBAL_SCALE # From hip to knee
CALF_LEN = 0.45 * GLOBAL_SCALE  # From knee to ankle

# --- Animation Parameters ---
ANIMATION_SPEED = 0.1 # Radians per frame, adjusts speed of the running cycle

# Overall vertical bobbing of the figure (pelvis root)
PELVIS_BOB_AMPLITUDE = 0.05 * GLOBAL_SCALE
PELVIS_BOB_FREQ_FACTOR = 2.0 # Bobbing frequency relative to stride cycle

# Torso swing (slight forward/backward tilt)
TORSO_SWING_AMPLITUDE = math.radians(5) # Radians

# Leg motion parameters
# Angles are relative to the parent segment's orientation.
# A 'base_angle' of 0 degrees means the segment points along the positive X-axis (right).
# Angles increase counter-clockwise.
HIP_SWING_AMPLITUDE = math.radians(25) # Max forward/backward swing from vertical
HIP_BASE_ANGLE = -math.pi / 2 # Initial orientation: segment points straight down from hip

KNEE_MAX_FLEXION = math.radians(70) # Max bend from straight
KNEE_MIN_FLEXION = math.radians(10) # Min bend (always slightly bent)
KNEE_BASE_ANGLE = 0 # 0 means straight extension from thigh. Negative angle for backward bend.

ANKLE_MAX_FLEXION = math.radians(20) # Max bend
ANKLE_MIN_FLEXION = math.radians(0) # Min bend
ANKLE_BASE_ANGLE = 0 # 0 means straight extension from calf. Negative angle for foot pointing down.

# Arm motion parameters
ARM_SWING_AMPLITUDE = math.radians(35) # Max forward/backward shoulder swings
SHOULDER_BASE_ANGLE = -math.pi / 2 # Initial orientation: segment points straight down from shoulder

ELBOW_MAX_FLEXION = math.radians(80) # Max bend
ELBOW_MIN_FLEXION = math.radians(30) # Min bend
ELBOW_BASE_ANGLE = 0 # 0 means straight extension from upper arm. Negative angle for inward bend.

WRIST_MAX_FLEXION = math.radians(10) # Max bend
WRIST_MIN_FLEXION = math.radians(0) # Min bend
WRIST_BASE_ANGLE = 0 # 0 means straight extension from forearm. Negative angle for hand pointing down.

# --- Helper Functions ---
def rotate_point(x, y, angle):
    """Rotates a point (x, y) around the origin (0,0) by 'angle' radians."""
    rotated_x = x * math.cos(angle) - y * math.sin(angle)
    rotated_y = x * math.sin(angle) + y * math.cos(angle)
    return rotated_x, rotated_y

class PointLightFigure:
    def __init__(self, x_screen_center, y_screen_center):
        self.x_screen_center = x_screen_center
        self.y_screen_center = y_screen_center
        self.time = 0.0 # Animation time variable

        # Define the kinematic chain segments.
        # Each segment is defined by its parent, length, static base angle,
        # and a function for dynamic animation angle offset.
        # 'base_angle': Angle of this segment relative to its parent's orientation.
        #               0 = points right, pi/2 = up, -pi/2 = down, pi = left.
        # 'anim_func': A lambda function `(time, side_char)` returning an angle offset.
        #              `side_char` is 'l' for left, 'r' for right, used for phase.
        
        # 'total_pos' and 'total_angle' (absolute screen position and angle)
        # will be calculated each frame.
        self.segments = {
            # Internal root point, positioned at the screen's center and acts as the anchor for the figure.
            'pelvis_root': {'parent': None, 'length': 0, 'base_angle': 0, 'anim_func': None, 'total_pos': (0,0), 'total_angle': 0},

            # Torso/Spine segments. Points go up from pelvis.
            # 'lower_torso' is the first visible point of the torso from the pelvis root.
            'lower_torso': {'parent': 'pelvis_root', 'length': TORSO_LOWER_LEN, 'base_angle': math.pi/2, # Points up from pelvis_root
                            'anim_func': lambda t, side: -TORSO_SWING_AMPLITUDE * math.sin(t * 0.5)}, # Slight forward/backward tilt
            'upper_torso': {'parent': 'lower_torso', 'length': TORSO_UPPER_LEN, 'base_angle': 0, # Continues straight up from lower_torso
                            'anim_func': lambda t, side: TORSO_SWING_AMPLITUDE * math.sin(t * 0.5)},
            'head':        {'parent': 'upper_torso', 'length': HEAD_LEN + NECK_OFFSET, 'base_angle': math.pi/2, # Points up from upper_torso
                            'anim_func': lambda t, side: 0}, # No specific head animation beyond torso

            # Legs - Left Side
            # 'l_hip' is a horizontal segment from pelvis_root to the hip joint.
            'l_hip':      {'parent': 'pelvis_root', 'length': HIP_WIDTH_HALF, 'base_angle': math.pi, # Points left from pelvis_root
                           'anim_func': lambda t, side: 0}, # Hips mostly fixed horizontally
            # 'l_thigh' is the segment from hip to knee.
            'l_thigh':    {'parent': 'l_hip', 'length': THIGH_LEN, 'base_angle': HIP_BASE_ANGLE,
                           'anim_func': lambda t, side: HIP_SWING_AMPLITUDE * math.sin(t)}, # Leg swing
            # 'l_calf' is the segment from knee to ankle.
            'l_calf':     {'parent': 'l_thigh', 'length': CALF_LEN, 'base_angle': KNEE_BASE_ANGLE,
                           # Knee bend: max bend when hip is at extrema (sin(t)=+/-1), using abs(cos(t))
                           'anim_func': lambda t, side: -(KNEE_MIN_FLEXION + (KNEE_MAX_FLEXION - KNEE_MIN_FLEXION) * abs(math.cos(t)))},
            # 'l_foot' is a zero-length segment to represent the ankle point
            'l_foot':     {'parent': 'l_calf', 'length': 0, 'base_angle': ANKLE_BASE_ANGLE,
                           'anim_func': lambda t, side: -(ANKLE_MIN_FLEXION + (ANKLE_MAX_FLEXION - ANKLE_MIN_FLEXION) * math.sin(t))},

            # Legs - Right Side (phases offset by pi for opposite motion)
            'r_hip':      {'parent': 'pelvis_root', 'length': HIP_WIDTH_HALF, 'base_angle': 0, # Points right from pelvis_root
                           'anim_func': lambda t, side: 0},
            'r_thigh':    {'parent': 'r_hip', 'length': THIGH_LEN, 'base_angle': HIP_BASE_ANGLE,
                           'anim_func': lambda t, side: HIP_SWING_AMPLITUDE * math.sin(t + math.pi)},
            'r_calf':     {'parent': 'r_thigh', 'length': CALF_LEN, 'base_angle': KNEE_BASE_ANGLE,
                           'anim_func': lambda t, side: -(KNEE_MIN_FLEXION + (KNEE_MAX_FLEXION - KNEE_MIN_FLEXION) * abs(math.cos(t + math.pi)))},
            'r_foot':     {'parent': 'r_calf', 'length': 0, 'base_angle': ANKLE_BASE_ANGLE,
                           'anim_func': lambda t, side: -(ANKLE_MIN_FLEXION + (ANKLE_MAX_FLEXION - ANKLE_MIN_FLEXION) * math.sin(t + math.pi))},

            # Arms - Left Side (opposite phase to its corresponding leg, e.g. L arm with R leg)
            'l_shoulder': {'parent': 'upper_torso', 'length': SHOULDER_WIDTH_HALF, 'base_angle': math.pi, # Points left from upper_torso
                           'anim_func': lambda t, side: 0},
            'l_upper_arm':{'parent': 'l_shoulder', 'length': UPPER_ARM_LEN, 'base_angle': SHOULDER_BASE_ANGLE,
                           'anim_func': lambda t, side: ARM_SWING_AMPLITUDE * math.sin(t + math.pi)}, # Opposite phase of left leg
            'l_forearm':  {'parent': 'l_upper_arm', 'length': FOREARM_LEN, 'base_angle': ELBOW_BASE_ANGLE,
                           'anim_func': lambda t, side: -(ELBOW_MIN_FLEXION + (ELBOW_MAX_FLEXION - ELBOW_MIN_FLEXION) * abs(math.cos(t + math.pi)))},
            'l_hand':     {'parent': 'l_forearm', 'length': 0, 'base_angle': WRIST_BASE_ANGLE,
                           'anim_func': lambda t, side: -(WRIST_MIN_FLEXION + (WRIST_MAX_FLEXION - WRIST_MIN_FLEXION) * math.sin(t + math.pi))},

            # Arms - Right Side (opposite phase to its corresponding leg, e.g. R arm with L leg)
            'r_shoulder': {'parent': 'upper_torso', 'length': SHOULDER_WIDTH_HALF, 'base_angle': 0, # Points right from upper_torso
                           'anim_func': lambda t, side: 0},
            'r_upper_arm':{'parent': 'r_shoulder', 'length': UPPER_ARM_LEN, 'base_angle': SHOULDER_BASE_ANGLE,
                           'anim_func': lambda t, side: ARM_SWING_AMPLITUDE * math.sin(t)}, # Opposite phase of right leg
            'r_forearm':  {'parent': 'r_upper_arm', 'length': FOREARM_LEN, 'base_angle': ELBOW_BASE_ANGLE,
                           'anim_func': lambda t, side: -(ELBOW_MIN_FLEXION + (ELBOW_MAX_FLEXION - ELBOW_MIN_FLEXION) * abs(math.cos(t)))},
            'r_hand':     {'parent': 'r_forearm', 'length': 0, 'base_angle': WRIST_BASE_ANGLE,
                           'anim_func': lambda t, side: -(WRIST_MIN_FLEXION + (WRIST_MAX_FLEXION - WRIST_MIN_FLEXION) * math.sin(t))},
        }
        
        # Map of the 15 required point IDs to the segment that represents their location.
        # Each point corresponds to the *distal end* of a segment.
        self.draw_points_map = {
            'head': 'head',
            'l_shoulder': 'l_shoulder',
            'r_shoulder': 'r_shoulder',
            'l_elbow': 'l_upper_arm',  # Elbow is the end of the upper arm segment
            'r_elbow': 'r_upper_arm',
            'l_wrist': 'l_forearm',    # Wrist is the end of the forearm segment
            'r_wrist': 'r_forearm',
            'upper_torso': 'upper_torso',
            'lower_torso': 'lower_torso', # This point corresponds to the lower central torso/pelvis
            'l_hip': 'l_hip',          # Hip is the end of the hip-offset segment
            'r_hip': 'r_hip',
            'l_knee': 'l_thigh',       # Knee is the end of the thigh segment
            'r_knee': 'r_thigh',
            'l_ankle': 'l_calf',       # Ankle is the end of the calf segment
            'r_ankle': 'r_calf',
        }

    def update(self):
        """Updates the position and orientation of all segments based on time."""
        self.time += ANIMATION_SPEED

        # Calculate global vertical bobbing for the entire figure
        pelvis_offset_y = PELVIS_BOB_AMPLITUDE * math.sin(self.time * PELVIS_BOB_FREQ_FACTOR)

        # Initialize the pelvis_root's absolute position and angle
        self.segments['pelvis_root']['total_pos'] = (self.x_screen_center, self.y_screen_center + pelvis_offset_y)
        self.segments['pelvis_root']['total_angle'] = 0 # The root itself has no intrinsic rotation

        # Define the order in which segments must be calculated to ensure parent segments are processed first.
        calculation_order = [
            'pelvis_root',
            'lower_torso', 'upper_torso', 'head',
            'l_hip', 'l_thigh', 'l_calf', 'l_foot',
            'r_hip', 'r_thigh', 'r_calf', 'r_foot',
            'l_shoulder', 'l_upper_arm', 'l_forearm', 'l_hand',
            'r_shoulder', 'r_upper_arm', 'r_forearm', 'r_hand'
        ]

        for seg_id in calculation_order:
            segment = self.segments[seg_id]
            if segment['parent'] is None:
                continue # Skip the root, already processed

            parent_seg = self.segments[segment['parent']]

            # Calculate this segment's animation angle offset
            anim_angle = 0
            if segment['anim_func']:
                # Pass the time and the side identifier ('l' or 'r') to the animation function
                anim_angle = segment['anim_func'](self.time, seg_id[0]) 

            # Total angle of this segment is its parent's absolute angle + this segment's base angle + animation offset
            segment['total_angle'] = parent_seg['total_angle'] + segment['base_angle'] + anim_angle

            # Calculate this segment's absolute position (which is its distal end)
            # Starting from parent's absolute position, move by segment length rotated by its total absolute angle
            dx, dy = rotate_point(segment['length'], 0, segment['total_angle']) # Segment defined horizontally (length, 0) then rotated
            
            segment['total_pos'] = (parent_seg['total_pos'][0] + dx, parent_seg['total_pos'][1] + dy)

    def draw(self, screen):
        """Draws the 15 point-lights on the screen."""
        for point_name, seg_id in self.draw_points_map.items():
            segment = self.segments.get(seg_id)
            if segment:
                x, y = segment['total_pos']
                pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

def main():
    """Main function to initialize Pygame, run the animation loop, and handle events."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Point-Light Biological Motion (Running)")
    clock = pygame.time.Clock()

    # Create the point-light figure instance, centered on the screen
    figure = PointLightFigure(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK) # Clear screen with black background
        
        figure.update() # Update the figure's joint positions for the current frame
        figure.draw(screen) # Draw the point-lights

        pygame.display.flip() # Update the full display Surface to the screen

        clock.tick(FPS) # Control the frame rate

    pygame.quit() # Uninitialize Pygame modules

if __name__ == '__main__':
    main()
