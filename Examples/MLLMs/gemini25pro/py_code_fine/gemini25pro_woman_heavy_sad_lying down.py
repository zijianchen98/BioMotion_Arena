
import pygame
import math

def main():
    """
    Main function to run the biological motion animation.
    """
    # --- Pygame Setup ---
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman Lying Down")
    clock = pygame.time.Clock()

    # --- Constants and Colors ---
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FPS = 60
    POINT_RADIUS = 6

    # --- Easing Function for Smooth Motion ---
    def ease_in_out_sine(t):
        """Sine-based easing function for smooth start and end of motion."""
        return -(math.cos(math.pi * t) - 1) / 2

    # --- Keyframe Data ---
    # The animation is defined by a series of keyframes.
    # Each keyframe contains the (x, y) coordinates for the 15 points.
    # The coordinate system origin (0,0) is the figure's center of mass.
    # Y increases downwards.
    # The points are:
    # 0: Head, 1: Neck, 2: Left Shoulder, 3: Right Shoulder,
    # 4: Left Elbow, 5: Right Elbow, 6: Left Wrist, 7: Right Wrist,
    # 8: Pelvis, 9: Left Hip, 10: Right Hip, 11: Left Knee,
    # 12: Right Knee, 13: Left Ankle, 14: Right Ankle

    y_offset = -60  # Vertical offset to center the animation on the screen

    # Keyframe 0: Standing with a sad, heavy posture (slumped)
    k0 = [
        (0, -145 + y_offset),   # Head
        (0, -120 + y_offset),   # Neck
        (-40, -115 + y_offset),  # L Shoulder
        (40, -115 + y_offset),   # R Shoulder
        (-45, -55 + y_offset),   # L Elbow
        (45, -55 + y_offset),    # R Elbow
        (-50, 5 + y_offset),     # L Wrist
        (50, 5 + y_offset),      # R Wrist
        (0, 0 + y_offset),       # Pelvis
        (-30, 0 + y_offset),     # L Hip
        (30, 0 + y_offset),      # R Hip
        (-35, 70 + y_offset),    # L Knee
        (35, 70 + y_offset),     # R Knee
        (-35, 140 + y_offset),   # L Ankle
        (35, 140 + y_offset)     # R Ankle
    ]

    # Keyframe 1: Crouching low, preparing to go to the ground
    k1 = [
        (25, -40 + y_offset),    # Head
        (20, -30 + y_offset),    # Neck
        (-15, -35 + y_offset),   # L Shoulder
        (55, -35 + y_offset),    # R Shoulder
        (0, 30 + y_offset),      # L Elbow
        (70, 30 + y_offset),     # R Elbow
        (40, 90 + y_offset),     # L Wrist
        (90, 90 + y_offset),     # R Wrist
        (15, 70 + y_offset),     # Pelvis
        (-15, 70 + y_offset),    # L Hip
        (45, 70 + y_offset),     # R Hip
        (-25, 120 + y_offset),   # L Knee
        (55, 120 + y_offset),    # R Knee
        (-30, 145 + y_offset),   # L Ankle
        (50, 145 + y_offset)     # R Ankle
    ]

    # Keyframe 2: Body collapsing, hands and one knee on the ground
    k2 = [
        (75, 50 + y_offset),     # Head
        (65, 40 + y_offset),     # Neck
        (35, 30 + y_offset),     # L Shoulder
        (95, 50 + y_offset),     # R Shoulder
        (45, 90 + y_offset),     # L Elbow
        (105, 90 + y_offset),    # R Elbow
        (55, 140 + y_offset),    # L Wrist (on ground)
        (115, 140 + y_offset),   # R Wrist (on ground)
        (45, 80 + y_offset),     # Pelvis
        (15, 80 + y_offset),     # L Hip
        (75, 80 + y_offset),     # R Hip
        (5, 120 + y_offset),     # L Knee
        (85, 140 + y_offset),    # R Knee (on ground)
        (-5, 150 + y_offset),    # L Ankle
        (75, 160 + y_offset)     # R Ankle
    ]

    # Keyframe 3: Final lying position on the side, in a fetal-like pose
    final_x_center = 70
    final_y_center = 170 + y_offset
    k3 = [
        (final_x_center - 70, final_y_center - 5),   # Head
        (final_x_center - 50, final_y_center),       # Neck
        (final_x_center - 45, final_y_center - 15),  # L Shoulder (top)
        (final_x_center - 45, final_y_center + 15),  # R Shoulder (bottom)
        (final_x_center - 10, final_y_center - 30),  # L Elbow
        (final_x_center - 5, final_y_center + 30),   # R Elbow
        (final_x_center + 20, final_y_center - 5),   # L Wrist
        (final_x_center + 25, final_y_center + 5),   # R Wrist
        (final_x_center, final_y_center),            # Pelvis
        (final_x_center, final_y_center - 15),       # L Hip (top)
        (final_x_center, final_y_center + 15),       # R Hip (bottom)
        (final_x_center + 45, final_y_center - 20),  # L Knee
        (final_x_center + 40, final_y_center + 20),  # R Knee
        (final_x_center + 80, final_y_center - 25),  # L Ankle
        (final_x_center + 75, final_y_center + 25)   # R Ankle
    ]

    # --- Animation Setup ---
    animation_phases = [
        (k0, k1, 3.0),  # Phase 1: Slump to crouch
        (k1, k2, 2.5),  # Phase 2: Collapse to hands and knees
        (k2, k3, 2.0)   # Phase 3: Settle into final side-lying pose
    ]
    hold_duration = 4.0
    
    phase_index = 0
    timer = 0.0
    state = "animating"
    current_points = k0

    # --- Main Loop ---
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        timer += dt

        # --- State Machine for Animation Control ---
        if state == "animating":
            start_frame, end_frame, duration = animation_phases[phase_index]
            
            if timer >= duration:
                timer = 0
                phase_index += 1
                if phase_index >= len(animation_phases):
                    state = "holding"
                    current_points = end_frame
                continue

            t = ease_in_out_sine(timer / duration)
            
            # Interpolate points
            interpolated_points = []
            for i in range(len(start_frame)):
                x = start_frame[i][0] + (end_frame[i][0] - start_frame[i][0]) * t
                y = start_frame[i][1] + (end_frame[i][1] - start_frame[i][1]) * t
                interpolated_points.append((x, y))
            current_points = interpolated_points

        elif state == "holding":
            # Add a subtle breathing motion to the final pose
            breath_cycle = math.sin(timer * math.pi * 0.5) # Slow breath
            breath_amount = 2 * breath_cycle
            
            final_pose = list(animation_phases[-1][1]) # Get the last keyframe
            breathing_points = list(final_pose)

            # Apply breathing to torso points
            # Left shoulder (top) moves most
            breathing_points[2] = (final_pose[2][0], final_pose[2][1] - breath_amount)
            # Neck and hips move slightly
            breathing_points[1] = (final_pose[1][0], final_pose[1][1] - breath_amount * 0.5)
            breathing_points[9] = (final_pose[9][0], final_pose[9][1] - breath_amount * 0.3)
            current_points = breathing_points
            
            if timer >= hold_duration:
                state = "resetting"

        elif state == "resetting":
            # Instantly reset the animation to the beginning
            phase_index = 0
            timer = 0.0
            state = "animating"
            continue

        # --- Drawing ---
        screen.fill(BLACK)
        
        for point in current_points:
            # Translate from model coordinates to screen coordinates
            screen_x = int(point[0] + SCREEN_WIDTH / 2)
            screen_y = int(point[1] + SCREEN_HEIGHT / 2)
            pygame.draw.circle(screen, WHITE, (screen_x, screen_y), POINT_RADIUS)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
