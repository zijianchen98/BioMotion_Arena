
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_CENTER_X = SCREEN_WIDTH // 2
SCREEN_CENTER_Y = SCREEN_HEIGHT // 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point settings
POINT_RADIUS = 5

# Animation settings
FPS = 60
ANIMATION_DURATION_SECONDS = 3.0  # Duration of one full wave cycle for smoothness and a "sadwoman" feel

# --- Biomechanical Model Constants (relative lengths) ---
# These proportions are adjusted for a 'light weight' (slender) appearance.
P_HEAD_RADIUS = 0.5  # Represents height of the head from CST to top point
P_NECK_LENGTH = 0.4
P_TORSO_LENGTH = 1.7  # Chest/Upper Spine (CST) to Lower Spine/Pelvis (CSP)
P_SHOULDER_WIDTH = 0.9  # Half width from central spine to shoulder
P_UPPER_ARM_LENGTH = 1.4
P_FOREARM_LENGTH = 1.2
P_HIP_WIDTH = 0.7  # Half width from central spine to hip
P_UPPER_LEG_LENGTH = 1.7
P_LOWER_LEG_LENGTH = 1.5

# Scaling factor for the entire figure to fit the screen
FIGURE_SCALE = 50

# Mapping logical joint names to a list index (0-14 for 15 points, matching example image)
POINT_MAP = {
    "H": 0,    # Head
    "SL": 1,   # Shoulder Left
    "SR": 2,   # Shoulder Right
    "CST": 3,  # Chest/Upper Spine (Central)
    "EL": 4,   # Elbow Left
    "ER": 5,   # Elbow Right
    "WL": 6,   # Wrist Left
    "WR": 7,   # Wrist Right
    "CSP": 8,  # Lower Spine/Pelvis (Central)
    "HL": 9,   # Hip Left
    "HR": 10,  # Hip Right
    "KL": 11,  # Knee Left
    "KR": 12,  # Knee Right
    "AL": 13,  # Ankle Left
    "AR": 14   # Ankle Right
}

class HumanFigure:
    def __init__(self, x_offset, y_offset, scale):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale

        # Scaled lengths based on proportions
        self.head_radius = P_HEAD_RADIUS * self.scale
        self.neck_length = P_NECK_LENGTH * self.scale
        self.torso_length = P_TORSO_LENGTH * self.scale
        self.shoulder_width = P_SHOULDER_WIDTH * self.scale
        self.upper_arm_length = P_UPPER_ARM_LENGTH * self.scale
        self.forearm_length = P_FOREARM_LENGTH * self.scale
        self.hip_width = P_HIP_WIDTH * self.scale
        self.upper_leg_length = P_UPPER_LEG_LENGTH * self.scale
        self.lower_leg_length = P_LOWER_LEG_LENGTH * self.scale

        # List of (x,y) tuples for the 15 points
        self.point_coords = [(0, 0)] * 15

        # Initial Angles (in radians) for a relaxed, standing pose
        # Angle of segment from horizontal positive x-axis, counter-clockwise.
        # -math.pi / 2 (-90 deg) is straight down.
        self.angles = {
            # Left arm (static, hanging down)
            "upper_arm_L": -math.pi / 2,
            "forearm_L_relative": 0, # relative to upper arm (straight)
            # Legs (static, straight down)
            "upper_leg_L": -math.pi / 2,
            "lower_leg_L_relative": 0,
            "upper_leg_R": -math.pi / 2,
            "lower_leg_R_relative": 0,
            # Right arm (waving) - these will be dynamically calculated
            "upper_arm_R_absolute": 0,
            "forearm_R_absolute": 0,
            "wrist_R_absolute": 0
        }
        
        # Calculate absolute angles for static limbs
        self.angles["forearm_L_absolute"] = self.angles["upper_arm_L"] + self.angles["forearm_L_relative"]
        self.angles["lower_leg_L_absolute"] = self.angles["upper_leg_L"] + self.angles["lower_leg_L_relative"]
        self.angles["lower_leg_R_absolute"] = self.angles["upper_leg_R"] + self.angles["lower_leg_R_relative"]

    def update(self, time_s):
        # Base position for the Chest/Upper Spine (CST) point
        base_x = self.x_offset
        base_y = self.y_offset

        # Calculate coordinates for all points based on the kinematic chain
        # Order of calculation matters for parent-child relationships

        # 1. Chest/Upper Spine (CST) - root of the upper body
        self.point_coords[POINT_MAP["CST"]] = (base_x, base_y)

        # 2. Head (H) - above CST
        self.point_coords[POINT_MAP["H"]] = (
            self.point_coords[POINT_MAP["CST"]][0],
            self.point_coords[POINT_MAP["CST"]][1] - self.neck_length - self.head_radius
        )

        # 3. Shoulders (SL, SR) - to the sides of CST, slightly below for a natural look
        shoulder_y_offset_from_CST = self.neck_length * 0.2
        self.point_coords[POINT_MAP["SL"]] = (
            self.point_coords[POINT_MAP["CST"]][0] - self.shoulder_width,
            self.point_coords[POINT_MAP["CST"]][1] + shoulder_y_offset_from_CST
        )
        self.point_coords[POINT_MAP["SR"]] = (
            self.point_coords[POINT_MAP["CST"]][0] + self.shoulder_width,
            self.point_coords[POINT_MAP["CST"]][1] + shoulder_y_offset_from_CST
        )

        # 4. Lower Spine/Pelvis (CSP) - below CST
        self.point_coords[POINT_MAP["CSP"]] = (
            self.point_coords[POINT_MAP["CST"]][0],
            self.point_coords[POINT_MAP["CST"]][1] + self.torso_length
        )

        # 5. Hips (HL, HR) - to the sides of CSP
        self.point_coords[POINT_MAP["HL"]] = (
            self.point_coords[POINT_MAP["CSP"]][0] - self.hip_width,
            self.point_coords[POINT_MAP["CSP"]][1]
        )
        self.point_coords[POINT_MAP["HR"]] = (
            self.point_coords[POINT_MAP["CSP"]][0] + self.hip_width,
            self.point_coords[POINT_MAP["CSP"]][1]
        )

        # --- Animate Right Arm (Waving) ---
        # The wave motion combines:
        # 1. Upper arm slightly raised/forward from body.
        # 2. Elbow bending and straightening slightly.
        # 3. Wrist waving side-to-side.

        # Phase for the wave animation (using sine waves for smooth, cyclical motion)
        # Multipliers (1.0, 1.5, 2.0) provide slightly different frequencies for naturalness
        wave_phase = time_s * (2 * math.pi / ANIMATION_DURATION_SECONDS)

        # Upper arm (SR-ER) angle: Oscillate around a slightly raised base angle
        # Base angle: -90 deg (straight down). Target: -70 deg (raised ~20 deg forward/side from vertical)
        base_upper_arm_R_angle = math.radians(-70)
        upper_arm_R_swing_amplitude = math.radians(10) # Small swing
        self.angles["upper_arm_R_absolute"] = base_upper_arm_R_angle + math.sin(wave_phase * 1.0) * upper_arm_R_swing_amplitude

        # Forearm (ER-WR) angle: Oscillate elbow bend relative to upper arm
        # Base elbow bend: 70 degrees (relative from straight, where 0=straight, 90=L-shape)
        base_forearm_R_bend_relative = math.radians(70)
        forearm_R_bend_amplitude = math.radians(20) # Small bend variation
        # Add math.pi/2 to phase for a slight offset in motion timing
        current_forearm_R_bend_relative = base_forearm_R_bend_relative + math.sin(wave_phase * 1.5 + math.pi/2) * forearm_R_bend_amplitude
        # Absolute angle of forearm is upper arm's absolute angle plus relative bend
        self.angles["forearm_R_absolute"] = self.angles["upper_arm_R_absolute"] + current_forearm_R_bend_relative

        # Wrist (WR) angle: Oscillate wrist wave relative to forearm
        # Base wrist angle: 0 (straight relative). Wave amplitude: +/- 25 degrees
        wrist_R_wave_amplitude = math.radians(25)
        current_wrist_R_wave_relative = math.sin(wave_phase * 2.0) * wrist_R_wave_amplitude
        # Absolute angle of the wrist point
        self.angles["wrist_R_absolute"] = self.angles["forearm_R_absolute"] + current_wrist_R_wave_relative

        # 6. Elbows (EL, ER)
        # Left Arm (static)
        self.point_coords[POINT_MAP["EL"]] = (
            self.point_coords[POINT_MAP["SL"]][0] + self.upper_arm_length * math.cos(self.angles["upper_arm_L"]),
            self.point_coords[POINT_MAP["SL"]][1] + self.upper_arm_length * math.sin(self.angles["upper_arm_L"])
        )
        # Right Arm (waving)
        self.point_coords[POINT_MAP["ER"]] = (
            self.point_coords[POINT_MAP["SR"]][0] + self.upper_arm_length * math.cos(self.angles["upper_arm_R_absolute"]),
            self.point_coords[POINT_MAP["SR"]][1] + self.upper_arm_length * math.sin(self.angles["upper_arm_R_absolute"])
        )

        # 7. Wrists (WL, WR)
        # Left Arm (static)
        self.point_coords[POINT_MAP["WL"]] = (
            self.point_coords[POINT_MAP["EL"]][0] + self.forearm_length * math.cos(self.angles["forearm_L_absolute"]),
            self.point_coords[POINT_MAP["EL"]][1] + self.forearm_length * math.sin(self.angles["forearm_L_absolute"])
        )
        # Right Arm (waving)
        self.point_coords[POINT_MAP["WR"]] = (
            self.point_coords[POINT_MAP["ER"]][0] + self.forearm_length * math.cos(self.angles["wrist_R_absolute"]),
            self.point_coords[POINT_MAP["ER"]][1] + self.forearm_length * math.sin(self.angles["wrist_R_absolute"])
        )

        # 8. Knees (KL, KR)
        # Legs (static)
        self.point_coords[POINT_MAP["KL"]] = (
            self.point_coords[POINT_MAP["HL"]][0] + self.upper_leg_length * math.cos(self.angles["upper_leg_L"]),
            self.point_coords[POINT_MAP["HL"]][1] + self.upper_leg_length * math.sin(self.angles["upper_leg_L"])
        )
        self.point_coords[POINT_MAP["KR"]] = (
            self.point_coords[POINT_MAP["HR"]][0] + self.upper_leg_length * math.cos(self.angles["upper_leg_R"]),
            self.point_coords[POINT_MAP["HR"]][1] + self.upper_leg_length * math.sin(self.angles["upper_leg_R"])
        )

        # 9. Ankles (AL, AR)
        # Legs (static)
        self.point_coords[POINT_MAP["AL"]] = (
            self.point_coords[POINT_MAP["KL"]][0] + self.lower_leg_length * math.cos(self.angles["lower_leg_L_absolute"]),
            self.point_coords[POINT_MAP["KL"]][1] + self.lower_leg_length * math.sin(self.angles["lower_leg_L_absolute"])
        )
        self.point_coords[POINT_MAP["AR"]] = (
            self.point_coords[POINT_MAP["KR"]][0] + self.lower_leg_length * math.cos(self.angles["lower_leg_R_absolute"]),
            self.point_coords[POINT_MAP["KR"]][1] + self.lower_leg_length * math.sin(self.angles["lower_leg_R_absolute"])
        )

    def draw(self, screen):
        # Draw each of the 15 points
        for pos in self.point_coords:
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus: Waving Sadwoman")

clock = pygame.time.Clock()

# Position the figure: CST (Chest/Upper Spine) will be the anchor point.
# Calculate y_offset for CST to center the figure vertically.
# The `total_figure_height_scaled` calculates distance from top of head to ankles.
total_figure_height_scaled = (P_HEAD_RADIUS + P_NECK_LENGTH + P_TORSO_LENGTH + P_UPPER_LEG_LENGTH + P_LOWER_LEG_LENGTH) * FIGURE_SCALE
# CST's y_offset = screen_center_y - (distance from CST to top of head) + (half total figure height)
# Simplified: Place CST slightly above screen center.
initial_cst_y = SCREEN_CENTER_Y - (P_TORSO_LENGTH * FIGURE_SCALE / 2) + 20 

figure = HumanFigure(SCREEN_CENTER_X, initial_cst_y, FIGURE_SCALE)

running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Allow closing with 'q' or 'escape' for convenience during testing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BLACK)

    # Calculate elapsed time in seconds for animation looping
    elapsed_time_ms = pygame.time.get_ticks() - start_time
    time_s = (elapsed_time_ms / 1000.0) % ANIMATION_DURATION_SECONDS

    figure.update(time_s)
    figure.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
