
import pygame
import math

def main():
    """
    Main function to set up and run the biological motion animation.
    """
    pygame.init()

    # --- Configuration ---
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    BG_COLOR = (0, 0, 0)
    POINT_COLOR = (255, 255, 255)
    POINT_RADIUS = 6
    NUM_POINTS = 15

    # --- Animation Timing (in frames) ---
    # The animation depicts a single jump cycle that loops.
    # 1. Preparation: Standing still, then crouching.
    # 2. Propulsion: The jump itself, from crouch to apex.
    # 3. Flight & Landing: From apex to landing absorption.
    # 4. Recovery: From landing crouch back to standing.
    
    # Duration of each phase
    PREP_DURATION = 40  # Slower preparation for a heavy jump
    JUMP_UP_DURATION = 35 # Explosive upward movement
    JUMP_DOWN_DURATION = 35 # Falling down
    RECOVERY_DURATION = 40 # Slower recovery

    # Frame markers for transitions
    T_START_CROUCH = 0
    T_END_CROUCH = T_START_CROUCH + PREP_DURATION
    T_APEX = T_END_CROUCH + JUMP_UP_DURATION
    T_LAND = T_APEX + JUMP_DOWN_DURATION
    T_END_RECOVERY = T_LAND + RECOVERY_DURATION
    
    TOTAL_FRAMES = T_END_RECOVERY

    # --- Biomechanical Model & Key Poses ---
    # We define the body's structure at key moments of the action.
    # The coordinate system is centered horizontally. Y=0 is at the top.
    # A base_y value is used to set the "ground" level.
    
    cx = WIDTH // 2
    base_y = HEIGHT * 0.9
    figure_height = 320
    jump_height = 130 # A lower jump due to "heavy weight"

    # Define the 15 joints for our model
    (HEAD, NECK_CENTER, PELVIS_CENTER, L_SHOULDER, R_SHOULDER, L_ELBOW, R_ELBOW,
     L_WRIST, R_WRIST, L_HIP, R_HIP, L_KNEE, R_KNEE, L_ANKLE, R_ANKLE) = range(15)

    # KEY POSE 1: Standing
    # A stable, slightly bent-knee stance to support weight.
    pose_stand = [None] * NUM_POINTS
    pose_stand[HEAD]          = (cx, base_y - figure_height)
    pose_stand[NECK_CENTER]   = (cx, base_y - figure_height * 0.8)
    pose_stand[PELVIS_CENTER] = (cx, base_y - figure_height * 0.5)
    pose_stand[L_SHOULDER]    = (cx - 35, base_y - figure_height * 0.8)
    pose_stand[R_SHOULDER]    = (cx + 35, base_y - figure_height * 0.8)
    pose_stand[L_ELBOW]       = (cx - 40, base_y - figure_height * 0.65)
    pose_stand[R_ELBOW]       = (cx + 40, base_y - figure_height * 0.65)
    pose_stand[L_WRIST]       = (cx - 40, base_y - figure_height * 0.5)
    pose_stand[R_WRIST]       = (cx + 40, base_y - figure_height * 0.5)
    pose_stand[L_HIP]         = (cx - 20, base_y - figure_height * 0.5)
    pose_stand[R_HIP]         = (cx + 20, base_y - figure_height * 0.5)
    pose_stand[L_KNEE]        = (cx - 25, base_y - figure_height * 0.25)
    pose_stand[R_KNEE]        = (cx + 25, base_y - figure_height * 0.25)
    pose_stand[L_ANKLE]       = (cx - 25, base_y)
    pose_stand[R_ANKLE]       = (cx + 25, base_y)

    # KEY POSE 2: Crouch
    # The lowest point before the jump, storing potential energy. Arms swing back.
    pose_crouch = [None] * NUM_POINTS
    crouch_y_pelvis = base_y - figure_height * 0.3
    pose_crouch[PELVIS_CENTER] = (cx, crouch_y_pelvis)
    pose_crouch[L_HIP]         = (cx - 25, crouch_y_pelvis)
    pose_crouch[R_HIP]         = (cx + 25, crouch_y_pelvis)
    pose_crouch[L_ANKLE]       = (cx - 35, base_y)
    pose_crouch[R_ANKLE]       = (cx + 35, base_y)
    pose_crouch[L_KNEE]        = (cx - 45, (crouch_y_pelvis + base_y) / 2)
    pose_crouch[R_KNEE]        = (cx + 45, (crouch_y_pelvis + base_y) / 2)
    torso_lean = 10
    crouch_y_neck = base_y - figure_height * 0.6
    pose_crouch[NECK_CENTER]   = (cx + torso_lean, crouch_y_neck)
    pose_crouch[HEAD]          = (cx + torso_lean, crouch_y_neck - figure_height * 0.2)
    pose_crouch[L_SHOULDER]    = (pose_crouch[NECK_CENTER][0] - 30, crouch_y_neck)
    pose_crouch[R_SHOULDER]    = (pose_crouch[NECK_CENTER][0] + 30, crouch_y_neck)
    pose_crouch[L_ELBOW]       = (pose_crouch[L_SHOULDER][0] + 10, crouch_y_neck + 30) # Arms back
    pose_crouch[R_ELBOW]       = (pose_crouch[R_SHOULDER][0] + 10, crouch_y_neck + 30)
    pose_crouch[L_WRIST]       = (pose_crouch[L_ELBOW][0] + 5, pose_crouch[L_ELBOW][1] + 30)
    pose_crouch[R_WRIST]       = (pose_crouch[R_ELBOW][0] + 5, pose_crouch[R_ELBOW][1] + 30)

    # KEY POSE 3: Apex
    # The highest point of the jump. Expansive, "happy" pose.
    pose_apex = [None] * NUM_POINTS
    pose_apex[HEAD]          = (cx, base_y - figure_height)
    pose_apex[NECK_CENTER]   = (cx, base_y - figure_height * 0.8)
    pose_apex[PELVIS_CENTER] = (cx, base_y - figure_height * 0.5)
    pose_apex[L_SHOULDER]    = (cx - 40, base_y - figure_height * 0.78) # Arms raised
    pose_apex[R_SHOULDER]    = (cx + 40, base_y - figure_height * 0.78)
    pose_apex[L_ELBOW]       = (cx - 70, base_y - figure_height * 0.7)
    pose_apex[R_ELBOW]       = (cx + 70, base_y - figure_height * 0.7)
    pose_apex[L_WRIST]       = (cx - 90, base_y - figure_height * 0.6)
    pose_apex[R_WRIST]       = (cx + 90, base_y - figure_height * 0.6)
    pose_apex[L_HIP]         = (cx - 20, base_y - figure_height * 0.5)
    pose_apex[R_HIP]         = (cx + 20, base_y - figure_height * 0.5)
    pose_apex[L_KNEE]        = (cx - 25, base_y - figure_height * 0.35) # Knees tucked
    pose_apex[R_KNEE]        = (cx + 25, base_y - figure_height * 0.35)
    pose_apex[L_ANKLE]       = (cx - 25, base_y - figure_height * 0.15)
    pose_apex[R_ANKLE]       = (cx + 25, base_y - figure_height * 0.15)
    
    # KEY POSE 4: Landing
    # A crouch pose to absorb impact, arms forward for balance.
    pose_land = list(pose_crouch) # Start with crouch pose
    pose_land[L_ELBOW]       = (pose_crouch[L_SHOULDER][0] - 20, crouch_y_neck + 30) # Arms forward
    pose_land[R_ELBOW]       = (pose_crouch[R_SHOULDER][0] + 20, crouch_y_neck + 30)
    pose_land[L_WRIST]       = (pose_land[L_ELBOW][0] - 25, pose_land[L_ELBOW][1] + 10)
    pose_land[R_WRIST]       = (pose_land[R_ELBOW][0] + 25, pose_land[R_ELBOW][1] + 10)

    # --- Frame Generation ---

    def lerp(p1, p2, t):
        """Linear interpolation between two values."""
        return p1 * (1 - t) + p2 * t

    def ease_in_out_cubic(t):
        """Easing function for smooth acceleration and deceleration."""
        return t * t * (3.0 - 2.0 * t)

    def interpolate_pose(p1, p2, t, ease_func=ease_in_out_cubic):
        """Interpolates between two full poses (all 15 points)."""
        t_eased = ease_func(t)
        new_pose = []
        for i in range(NUM_POINTS):
            x = lerp(p1[i][0], p2[i][0], t_eased)
            y = lerp(p1[i][1], p2[i][1], t_eased)
            new_pose.append((x, y))
        return new_pose

    all_frames = []
    for f in range(TOTAL_FRAMES):
        y_offset = 0
        current_pose = []

        if T_START_CROUCH <= f < T_END_CROUCH:
            # Phase 1: Stand -> Crouch
            t = (f - T_START_CROUCH) / PREP_DURATION
            current_pose = interpolate_pose(pose_stand, pose_crouch, t)
        
        elif T_END_CROUCH <= f < T_LAND:
            # Phase 2 & 3: Jump Arc (Crouch -> Apex -> Land)
            # Calculate overall vertical motion (ballistic arc)
            t_jump = (f - T_END_CROUCH) / (JUMP_UP_DURATION + JUMP_DOWN_DURATION)
            y_offset = jump_height * math.sin(t_jump * math.pi)

            # Interpolate the pose itself from crouch to apex, then apex to land
            if f < T_APEX: # Going up
                t_pose = (f - T_END_CROUCH) / JUMP_UP_DURATION
                current_pose = interpolate_pose(pose_crouch, pose_apex, t_pose)
            else: # Going down
                t_pose = (f - T_APEX) / JUMP_DOWN_DURATION
                current_pose = interpolate_pose(pose_apex, pose_land, t_pose)
        
        elif T_LAND <= f < T_END_RECOVERY:
            # Phase 4: Land -> Stand
            t = (f - T_LAND) / RECOVERY_DURATION
            current_pose = interpolate_pose(pose_land, pose_stand, t)

        # Apply the vertical jump offset to the calculated pose
        final_pose = [(p[0], p[1] - y_offset) for p in current_pose]
        all_frames.append(final_pose)

    # --- Pygame Main Loop ---
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Happy Woman Jumping with Heavy Weight")
    clock = pygame.time.Clock()
    frame_count = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Clear the screen
        screen.fill(BG_COLOR)

        # Get the current frame's points
        current_frame_points = all_frames[frame_count]

        # Draw the points
        for point in current_frame_points:
            pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), POINT_RADIUS)

        # Update the display
        pygame.display.flip()

        # Advance to the next frame, looping the animation
        frame_count = (frame_count + 1) % TOTAL_FRAMES

        # Maintain the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
