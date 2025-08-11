
import pygame
import math

# Screen dimensions
WIDTH, HEIGHT = 600, 800
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point size
POINT_RADIUS = 5

# Mapping point names to indices for easy access
# 15 points: Head, L/R Shoulder, L/R Elbow, L/R Wrist, Center Thorax, L/R Hip, Pelvis, L/R Knee, L/R Ankle.
POINT_NAMES = [
    'head',
    'shoulder_l', 'shoulder_r',
    'elbow_l', 'elbow_r',
    'wrist_l', 'wrist_r',
    'torso_c',
    'hip_l', 'hip_r',
    'pelvis_c',
    'knee_l', 'knee_r',
    'ankle_l', 'ankle_r'
]

class BioMotion:
    def __init__(self, x_center, y_center, scale=1.0):
        self.x_center = x_center
        self.y_center = y_center
        self.scale = scale # Overall scale factor for the figure

        # Biomechanical constants (approximate relative proportions)
        # These are segment lengths relative to a 'unit' scale
        self.segment_lengths = {
            'torso_pelvis_c': 0.1,  # Pelvis to Torso_Center (approx half torso height)
            'torso_shoulder_c': 0.1, # Torso_Center to Shoulder Center (approx half torso height)
            'shoulder_half_width': 0.15,
            'hip_half_width': 0.125,
            'arm_upper': 0.2,       # shoulder to elbow
            'arm_lower': 0.18,      # elbow to wrist
            'leg_upper': 0.25,      # hip to knee
            'leg_lower': 0.23,      # knee to ankle
            'head_neck': 0.1        # Neck base (shoulder center) to head
        }

        # Joint angles (radians) and direct offsets
        # Angles are generally relative to a parent joint. For vertical limbs, angle 0 is vertical down.
        # For torso/head, angles are from a vertical line (negative Y axis). Positive is clockwise (leaning forward/right).
        self.angles = {
            # Initial 'sad' / 'heavy' posture
            'torso_lean': math.radians(5),    # Slight forward lean of torso
            'head_tilt': math.radians(-10),   # Head slightly tilted down (negative is counter-clockwise from vertical up)
            'shoulder_slump': math.radians(5),# Shoulders drooping inwards

            # Right arm (waving) initial pose
            'r_shoulder_flexion': math.radians(20), # Angle from vertical, forward/back motion
            'r_shoulder_abduction': math.radians(0), # Angle from side, out/in motion
            'r_elbow_flexion': math.radians(30), # Angle of forearm relative to upper arm (0=straight, positive=flexed)
            'r_wrist_wave_offset_x': 0.0,    # Direct X offset for wrist wave (simulation)

            # Left arm (static, subtle sway) initial pose
            'l_shoulder_flexion': math.radians(20),
            'l_shoulder_abduction': math.radians(0),
            'l_elbow_flexion': math.radians(30),

            # Legs (stance, subtle weight shift) initial pose
            'r_hip_flexion': math.radians(0), # Front/back leg swing
            'r_hip_abduction': math.radians(5), # Out/in leg spread
            'r_knee_flexion': math.radians(10), # Knee bend

            'l_hip_flexion': math.radians(0),
            'l_hip_abduction': math.radians(5),
            'l_knee_flexion': math.radians(10),

            # Overall body position for subtle sway
            'body_sway_x_offset': 0.0, # Horizontal offset for the entire figure
        }

        self.animation_time = 0.0
        self.wave_speed = 0.8 # Overall animation speed (slower for 'sad' / 'heavy')

        # This will store the calculated (x,y) for each point in the current frame (screen coordinates)
        self.current_points_display = {name: [0, 0] for name in POINT_NAMES}

        # Calculate initial pose
        self._calculate_current_frame_positions()

    def _get_segment_length(self, name):
        """Helper to get scaled segment length."""
        return self.segment_lengths[name] * self.scale

    def _calculate_current_frame_positions(self):
        """
        Calculates the (x,y) positions for all 15 points based on current joint angles.
        All calculations are relative to a fixed (0,0) origin (the pelvis_c's animated position),
        then translated to screen coordinates at the end.
        """
        relative_points = {name: [0.0, 0.0] for name in POINT_NAMES}

        # Root joint: Pelvis Center
        # This point itself can have an animated horizontal offset (body sway)
        pelvis_c_x_relative_to_model_origin = self.angles['body_sway_x_offset']
        pelvis_c_y_relative_to_model_origin = 0.0 # Pelvis is the vertical anchor for the model

        relative_points['pelvis_c'] = [pelvis_c_x_relative_to_model_origin, pelvis_c_y_relative_to_model_origin]
        
        # Hips (relative to pelvis_c)
        hip_half_width = self._get_segment_length('hip_half_width')
        # Left hip is to the left (negative x), right hip to the right (positive x)
        relative_points['hip_l'] = [pelvis_c_x_relative_to_model_origin - hip_half_width, pelvis_c_y_relative_to_model_origin]
        relative_points['hip_r'] = [pelvis_c_x_relative_to_model_origin + hip_half_width, pelvis_c_y_relative_to_model_origin]

        # Torso Center (relative to pelvis_c, applying torso lean)
        tc_parent_x, tc_parent_y = relative_points['pelvis_c']
        torso_len_p = self._get_segment_length('torso_pelvis_c')
        # Angles are from -Y axis (upwards) clockwise.
        # For a forward lean (positive lean_angle), x increases, y decreases (moves up).
        relative_points['torso_c'][0] = tc_parent_x + torso_len_p * math.sin(self.angles['torso_lean'])
        relative_points['torso_c'][1] = tc_parent_y - torso_len_p * math.cos(self.angles['torso_lean'])

        # Shoulders (relative to torso_c)
        sc_parent_x, sc_parent_y = relative_points['torso_c']
        torso_len_shoulder_c = self._get_segment_length('torso_shoulder_c')
        shoulder_half_width = self._get_segment_length('shoulder_half_width')

        # Calculate shoulder center point relative to torso_c (considering torso lean for alignment)
        # The shoulder_center_x_local, y_local ensures it pivots with the torso
        shoulder_center_x_local = torso_len_shoulder_c * math.sin(self.angles['torso_lean'])
        shoulder_center_y_local = -torso_len_shoulder_c * math.cos(self.angles['torso_lean'])

        # Apply slump effect: Shoulders move slightly down and in
        slump_offset_x = math.sin(self.angles['shoulder_slump']) * shoulder_half_width * 0.2
        slump_offset_y = math.cos(self.angles['shoulder_slump']) * torso_len_shoulder_c * 0.1 # Slight vertical drop

        relative_points['shoulder_l'] = [sc_parent_x + shoulder_center_x_local - shoulder_half_width + slump_offset_x, sc_parent_y + shoulder_center_y_local + slump_offset_y]
        relative_points['shoulder_r'] = [sc_parent_x + shoulder_center_x_local + shoulder_half_width - slump_offset_x, sc_parent_y + shoulder_center_y_local + slump_offset_y]

        # Head (relative to neck base = average of shoulders, then tilt)
        neck_base_x = (relative_points['shoulder_l'][0] + relative_points['shoulder_r'][0]) / 2
        neck_base_y = (relative_points['shoulder_l'][1] + relative_points['shoulder_r'][1]) / 2
        
        head_neck_len = self._get_segment_length('head_neck')
        # Head angle relative to vertical (-Y axis) from neck base, also influenced by torso lean
        head_abs_angle = self.angles['head_tilt'] + self.angles['torso_lean']
        relative_points['head'][0] = neck_base_x + head_neck_len * math.sin(head_abs_angle)
        relative_points['head'][1] = neck_base_y - head_neck_len * math.cos(head_abs_angle)


        # --- Arms ---
        arm_upper_len = self._get_segment_length('arm_upper')
        arm_lower_len = self._get_segment_length('arm_lower')

        # Right Arm (Waving)
        sr_x, sr_y = relative_points['shoulder_r']
        # Shoulder flexion and abduction combined for a 2D-like swing
        shoulder_abs_angle_r = self.angles['r_shoulder_flexion'] + self.angles['r_shoulder_abduction'] 
        relative_points['elbow_r'][0] = sr_x + arm_upper_len * math.sin(shoulder_abs_angle_r)
        relative_points['elbow_r'][1] = sr_y + arm_upper_len * math.cos(shoulder_abs_angle_r)

        # Elbow (relative to shoulder)
        er_x, er_y = relative_points['elbow_r']
        # Forearm angle is relative to upper arm
        forearm_abs_angle_r = shoulder_abs_angle_r + self.angles['r_elbow_flexion']
        
        # Wrist_R (Apply the direct X offset for the wave, to the base position)
        wrist_base_x = er_x + arm_lower_len * math.sin(forearm_abs_angle_r)
        wrist_base_y = er_y + arm_lower_len * math.cos(forearm_abs_angle_r)
        
        relative_points['wrist_r'] = [wrist_base_x + self.angles['r_wrist_wave_offset_x'], wrist_base_y]

        # Left Arm (Static)
        sl_x, sl_y = relative_points['shoulder_l']
        shoulder_abs_angle_l = self.angles['l_shoulder_flexion'] + self.angles['l_shoulder_abduction']
        relative_points['elbow_l'][0] = sl_x - arm_upper_len * math.sin(shoulder_abs_angle_l) # Mirror x for left arm
        relative_points['elbow_l'][1] = sl_y + arm_upper_len * math.cos(shoulder_abs_angle_l)

        el_x, el_y = relative_points['elbow_l']
        forearm_abs_angle_l = shoulder_abs_angle_l + self.angles['l_elbow_flexion']
        relative_points['wrist_l'][0] = el_x - arm_lower_len * math.sin(forearm_abs_angle_l) # Mirror x
        relative_points['wrist_l'][1] = el_y + arm_lower_len * math.cos(forearm_abs_angle_l)


        # --- Legs ---
        leg_upper_len = self._get_segment_length('leg_upper')
        leg_lower_len = self._get_segment_length('leg_lower')

        # Right Leg
        hr_x, hr_y = relative_points['hip_r']
        hip_abs_angle_r = self.angles['r_hip_abduction']
        relative_points['knee_r'][0] = hr_x + leg_upper_len * math.sin(hip_abs_angle_r)
        relative_points['knee_r'][1] = hr_y + leg_upper_len * math.cos(hip_abs_angle_r)

        kr_x, kr_y = relative_points['knee_r']
        calf_abs_angle_r = hip_abs_angle_r + self.angles['r_knee_flexion']
        relative_points['ankle_r'][0] = kr_x + leg_lower_len * math.sin(calf_abs_angle_r)
        relative_points['ankle_r'][1] = kr_y + leg_lower_len * math.cos(calf_abs_angle_r)

        # Left Leg
        hl_x, hl_y = relative_points['hip_l']
        hip_abs_angle_l = self.angles['l_hip_abduction']
        relative_points['knee_l'][0] = hl_x - leg_upper_len * math.sin(hip_abs_angle_l) # Mirror x for left leg
        relative_points['knee_l'][1] = hl_y + leg_upper_len * math.cos(hip_abs_angle_l)

        kl_x, kl_y = relative_points['knee_l']
        calf_abs_angle_l = hip_abs_angle_l + self.angles['l_knee_flexion']
        relative_points['ankle_l'][0] = kl_x - leg_lower_len * math.sin(calf_abs_angle_l) # Mirror x
        relative_points['ankle_l'][1] = kl_y + leg_lower_len * math.cos(calf_abs_angle_l)


        # --- Apply global translation to screen coordinates ---
        # Find the lowest y (highest value in pygame coords) among ankles for grounding.
        lowest_y_model = max(relative_points['ankle_l'][1], relative_points['ankle_r'][1])
        
        # Calculate the offset needed to move the lowest point to `self.y_center`
        overall_y_offset = self.y_center - lowest_y_model
        
        for name in POINT_NAMES:
            self.current_points_display[name][0] = relative_points[name][0] + self.x_center
            self.current_points_display[name][1] = relative_points[name][1] + overall_y_offset

    def update(self, dt):
        """Updates the animation state based on time elapsed."""
        self.animation_time += dt

        # --- Waving Arm Animation (Right Arm) ---
        wave_cycle_main = math.sin(self.animation_time * self.wave_speed) # Main cycle for wave speed
        wave_cycle_faster = math.sin(self.animation_time * self.wave_speed * 1.5) # Faster cycle for wrist

        # Shoulder lift/swing: small forward/backward and slight lift
        # (wave_cycle_main + 1) / 2 transforms sine from [-1, 1] to [0, 1]
        self.angles['r_shoulder_flexion'] = math.radians(20) + (wave_cycle_main + 1) / 2 * math.radians(25) # Lift arm forward/up
        self.angles['r_shoulder_abduction'] = math.radians(0) + (wave_cycle_main + 1) / 2 * math.radians(10) # Lift slightly outwards

        # Elbow bend: follows the shoulder, adding to the waving motion
        self.angles['r_elbow_flexion'] = math.radians(30) + (wave_cycle_main + 1) / 2 * math.radians(30) # Bend more during wave

        # Wrist wave: the actual "waving" motion (simulated by X offset)
        self.angles['r_wrist_wave_offset_x'] = wave_cycle_faster * self._get_segment_length('arm_lower') * 0.4 # Horizontal swing

        # --- Left Arm subtle sway ---
        left_arm_sway_magnitude = math.radians(3)
        left_arm_sway_offset = math.sin(self.animation_time * self.wave_speed * 0.5) * left_arm_sway_magnitude
        self.angles['l_shoulder_flexion'] = math.radians(20) + left_arm_sway_offset

        # --- Torso/Head/Legs subtle compensation for "sad" and "heavy" ---
        # Overall body sway (slow, heavy)
        body_sway_magnitude_x = self.scale * 0.015 # Small side-to-side body shift for "heavy"
        self.angles['body_sway_x_offset'] = math.sin(self.animation_time * self.wave_speed * 0.2) * body_sway_magnitude_x
        
        # Small adjustments to initial angles for "sad" / "heavy"
        self.angles['torso_lean'] = math.radians(5) + math.sin(self.animation_time * self.wave_speed * 0.3) * math.radians(2) # Slight sway in torso lean
        self.angles['head_tilt'] = math.radians(-10) + math.sin(self.animation_time * self.wave_speed * 0.4) * math.radians(2) # Slight head bob
        self.angles['shoulder_slump'] = math.radians(5) + math.sin(self.animation_time * self.wave_speed * 0.6) * math.radians(1) # Subtle shoulder movement

        # Leg weight shift (subtle hip abduction change for balance)
        leg_weight_shift_magnitude = math.radians(2)
        leg_shift_phase = math.sin(self.animation_time * self.wave_speed * 0.4)
        self.angles['r_hip_abduction'] = math.radians(5) + leg_shift_phase * leg_weight_shift_magnitude
        self.angles['l_hip_abduction'] = math.radians(5) - leg_shift_phase * leg_weight_shift_magnitude # Opposite shift

        # Now, re-calculate all point positions based on updated angles
        self._calculate_current_frame_positions()

    def draw(self, screen):
        """Draws the current points on the screen."""
        for name in POINT_NAMES:
            x, y = self.current_points_display[name]
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Waving")
clock = pygame.time.Clock()

# Create BioMotion instance
# Estimate total height ratio based on initial segment lengths for scaling.
# This ensures the figure approximately fills a desired portion of the screen.
estimated_height_ratio = (BioMotion(0,0,1).segment_lengths['leg_upper'] +
                          BioMotion(0,0,1).segment_lengths['leg_lower'] +
                          BioMotion(0,0,1).segment_lengths['torso_pelvis_c'] +
                          BioMotion(0,0,1).segment_lengths['torso_shoulder_c'] +
                          BioMotion(0,0,1).segment_lengths['head_neck'])

figure_scale = HEIGHT * 0.75 / estimated_height_ratio # Make figure about 75% of screen height

# figure_y_center: This is the Y-coordinate where the lowest point (ankles) of the figure will be placed.
figure_y_center = HEIGHT * 0.9 # Place ankles at 90% down the screen for grounding

# Initialize the BioMotion figure
figure = BioMotion(WIDTH // 2, figure_y_center, scale=figure_scale)

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(FPS) / 1000.0 # Time since last frame in seconds (for consistent speed)

    figure.update(dt) # Update joint angles and recalculate positions

    screen.fill(BLACK) # Clear screen to black
    figure.draw(screen) # Draw the white point-lights
    pygame.display.flip() # Update the full display Surface to the screen

pygame.quit()
