
import pygame
import math

# --- Constants ---
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 5

# --- 3D Projection Settings ---
# FOV (Field of View) affects the perspective distortion.
FOV = 300
# Viewer distance from the origin (0,0,0) of the 3D space.
VIEWER_DISTANCE = 6
# Scale factor to control the overall size of the figure on screen.
SCALE_FACTOR = 250

# --- Point-light data (15 points) ---
# The 3D coordinates for a base pose, derived from the structure in the example image.
# The origin (0,0,0) is on the floor, between the feet.
# Coordinate system: +Y is up, +X is right, +Z is toward the viewer.
# Structure based on image:
# Head, L/R Shoulders, L/R Elbows + Sternum, L/R Wrists + Abdomen, L/R Hips, L/R Knees, L/R Ankles
POINTS_3D_BASE = [
    # (x, y, z)
    (0, 1.7, 0),      # 0: Head
    # Shoulders
    (-0.25, 1.5, 0),  # 1: L Shoulder
    (0.25, 1.5, 0),   # 2: R Shoulder
    # Elbows and Sternum
    (-0.35, 1.2, 0),  # 3: L Elbow
    (0, 1.3, 0),      # 4: Sternum
    (0.35, 1.2, 0),   # 5: R Elbow
    # Wrists and Abdomen
    (-0.4, 0.95, 0),  # 6: L Wrist
    (0, 1.0, 0),      # 7: Abdomen
    (0.4, 0.95, 0),   # 8: R Wrist
    # Hips
    (-0.18, 0.9, 0),  # 9: L Hip
    (0.18, 0.9, 0),   # 10: R Hip
    # Knees
    (-0.2, 0.5, 0),   # 11: L Knee
    (0.2, 0.5, 0),    # 12: R Knee
    # Ankles
    (-0.22, 0.1, 0),  # 13: L Ankle
    (0.22, 0.1, 0)    # 14: R Ankle
]


def main():
    """
    Main function to set up Pygame and run the animation loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Turning Around")
    clock = pygame.time.Clock()

    angle_deg = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # --- Update Animation State ---
        # Increment the main rotation angle for the turn.
        angle_deg += 1.3  # Controls the speed of the turn
        if angle_deg >= 360:
            angle_deg -= 360
        
        angle_rad = math.radians(angle_deg)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # Use a time variable based on the angle for synchronized oscillations.
        # This completes two gait cycles per 360-degree turn.
        t = angle_rad * 2

        projected_points_2d = []

        # --- Animation and Projection Calculation ---
        for i, p_base in enumerate(POINTS_3D_BASE):
            base_x, base_y, base_z = p_base
            
            # 1. Calculate animation offsets in the figure's local coordinate frame
            dx, dy, dz = 0, 0, 0

            # Vertical bobbing motion for the whole body to simulate stepping
            bob_freq = 2
            bob_amp = 0.035
            dy += bob_amp * math.sin(t * bob_freq)

            # Torso sway for a more natural, happy motion
            sway_freq = 1
            sway_amp = 0.02
            if i in [0, 4, 7]: # Head, Sternum, Abdomen
                dx += sway_amp * math.sin(t * sway_freq)
            
            # Arm swing (oppositional)
            arm_swing_amp_z = 0.18  # Forward/backward
            arm_swing_amp_x = 0.05  # Sideways
            
            # Left arm (points 1, 3, 6)
            if i in [1, 3, 6]: 
                dz += arm_swing_amp_z * math.sin(t)
                dx -= arm_swing_amp_x * (1 + math.cos(t)) / 2
            # Right arm (points 2, 5, 8)
            if i in [2, 5, 8]:
                dz += arm_swing_amp_z * math.sin(t + math.pi)
                dx -= arm_swing_amp_x * (1 + math.cos(t + math.pi)) / 2

            # Leg movement to simulate stepping/pivoting
            leg_step_amp_z = 0.12
            knee_bend_amp = 0.07

            # Left leg (points 9, 11, 13)
            if i in [9, 11, 13]:
                dz += leg_step_amp_z * math.sin(t + math.pi) # Out of phase with left arm
                if i == 11: # Knee bend
                     dy -= knee_bend_amp * (1 - math.cos(t * 2)) / 2
            # Right leg (points 10, 12, 14)
            if i in [10, 12, 14]:
                dz += leg_step_amp_z * math.sin(t) # Out of phase with right arm
                if i == 12: # Knee bend
                     dy -= knee_bend_amp * (1 - math.cos(t * 2 + math.pi)) / 2

            # 2. Apply offsets to base point to get the animated point in local space
            local_anim_x = base_x + dx
            local_anim_y = base_y + dy
            local_anim_z = base_z + dz

            # 3. Rotate the animated point around the world's Y-axis
            world_x = local_anim_x * cos_a - local_anim_z * sin_a
            world_y = local_anim_y
            world_z = local_anim_x * sin_a + local_anim_z * cos_a

            # 4. Project the 3D world point to 2D screen coordinates
            z_with_viewer_distance = world_z + VIEWER_DISTANCE
            if z_with_viewer_distance > 0: # Avoid points behind the viewer
                scale = FOV / z_with_viewer_distance
                screen_x = int(WIDTH / 2 + world_x * scale * SCALE_FACTOR)
                # Position the figure vertically on the screen
                screen_y = int(HEIGHT * 0.8 - world_y * scale * SCALE_FACTOR)
                projected_points_2d.append((screen_x, screen_y))

        # --- Drawing ---
        screen.fill(BLACK)
        
        for p in projected_points_2d:
            pygame.draw.circle(screen, WHITE, p, POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
