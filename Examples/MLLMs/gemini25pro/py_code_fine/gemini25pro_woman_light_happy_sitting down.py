
import pygame
import sys
import math

# --- Constants ---
# Window settings
WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation settings
FPS = 60
# A 2.5-second animation provides a natural, unhurried pace.
TOTAL_FRAMES = 150
POINT_RADIUS = 6

# --- Keyframe Data ---
# The animation uses 3 keyframes to define the start, middle, and end of the motion.
# The 15 points represent the main joints of a human figure:
# Head, L/R Shoulder, L/R Elbow, L/R Wrist, L/R Hip, L/R Knee, L/R Ankle,
# plus central points for the Neck/Sternum and Pelvis.

# Keyframe 1: Standing upright, relaxed posture.
KEYFRAME_1_STANDING = [
    (300, 220),  # 1. Head
    (260, 300),  # 2. L Shoulder
    (340, 300),  # 3. R Shoulder
    (255, 380),  # 4. L Elbow
    (345, 380),  # 5. R Elbow
    (250, 450),  # 6. L Wrist
    (350, 450),  # 7. R Wrist
    (280, 460),  # 8. L Hip
    (320, 460),  # 9. R Hip
    (285, 580),  # 10. L Knee
    (315, 580),  # 11. R Knee
    (290, 700),  # 12. L Ankle
    (310, 700),  # 13. R Ankle
    (300, 300),  # 14. Neck/Sternum
    (300, 460),  # 15. Pelvis
]

# Keyframe 2: Mid-point of sitting down. Hips are lowered, torso leans forward for balance.
KEYFRAME_2_MID_SIT = [
    (285, 280),  # 1. Head
    (240, 360),  # 2. L Shoulder
    (320, 360),  # 3. R Shoulder
    (260, 440),  # 4. L Elbow
    (340, 440),  # 5. R Elbow
    (275, 510),  # 6. L Wrist
    (355, 510),  # 7. R Wrist
    (260, 530),  # 8. L Hip
    (300, 530),  # 9. R Hip
    (285, 615),  # 10. L Knee
    (315, 615),  # 11. R Knee
    (290, 700),  # 12. L Ankle
    (310, 700),  # 13. R Ankle
    (280, 360),  # 14. Neck/Sternum
    (280, 530),  # 15. Pelvis
]

# Keyframe 3: Fully seated. Body is stable and relaxed.
KEYFRAME_3_SEATED = [
    (260, 360),  # 1. Head
    (220, 440),  # 2. L Shoulder
    (300, 440),  # 3. R Shoulder
    (230, 510),  # 4. L Elbow
    (310, 510),  # 5. R Elbow
    (265, 585),  # 6. L Wrist (resting on thigh)
    (305, 585),  # 7. R Wrist (resting on thigh)
    (230, 560),  # 8. L Hip
    (270, 560),  # 9. R Hip
    (290, 630),  # 10. L Knee
    (320, 630),  # 11. R Knee
    (290, 700),  # 12. L Ankle
    (310, 700),  # 13. R Ankle
    (260, 440),  # 14. Neck/Sternum
    (250, 560),  # 15. Pelvis
]

keyframes = [KEYFRAME_1_STANDING, KEYFRAME_2_MID_SIT, KEYFRAME_3_SEATED]

def ease_in_out_cubic(t):
    """A smooth easing function for more natural acceleration and deceleration."""
    return 4 * t * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 3) / 2

def lerp(p1, p2, t):
    """Linear interpolation for a single value."""
    return p1 * (1 - t) + p2 * t

def interpolate_frames(frame1, frame2, t):
    """
    Interpolates all 15 points between two keyframes using an easing function
    for more natural motion.
    """
    eased_t = ease_in_out_cubic(t)
    current_points = []
    for i in range(len(frame1)):
        x1, y1 = frame1[i]
        x2, y2 = frame2[i]
        x = lerp(x1, x2, eased_t)
        y = lerp(y1, y2, eased_t)
        current_points.append((x, y))
    return current_points

def main():
    """Main function to run the Pygame animation loop."""
    pygame.init()
    clock = pygame.time.Clock()
    frame_count = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Animation Logic ---
        # Calculate overall progress as a value from 0.0 to 1.0
        progress = (frame_count % TOTAL_FRAMES) / (TOTAL_FRAMES - 1)

        # Determine which two keyframes to interpolate between
        num_segments = len(keyframes) - 1
        segment_length = 1.0 / num_segments
        
        segment_index = min(math.floor(progress / segment_length), num_segments - 1)
        
        # Calculate progress within the current segment
        segment_progress = (progress - (segment_index * segment_length)) / segment_length

        start_keyframe = keyframes[segment_index]
        end_keyframe = keyframes[segment_index + 1]

        # Get the current coordinates of all points
        points = interpolate_frames(start_keyframe, end_keyframe, segment_progress)
        
        # --- Drawing ---
        WIN.fill(BLACK)
        for point in points:
            pygame.draw.circle(WIN, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)

        pygame.display.flip()

        # --- Update ---
        frame_count = (frame_count + 1)
        if frame_count >= TOTAL_FRAMES:
             frame_count = 0 # Loop the animation

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
