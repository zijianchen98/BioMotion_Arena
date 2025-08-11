
import pygame
import math

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800  # Portrait mode is suitable for a human figure
CENTER_X = SCREEN_WIDTH // 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point radius
POINT_RADIUS = 5

# Animation parameters
FPS = 60
ANIMATION_DURATION_SECONDS = 3.5  # Duration of one full jump cycle (slightly longer for 'heavy' feel)
TOTAL_FRAMES = int(FPS * ANIMATION_DURATION_SECONDS)

# Scale factor for display
SCALE = 3.0  # Adjust based on how large the figure should be

# Point mapping for 15 points, following the example image's structure.
# Each point's (x, y) is defined relative to the Mid-Torso (point 7) at (0, 0) for the base pose.
# y-values: negative for points above torso, positive for points below (standard Pygame y-axis).
# x-values: positive for right side, negative for left side.
# Initial pose is slightly slumped to represent a "sadman".
BASE_OFFSETS = {
    0: (0, -100),  # Head
    1: (-30, -60), # L Shoulder (slumped inwards slightly)
    2: (30, -60),  # R Shoulder
    3: (-45, -20), # L Elbow (arms slightly bent, hanging forward slightly)
    4: (45, -20),  # R Elbow
    5: (-55, 20),  # L Wrist (hanging lower, slightly forward)
    6: (55, 20),   # R Wrist
    7: (0, 0),     # Mid-Torso (reference point, usually around pelvis/waist)
    8: (-25, 20),  # L Hip
    9: (25, 20),   # R Hip
    10: (-25, 65), # L Knee (slight bend for sadman)
    11: (25, 65),  # R Knee
    12: (-25, 110),# L Ankle
    13: (25, 110), # R Ankle
    14: (0, 120)   # Mid-Foot (directly below Mid-Torso, just below ankles)
}

class HumanFigure:
    def __init__(self, scale=1.0):
        self.scale = scale
        self.points = {}  # Stores current screen (x, y) for each point
        # Scale base offsets once during initialization
        self.base_offsets_scaled = {k: [v[0] * self.scale, v[1] * self.scale] for k, v in BASE_OFFSETS.items()}

        # Sadman specific constants for initial posture adjustments
        self.sad_slump_head_x = 5 * self.scale
        self.sad_slump_head_y = 5 * self.scale
        self.sad_shoulder_in_x = 5 * self.scale
        self.sad_shoulder_down_y = 5 * self.scale

        self.reset_pose()

    def reset_pose(self):
        # Initial posture setup (not strictly used during animation cycle, but good for reset)
        for i, (dx, dy) in self.base_offsets_scaled.items():
            self.points[i] = [dx, dy]

    def update(self, frame_num):
        # Normalize time 't' for the animation cycle (0 to 1)
        t = (frame_num % TOTAL_FRAMES) / TOTAL_FRAMES

        # Define phases for the jump cycle. These are normalized time points (0 to 1).
        t_crouch_start = 0.2
        t_crouch_end = 0.4
        t_push_off_end = 0.6
        t_peak_start = 0.65  # Short peak duration
        t_peak_end = 0.75
        t_land_start = 0.9
        t_land_end = 1.0

        # Max displacement values for torso and limb dynamics (relative to standing posture)
        y_max_crouch_val = 100 * self.scale  # Max torso downward travel during crouch
        y_max_jump_val = -180 * self.scale   # Max torso upward travel during jump (negative means moving up)
        land_impact_depth_val = 40 * self.scale  # How much torso dips below standing on landing

        # Dynamic factors that control limb bending and swinging
        current_y_offset = 0    # Torso Y offset relative to its standing Y (positive=down, negative=up)
        legs_bend_factor = 0    # 0 = straight, 1 = max bend
        arms_swing_factor = 0   # Negative = swing back, Positive = swing forward/up

        # --- Motion Logic based on 't' (time in animation cycle) ---
        if 0 <= t < t_crouch_start:  # Initial "sadman" slump, preparing to crouch
            current_y_offset = 0
            legs_bend_factor = 0.05  # Initial slight bend for sadman
            arms_swing_factor = 0.0  # Arms neutral/slightly forward
        elif t_crouch_start <= t < t_crouch_end:  # Deepen crouch
            t_phase = (t - t_crouch_start) / (t_crouch_end - t_crouch_start)
            current_y_offset = self._ease_in_out(t_phase) * y_max_crouch_val
            legs_bend_factor = 0.05 + self._ease_in_out(t_phase) * 0.95  # From slight to full bend
            arms_swing_factor = -self._ease_in(t_phase) * 0.6  # Arms swing backward (negative x-direction)
        elif t_crouch_end <= t < t_push_off_end:  # Push-off and ascend
            t_phase = (t - t_crouch_end) / (t_push_off_end - t_crouch_end)
            # Torso moves from max crouch depth to max jump height
            current_y_offset = y_max_crouch_val + (y_max_jump_val - y_max_crouch_val) * self._ease_out(t_phase)
            legs_bend_factor = 1.0 - self._ease_out(t_phase) * 1.0  # From full bend to straight
            arms_swing_factor = -0.6 + self._ease_out(t_phase) * 1.2  # Arms swing from back to forward/up
        elif t_peak_start <= t < t_peak_end:  # Peak/Airborne
            current_y_offset = y_max_jump_val
            legs_bend_factor = 0.0  # Legs mostly straight
            arms_swing_factor = 0.6  # Arms held up at peak of swing
        elif t_peak_end <= t < t_land_start:  # Descent
            t_phase = (t - t_peak_end) / (t_land_start - t_peak_end)
            # Torso falls from max jump height back towards standing level
            current_y_offset = y_max_jump_val * (1 - self._ease_in(t_phase))
            legs_bend_factor = self._ease_in(t_phase) * 0.2  # Prepare to bend legs for landing
            arms_swing_factor = 0.6 - self._ease_in(t_phase) * 0.6  # Arms return to neutral
        else:  # t_land_start <= t <= 1.0 (Land/Absorb and return to sadman stance)
            t_phase = (t - t_land_start) / (1.0 - t_land_start)
            # Heavy landing: quick drop below standing, then slower recovery back to initial slump.
            if t_phase < 0.5:
                # Quick dip down for impact
                current_y_offset = self._ease_in(t_phase * 2) * land_impact_depth_val
            else:
                # Slower recovery up to standing position
                current_y_offset = land_impact_depth_val * (1 - self._ease_out((t_phase - 0.5) * 2))

            legs_bend_factor = 0.2 + self._ease_in_out(t_phase) * 0.8  # Deep bend to absorb impact
            arms_swing_factor = 0.0  # Arms return to neutral

        # --- Calculate dynamic limb positions relative to Mid-Torso (point 7) ---
        # `temp_points` stores the dynamically calculated positions relative to point 7.
        temp_points = {7: [0, 0]} # Mid-Torso is the local origin

        # Head (0) - slight slump adjustments
        temp_points[0] = [
            self.base_offsets_scaled[0][0] + self.sad_slump_head_x,
            self.base_offsets_scaled[0][1] + self.sad_slump_head_y
        ]
        
        # Shoulders (1, 2) - slight slump adjustments
        temp_points[1] = [self.base_offsets_scaled[1][0] - self.sad_shoulder_in_x, self.base_offsets_scaled[1][1] + self.sad_shoulder_down_y]
        temp_points[2] = [self.base_offsets_scaled[2][0] + self.sad_shoulder_in_x, self.base_offsets_scaled[2][1] + self.sad_shoulder_down_y]

        # Arms (Elbows 3,4 and Wrists 5,6) - dynamic swinging
        arm_x_swing_amplitude = 30 * self.scale  # Max horizontal swing distance
        arm_y_swing_amplitude = 20 * self.scale  # Max vertical swing distance

        # Arms swing horizontally by `arm_x_swing` (negative for back, positive for forward)
        # Arms also move vertically by `abs(arm_swing_factor)` for an arc-like motion
        arm_x_swing = arms_swing_factor * arm_x_swing_amplitude
        arm_y_swing = abs(arms_swing_factor) * arm_y_swing_amplitude 

        temp_points[3] = [self.base_offsets_scaled[3][0] + arm_x_swing, self.base_offsets_scaled[3][1] - arm_y_swing]
        temp_points[4] = [self.base_offsets_scaled[4][0] + arm_x_swing, self.base_offsets_scaled[4][1] - arm_y_swing]
        temp_points[5] = [self.base_offsets_scaled[5][0] + arm_x_swing * 1.5, self.base_offsets_scaled[5][1] - arm_y_swing * 1.5] # Wrists swing further
        temp_points[6] = [self.base_offsets_scaled[6][0] + arm_x_swing * 1.5, self.base_offsets_scaled[6][1] - arm_y_swing * 1.5]
        
        # Hips (8, 9) - relatively fixed to torso
        temp_points[8] = [self.base_offsets_scaled[8][0], self.base_offsets_scaled[8][1]]
        temp_points[9] = [self.base_offsets_scaled[9][0], self.base_offsets_scaled[9][1]]

        # Legs (Knees 10,11 and Ankles 12,13 and Mid-Foot 14) - dynamic bending
        leg_bend_y_offset = legs_bend_factor * (40 * self.scale)  # Vertical shortening due to bend
        leg_bend_x_offset = legs_bend_factor * (15 * self.scale)  # Horizontal shift (knees forward)

        temp_points[10] = [self.base_offsets_scaled[10][0] + leg_bend_x_offset, self.base_offsets_scaled[10][1] - leg_bend_y_offset]
        temp_points[11] = [self.base_offsets_scaled[11][0] - leg_bend_x_offset, self.base_offsets_scaled[11][1] - leg_bend_y_offset]
        temp_points[12] = [self.base_offsets_scaled[12][0] + leg_bend_x_offset * 0.8, self.base_offsets_scaled[12][1] - leg_bend_y_offset * 1.5] # Ankles move more vertically
        temp_points[13] = [self.base_offsets_scaled[13][0] - leg_bend_x_offset * 0.8, self.base_offsets_scaled[13][1] - leg_bend_y_offset * 1.5]
        temp_points[14] = [self.base_offsets_scaled[14][0] + leg_bend_x_offset * 0.3, self.base_offsets_scaled[14][1] - leg_bend_y_offset * 1.8] # Mid-Foot moves even more

        # --- Apply global screen transformation ---
        # Define the Y coordinate on screen for the approximate ground level where the feet land.
        ground_level_y = SCREEN_HEIGHT * 0.85 

        # Calculate the Y coordinate of Mid-Torso (point 7) when the figure is standing (t=0).
        # This is `ground_level_y` minus the vertical distance from Mid-Torso to Mid-Foot in the base pose.
        initial_mid_torso_screen_y = ground_level_y - abs(self.base_offsets_scaled[7][1] - self.base_offsets_scaled[14][1])

        # Apply global x-centering and y-translation to all points to get final screen coordinates
        for i in range(15):
            self.points[i][0] = CENTER_X + temp_points[i][0]
            self.points[i][1] = initial_mid_torso_screen_y + temp_points[i][1] + current_y_offset

    # --- Easing Functions for Smooth Motion ---
    def _ease_in_out(self, t):
        # Smooth start and end (smootherstep function)
        return 3 * t**2 - 2 * t**3

    def _ease_in(self, t):
        # Accelerate from zero velocity
        return t**2

    def _ease_out(self, t):
        # Decelerate to zero velocity
        return 1 - (1 - t)**2

    def draw(self, screen):
        # Draw each point as a white circle on the black background
        for i in range(15):
            pygame.draw.circle(screen, WHITE, (int(self.points[i][0]), int(self.points[i][1])), POINT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sadman with Heavy Weight Jumping")
    clock = pygame.time.Clock()

    figure = HumanFigure(scale=SCALE)
    
    running = True
    frame_num = 0

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Allow ESC to quit
                    running = False

        # Update the figure's pose for the current frame
        figure.update(frame_num)

        # Drawing
        screen.fill(BLACK)  # Clear the screen with black
        figure.draw(screen) # Draw the updated figure
        pygame.display.flip() # Update the full display surface to the screen

        # Control frame rate and advance frame number
        frame_num += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
