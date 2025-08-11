
import pygame
import sys

def main():
    """
    Main function to set up and run the point-light stimulus animation.
    """
    pygame.init()

    # --- Configuration ---
    WIDTH, HEIGHT = 600, 800
    FPS = 30
    BG_COLOR = (0, 0, 0)
    DOT_COLOR = (255, 255, 255)
    DOT_RADIUS = 6

    # --- Screen Setup ---
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Jumping Up")
    clock = pygame.time.Clock()

    # --- Animation Data ---
    # The animation is defined by a series of keyframes.
    # Each keyframe consists of:
    # 1. The central (pelvis) position on the screen: (x, y)
    # 2. The relative positions of the 15 joints from the pelvis.
    # The joints are ordered as follows:
    # 0: Head, 1: Sternum, 2: L Shoulder, 3: R Shoulder, 4: L Elbow,
    # 5: R Elbow, 6: L Wrist, 7: R Wrist, 8: Pelvis, 9: L Hip, 10: R Hip,
    # 11: L Knee, 12: R Knee, 13: L Ankle, 14: R Ankle

    # Keyframe 1: Neutral standing pose
    kf1_pelvis = (300, 610)
    kf1_pose = [
        (0, -80), (0, -50), (-25, -55), (25, -55), (-25, -20), (25, -20),
        (-25, 15), (25, 15), (0, 0), (-15, 0), (15, 0), (-15, 45), (15, 45),
        (-15, 90), (15, 90)
    ]

    # Keyframe 2: Crouching down, arms swing back
    kf2_pelvis = (300, 650)
    kf2_pose = [
        (10, -80), (5, -50), (-20, -55), (30, -55), (-35, -30), (40, -30),
        (-40, 0), (45, 0), (0, 0), (-15, 0), (15, 0), (-20, 25), (20, 25),
        (-15, 50), (15, 50)
    ]

    # Keyframe 3: Takeoff, body extended, arms swing up
    kf3_pelvis = (300, 610)
    kf3_pose = [
        (0, -80), (0, -50), (-25, -55), (25, -55), (-25, -85), (25, -85),
        (-25, -120), (25, -120), (0, 0), (-15, 0), (15, 0), (-15, 45), (15, 45),
        (-15, 90), (15, 90)
    ]

    # Keyframe 4: Peak of the jump, body slightly tucked
    kf4_pelvis = (300, 400)
    kf4_pose = [
        (0, -80), (0, -50), (-25, -55), (25, -55), (-20, -25), (20, -25),
        (-15, 10), (15, 10), (0, 0), (-15, 0), (15, 0), (-15, 30), (15, 30),
        (-15, 60), (15, 60)
    ]

    # Keyframe 5: Descending, preparing to land, legs extended
    kf5_pelvis = (300, 610)
    kf5_pose = [
        (0, -80), (0, -50), (-25, -55), (25, -55), (-30, -20), (30, -20),
        (-35, 15), (35, 15), (0, 0), (-15, 0), (15, 0), (-15, 45), (15, 45),
        (-15, 90), (15, 90)
    ]

    # Keyframe 6: Landed, absorbing impact (same as crouch)
    kf6_pelvis = kf2_pelvis
    kf6_pose = kf2_pose

    # Keyframe 7: Returning to standing pose (same as start)
    kf7_pelvis = kf1_pelvis
    kf7_pose = kf1_pose

    keyframes = [
        (kf1_pelvis, kf1_pose), (kf2_pelvis, kf2_pose), (kf3_pelvis, kf3_pose),
        (kf4_pelvis, kf4_pose), (kf5_pelvis, kf5_pose), (kf6_pelvis, kf6_pose),
        (kf7_pelvis, kf7_pose)
    ]

    # Number of frames to generate between keyframes to control timing
    inter_frames_count = [20, 8, 20, 20, 8, 20]

    def generate_animation_frames(keyframes, inter_frames_count):
        """
        Generates all animation frames by interpolating between keyframes.
        """
        all_frames = []

        def lerp(p1, p2, t):
            """Linear interpolation."""
            return p1 + t * (p2 - p1)

        for i in range(len(keyframes) - 1):
            start_pelvis, start_pose = keyframes[i]
            end_pelvis, end_pose = keyframes[i + 1]
            num_steps = inter_frames_count[i]

            for step in range(num_steps):
                t = step / num_steps
                
                # Interpolate pelvis position
                current_pelvis_x = lerp(start_pelvis[0], end_pelvis[0], t)
                current_pelvis_y = lerp(start_pelvis[1], end_pelvis[1], t)
                
                frame_points = []
                for j in range(len(start_pose)):
                    # Interpolate relative joint position
                    start_rel_x, start_rel_y = start_pose[j]
                    end_rel_x, end_rel_y = end_pose[j]
                    
                    current_rel_x = lerp(start_rel_x, end_rel_x, t)
                    current_rel_y = lerp(start_rel_y, end_rel_y, t)
                    
                    # Calculate absolute screen position
                    abs_x = current_pelvis_x + current_rel_x
                    abs_y = current_pelvis_y + current_rel_y
                    frame_points.append((int(abs_x), int(abs_y)))
                
                all_frames.append(frame_points)
                
        # Add the very last keyframe to ensure the animation loop is perfect
        last_pelvis, last_pose = keyframes[-1]
        frame_points = []
        for rel_x, rel_y in last_pose:
            abs_x = last_pelvis[0] + rel_x
            abs_y = last_pelvis[1] + rel_y
            frame_points.append((int(abs_x), int(abs_y)))
        all_frames.append(frame_points)

        return all_frames

    animation_frames = generate_animation_frames(keyframes, inter_frames_count)
    frame_index = 0
    total_frames = len(animation_frames)

    # --- Main Game Loop ---
    running = True
    while running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Drawing
        screen.fill(BG_COLOR)

        # Get the points for the current frame
        current_points = animation_frames[frame_index]

        # Draw each point
        for point in current_points:
            pygame.draw.circle(screen, DOT_COLOR, point, DOT_RADIUS)

        # Update Display
        pygame.display.flip()

        # Update Frame Index for next iteration
        frame_index = (frame_index + 1) % total_frames

        # Control Frame Rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
