
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800  # Taller screen to accommodate full figure and bowing motion
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 4
FPS = 60

# Animation timings (in seconds)
BOW_DOWN_DURATION = 2.5
HOLD_BOW_DURATION = 1.0
STAND_UP_DURATION = 2.5
PAUSE_DURATION = 1.0  # Pause at the end of the cycle before repeating

# Scale for proportions (arbitrary unit to pixels)
SCALE = 150

# Body segment lengths (in arbitrary units, will be scaled to pixels)
# These define the proportions of the figure.
L_HEAD_NECK_UNIT = 0.2
L_NECK_TORSO_UNIT = 0.2  # From Neck to TORSO_MID
L_TORSO_HIP_UNIT = 0.4   # From TORSO_MID (lower back) to average Hip Joint level
L_UPPER_ARM_UNIT = 0.35
L_FOREARM_UNIT = 0.3
L_THIGH_UNIT = 0.45
L_SHIN_UNIT = 0.45
W_SHOULDER_UNIT = 0.2    # Half-width from spine center to shoulder joint
W_HIP_UNIT = 0.15        # Half-width from pelvis center to hip joint

# Convert unit lengths to pixel lengths
L_HEAD_NECK = L_HEAD_NECK_UNIT * SCALE
L_NECK_TORSO = L_NECK_TORSO_UNIT * SCALE
L_TORSO_HIP = L_TORSO_HIP_UNIT * SCALE
L_UPPER_ARM = L_UPPER_ARM_UNIT * SCALE
L_FOREARM = L_FOREARM_UNIT * SCALE
L_THIGH = L_THIGH_UNIT * SCALE
L_SHIN = L_SHIN_UNIT * SCALE
W_SHOULDER = W_SHOULDER_UNIT * SCALE
W_HIP = W_HIP_UNIT * SCALE

# Joint angle definitions (in radians, converted from degrees for clarity)
# All angles are relative to the parent segment's orientation.
# For torso: 0 radians means pointing straight up relative to the pelvis.
# For limbs: 0 radians means the segment is straight (180 degrees internal angle).
# Positive angles indicate clockwise rotation in Pygame's coordinate system (Y-down, X-right).

# Initial Pose: Standing, slightly sad/hunched
INITIAL_ANGLES = {
    "torso_rot": math.radians(-10),  # Torso angle relative to vertical (negative is forward hunch)
    "neck_rot": math.radians(-15),   # Neck angle relative to torso (negative is head down)
    "head_rot": math.radians(-10),   # Head angle relative to neck (negative is head further down)
    "knee_L_bend": math.radians(175), # Internal knee angle (180 is straight)
    "knee_R_bend": math.radians(175),
    "elbow_L_bend": math.radians(160), # Internal elbow angle
    "elbow_R_bend": math.radians(160),
    "shoulder_L_rot": math.radians(0), # Shoulder rotation relative to torso (arms hanging)
    "shoulder_R_rot": math.radians(0),
    "wrist_L_rot": math.radians(0),    # Wrist rotation relative to forearm
    "wrist_R_rot": math.radians(0),
}

# Final Pose: Bowed, sad and slumped
FINAL_ANGLES = {
    "torso_rot": math.radians(-70),  # Deep forward bow
    "neck_rot": math.radians(-35),   # Head drops further
    "head_rot": math.radians(-25),   # Head drops even further
    "knee_L_bend": math.radians(150), # More significant knee bend
    "knee_R_bend": math.radians(150),
    "elbow_L_bend": math.radians(170), # Arms straighter, hanging more
    "elbow_R_bend": math.radians(170),
    "shoulder_L_rot": math.radians(0),
    "shoulder_R_rot": math.radians(0),
    "wrist_L_rot": math.radians(0),
    "wrist_R_rot": math.radians(0),
}

# Point IDs (exactly 15 points as required)
# These represent the major joints and body parts for the point-light display.
(HEAD, NECK, TORSO_MID, SHOULDER_L, SHOULDER_R, ELBOW_L, ELBOW_R,
 WRIST_L, WRIST_R, HIP_L, HIP_R, KNEE_L, KNEE_R, ANKLE_L, ANKLE_R) = range(15)

# --- HumanFigure Class ---
class HumanFigure:
    def __init__(self, x_center=SCREEN_WIDTH // 2, y_ground=SCREEN_HEIGHT - 50):
        self.x_center = x_center  # Center X position of the figure
        self.y_ground = y_ground  # Y-coordinate representing the ground in Pygame

        # List to store the current (x, y) coordinates of each point in Pygame screen space
        self.points = [(0, 0)] * 15

        # Store current angles for each joint, initialized to the starting pose
        self.current_angles = INITIAL_ANGLES.copy()

    def _rotate_point(self, origin, point, angle):
        """Rotates a point (px, py) around an origin (ox, oy) by an angle (radians).
           Angle is typically relative to the X-axis in standard rotation.
           Here, adapting for segments where angle is relative to parent.
           This helper is for rotating local coordinates.
        """
        ox, oy = origin
        px, py = point

        # Translate point so origin is at (0,0)
        temp_x, temp_y = px - ox, py - oy

        # Rotate point
        rotated_x = temp_x * math.cos(angle) - temp_y * math.sin(angle)
        rotated_y = temp_x * math.sin(angle) + temp_y * math.cos(angle)

        # Translate point back
        return rotated_x + ox, rotated_y + oy

    def _calculate_segment_end(self, start_pos, global_angle, length):
        """Calculates the end point of a segment.
           start_pos: (x,y) of the joint.
           global_angle: The absolute angle of the segment (e.g., torso, thigh) relative to vertical in Pygame's Y-down coords.
                         0 for straight down, positive for clockwise.
           length: Length of the segment.
        """
        end_x = start_pos[0] + length * math.sin(global_angle)
        end_y = start_pos[1] + length * math.cos(global_angle)
        return end_x, end_y

    def update_points(self):
        """Calculates the 15 point positions based on current joint angles."""

        # 1. Anchor feet to the ground (fixed points)
        # Assuming ankles are slightly apart and fixed on the Y_ground line
        ankle_L_pygame = (self.x_center - W_HIP, self.y_ground) # W_HIP is half-width, so full width is 2*W_HIP
        ankle_R_pygame = (self.x_center + W_HIP, self.y_ground)

        self.points[ANKLE_L] = ankle_L_pygame
        self.points[ANKLE_R] = ankle_R_pygame

        # 2. Calculate Knee positions (based on ankles and shin length)
        # Shin angle is essentially 0 (straight down) relative to vertical, as feet are flat.
        knee_L_pygame = self._calculate_segment_end(ankle_L_pygame, 0, -L_SHIN) # -L_SHIN because going upwards
        knee_R_pygame = self._calculate_segment_end(ankle_R_pygame, 0, -L_SHIN)
        self.points[KNEE_L] = knee_L_pygame
        self.points[KNEE_R] = knee_R_pygame

        # 3. Calculate Hip positions (based on knees and thigh length)
        # Thigh angle is relative to the *vertical* (0 for straight up).
        # Internal knee angle (self.current_angles["knee_L_bend"]) affects thigh orientation.
        # Global thigh angle = (angle of shin) + (180 - internal knee angle)
        # Since shin angle is 0 (vertical down), thigh angle relative to vertical up is:
        # -(math.pi - self.current_angles["knee_L_bend"]) for forward bend.
        # This angle is relative to vertical.
        thigh_global_angle_L = math.pi - self.current_angles["knee_L_bend"] # Angle from vertical upwards for thigh
        thigh_global_angle_R = math.pi - self.current_angles["knee_R_bend"]

        hip_L_pygame = self._calculate_segment_end(knee_L_pygame, thigh_global_angle_L, -L_THIGH) # -L_THIGH because going upwards
        hip_R_pygame = self._calculate_segment_end(knee_R_pygame, thigh_global_angle_R, -L_THIGH)
        self.points[HIP_L] = hip_L_pygame
        self.points[HIP_R] = hip_R_pygame

        # 4. Calculate TORSO_MID position (lower back, main pivot for bowing)
        # Average of hip positions for the root of the torso chain
        pelvis_center_pygame_x = (hip_L_pygame[0] + hip_R_pygame[0]) / 2
        pelvis_center_pygame_y = (hip_L_pygame[1] + hip_R_pygame[1]) / 2
        pelvis_center_pygame = (pelvis_center_pygame_x, pelvis_center_pygame_y)

        # Torso angle is relative to the vertical (0 for upright, negative for forward bow)
        torso_global_angle = self.current_angles["torso_rot"]
        torso_mid_pygame = self._calculate_segment_end(pelvis_center_pygame, torso_global_angle, -L_TORSO_HIP)
        self.points[TORSO_MID] = torso_mid_pygame

        # 5. Calculate NECK position (based on TORSO_MID and neck rotation)
        # Neck angle is relative to the torso segment.
        neck_global_angle = torso_global_angle + self.current_angles["neck_rot"]
        neck_pygame = self._calculate_segment_end(torso_mid_pygame, neck_global_angle, -L_NECK_TORSO)
        self.points[NECK] = neck_pygame

        # 6. Calculate HEAD position (based on NECK and head rotation)
        # Head angle is relative to the neck segment.
        head_global_angle = neck_global_angle + self.current_angles["head_rot"]
        head_pygame = self._calculate_segment_end(neck_pygame, head_global_angle, -L_HEAD_NECK)
        self.points[HEAD] = head_pygame

        # 7. Calculate Shoulder, Elbow, Wrist positions
        # Shoulders are positioned relative to TORSO_MID and follow torso's rotation.
        # Assuming shoulders are slightly above TORSO_MID for natural posture.
        shoulder_offset_y = -L_TORSO_HIP * 0.1 # A small offset upwards from torso_mid
        
        shoulder_L_base = (torso_mid_pygame[0] - W_SHOULDER, torso_mid_pygame[1] + shoulder_offset_y)
        shoulder_R_base = (torso_mid_pygame[0] + W_SHOULDER, torso_mid_pygame[1] + shoulder_offset_y)

        # Arms hang naturally. Shoulder rotation relative to torso_mid.
        # Upper arm global angle = torso_global_angle + shoulder_rot
        upper_arm_global_angle_L = torso_global_angle + self.current_angles["shoulder_L_rot"]
        upper_arm_global_angle_R = torso_global_angle + self.current_angles["shoulder_R_rot"]
        
        self.points[SHOULDER_L] = shoulder_L_base
        self.points[SHOULDER_R] = shoulder_R_base

        # Elbows
        # Upper arms point down from shoulders.
        elbow_L_pygame = self._calculate_segment_end(shoulder_L_base, upper_arm_global_angle_L, L_UPPER_ARM)
        elbow_R_pygame = self._calculate_segment_end(shoulder_R_base, upper_arm_global_angle_R, L_UPPER_ARM)
        self.points[ELBOW_L] = elbow_L_pygame
        self.points[ELBOW_R] = elbow_R_pygame

        # Wrists
        # Forearm angle relative to upper arm (math.pi is straight, less than pi is bent).
        # global angle of forearm = upper_arm_global_angle + (math.pi - elbow_bend)
        forearm_global_angle_L = upper_arm_global_angle_L + (math.pi - self.current_angles["elbow_L_bend"])
        forearm_global_angle_R = upper_arm_global_angle_R + (math.pi - self.current_angles["elbow_R_bend"])

        wrist_L_pygame = self._calculate_segment_end(elbow_L_pygame, forearm_global_angle_L, L_FOREARM)
        wrist_R_pygame = self._calculate_segment_end(elbow_R_pygame, forearm_global_angle_R, L_FOREARM)
        self.points[WRIST_L] = wrist_L_pygame
        self.points[WRIST_R] = wrist_R_pygame

    def draw(self, screen):
        """Draws all 15 point-lights on the screen."""
        for point_pos in self.points:
            pygame.draw.circle(screen, WHITE, (int(point_pos[0]), int(point_pos[1])), POINT_RADIUS)

# --- Main Program Logic ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman Bowing")
    clock = pygame.time.Clock()

    figure = HumanFigure()

    # Calculate total animation duration for looping
    total_animation_duration = BOW_DOWN_DURATION + HOLD_BOW_DURATION + STAND_UP_DURATION + PAUSE_DURATION
    total_frames = int(total_animation_duration * FPS)
    frame_count = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Determine current phase and interpolation progress
        current_time = frame_count / FPS
        
        start_angles_interp = INITIAL_ANGLES
        end_angles_interp = FINAL_ANGLES
        interpolation_progress = 0

        if current_time < BOW_DOWN_DURATION:
            # Phase 1: Bowing down
            interpolation_progress = current_time / BOW_DOWN_DURATION
        elif current_time < BOW_DOWN_DURATION + HOLD_BOW_DURATION:
            # Phase 2: Holding bow (stay at final pose)
            interpolation_progress = 1.0 # Ensures final pose is maintained
        elif current_time < BOW_DOWN_DURATION + HOLD_BOW_DURATION + STAND_UP_DURATION:
            # Phase 3: Standing up
            start_angles_interp = FINAL_ANGLES
            end_angles_interp = INITIAL_ANGLES
            time_in_phase = current_time - (BOW_DOWN_DURATION + HOLD_BOW_DURATION)
            interpolation_progress = time_in_phase / STAND_UP_DURATION
        else:
            # Phase 4: Pause before repeating
            interpolation_progress = 1.0 # Ensures initial pose is maintained
            # Reset animation cycle if it completes
            if current_time >= total_animation_duration:
                frame_count = 0 
                current_time = 0 # Reset time for the new cycle

        # Interpolate angles for the current frame
        for joint in INITIAL_ANGLES:
            start_val = start_angles_interp[joint]
            end_val = end_angles_interp[joint]
            figure.current_angles[joint] = start_val + (end_val - start_val) * interpolation_progress

        # Update and draw the figure
        figure.update_points()
        figure.draw(screen)

        pygame.display.flip()
        frame_count += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
