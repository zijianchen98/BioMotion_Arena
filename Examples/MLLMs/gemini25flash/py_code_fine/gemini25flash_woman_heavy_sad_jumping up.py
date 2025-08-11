
import pygame
import numpy as np
import math

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
POINT_RADIUS = 5
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- Human Body Proportions (relative units) ---
# These proportions are chosen to create a realistic figure for a point-light display.
# The overall scale can be adjusted via SCALE_FACTOR.
PROPORTIONS = {
    'head_neck': 0.10,       # From top of head to base of neck
    'neck_mid_torso': 0.15,  # From base of neck to mid-torso (chest/upper spine)
    'mid_torso_hip': 0.15,   # From mid-torso to hip joints
    'shoulder_width': 0.15,  # Half width from center to shoulder
    'hip_width': 0.10,       # Half width from center to hip
    'upper_arm': 0.15,       # Upper arm length
    'lower_arm': 0.15,       # Lower arm length
    'upper_leg': 0.20,       # Upper leg length (thigh)
    'lower_leg': 0.20,       # Lower leg length (shin)
}

# Scales the proportions to screen units
# Makes the figure roughly 50% of screen height in its neutral standing pose.
SCALE_FACTOR = SCREEN_HEIGHT * 0.5 

# --- Animation Parameters ---
ANIM_DURATION = 4.5 # seconds for one full jump cycle (slower for heavy/sad)
JUMP_HEIGHT = SCREEN_HEIGHT * 0.15 # Max vertical rise of the figure's base
SQUAT_DEPTH = SCREEN_HEIGHT * 0.10 # Max vertical drop during squat preparation

# Phase durations (normalized to 1.0 total)
# Adjusted to emphasize "heavy" (longer squat, push, landing)
PHASE_SQUAT = 0.25      # Deep preparation
PHASE_PUSH_OFF = 0.20   # Forceful extension
PHASE_ASCENT = 0.20     # Rising in air
PHASE_DESCENT = 0.20    # Falling to ground
PHASE_LANDING = 0.10    # Impact absorption
PHASE_RECOVERY = 0.05   # Settling after landing

# Ensure phases sum to 1.0
assert abs(PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT + PHASE_LANDING + PHASE_RECOVERY - 1.0) < 0.001, "Phase durations must sum to 1.0"

class HumanFigure:
    def __init__(self, scale_factor, screen_width, screen_height):
        self.scale = scale_factor
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.points = {}
        self.initialize_body_structure()

        self.base_x = screen_width // 2 # Center horizontally
        self.ground_y = screen_height * 0.9 # Nominal ground level on screen

        self.animation_time = 0.0

        # Ordered list of point names for drawing (total 15 points)
        self.point_names = [
            'head', 'neck', 'mid_torso',
            'r_shoulder', 'l_shoulder',
            'r_elbow', 'l_elbow',
            'r_wrist', 'l_wrist',
            'r_hip', 'l_hip',
            'r_knee', 'l_knee',
            'r_ankle', 'l_ankle'
        ]

    def initialize_body_structure(self):
        # Calculate actual segment lengths in pixels based on proportions and scale factor
        self.head_neck_len = PROPORTIONS['head_neck'] * self.scale
        self.neck_mid_torso_len = PROPORTIONS['neck_mid_torso'] * self.scale
        self.mid_torso_hip_len = PROPORTIONS['mid_torso_hip'] * self.scale
        self.shoulder_half_width = PROPORTIONS['shoulder_width'] * self.scale
        self.hip_half_width = PROPORTIONS['hip_width'] * self.scale
        self.upper_arm_len = PROPORTIONS['upper_arm'] * self.scale
        self.lower_arm_len = PROPORTIONS['lower_arm'] * self.scale
        self.upper_leg_len = PROPORTIONS['upper_leg'] * self.scale
        self.lower_leg_len = PROPORTIONS['lower_leg'] * self.scale

    def _lerp(self, a, b, t):
        """Linear interpolation between a and b by factor t."""
        return a + (b - a) * t

    def _ease_in_out(self, t):
        """Smooth ease-in-out interpolation for t in [0, 1]."""
        return 0.5 - 0.5 * math.cos(math.pi * t)

    def update(self, dt):
        self.animation_time = (self.animation_time + dt) % ANIM_DURATION
        t_norm = self.animation_time / ANIM_DURATION

        # --- Calculate overall Y offset for the body (center of mass/hip level) ---
        # This offset determines the figure's vertical position relative to the ground.
        y_offset_from_ground = 0.0 

        # Define vertical movement for each phase using ease-in-out for smoothness
        if t_norm < PHASE_SQUAT:
            phase_t = self._ease_in_out(t_norm / PHASE_SQUAT)
            y_offset_from_ground = -SQUAT_DEPTH * phase_t 
        elif t_norm < PHASE_SQUAT + PHASE_PUSH_OFF:
            phase_t_start = PHASE_SQUAT
            phase_t_end = PHASE_SQUAT + PHASE_PUSH_OFF
            phase_t = self._ease_in_out((t_norm - phase_t_start) / (phase_t_end - phase_t_start))
            y_offset_from_ground = self._lerp(-SQUAT_DEPTH, JUMP_HEIGHT, phase_t)
        elif t_norm < PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT:
            phase_t_start = PHASE_SQUAT + PHASE_PUSH_OFF
            phase_t_end = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT
            phase_t = self._ease_in_out((t_norm - phase_t_start) / (phase_t_end - phase_t_start))
            max_peak_height = JUMP_HEIGHT + (JUMP_HEIGHT * 0.2) # A slight extra peak
            y_offset_from_ground = self._lerp(JUMP_HEIGHT, max_peak_height, phase_t)
        elif t_norm < PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT:
            phase_t_start = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT
            phase_t_end = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT
            phase_t = self._ease_in_out((t_norm - phase_t_start) / (phase_t_end - phase_t_start))
            max_peak_height = JUMP_HEIGHT + (JUMP_HEIGHT * 0.2)
            y_offset_from_ground = self._lerp(max_peak_height, 0, phase_t) # Descend to ground level
        elif t_norm < PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT + PHASE_LANDING:
            phase_t_start = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT
            phase_t_end = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT + PHASE_LANDING
            phase_t = self._ease_in_out((t_norm - phase_t_start) / (phase_t_end - phase_t_start))
            # Landing absorption: dip slightly below ground, then rebound slightly above.
            # Using a parabolic shape for the dip and rebound: phase_t * (1-phase_t) makes a 0-1-0 curve.
            y_offset_from_ground = -SQUAT_DEPTH * 0.6 * phase_t * (1 - phase_t) * 4 
        else: # Recovery
            phase_t_start = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT + PHASE_LANDING
            phase_t_end = 1.0
            phase_t = self._ease_in_out((t_norm - phase_t_start) / (phase_t_end - phase_t_start))
            # Settle back to initial sad pose from slight rebound after landing
            y_offset_from_ground = self._lerp(-SQUAT_DEPTH * 0.3, 0, phase_t) 
        
        # --- Define joint angles based on current phase and time ---
        # All angles in degrees. For segments: 0 is straight down (along positive Y-axis in Pygame).
        # Positive angle indicates clockwise rotation.

        # Initial slumped/sad pose
        pose_sad_initial = {
            'torso_lean': 5, 'neck_lean': 5, 'head_pitch': 5,
            'hip_angle': 5, 'knee_angle': 5, 'ankle_angle': 0,
            'arm_swing': -10, 'elbow_angle': 15, 'wrist_angle': 0, # Arms slightly forward, bent
        }
        # Deep squat pose (emphasizes "heavy" with deep bend)
        pose_squat_deep = {
            'torso_lean': 25, 'neck_lean': 5, 'head_pitch': 0,
            'hip_angle': 70, 'knee_angle': 120, 'ankle_angle': 20, # Very bent legs
            'arm_swing': -50, 'elbow_angle': 10, 'wrist_angle': 0, # Arms swing back powerfully
        }
        # Push-off / Extension pose
        pose_push_off = {
            'torso_lean': 0, 'neck_lean': 0, 'head_pitch': 0,
            'hip_angle': -10, 'knee_angle': -5, 'ankle_angle': -15, # Almost hyperextended for push
            'arm_swing': 50, 'elbow_angle': 0, 'wrist_angle': 0, # Arms swing up/forward
        }
        # Airborne pose (tucked slightly)
        pose_airborne = {
            'torso_lean': 0, 'neck_lean': 0, 'head_pitch': 0,
            'hip_angle': 20, 'knee_angle': 30, 'ankle_angle': 0, # Slightly tucked legs
            'arm_swing': 30, 'elbow_angle': 10, 'wrist_angle': 0, # Arms still slightly up
        }
        # Landing pose (impact absorption)
        pose_landing = {
            'torso_lean': 20, 'neck_lean': 5, 'head_pitch': 5,
            'hip_angle': 60, 'knee_angle': 100, 'ankle_angle': 15, # Deep bend to absorb
            'arm_swing': -40, 'elbow_angle': 15, 'wrist_angle': 0, # Arms swing back to counterbalance
        }

        current_pose_deg = {}
        # Interpolate between key poses based on the current animation phase
        if t_norm < PHASE_SQUAT:
            phase_t = self._ease_in_out(t_norm / PHASE_SQUAT)
            for key in pose_sad_initial:
                current_pose_deg[key] = self._lerp(pose_sad_initial[key], pose_squat_deep[key], phase_t)
        elif t_norm < PHASE_SQUAT + PHASE_PUSH_OFF:
            phase_t_start = PHASE_SQUAT
            phase_t_end = PHASE_SQUAT + PHASE_PUSH_OFF
            phase_t = self._ease_in_out((t_norm - phase_t_start) / (phase_t_end - phase_t_start))
            for key in pose_sad_initial:
                current_pose_deg[key] = self._lerp(pose_squat_deep[key], pose_push_off[key], phase_t)
        elif t_norm < PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT:
            phase_t_start = PHASE_SQUAT + PHASE_PUSH_OFF
            phase_t_end = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT
            phase_t = self._ease_in_out((t_norm - phase_t_start) / (phase_t_end - phase_t_start))
            for key in pose_sad_initial:
                current_pose_deg[key] = self._lerp(pose_push_off[key], pose_airborne[key], phase_t)
        elif t_norm < PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT:
            phase_t_start = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT
            phase_t_end = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT
            phase_t = self._ease_in_out((t_norm - phase_t_start) / (phase_t_end - phase_t_start))
            for key in pose_sad_initial:
                current_pose_deg[key] = self._lerp(pose_airborne[key], pose_sad_initial[key], phase_t) # Transition to pre-landing
        elif t_norm < PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT + PHASE_LANDING:
            phase_t_start = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT
            phase_t_end = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT + PHASE_LANDING
            phase_t = self._ease_in_out((t_norm - phase_t_start) / (phase_t_end - phase_t_start))
            for key in pose_sad_initial:
                current_pose_deg[key] = self._lerp(pose_sad_initial[key], pose_landing[key], phase_t)
        else: # Recovery
            phase_t_start = PHASE_SQUAT + PHASE_PUSH_OFF + PHASE_ASCENT + PHASE_DESCENT + PHASE_LANDING
            phase_t_end = 1.0
            phase_t = self._ease_in_out((t_norm - phase_t_start) / (phase_t_end - phase_t_start))
            for key in pose_sad_initial:
                current_pose_deg[key] = self._lerp(pose_landing[key], pose_sad_initial[key], phase_t)
        
        # Convert all angles from degrees to radians for math functions
        current_pose = {k: math.radians(v) for k, v in current_pose_deg.items()}

        # --- Calculate actual point positions ---
        # Determine the effective Y-level of the figure's base (e.g., feet)
        figure_y_level = self.ground_y + y_offset_from_ground

        # Mid-torso point is the primary anchor for calculating other body parts
        # Its Y position is derived from the feet's nominal position minus leg and lower torso lengths
        mid_torso_y = figure_y_level - (self.upper_leg_len + self.lower_leg_len + self.mid_torso_hip_len)
        mid_torso_x = self.base_x # Figure remains centered horizontally

        self.points['mid_torso'] = [mid_torso_x, mid_torso_y]

        # Hips (relative to mid-torso, considering torso lean)
        # Hips are below mid_torso and spread out horizontally.
        hip_y = mid_torso_y + self.mid_torso_hip_len * math.cos(current_pose['torso_lean'])
        hip_x_offset_from_center = self.mid_torso_hip_len * math.sin(current_pose['torso_lean'])

        self.points['r_hip'] = [mid_torso_x + self.hip_half_width + hip_x_offset_from_center, hip_y]
        self.points['l_hip'] = [mid_torso_x - self.hip_half_width + hip_x_offset_from_center, hip_y]

        # Legs (Hip -> Knee -> Ankle)
        # Segment angles are relative to the parent joint and measure from the vertical (positive Y axis).
        # Positive angle = clockwise rotation.
        
        # Right Leg
        thigh_angle_r = current_pose['hip_angle'] # Angle of upper leg from vertical
        
        dx_rk = self.upper_leg_len * math.sin(thigh_angle_r)
        dy_rk = self.upper_leg_len * math.cos(thigh_angle_r)
        self.points['r_knee'] = [self.points['r_hip'][0] + dx_rk, self.points['r_hip'][1] + dy_rk]

        lower_leg_angle_r = thigh_angle_r + current_pose['knee_angle'] # Total angle of lower leg from vertical
        dx_ra = self.lower_leg_len * math.sin(lower_leg_angle_r)
        dy_ra = self.lower_leg_len * math.cos(lower_leg_angle_r)
        self.points['r_ankle'] = [self.points['r_knee'][0] + dx_ra, self.points['r_knee'][1] + dy_ra]

        # Left Leg (symmetric)
        thigh_angle_l = current_pose['hip_angle']
        
        dx_lk = self.upper_leg_len * math.sin(thigh_angle_l)
        dy_lk = self.upper_leg_len * math.cos(thigh_angle_l)
        self.points['l_knee'] = [self.points['l_hip'][0] + dx_lk, self.points['l_hip'][1] + dy_lk]

        lower_leg_angle_l = thigh_angle_l + current_pose['knee_angle']
        dx_la = self.lower_leg_len * math.sin(lower_leg_angle_l)
        dy_la = self.lower_leg_len * math.cos(lower_leg_angle_l)
        self.points['l_ankle'] = [self.points['l_knee'][0] + dx_la, self.points['l_knee'][1] + dy_la]

        # Torso (mid-torso -> Neck -> Head)
        # Neck relative to mid-torso, considering torso lean.
        # The angle is relative to the segment's parent's orientation.
        neck_angle_from_vertical = current_pose['torso_lean'] # Neck base follows torso lean
        
        dx_neck = self.neck_mid_torso_len * math.sin(neck_angle_from_vertical)
        dy_neck = -self.neck_mid_torso_len * math.cos(neck_angle_from_vertical) # Negative dy because neck is above mid_torso (y decreases upwards)
        self.points['neck'] = [mid_torso_x + dx_neck, mid_torso_y + dy_neck]

        # Head relative to neck, considering neck lean and head pitch.
        head_segment_angle = neck_angle_from_vertical + current_pose['neck_lean'] + current_pose['head_pitch']
        
        dx_head = self.head_neck_len * math.sin(head_segment_angle)
        dy_head = -self.head_neck_len * math.cos(head_segment_angle) 
        self.points['head'] = [self.points['neck'][0] + dx_head, self.points['neck'][1] + dy_head]

        # Shoulders (relative to mid-torso)
        # Shoulders are slightly above mid-torso and out to the sides.
        # They rotate with the torso's lean around the mid-torso point.
        
        # Neutral shoulder positions relative to mid-torso (no lean)
        shoulder_neutral_y_offset = -self.neck_mid_torso_len * 0.5 # Approx. halfway up to the neck from mid-torso
        
        r_shoulder_neutral_x = self.shoulder_half_width
        l_shoulder_neutral_x = -self.shoulder_half_width

        # Vector from mid_torso to neutral shoulder
        r_shoulder_vec_neutral = np.array([r_shoulder_neutral_x, shoulder_neutral_y_offset])
        l_shoulder_vec_neutral = np.array([l_shoulder_neutral_x, shoulder_neutral_y_offset])

        # Rotation matrix (positive angle is clockwise)
        rot_angle = current_pose['torso_lean'] 
        rotation_matrix = np.array([
            [math.cos(rot_angle), -math.sin(rot_angle)],
            [math.sin(rot_angle),  math.cos(rot_angle)]
        ])

        r_shoulder_rotated = np.dot(rotation_matrix, r_shoulder_vec_neutral)
        l_shoulder_rotated = np.dot(rotation_matrix, l_shoulder_vec_neutral)

        self.points['r_shoulder'] = [mid_torso_x + r_shoulder_rotated[0], mid_torso_y + r_shoulder_rotated[1]]
        self.points['l_shoulder'] = [mid_torso_x + l_shoulder_rotated[0], mid_torso_y + l_shoulder_rotated[1]]

        # Arms (Shoulder -> Elbow -> Wrist)
        # arm_swing: overall rotation of the upper arm from vertical (0 is straight down)
        # elbow_angle: angle of lower arm relative to upper arm (0 is straight, positive is bending)

        # Right Arm
        upper_arm_angle_r = current_pose['arm_swing'] # From vertical
        
        dx_re = self.upper_arm_len * math.sin(upper_arm_angle_r)
        dy_re = self.upper_arm_len * math.cos(upper_arm_angle_r)
        self.points['r_elbow'] = [self.points['r_shoulder'][0] + dx_re, self.points['r_shoulder'][1] + dy_re]

        lower_arm_angle_r = upper_arm_angle_r + current_pose['elbow_angle'] # Total angle of lower arm from vertical
        dx_rw = self.lower_arm_len * math.sin(lower_arm_angle_r)
        dy_rw = self.lower_arm_len * math.cos(lower_arm_angle_r)
        self.points['r_wrist'] = [self.points['r_elbow'][0] + dx_rw, self.points['r_elbow'][1] + dy_rw]

        # Left Arm (symmetric)
        # Use the same angle for left arm, as 'arm_swing' indicates overall back/forward swing.
        upper_arm_angle_l = current_pose['arm_swing'] 

        dx_le = self.upper_arm_len * math.sin(upper_arm_angle_l)
        dy_le = self.upper_arm_len * math.cos(upper_arm_angle_l)
        self.points['l_elbow'] = [self.points['l_shoulder'][0] + dx_le, self.points['l_shoulder'][1] + dy_le]

        lower_arm_angle_l = upper_arm_angle_l + current_pose['elbow_angle']
        dx_lw = self.lower_arm_len * math.sin(lower_arm_angle_l)
        dy_lw = self.lower_arm_len * math.cos(lower_arm_angle_l)
        self.points['l_wrist'] = [self.points['l_elbow'][0] + dx_lw, self.points['l_elbow'][1] + dy_lw]

    def draw(self, screen):
        """Draws all point lights on the screen."""
        for name in self.point_names:
            point = self.points.get(name)
            if point:
                pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)

# --- Main Pygame Loop ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Heavy Woman Jumping")
    clock = pygame.time.Clock()

    figure = HumanFigure(SCALE_FACTOR, SCREEN_WIDTH, SCREEN_HEIGHT)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0 # Time since last frame in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Option to restart animation by pressing 'R'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                figure.animation_time = 0.0

        figure.update(dt)

        screen.fill(BLACK) # Clear screen with black background
        figure.draw(screen) # Draw the updated figure
        pygame.display.flip() # Update the full display surface to the screen

    pygame.quit()

if __name__ == "__main__":
    main()
