
import pygame
import math

# --- Pygame Setup ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- Point Light Constants ---
POINT_RADIUS = 4 # Size of the dots

# --- Biomechanical Constants (Adjust for appearance) ---
# These lengths are in abstract units and will be scaled by SCALE_FACTOR.
# Tuning these values is crucial for a realistic look.
SEG_HEAD_RADIUS = 10     # Represents roughly half height of head
SEG_SPINE_UPPER = 50     # From lower_spine to upper_spine/chest
SEG_SPINE_LOWER = 30     # From upper_spine to base of head (topmost point)
SEG_SHOULDER_WIDTH = 25  # Half width from spine to shoulder joint
SEG_HIP_WIDTH = 15       # Half width from spine to hip joint
SEG_UPPER_ARM = 35       # Shoulder to Elbow
SEG_LOWER_ARM = 30       # Elbow to Wrist
SEG_UPPER_LEG = 50       # Hip to Knee
SEG_LOWER_LEG = 50       # Knee to Ankle

# Overall scaling factor for the figure
SCALE_FACTOR = 0.8 # Adjust to fit the screen and desired size

class Person:
    def __init__(self, start_x, start_y):
        # Initial position of the entire figure (LOWER_SPINE is the root for Y-positioning)
        self.base_x = start_x # X position for the "ground" reference
        self.base_y = start_y # Y position for the "ground" reference (where feet land when standing)
        self.global_x = start_x # Current X position of the figure's root (LOWER_SPINE)

        self.time = 0.0 # Current time in the animation cycle

        # Duration of one full jump cycle in seconds. Tune this for desired speed.
        self.cycle_duration = 2.0 

        # Stores current (x,y) coordinates for each named point.
        self.point_coords = {} 

        # Keyframe definitions for the jump motion.
        # Each keyframe is a tuple of:
        # (time_ratio, torso_lean_deg, hip_angle_deg, knee_angle_deg, shoulder_angle_deg, elbow_angle_deg, y_offset_rel_to_ground_stand, x_velocity_multiplier)
        #
        # Angles (in degrees):
        # - torso_lean_deg: Angle of torso from global vertical (Y-axis). 0=straight up, positive = forward lean (clockwise rotation).
        # - hip_angle_deg: Angle of upper leg relative to torso's long axis. 0=straight down (aligned with torso), positive = forward/up swing.
        # - knee_angle_deg: Angle of lower leg relative to upper leg. 0=straight, positive = bend (heel towards butt).
        # - shoulder_angle_deg: Angle of upper arm relative to torso's long axis. 0=straight down (aligned with torso), positive = forward/up swing.
        # - elbow_angle_deg: Angle of forearm relative to upper arm. 0=straight, positive = bend (hand towards shoulder).
        #
        # Positions:
        # - y_offset_rel_to_ground_stand: Vertical offset of LOWER_SPINE from its standing position (relative to `base_y`).
        #   0 is standing. Positive value means LOWER_SPINE is lower (crouch/land), negative means higher (jump).
        # - x_velocity_multiplier: Affects horizontal speed of the figure during the jump. Multiplied by a base speed.
        self.keyframes = [
            # t_ratio, torso_L, hip_A, knee_A, shoulder_A, elbow_A, y_offset, x_vel_mult
            (0.0,   0,     0,      0,     0,       0,    0,    0.5), # Stand (arms straight down)
            (0.15,  15,    40,    60,    -30,     20,   40,    1.0), # Crouch start (arms back)
            (0.3,   25,    65,    90,    -50,     40,   70,    1.5), # Deep crouch (wind-up)
            (0.45,  5,     -10,   -10,    50,      0,  -40,    2.0), # Launch (legs extend, arms forward)
            (0.6,   -5,     0,    20,    30,     10,  -100,   2.0), # Apex of jump (highest point, slight torso lean back)
            (0.75,  10,    30,    40,    -10,     20,  -30,    1.5), # Descent (preparing for landing)
            (0.9,   20,    60,    80,    -30,     30,   50,    0.8), # Land (absorb shock)
            (1.0,   0,     0,      0,     0,       0,    0,    0.5)  # Recovery to Stand (loops to 0.0)
        ]
        
        # Store current interpolated angles and offsets
        self.current_params = {
            "torso_lean": 0, "hip_angle": 0, "knee_angle": 0,
            "shoulder_angle": 0, "elbow_angle": 0,
            "y_offset": 0, "x_velocity": 0
        }
        
        # Initialize point positions
        self.update_kinematics()

    def interpolate_params(self, t):
        # Normalize time to be within [0, 1] cycle
        t_norm = (t % self.cycle_duration) / self.cycle_duration
        
        # Find the two keyframes to interpolate between
        kf1 = self.keyframes[0]
        kf2 = self.keyframes[0] # Default to first keyframe in case of error
        for i in range(len(self.keyframes) - 1):
            if t_norm >= self.keyframes[i][0] and t_norm <= self.keyframes[i+1][0]:
                kf1 = self.keyframes[i]
                kf2 = self.keyframes[i+1]
                break
        
        # If t_norm is exactly 1.0 (end of cycle), use the last keyframe and loop to first's values
        if t_norm == 1.0:
            kf1 = self.keyframes[-2] # Second to last (e.g., t_ratio=0.9)
            kf2 = self.keyframes[-1] # Last (t_ratio=1.0, which has same values as 0.0)
            
        # Calculate interpolation ratio (alpha)
        if kf1[0] == kf2[0]: # Avoid division by zero if keyframes are at same time (shouldn't happen with valid keyframes)
            alpha = 0
        else:
            alpha = (t_norm - kf1[0]) / (kf2[0] - kf1[0])
        
        # Interpolate each parameter
        self.current_params["torso_lean"] = kf1[1] + alpha * (kf2[1] - kf1[1])
        self.current_params["hip_angle"] = kf1[2] + alpha * (kf2[2] - kf1[2])
        self.current_params["knee_angle"] = kf1[3] + alpha * (kf2[3] - kf1[3])
        self.current_params["shoulder_angle"] = kf1[4] + alpha * (kf2[4] - kf1[4])
        self.current_params["elbow_angle"] = kf1[5] + alpha * (kf2[5] - kf1[5])
        self.current_params["y_offset"] = kf1[6] + alpha * (kf2[6] - kf1[6])
        self.current_params["x_velocity"] = kf1[7] + alpha * (kf2[7] - kf1[7])

    def update(self, dt):
        self.time += dt
        self.interpolate_params(self.time)
        
        # Update global horizontal position. Base speed chosen for smooth left-to-right movement.
        self.global_x += self.current_params["x_velocity"] * 10 * dt 

        # If figure goes off screen to the right, reset its X position to the left.
        # This creates a continuous loop of a single figure.
        person_render_width = (SEG_HIP_WIDTH * 2 + SEG_UPPER_ARM + SEG_LOWER_ARM) * SCALE_FACTOR * 1.5 
        if self.global_x - person_render_width/2 > SCREEN_WIDTH + person_render_width:
            self.global_x = -person_render_width 
        
        self.update_kinematics()

    def update_kinematics(self):
        # Convert angles from degrees to radians
        torso_lean_rad = math.radians(self.current_params["torso_lean"])
        hip_angle_rad = math.radians(self.current_params["hip_angle"])
        knee_angle_rad = math.radians(self.current_params["knee_angle"])
        shoulder_angle_rad = math.radians(self.current_params["shoulder_angle"])
        elbow_angle_rad = math.radians(self.current_params["elbow_angle"])

        # Base point for calculations: LOWER_SPINE
        # It moves horizontally (global_x) and vertically (y_offset) relative to ground.
        lower_spine_x = self.global_x
        lower_spine_y = self.base_y + self.current_params["y_offset"] * SCALE_FACTOR
        self.point_coords["LOWER_SPINE"] = (lower_spine_x, lower_spine_y)

        # Upper Spine (relative to LOWER_SPINE, rotated by torso_lean)
        # Angle `torso_lean_rad` is from vertical (Y-axis), positive clockwise (forward lean).
        current_torso_angle = torso_lean_rad
        upper_spine_x = lower_spine_x + SEG_SPINE_UPPER * SCALE_FACTOR * math.sin(current_torso_angle)
        upper_spine_y = lower_spine_y - SEG_SPINE_UPPER * SCALE_FACTOR * math.cos(current_torso_angle)
        self.point_coords["UPPER_SPINE"] = (upper_spine_x, upper_spine_y)

        # Head (relative to UPPER_SPINE, continues torso angle)
        # Using SEG_SPINE_LOWER here to define head's distance from upper_spine.
        head_x = upper_spine_x + SEG_SPINE_LOWER * SCALE_FACTOR * math.sin(current_torso_angle) 
        head_y = upper_spine_y - SEG_SPINE_LOWER * SCALE_FACTOR * math.cos(current_torso_angle)
        self.point_coords["HEAD"] = (head_x, head_y)

        # Hips (offset horizontally from LOWER_SPINE)
        l_hip_x = lower_spine_x - SEG_HIP_WIDTH * SCALE_FACTOR
        r_hip_x = lower_spine_x + SEG_HIP_WIDTH * SCALE_FACTOR
        l_hip_y = lower_spine_y
        r_hip_y = lower_spine_y
        self.point_coords["L_HIP"] = (l_hip_x, l_hip_y)
        self.point_coords["R_HIP"] = (r_hip_x, r_hip_y)

        # Legs (relative to Hips and current torso angle)
        # Global angle of upper leg: `current_torso_angle + hip_angle_rad` (hip_angle_rad is relative to torso)
        # Global angle of lower leg: `global_upper_leg_angle + knee_angle_rad` (knee_angle_rad is relative to upper leg)
        
        # Left Leg
        global_upper_leg_angle_l = current_torso_angle + hip_angle_rad 
        l_knee_x = l_hip_x + SEG_UPPER_LEG * SCALE_FACTOR * math.sin(global_upper_leg_angle_l)
        l_knee_y = l_hip_y + SEG_UPPER_LEG * SCALE_FACTOR * math.cos(global_upper_leg_angle_l)
        self.point_coords["L_KNEE"] = (l_knee_x, l_knee_y)

        global_lower_leg_angle_l = global_upper_leg_angle_l + knee_angle_rad
        l_ankle_x = l_knee_x + SEG_LOWER_LEG * SCALE_FACTOR * math.sin(global_lower_leg_angle_l)
        l_ankle_y = l_knee_y + SEG_LOWER_LEG * SCALE_FACTOR * math.cos(global_lower_leg_angle_l)
        self.point_coords["L_ANKLE"] = (l_ankle_x, l_ankle_y)

        # Right Leg (symmetric angles)
        global_upper_leg_angle_r = current_torso_angle + hip_angle_rad 
        r_knee_x = r_hip_x + SEG_UPPER_LEG * SCALE_FACTOR * math.sin(global_upper_leg_angle_r)
        r_knee_y = r_hip_y + SEG_UPPER_LEG * SCALE_FACTOR * math.cos(global_upper_leg_angle_r)
        self.point_coords["R_KNEE"] = (r_knee_x, r_knee_y)

        global_lower_leg_angle_r = global_upper_leg_angle_r + knee_angle_rad
        r_ankle_x = r_knee_x + SEG_LOWER_LEG * SCALE_FACTOR * math.sin(global_lower_leg_angle_r)
        r_ankle_y = r_knee_y + SEG_LOWER_LEG * SCALE_FACTOR * math.cos(global_lower_leg_angle_r)
        self.point_coords["R_ANKLE"] = (r_ankle_x, r_ankle_y)

        # Shoulders (offset horizontally from UPPER_SPINE)
        l_shoulder_x = upper_spine_x - SEG_SHOULDER_WIDTH * SCALE_FACTOR
        r_shoulder_x = upper_spine_x + SEG_SHOULDER_WIDTH * SCALE_FACTOR
        l_shoulder_y = upper_spine_y
        r_shoulder_y = upper_spine_y
        self.point_coords["L_SHOULDER"] = (l_shoulder_x, l_shoulder_y)
        self.point_coords["R_SHOULDER"] = (r_shoulder_x, r_shoulder_y)

        # Arms (relative to Shoulders and current torso angle)
        # Global angle of upper arm: `current_torso_angle + shoulder_angle_rad` (shoulder_angle_rad is relative to torso)
        # Global angle of lower arm: `global_upper_arm_angle + elbow_angle_rad` (elbow_angle_rad is relative to upper arm)
        
        # Left Arm
        global_upper_arm_angle_l = current_torso_angle + shoulder_angle_rad
        l_elbow_x = l_shoulder_x + SEG_UPPER_ARM * SCALE_FACTOR * math.sin(global_upper_arm_angle_l)
        l_elbow_y = l_shoulder_y + SEG_UPPER_ARM * SCALE_FACTOR * math.cos(global_upper_arm_angle_l)
        self.point_coords["L_ELBOW"] = (l_elbow_x, l_elbow_y)

        global_lower_arm_angle_l = global_upper_arm_angle_l + elbow_angle_rad
        l_wrist_x = l_elbow_x + SEG_LOWER_ARM * SCALE_FACTOR * math.sin(global_lower_arm_angle_l)
        l_wrist_y = l_elbow_y + SEG_LOWER_ARM * SCALE_FACTOR * math.cos(global_lower_arm_angle_l)
        self.point_coords["L_WRIST"] = (l_wrist_x, l_wrist_y)

        # Right Arm (symmetric angles)
        global_upper_arm_angle_r = current_torso_angle + shoulder_angle_rad
        r_elbow_x = r_shoulder_x + SEG_UPPER_ARM * SCALE_FACTOR * math.sin(global_upper_arm_angle_r)
        r_elbow_y = r_shoulder_y + SEG_UPPER_ARM * SCALE_FACTOR * math.cos(global_upper_arm_angle_r)
        self.point_coords["R_ELBOW"] = (r_elbow_x, r_elbow_y)

        global_lower_arm_angle_r = global_upper_arm_angle_r + elbow_angle_rad
        r_wrist_x = r_elbow_x + SEG_LOWER_ARM * SCALE_FACTOR * math.sin(global_lower_arm_angle_r)
        r_wrist_y = r_elbow_y + SEG_LOWER_ARM * SCALE_FACTOR * math.cos(global_lower_arm_angle_r)
        self.point_coords["R_WRIST"] = (r_wrist_x, r_wrist_y)


# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Jumping Forward")
clock = pygame.time.Clock()

# --- Create Person Object ---
# Position the person such that their feet are at the bottom of the screen when standing
# and the whole figure is roughly centered horizontally initially.
# Calculate the standing height of the person to place the base_y correctly.
# Total approximate height from lower_spine to feet (straight legs): SEG_UPPER_LEG + SEG_LOWER_LEG
# Total approximate height from lower_spine to head: SEG_SPINE_UPPER + SEG_SPINE_LOWER + SEG_HEAD_RADIUS
# We care about feet being on the "ground"
person_approx_height_standing = (SEG_UPPER_LEG + SEG_LOWER_LEG + SEG_HEAD_RADIUS + SEG_SPINE_UPPER + SEG_SPINE_LOWER) * SCALE_FACTOR

# We want the lowest point (feet) to be at SCREEN_HEIGHT - padding.
# The `base_y` for the `Person` class represents the Y-coordinate of the `LOWER_SPINE` when standing at `y_offset=0`.
# So, `base_y` = (screen_height - feet_padding) - (SEG_UPPER_LEG + SEG_LOWER_LEG) * SCALE_FACTOR
feet_padding = 20 # Pixels from the bottom of the screen
person_start_x = SCREEN_WIDTH // 2
person_start_y = SCREEN_HEIGHT - feet_padding - (SEG_UPPER_LEG + SEG_LOWER_LEG) * SCALE_FACTOR

person = Person(person_start_x, person_start_y)

# --- Game Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(FPS) / 1000.0 # Time in seconds since last frame

    # Update person's animation
    person.update(dt)

    # Drawing
    screen.fill(BLACK) # Solid black background

    # Draw each point
    # Ensure there are exactly 15 points
    if len(person.point_coords) != 15:
        print(f"Warning: Expected 15 points, but got {len(person.point_coords)}. Please check point definitions.")

    for point_name, (x, y) in person.point_coords.items():
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

    pygame.display.flip()

pygame.quit()
