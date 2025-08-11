
import pygame
import math

# --- Constants ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
# A 2.5 second animation for a more deliberate roll
NUM_FRAMES = int(2.5 * FPS)
POINT_RADIUS = 4
SCALE = 110  # Scale factor for the coordinates

# --- Point Indices for the 15-point model ---
# This defines the standard skeleton structure used in biological motion studies.
HEAD, NECK, PELVIS = 0, 1, 2
L_SHOULDER, R_SHOULDER = 3, 4
L_ELBOW, R_ELBOW = 5, 6
L_WRIST, R_WRIST = 7, 8
L_HIP, R_HIP = 9, 10
L_KNEE, R_KNEE = 11, 12
L_ANKLE, R_ANKLE = 13, 14

def get_forward_roll_data(num_frames):
    """
    Generates the 2D point data for a sadman performing a forward roll.
    The motion is defined procedurally using a hierarchical model, where
    limb positions are calculated relative to a moving and rotating torso.
    """
    # Proportions of the body segments (normalized)
    L_TORSO = 1.0
    L_NECK = 0.25
    L_UPPER_ARM = 0.55
    L_LOWER_ARM = 0.55
    L_UPPER_LEG = 0.65
    L_LOWER_LEG = 0.65
    L_SHOULDER_WIDTH = 0.35
    L_HIP_WIDTH = 0.3

    def smoothstep(t):
        """A smooth interpolation function (cubic) for natural easing."""
        return t * t * (3.0 - 2.0 * t)

    def interpolate(val1, val2, factor):
        """Interpolate between two values using the smoothstep function."""
        return val1 + (val2 - val1) * smoothstep(factor)

    frames_data = []
    for i in range(num_frames):
        t = i / (num_frames - 1)
        points = [(0, 0)] * 15

        # 1. Pelvis Trajectory: Defines the overall movement of the body's center.
        pelvis_x = -1.8 + 3.6 * t
        
        # The y-path follows the classic roll motion: squat -> rise -> arc -> fall -> squat
        if t < 0.15:  # Initial squat
            pelvis_y = interpolate(-0.9, -0.6, t / 0.15)
        elif t < 0.65:  # The main rolling arc
            phase_t = (t - 0.15) / 0.5
            pelvis_y = -0.6 + 1.2 * math.sin(smoothstep(phase_t) * math.pi)
        else:  # Landing and finishing in a squat
            pelvis_y = interpolate(0.6, -0.9, (t - 0.65) / 0.35)

        pelvis_pos = (pelvis_x, pelvis_y)
        points[PELVIS] = pelvis_pos

        # 2. Torso Rotation: The core of the rolling motion.
        initial_hunch_deg = 20  # A hunched posture to convey "sadman"
        torso_angle_rad = math.radians(initial_hunch_deg - 360 * t)
        
        neck_pos = (pelvis_pos[0] + L_TORSO * math.sin(torso_angle_rad),
                    pelvis_pos[1] + L_TORSO * math.cos(torso_angle_rad))
        points[NECK] = neck_pos

        # 3. Head Motion: Includes a tuck for the roll and a droop for sadness.
        head_droop_deg = 15  # Constant head droop for "sadman" feel
        head_angle_rad = torso_angle_rad + math.radians(head_droop_deg)
        if 0.1 <= t <= 0.6:  # Tucking phase for safety and momentum
            phase_t = (t - 0.1) / 0.5
            tuck_factor = math.sin(smoothstep(phase_t) * math.pi)
            head_angle_rad += math.radians(45 * tuck_factor)
        
        points[HEAD] = (neck_pos[0] + L_NECK * math.sin(head_angle_rad),
                        neck_pos[1] + L_NECK * math.cos(head_angle_rad))

        # --- Limb Angles (relative to the torso's orientation) ---
        # 4. Leg Angles: Defines the tucking, pushing, and landing motions.
        if t < 0.2:  # From squat to push-off
            hip_angle = interpolate(100, 170, t / 0.2)
            knee_angle = interpolate(70, 170, t / 0.2)
        elif t < 0.7:  # Tucked during the roll
            hip_angle = interpolate(170, 45, (t - 0.2) / 0.5)
            knee_angle = interpolate(170, 45, (t - 0.2) / 0.5)
        else:  # Unfurling for landing
            hip_angle = interpolate(45, 100, (t - 0.7) / 0.3)
            knee_angle = interpolate(45, 70, (t - 0.7) / 0.3)

        # 5. Arm Angles: Defines reaching, supporting, and recovering.
        if t < 0.25:  # Reaching down to the ground
            shoulder_angle = interpolate(45, 90, t / 0.25)
            elbow_angle = interpolate(160, 175, t / 0.25)
        elif t < 0.6:  # Tucked while rolling over the shoulders
            shoulder_angle = interpolate(90, -60, (t - 0.25) / 0.35)
            elbow_angle = interpolate(175, 60, (t - 0.25) / 0.35)
        else:  # Recovering forward for balance
            shoulder_angle = interpolate(-60, 20, (t - 0.6) / 0.4)
            elbow_angle = interpolate(60, 160, (t - 0.6) / 0.4)

        # --- Calculate Final Joint Positions using the hierarchical model ---
        torso_perp_rad = torso_angle_rad - math.pi / 2
        cos_perp, sin_perp = math.cos(torso_perp_rad), math.sin(torso_perp_rad)
        
        points[L_SHOULDER] = (neck_pos[0] + (L_SHOULDER_WIDTH/2)*cos_perp, neck_pos[1] + (L_SHOULDER_WIDTH/2)*sin_perp)
        points[R_SHOULDER] = (neck_pos[0] - (L_SHOULDER_WIDTH/2)*cos_perp, neck_pos[1] - (L_SHOULDER_WIDTH/2)*sin_perp)
        points[L_HIP] = (pelvis_pos[0] + (L_HIP_WIDTH/2)*cos_perp, pelvis_pos[1] + (L_HIP_WIDTH/2)*sin_perp)
        points[R_HIP] = (pelvis_pos[0] - (L_HIP_WIDTH/2)*cos_perp, pelvis_pos[1] - (L_HIP_WIDTH/2)*sin_perp)
        
        def calculate_limb(start_pos, angle1_deg, angle2_deg, len1, len2):
            """Helper to calculate positions of a two-segment limb."""
            angle1_rad = torso_angle_rad + math.radians(angle1_deg)
            joint1_pos = (start_pos[0] + len1 * math.sin(angle1_rad),
                          start_pos[1] + len1 * math.cos(angle1_rad))
            angle2_rad = angle1_rad + math.radians(angle2_deg - 180)
            joint2_pos = (joint1_pos[0] + len2 * math.sin(angle2_rad),
                          joint1_pos[1] + len2 * math.cos(angle2_rad))
            return joint1_pos, joint2_pos
        
        points[L_ELBOW], points[L_WRIST] = calculate_limb(points[L_SHOULDER], shoulder_angle, elbow_angle, L_UPPER_ARM, L_LOWER_ARM)
        points[R_ELBOW], points[R_WRIST] = calculate_limb(points[R_SHOULDER], shoulder_angle, elbow_angle, L_UPPER_ARM, L_LOWER_ARM)
        points[L_KNEE], points[L_ANKLE] = calculate_limb(points[L_HIP], hip_angle, knee_angle, L_UPPER_LEG, L_LOWER_LEG)
        points[R_KNEE], points[R_ANKLE] = calculate_limb(points[R_HIP], hip_angle, knee_angle, L_UPPER_LEG, L_LOWER_LEG)

        frames_data.append(points)
    
    return frames_data

def main():
    """
    Sets up the pygame window and runs the main animation loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sadman Forward Rolling")
    clock = pygame.time.Clock()

    # Generate all frame data at the start
    motion_data = get_forward_roll_data(NUM_FRAMES)
    
    frame_index = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # --- Drawing ---
        screen.fill(BLACK)
        
        current_points = motion_data[frame_index]
        
        # Transform from normalized coordinates to screen coordinates and draw
        for point in current_points:
            x = int(SCREEN_WIDTH / 2 + point[0] * SCALE)
            y = int(SCREEN_HEIGHT / 2 - point[1] * SCALE) # Y is inverted in pygame
            pygame.draw.circle(screen, WHITE, (x, y), POINT_RADIUS)
            
        pygame.display.flip()
        
        # --- Update ---
        frame_index = (frame_index + 1) % NUM_FRAMES
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == '__main__':
    main()
