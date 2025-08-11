
import pygame

def main():
    """
    Main function to set up and run the point-light animation.
    """
    # --- Pygame Setup ---
    pygame.init()
    
    # --- Constants ---
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # Animation properties
    DOT_RADIUS = 6
    ANIMATION_DURATION_S = 3.5  # Duration of one roll cycle in seconds

    # --- Keyframe Data ---
    # This data represents the (x, y) coordinates of 15 joints at different
    # key moments of a forward roll. The animation will interpolate between these points.
    # The 15 joints are ordered as follows:
    # 0: Head, 1: Sternum, 2: Pelvis, 3: Left Shoulder, 4: Right Shoulder,
    # 5: Left Elbow, 6: Right Elbow, 7: Left Wrist, 8: Right Wrist,
    # 9: Left Hip, 10: Right Hip, 11: Left Knee, 12: Right Knee,
    # 13: Left Ankle, 14: Right Ankle
    keyframes = [
        # KF 0: Start in a crouch/squat
        [
            (170, 320), (160, 370), (150, 440), (150, 375), (170, 365),
            (180, 400), (200, 390), (210, 420), (230, 410), (140, 445),
            (160, 435), (150, 480), (170, 475), (150, 520), (170, 520)
        ],
        # KF 1: Hands down, body tucked, hips rising
        [
            (280, 390), (260, 420), (220, 400), (250, 425), (270, 415),
            (280, 460), (300, 450), (300, 520), (320, 520), (210, 405),
            (230, 395), (200, 460), (220, 450), (180, 520), (200, 520)
        ],
        # KF 2: Rolling onto shoulders, body is a ball
        [
            (380, 510), (350, 500), (350, 400), (340, 520), (360, 520),
            (330, 505), (350, 500), (320, 490), (340, 480), (340, 405),
            (360, 395), (380, 440), (400, 430), (370, 480), (390, 470)
        ],
        # KF 3: Mid-roll, on the back, legs coming over
        [
            (450, 380), (450, 430), (450, 500), (440, 435), (460, 425),
            (410, 460), (430, 450), (400, 430), (420, 420), (440, 505),
            (460, 495), (420, 440), (440, 430), (430, 400), (450, 390)
        ],
        # KF 4: Finishing roll, landing in a crouch
        [
            (530, 320), (540, 370), (550, 440), (530, 375), (550, 365),
            (500, 400), (520, 390), (470, 420), (490, 410), (540, 445),
            (560, 435), (550, 480), (570, 475), (550, 520), (570, 520)
        ],
        # KF 5: Standing up from the crouch
        [
            (560, 250), (560, 300), (560, 370), (540, 300), (580, 300),
            (540, 350), (580, 350), (540, 400), (580, 400), (550, 375),
            (570, 375), (550, 440), (570, 440), (550, 520), (570, 520)
        ],
        # KF 6: Brief pause in standing position
        [
            (560, 250), (560, 300), (560, 370), (540, 300), (580, 300),
            (540, 350), (580, 350), (540, 400), (580, 400), (550, 375),
            (570, 375), (550, 440), (570, 440), (550, 520), (570, 520)
        ]
    ]

    # --- Helper Function for Interpolation ---
    def linear_interpolate(p1, p2, t):
        """Linearly interpolates between two 2D points p1 and p2."""
        x1, y1 = p1
        x2, y2 = p2
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        return x, y

    # --- Animation Setup ---
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Forward Rolling")
    clock = pygame.time.Clock()
    
    total_frames_in_cycle = int(FPS * ANIMATION_DURATION_S)
    num_segments = len(keyframes) - 1
    frames_per_segment = total_frames_in_cycle / num_segments
    
    frame_count = 0
    running = True

    # --- Main Loop ---
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Animation Logic ---
        # Determine current position in the animation cycle
        current_cycle_frame = frame_count % total_frames_in_cycle
        
        # Determine which keyframe segment and the interpolation factor 't'
        segment_progress = current_cycle_frame / frames_per_segment
        segment_index = int(segment_progress)
        t = segment_progress - segment_index
        
        # Ensure we don't go out of bounds
        segment_index = min(segment_index, num_segments - 1)

        # Get the start and end keyframes for the current segment
        start_frame_points = keyframes[segment_index]
        end_frame_points = keyframes[segment_index + 1]

        # Calculate the current position for each of the 15 points
        current_points = []
        for i in range(len(start_frame_points)):
            pos = linear_interpolate(start_frame_points[i], end_frame_points[i], t)
            current_points.append(pos)

        # --- Drawing ---
        screen.fill(BLACK)
        for point in current_points:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), DOT_RADIUS)
        
        pygame.display.flip()

        # --- Update ---
        frame_count += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
