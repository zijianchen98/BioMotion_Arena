
import pygame
import math

def main():
    """
    This program displays a point-light stimulus animation of a sad woman lying down.
    The animation is rendered using Pygame and consists of 15 white points on a black background.
    The motion is designed to be smooth, realistic, and biomechanically plausible.
    """
    
    # --- Constants ---
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 60  # Using a higher FPS for smoother animation
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    DOT_RADIUS = 6

    # --- Point-light data ---
    # The data represents the (x, y) coordinates for 15 joints at different keyframes.
    # The joints are ordered as follows:
    # 0: Head, 1: Sternum, 2: Pelvis
    # 3: Left Shoulder, 4: Right Shoulder
    # 5: Left Elbow,    6: Right Elbow
    # 7: Left Wrist,    8: Right Wrist
    # 9: Left Hip,      10: Right Hip
    # 11: Left Knee,    12: Right Knee
    # 13: Left Ankle,   14: Right Ankle
    # Note: "Left" and "Right" are from the character's perspective.

    keyframes = [
        # Keyframe 0: Standing with a sad, slumped posture.
        [
            (315, 210), (305, 270), (300, 350),  # Head, Sternum, Pelvis
            (295, 270), (315, 270),              # L/R Shoulder
            (285, 330), (325, 330),              # L/R Elbow
            (280, 390), (330, 390),              # L/R Wrist
            (290, 350), (310, 350),              # L/R Hip
            (290, 420), (310, 420),              # L/R Knee
            (290, 500), (310, 500)               # L/R Ankle
        ],
        # Keyframe 1: Crouching down, beginning to reach out with hands for support.
        [
            (360, 290), (350, 340), (340, 410),  # Head, Sternum, Pelvis
            (335, 340), (365, 340),              # L/R Shoulder
            (360, 400), (390, 400),              # L/R Elbow
            (390, 450), (420, 450),              # L/R Wrist
            (330, 410), (350, 410),              # L/R Hip
            (330, 470), (350, 470),              # L/R Knee
            (310, 520), (330, 520)               # L/R Ankle
        ],
        # Keyframe 2: Kneeling, with hands placed on the ground for stability.
        [
            (420, 330), (400, 380), (350, 420),  # Head, Sternum, Pelvis
            (390, 380), (410, 380),              # L/R Shoulder
            (410, 430), (430, 430),              # L/R Elbow
            (430, 490), (450, 490),              # L/R Wrist
            (340, 420), (360, 420),              # L/R Hip
            (350, 480), (370, 480),              # L/R Knee
            (320, 510), (340, 510)               # L/R Ankle
        ],
        # Keyframe 3: Shifting weight to lie down on the right side.
        [
            (490, 485), (415, 485), (380, 480),  # Head, Sternum, Pelvis
            (415, 475), (450, 490),              # L/R Shoulder
            (380, 460), (430, 510),              # L/R Elbow
            (350, 470), (450, 520),              # L/R Wrist
            (380, 470), (380, 500),              # L/R Hip
            (340, 460), (350, 480),              # L/R Knee
            (320, 470), (330, 500)               # L/R Ankle
        ],
        # Keyframe 4: Settling into a final, fetal-like position on the side.
        [
            (480, 490), (420, 485), (390, 480),  # Head, Sternum, Pelvis
            (420, 475), (450, 490),              # L/R Shoulder
            (390, 465), (440, 510),              # L/R Elbow
            (370, 475), (460, 520),              # L/R Wrist
            (390, 475), (390, 495),              # L/R Hip
            (350, 460), (360, 480),              # L/R Knee
            (340, 480), (350, 495)               # L/R Ankle
        ],
        # Keyframe 5: Holding the final pose to give a sense of finality.
        [
            (480, 490), (420, 485), (390, 480),  # Head, Sternum, Pelvis
            (420, 475), (450, 490),              # L/R Shoulder
            (390, 465), (440, 510),              # L/R Elbow
            (370, 475), (460, 520),              # L/R Wrist
            (390, 475), (390, 495),              # L/R Hip
            (350, 460), (360, 480),              # L/R Knee
            (340, 480), (350, 495)               # L/R Ankle
        ]
    ]

    # Number of frames to generate between each keyframe segment.
    # The timings are chosen to reflect the slow, heavy nature of the sad motion.
    frames_per_segment = [90, 60, 70, 60, 90]

    def ease_in_out_sine(t):
        """A smooth easing function for natural acceleration and deceleration."""
        return -(math.cos(math.pi * t) - 1) / 2

    def interpolate(p1, p2, t):
        """Interpolates between two points (p1, p2) using an eased time value (t)."""
        eased_t = ease_in_out_sine(t)
        x1, y1 = p1
        x2, y2 = p2
        x = x1 + (x2 - x1) * eased_t
        y = y1 + (y2 - y1) * eased_t
        return int(x), int(y)

    def generate_all_frames(keyframes_data, segments_data):
        """Generates a complete list of frames by interpolating between keyframes."""
        all_frames = []
        for i in range(len(keyframes_data) - 1):
            start_frame = keyframes_data[i]
            end_frame = keyframes_data[i+1]
            num_steps = segments_data[i]
            
            if num_steps == 0:
                continue

            for step in range(num_steps):
                t = step / num_steps
                current_frame_points = []
                for point_idx in range(len(start_frame)):
                    p1 = start_frame[point_idx]
                    p2 = end_frame[point_idx]
                    interpolated_point = interpolate(p1, p2, t)
                    current_frame_points.append(interpolated_point)
                all_frames.append(current_frame_points)
        
        all_frames.append(keyframes_data[-1]) # Ensure the last frame is included
        return all_frames

    # --- Pygame Setup and Main Loop ---
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Lying Down")
    clock = pygame.time.Clock()

    all_frames = generate_all_frames(keyframes, frames_per_segment)
    
    frame_index = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Drawing
        screen.fill(BLACK)
        
        current_points = all_frames[frame_index]
        for point in current_points:
            pygame.draw.circle(screen, WHITE, point, DOT_RADIUS)

        # Update display
        pygame.display.flip()
        
        # Advance to the next frame
        frame_index += 1
        if frame_index >= len(all_frames):
            frame_index = 0 # Loop the animation
            
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
