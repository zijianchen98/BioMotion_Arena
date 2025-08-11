
import pygame
import math

# --- Pygame Setup ---
WIDTH, HEIGHT = 800, 600
FPS = 60
DOT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down")
clock = pygame.time.Clock()

# --- Body Segment Lengths (arbitrary, adjust for realism and visual scale) ---
# All units are conceptual pixels. These define the proportions of the human figure.
SHOULDER_WIDTH = 30
HEAD_NECK_LENGTH = 20  # Length from neck base to top of head
TORSO_LENGTH = 60      # Length from hips (pelvis_center) to shoulder level

UPPER_ARM_LENGTH = 40
LOWER_ARM_LENGTH = 35

UPPER_LEG_LENGTH = 60
LOWER_LEG_LENGTH = 55  # Length from knee to ankle

# --- Humanoid Class ---
class Humanoid:
    def __init__(self, center_x, ground_y):
        self.center_x = center_x
        self.ground_y = ground_y  # The Y coordinate of the "ground" plane

        # Dictionaries to store point coordinates
        self.points = {}       # Stores (x, y) for each point in its local skeleton space (relative to pelvis_center)
        self.display_points = {} # Stores final (x, y) after global translation for drawing

        # Animation progress (0.0 = standing, 1.0 = fully seated)
        self.sit_progress = 0.0
        self.sit_speed = 0.015  # Speed of sitting transition (adjust for faster/slower animation)

        # Define specific pelvis_center heights above the ground for standing and sitting
        # These are empirically set for a visually pleasing and stable animation
        # Standing: Pelvis_center is above the ground, allowing full leg extension.
        self.standing_pelvis_height_above_ground = LOWER_LEG_LENGTH + UPPER_LEG_LENGTH - 10 
        # Sitting: Pelvis_center is lower, simulating sitting on a surface.
        self.sitting_pelvis_height_above_ground = LOWER_LEG_LENGTH / 2 + 5 

    def update(self):
        # Update animation progress
        self.sit_progress = min(1.0, self.sit_progress + self.sit_speed)

        # --- Interpolate Joint Angles and Determine Apparent Segment Lengths ---
        # For a frontal 2D point-light display, actual 3D joint bends (like hip/knee flexion)
        # are represented as an apparent vertical shortening of the segments.
        
        # Hip bend angle (in the sagittal plane - effectively controls vertical leg compression)
        standing_hip_bend_angle = math.radians(0)  # Straight leg
        sitting_hip_bend_angle = math.radians(90) # Bent 90 degrees at hip (upper leg becomes "horizontal" in 3D)
        current_hip_bend_angle = standing_hip_bend_angle + \
                                 (sitting_hip_bend_angle - standing_hip_bend_angle) * self.sit_progress

        # Knee bend angle (in the sagittal plane - controls lower leg compression)
        standing_knee_bend_angle = math.radians(0)  # Straight leg
        sitting_knee_bend_angle = math.radians(90) # Bent 90 degrees at knee (lower leg becomes "horizontal" in 3D)
        current_knee_bend_angle = standing_knee_bend_angle + \
                                  (sitting_knee_bend_angle - standing_knee_bend_angle) * self.sit_progress

        # Calculate apparent vertical lengths (projection onto the 2D frontal plane)
        # When a segment bends in 3D (e.g., knee bends), its projection onto the 2D plane shortens.
        # This shortening is approximated by cos(bend_angle).
        apparent_upper_leg_len = UPPER_LEG_LENGTH * math.cos(current_hip_bend_angle)
        apparent_lower_leg_len = LOWER_LEG_LENGTH * math.cos(current_knee_bend_angle)

        # Torso angle (frontal plane lean)
        # For a frontal view, a 'sitting down' action typically keeps the torso mostly upright.
        # We will keep the torso strictly vertical for simplicity and symmetry, aligning with the example image.
        current_torso_angle = math.radians(0) 

        # Arm angles (hanging down naturally)
        current_shoulder_angle = math.radians(0) # Upper arms hanging vertically
        current_elbow_angle = math.radians(0)    # Lower arms straight from upper arms

        # --- Calculate Global Y Position of Pelvis_center ---
        # The pelvis_center is the reference point for the entire figure's vertical movement.
        # It interpolates between the standing and sitting heights relative to the ground.
        self.pelvis_center_global_y = self.ground_y - \
                                      (self.standing_pelvis_height_above_ground * (1 - self.sit_progress) +
                                       self.sitting_pelvis_height_above_ground * self.sit_progress)
        
        # --- Calculate Joint Positions in Local Skeleton Space (relative to pelvis_center at 0,0) ---
        pelvis_center_x_local, pelvis_center_y_local = 0, 0
        self.points['pelvis_center'] = (pelvis_center_x_local, pelvis_center_y_local)

        # Hip joints (slightly above the conceptual pelvis_center point)
        hip_y_offset = -5 # Hip joints are anatomically slightly above the very center of the pelvis mass
        hip_L_local_x, hip_L_local_y = pelvis_center_x_local - SHOULDER_WIDTH/4, pelvis_center_y_local + hip_y_offset
        hip_R_local_x, hip_R_local_y = pelvis_center_x_local + SHOULDER_WIDTH/4, pelvis_center_y_local + hip_y_offset
        self.points['hip_L'] = (hip_L_local_x, hip_L_local_y)
        self.points['hip_R'] = (hip_R_local_x, hip_R_local_y)

        # Legs (frontal view: primarily vertical compression)
        # Left Leg
        knee_L_local_x = hip_L_local_x
        knee_L_local_y = hip_L_local_y + apparent_upper_leg_len

        ankle_L_local_x = knee_L_local_x
        ankle_L_local_y = knee_L_local_y + apparent_lower_leg_len

        self.points['knee_L'] = (knee_L_local_x, knee_L_local_y)
        self.points['ankle_L'] = (ankle_L_local_x, ankle_L_local_y)

        # Right Leg (symmetric to left leg)
        knee_R_local_x = hip_R_local_x
        knee_R_local_y = hip_R_local_y + apparent_upper_leg_len

        ankle_R_local_x = knee_R_local_x
        ankle_R_local_y = knee_R_local_y + apparent_lower_leg_len

        self.points['knee_R'] = (knee_R_local_x, knee_R_local_y)
        self.points['ankle_R'] = (ankle_R_local_x, ankle_R_local_y)

        # Torso, Head, Neck (rotated by torso_angle around pelvis_center)
        shoulder_y_offset = -TORSO_LENGTH # Shoulders are above pelvis_center in local coordinates

        # Define a helper function for rotation around origin (pelvis_center)
        def rotate_around_origin(px, py, angle):
            cos_angle = math.cos(angle)
            sin_angle = math.sin(angle)
            rotated_x = px * cos_angle - py * sin_angle
            rotated_y = px * sin_angle + py * cos_angle
            return rotated_x, rotated_y

        # Original points for torso/head/neck before applying torso rotation
        sL_orig_x, sL_orig_y = pelvis_center_x_local - SHOULDER_WIDTH/2, pelvis_center_y_local + shoulder_y_offset
        sR_orig_x, sR_orig_y = pelvis_center_x_local + SHOULDER_WIDTH/2, pelvis_center_y_local + shoulder_y_offset
        neck_orig_x, neck_orig_y = pelvis_center_x_local, pelvis_center_y_local + shoulder_y_offset - HEAD_NECK_LENGTH/2
        head_orig_x, head_orig_y = pelvis_center_x_local, pelvis_center_y_local + shoulder_y_offset - HEAD_NECK_LENGTH

        # Apply torso rotation (current_torso_angle is 0, so these effectively remain unchanged horizontally)
        self.points['shoulder_L'] = rotate_around_origin(sL_orig_x, sL_orig_y, current_torso_angle)
        self.points['shoulder_R'] = rotate_around_origin(sR_orig_x, sR_orig_y, current_torso_angle)
        self.points['neck'] = rotate_around_origin(neck_orig_x, neck_orig_y, current_torso_angle)
        self.points['head'] = rotate_around_origin(head_orig_x, head_orig_y, current_torso_angle)

        # Arms (hanging straight down from shoulders)
        # Left Arm
        elbow_L_local_x = self.points['shoulder_L'][0]
        elbow_L_local_y = self.points['shoulder_L'][1] + UPPER_ARM_LENGTH

        wrist_L_local_x = elbow_L_local_x
        wrist_L_local_y = elbow_L_local_y + LOWER_ARM_LENGTH

        self.points['elbow_L'] = (elbow_L_local_x, elbow_L_local_y)
        self.points['wrist_L'] = (wrist_L_local_x, wrist_L_local_y)

        # Right Arm (symmetric to left arm)
        elbow_R_local_x = self.points['shoulder_R'][0]
        elbow_R_local_y = self.points['shoulder_R'][1] + UPPER_ARM_LENGTH

        wrist_R_local_x = elbow_R_local_x
        wrist_R_local_y = elbow_R_local_y + LOWER_ARM_LENGTH

        self.points['elbow_R'] = (elbow_R_local_x, elbow_R_local_y)
        self.points['wrist_R'] = (wrist_R_local_x, wrist_R_local_y)

        # --- Apply Global Translation to all points for Display ---
        # Each local point is shifted by the global x-center and the dynamic global y-position of the pelvis.
        self.display_points = {}
        for name, (x_local, y_local) in self.points.items():
            self.display_points[name] = (self.center_x + x_local, self.pelvis_center_global_y + y_local)

    def draw(self, surface):
        # Draw each point as a white circle on the given surface
        for name, (x, y) in self.display_points.items():
            pygame.draw.circle(surface, WHITE, (int(x), int(y)), DOT_RADIUS)

# --- Main Program Loop ---
# Initialize the humanoid figure
human = Humanoid(WIDTH // 2, HEIGHT - 10) # Centered horizontally, ground 10 pixels from bottom

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: # Reset animation on 'R' key press
                human = Humanoid(WIDTH // 2, HEIGHT - 10)
            elif event.key == pygame.K_SPACE: # Pause/unpause animation on SPACE key press
                human.sit_speed = 0 if human.sit_speed > 0 else 0.015

    # Clear screen with black background
    screen.fill(BLACK)

    # Update humanoid's pose for the current frame
    human.update()
    # Draw the humanoid's points
    human.draw(screen)

    # Update the full display surface
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

pygame.quit()
