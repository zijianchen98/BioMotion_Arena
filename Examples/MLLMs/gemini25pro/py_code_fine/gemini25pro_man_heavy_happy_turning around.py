
import pygame
import math

def main():
    """
    This program displays a point-light stimulus animation of a person
    turning around while holding a heavy weight.
    """
    # --- Setup ---
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Turning with Heavy Weight")
    clock = pygame.time.Clock()

    # --- Constants ---
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FPS = 60
    NUM_FRAMES = 180  # A 3-second turn at 60 FPS
    POINT_RADIUS = 5

    # --- 3D Projection Settings ---
    FOCAL_LENGTH = 350
    CAMERA_DISTANCE = 500

    # --- Model Definition ---
    # This defines the 15 joints of the figure in a base pose.
    # The pose represents holding a heavy weight:
    # - Knees are bent, stance is wide for stability.
    # - Torso leans back slightly to counterbalance the weight.
    # - Arms are bent and held forward.
    # The origin (0,0,0) is at the pelvis. Y-axis is vertical.
    # Joint order: Head, R_Shoulder, L_Shoulder, R_Elbow, L_Elbow, R_Wrist, L_Wrist,
    #              Sternum, Pelvis, R_Hip, L_Hip, R_Knee, L_Knee, R_Ankle, L_Ankle
    BASE_POSE_3D = [
        # Upper Body
        (0, 100, -10),    # 0: Head
        (22, 80, -15),    # 1: R Shoulder
        (-22, 80, -15),   # 2: L Shoulder
        (30, 45, 25),     # 3: R Elbow
        (-30, 45, 25),    # 4: L Elbow
        (25, 15, 40),     # 5: R Wrist
        (-25, 15, 40),    # 6: L Wrist
        (0, 65, -5),      # 7: Sternum
        (0, 0, 0),        # 8: Pelvis (Origin)
        # Lower Body
        (15, -5, 0),      # 9: R Hip
        (-15, -5, 0),     # 10: L Hip
        (20, -50, 5),     # 11: R Knee
        (-20, -50, 5),    # 12: L Knee
        (22, -95, 0),     # 13: R Ankle
        (-22, -95, 0)     # 14: L Ankle
    ]

    def generate_animation_frames():
        """Pre-calculates all 3D point data for the turning animation."""
        frames = []
        for i in range(NUM_FRAMES):
            frame_points = []
            
            # 1. Overall rotation of the body
            turn_angle = (i / NUM_FRAMES) * 2 * math.pi
            cos_turn = math.cos(turn_angle)
            sin_turn = math.sin(turn_angle)

            # 2. Biomechanical nuances for a heavy turn
            # The body sways to shift weight over the pivot foot. (2 sways for 360 deg)
            sway_angle = (i / NUM_FRAMES) * 2 * math.pi * 2
            sway_dx = -12 * math.cos(sway_angle)
            
            # The body bobs down during steps. (4 bobs for 360 deg)
            bob_angle = (i / NUM_FRAMES) * 2 * math.pi * 4
            bob_dy = 4 * (math.cos(bob_angle) - 1)

            for j, p_base in enumerate(BASE_POSE_3D):
                x, y, z = p_base

                # 3. Apply main body rotation
                x_rot = x * cos_turn - z * sin_turn
                z_rot = x * sin_turn + z * cos_turn
                y_rot = y

                # 4. Simulate stepping motion for legs
                is_leg_joint = j in [11, 12, 13, 14]
                if is_leg_joint:
                    # A 4-step turn logic. A step happens every quarter of the animation.
                    step_period = NUM_FRAMES / 4
                    step_phase = (i % step_period) / step_period  # 0 to 1 within each step
                    lift_height = 20 * math.sin(step_phase * math.pi)

                    # Determine which foot is stepping
                    step_num = i // step_period
                    is_right_foot_stepping = step_num % 2 == 0
                    is_right_side_joint = j in [11, 13]

                    if (is_right_foot_stepping and is_right_side_joint) or \
                       (not is_right_foot_stepping and not is_right_side_joint):
                        # Apply lift to the stepping leg's joints
                        # Knees lift higher than ankles for a natural look
                        y_lift_amount = lift_height if j in [13, 14] else lift_height * 1.5
                        y_rot -= y_lift_amount
                
                # 5. Apply body sway and bob to all non-ankle joints
                # (Ankles act as pivots on the ground)
                if j not in [13, 14]:
                    x_rot += sway_dx
                    y_rot += bob_dy

                frame_points.append((x_rot, y_rot, z_rot))
                
            frames.append(frame_points)
        return frames

    def project_3d_to_2d(point_3d):
        """Projects a 3D point to 2D screen coordinates using perspective projection."""
        x, y, z = point_3d
        scale = FOCAL_LENGTH / (FOCAL_LENGTH + z + CAMERA_DISTANCE)
        screen_x = WIDTH / 2 + x * scale
        # Invert Y-axis for Pygame's coordinate system (0,0 is top-left)
        screen_y = HEIGHT / 2 - y * scale
        return int(screen_x), int(screen_y)

    # --- Main Loop ---
    animation_frames = generate_animation_frames()
    frame_index = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Clear the screen for the new frame
        screen.fill(BLACK)

        # Get the current frame's 3D points
        current_points_3d = animation_frames[frame_index]

        # Project and draw each point
        for point_3d in current_points_3d:
            pos_2d = project_3d_to_2d(point_3d)
            pygame.draw.circle(screen, WHITE, pos_2d, POINT_RADIUS)

        # Update the full display
        pygame.display.flip()

        # Advance to the next frame
        frame_index = (frame_index + 1) % NUM_FRAMES

        # Maintain the desired frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
