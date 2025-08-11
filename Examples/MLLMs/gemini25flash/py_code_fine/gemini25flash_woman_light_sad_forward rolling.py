
import pygame
import math

# Pygame setup
WIDTH, HEIGHT = 800, 600
FPS = 60
POINT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Forward Roll")
clock = pygame.time.Clock()

# --- Point Definitions (relative to the figure's center/pelvis) ---
# These coordinates are for a standing figure.
# The y-axis goes down in Pygame, so negative y is "up".
# The number of points is exactly 15 as per requirement.

# Define names for the 15 body points for clarity and consistency
POINT_NAMES = [
    "HEAD",
    "SHOULDER_L", "SHOULDER_R",
    "ELBOW_L", "ELBOW_R",
    "WRIST_L", "WRIST_R",
    "HIP_L", "HIP_R",
    "KNEE_L", "KNEE_R",
    "ANKLE_L", "ANKLE_R",
    "FOOT_L", "FOOT_R"
]

# Relative coordinates for different key poses of the figure.
# These represent the *shape* of the figure at various stages of the roll,
# relative to its *own* local origin (which will then be translated and rotated globally).

# Pose 0: Standing upright
POSE_STANDING = {
    "HEAD": (0, -100),
    "SHOULDER_L": (-30, -70), "SHOULDER_R": (30, -70),
    "ELBOW_L": (-40, -30), "ELBOW_R": (40, -30),
    "WRIST_L": (-50, 10), "WRIST_R": (50, 10),
    "HIP_L": (-20, 0), "HIP_R": (20, 0),
    "KNEE_L": (-30, 70), "KNEE_R": (30, 70),
    "ANKLE_L": (-30, 120), "ANKLE_R": (30, 120),
    "FOOT_L": (-30, 140), "FOOT_R": (30, 140)
}

# Pose 1: Crouching (preparing for roll)
POSE_CROUCH = {
    "HEAD": (0, -60),
    "SHOULDER_L": (-25, -40), "SHOULDER_R": (25, -40),
    "ELBOW_L": (-35, -10), "ELBOW_R": (35, -10),
    "WRIST_L": (-45, 20), "WRIST_R": (45, 20),
    "HIP_L": (-20, 30), "HIP_R": (20, 30),
    "KNEE_L": (-10, 80), "KNEE_R": (10, 80),
    "ANKLE_L": (-10, 100), "ANKLE_R": (10, 100),
    "FOOT_L": (-10, 110), "FOOT_R": (10, 110)
}

# Pose 2: Tucked (mid-roll, compact body shape)
POSE_TUCKED = {
    "HEAD": (0, -20),
    "SHOULDER_L": (-15, -10), "SHOULDER_R": (15, -10),
    "ELBOW_L": (-25, 0), "ELBOW_R": (25, 0),
    "WRIST_L": (-30, 10), "WRIST_R": (30, 10),
    "HIP_L": (-10, 20), "HIP_R": (10, 20),
    "KNEE_L": (-5, 30), "KNEE_R": (5, 30),
    "ANKLE_L": (-5, 40), "ANKLE_R": (5, 40),
    "FOOT_L": (-5, 50), "FOOT_R": (5, 50)
}

# Pose 3: Unfurling (after roll, beginning to stand up)
POSE_UNFURL = {
    "HEAD": (0, -50),
    "SHOULDER_L": (-28, -35), "SHOULDER_R": (28, -35),
    "ELBOW_L": (-38, -5), "ELBOW_R": (38, -5),
    "WRIST_L": (-48, 15), "WRIST_R": (48, 15),
    "HIP_L": (-20, 25), "HIP_R": (20, 25),
    "KNEE_L": (-15, 75), "KNEE_R": (15, 75),
    "ANKLE_L": (-15, 95), "ANKLE_R": (15, 95),
    "FOOT_L": (-15, 105), "FOOT_R": (15, 105)
}


# --- Animation Keyframes for overall motion (translation & rotation) ---
# Each keyframe defines: (frame_time, target_pose, target_translation_x, target_translation_y, target_rotation_degrees)
# The `target_translation_x/y` are displacements from the starting point of the *cycle*.
# The `target_rotation_degrees` is the overall rotation of the entire figure.
# The total animation cycle length in frames is determined by the last keyframe's time.
ROLL_CYCLE_LENGTH_FRAMES = 180 # Total frames for one full forward roll cycle

ANIMATION_KEYFRAMES = [
    (0,   POSE_STANDING, 0,   0,  0),     # Start: standing upright
    (30,  POSE_CROUCH,   30,  50, 20),    # Preparation: crouch down, lean forward slightly
    (60,  POSE_TUCKED,   120, 70, 90),    # Initiate roll: tuck into a ball, rotate to horizontal
    (90,  POSE_TUCKED,   240, 70, 180),   # Mid-roll: fully inverted, moving forward
    (120, POSE_TUCKED,   360, 70, 270),   # Ending roll: continue rotation
    (150, POSE_UNFURL,   420, 50, 340),   # Unfurling: extending from tucked position, coming upright
    (ROLL_CYCLE_LENGTH_FRAMES, POSE_STANDING, 450, 0, 360) # End: back to standing, displaced by 450 units, rotated 360 degrees
]

# Helper function for linear interpolation with cosine smoothing (ease-in-out)
def smooth_lerp(t, a, b):
    # t is expected to be between 0 and 1
    t_smooth = 0.5 - 0.5 * math.cos(t * math.pi)
    return a + (b - a) * t_smooth

class Person:
    def __init__(self, start_x, start_y):
        self.base_x = start_x # Base screen X position for the starting point of the first roll
        self.base_y = start_y # Base screen Y position (vertical reference for the ground)
        self.current_frame = 0 # Current frame within the ROLL_CYCLE_LENGTH_FRAMES
        self.points = {} # Dictionary to store current absolute (x,y) coordinates of the 15 points

        # These accumulate translation and rotation across multiple full roll cycles
        self.accumulated_x_offset = 0
        self.accumulated_rot_offset = 0

    def update(self):
        # Check if a full roll cycle just completed (i.e., we were on the last frame of a cycle).
        # This update occurs *before* current_frame wraps to 0 for the next cycle.
        if self.current_frame == ROLL_CYCLE_LENGTH_FRAMES - 1:
            # Add the total displacement and rotation of one cycle to the accumulated offsets
            self.accumulated_x_offset += ANIMATION_KEYFRAMES[-1][2] 
            self.accumulated_rot_offset += ANIMATION_KEYFRAMES[-1][4] 

        # Advance the current frame, wrapping around at the end of the cycle
        self.current_frame = (self.current_frame + 1) % ROLL_CYCLE_LENGTH_FRAMES

        # Find the two keyframes that define the current segment of the animation cycle
        kf_idx = 0
        while kf_idx < len(ANIMATION_KEYFRAMES) - 1 and ANIMATION_KEYFRAMES[kf_idx+1][0] <= self.current_frame:
            kf_idx += 1

        kf_start = ANIMATION_KEYFRAMES[kf_idx]
        kf_end = ANIMATION_KEYFRAMES[(kf_idx + 1) % len(ANIMATION_KEYFRAMES)]

        # Calculate the interpolation factor (t_segment) within the current keyframe segment (0 to 1)
        segment_start_time = kf_start[0]
        segment_end_time = kf_end[0]
        segment_duration = segment_end_time - segment_start_time
        
        # Avoid division by zero if keyframes are at the same time (shouldn't happen with this setup)
        if segment_duration == 0:
            t_segment = 0
        else:
            t_segment = (self.current_frame - segment_start_time) / segment_duration
        
        # Interpolate overall translation and rotation for the current cycle segment using smooth_lerp
        # These are displacements and rotations *relative to the start of the current cycle*.
        current_cycle_x = smooth_lerp(t_segment, kf_start[2], kf_end[2])
        current_cycle_y = smooth_lerp(t_segment, kf_start[3], kf_end[3])
        current_cycle_rot = smooth_lerp(t_segment, kf_start[4], kf_end[4])

        # Interpolate the relative point positions (the body's shape/pose) for the current frame
        interpolated_relative_points = {}
        for point_name in POINT_NAMES:
            start_pos = kf_start[1][point_name]
            end_pos = kf_end[1][point_name]
            interpolated_x = smooth_lerp(t_segment, start_pos[0], end_pos[0])
            interpolated_y = smooth_lerp(t_segment, start_pos[1], end_pos[1])
            interpolated_relative_points[point_name] = (interpolated_x, interpolated_y)

        # Calculate absolute screen coordinates for each point
        self.points = {}
        for name, rel_pos in interpolated_relative_points.items():
            # Total rotation is the sum of the current cycle's rotation and accumulated rotations
            total_rot_degrees = current_cycle_rot + self.accumulated_rot_offset
            rad_rot = math.radians(total_rot_degrees)
            
            # Rotate the relative point around the figure's local origin (0,0)
            # This simulates the body's rotation during the roll
            rotated_x = rel_pos[0] * math.cos(rad_rot) - rel_pos[1] * math.sin(rad_rot)
            rotated_y = rel_pos[0] * math.sin(rad_rot) + rel_pos[1] * math.cos(rad_rot)
            
            # Apply base screen position, accumulated x offset, current cycle's x/y offset, and the rotated point position
            # Note: Y offset does not accumulate, as the person always returns to the same baseline height after each roll.
            self.points[name] = (self.base_x + self.accumulated_x_offset + current_cycle_x + rotated_x,
                                 self.base_y + current_cycle_y + rotated_y)

    def draw(self, surface):
        # Draw each of the 15 points as a white circle
        for point_name in POINT_NAMES:
            x, y = self.points[point_name]
            pygame.draw.circle(surface, WHITE, (int(x), int(y)), POINT_RADIUS)

# Initialize the person at the center-left of the screen.
# The Y position is adjusted slightly to account for the rolling motion's lowest point.
person = Person(WIDTH // 4, HEIGHT // 2 - 50) 

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with black background
    screen.fill(BLACK)

    # Update and draw the person
    person.update()
    person.draw(screen)

    # Refresh the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

pygame.quit()
