
import pygame
import math

# --- Configuration ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5
FPS = 30

# --- Keyframe Data ---
# The animation is defined by a series of keyframes. Each keyframe describes the
# (x, y) position of 15 joints. The coordinate system has its origin at the
# center of the pelvis for the initial standing pose, with Y increasing upwards.
# This relative coordinate system is then translated to the screen coordinates.
#
# The 15 points represent:
# 0: Head, 1: Neck, 2: Left Shoulder, 3: Right Shoulder, 4: Left Elbow,
# 5: Right Elbow, 6: Left Wrist, 7: Right Wrist, 8: Pelvis/Torso Center,
# 9: Left Hip, 10: Right Hip, 11: Left Knee, 12: Right Knee,
# 13: Left Ankle, 14: Right Ankle

# Keyframe 1: Standing, but slumped and defeated. Head bowed, shoulders rounded.
keyframe_1 = [
    (0, 170),    # 0 Head
    (0, 150),    # 1 Neck
    (-25, 145),  # 2 L Shoulder
    (25, 145),   # 3 R Shoulder
    (-28, 110),  # 4 L Elbow
    (28, 110),   # 5 R Elbow
    (-30, 75),   # 6 L Wrist
    (30, 75),    # 7 R Wrist
    (0, 80),     # 8 Pelvis
    (-20, 80),   # 9 L Hip
    (20, 80),    # 10 R Hip
    (-18, 40),   # 11 L Knee
    (18, 40),    # 12 R Knee
    (-18, 0),    # 13 L Ankle
    (18, 0),     # 14 R Ankle
]

# Keyframe 2: Crouching down heavily. The body lowers and tilts forward.
# The arms come forward to brace for impact or for balance.
keyframe_2 = [
    (35, 105),   # 0 Head
    (30, 90),    # 1 Neck
    (10, 85),    # 2 L Shoulder
    (50, 85),    # 3 R Shoulder
    (35, 55),    # 4 L Elbow
    (75, 55),    # 5 R Elbow
    (50, 20),    # 6 L Wrist
    (90, 20),    # 7 R Wrist
    (20, 45),    # 8 Pelvis
    (0, 45),     # 9 L Hip
    (40, 45),    # 10 R Hip
    (-5, 25),    # 11 L Knee
    (45, 25),    # 12 R Knee
    (-10, 0),     # 13 L Ankle
    (25, 0),      # 14 R Ankle
]

# Keyframe 3: Collapsing to the side. The right knee and hand make contact
# with the ground, taking the weight. The body is low and off-balance.
keyframe_3 = [
    (80, 70),    # 0 Head
    (75, 60),    # 1 Neck
    (55, 55),    # 2 L Shoulder
    (95, 55),    # 3 R Shoulder
    (70, 25),    # 4 L Elbow
    (110, 35),   # 5 R Elbow
    (85, -5),    # 6 L Wrist
    (125, 10),   # 7 R Wrist (on ground)
    (60, 30),    # 8 Pelvis
    (40, 30),    # 9 L Hip
    (80, 30),    # 10 R Hip
    (35, 5),     # 11 L Knee
    (85, 10),    # 12 R Knee (on ground)
    (15, 0),     # 13 L Ankle
    (60, 0),     # 14 R Ankle
]

# Keyframe 4: Final resting pose. Lying on the side in a collapsed,
# semi-fetal position, conveying exhaustion and sadness.
keyframe_4 = [
    (120, 20),   # 0 Head
    (110, 25),   # 1 Neck
    (105, 35),   # 2 L Shoulder (on top)
    (115, 30),   # 3 R Shoulder (underneath)
    (90, 15),    # 4 L Elbow
    (100, 5),    # 5 R Elbow
    (80, -5),    # 6 L Wrist
    (90, -15),   # 7 R Wrist
    (70, 35),    # 8 Pelvis
    (65, 40),    # 9 L Hip
    (75, 30),    # 10 R Hip
    (50, 20),    # 11 L Knee
    (60, 10),    # 12 R Knee
    (30, 10),    # 13 L Ankle
    (40, 0),     # 14 R Ankle
]


keyframes = [keyframe_1, keyframe_2, keyframe_3, keyframe_4]
# Define the number of frames for each transition. More frames = slower movement.
# This pacing reflects the slow, heavy nature of the action.
transition_lengths = [60, 40, 80]

def linear_interpolate(p1, p2, t):
    """Linearly interpolates between two 2D points (x, y)."""
    x1, y1 = p1
    x2, y2 = p2
    x = x1 + (x2 - x1) * t
    y = y1 + (y2 - y1) * t
    return x, y

def generate_animation_frames(keyframes, transitions):
    """Generates all intermediate frames from a list of keyframes."""
    all_frames = []
    for i in range(len(keyframes) - 1):
        start_pose = keyframes[i]
        end_pose = keyframes[i+1]
        num_steps = transitions[i]
        
        for step in range(num_steps):
            t = step / float(num_steps)
            current_frame_points = []
            for j in range(len(start_pose)):
                p1 = start_pose[j]
                p2 = end_pose[j]
                interpolated_point = linear_interpolate(p1, p2, t)
                current_frame_points.append(interpolated_point)
            all_frames.append(current_frame_points)
    
    # Add a pause at the end to hold the final pose
    for _ in range(FPS * 2): # Pause for 2 seconds
        all_frames.append(keyframes[-1])
    
    return all_frames

def main():
    """Main function to initialize pygame and run the animation loop."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Lying Down")
    clock = pygame.time.Clock()

    animation_frames = generate_animation_frames(keyframes, transition_lengths)

    # Calculate offset to position the animation on the screen.
    # Center horizontally, and position vertically so the feet start near the bottom.
    center_x = SCREEN_WIDTH // 2
    base_y = SCREEN_HEIGHT - 150

    frame_index = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Drawing ---
        screen.fill(BACKGROUND_COLOR)

        current_points = animation_frames[frame_index]

        for point in current_points:
            x, y = point
            # Translate local coordinates to screen coordinates.
            # Y is inverted (subtracted) because pygame's Y-axis is inverted.
            draw_x = int(center_x + x)
            draw_y = int(base_y - y) 
            pygame.draw.circle(screen, POINT_COLOR, (draw_x, draw_y), POINT_RADIUS)

        pygame.display.flip()

        # --- Update ---
        frame_index += 1
        if frame_index >= len(animation_frames):
            frame_index = 0  # Loop the animation

        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
