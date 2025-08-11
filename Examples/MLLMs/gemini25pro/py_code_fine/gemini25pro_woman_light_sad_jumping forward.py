
import pygame
import numpy as np

# --- Configuration ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 4
GLOBAL_SCALE = 1.8
# Perspective is calculated relative to a viewer.
# +Z is into the screen (away from viewer).
VIEWER_DISTANCE = 400

# --- Animation Data: A sad woman with light weight is <jumping forward> ---
# The animation is defined by a series of keyframes.
# Each keyframe has a time, a 3D offset for the whole character, and a 'pose'.
# The pose consists of 3D coordinates for 15 joints.
# The joints are: Head, Neck, Torso, L-Shoulder, L-Elbow, L-Wrist, R-Shoulder, R-Elbow, R-Wrist,
# L-Hip, L-Knee, L-Ankle, R-Hip, R-Knee, R-Ankle.
# The 'sad' emotion is conveyed by a slightly slumped posture (drooping shoulders, head down).
# 'Jumping forward' is represented by motion across the screen (X-axis) and an arc
# towards and then away from the viewer (Z-axis).

keyframes = [
    {
        'time': 0.0, 'offset': np.array([-180.0, 0.0, 50.0]),
        'pose': np.array([ # Initial Stance (sad posture)
            [0, 105, -2], [0, 90, 0], [0, 70, 0], [-15, 87, 0], [-16, 60, -2],
            [-17, 32, 0], [15, 87, 0], [16, 60, -2], [17, 32, 0], [-10, 60, 0],
            [-11, 30, 0], [-11, 0, 0], [10, 60, 0], [11, 30, 0], [11, 0, 0]
        ])
    },
    {
        'time': 0.5, 'offset': np.array([-170.0, -10.0, 40.0]),
        'pose': np.array([ # Crouch / Preparation
            [0, 85, 2], [0, 70, 5], [0, 50, 5], [-15, 67, 5], [-20, 50, 15],
            [-25, 35, 25], [15, 67, 5], [20, 50, 15], [25, 35, 25], [-10, 40, 0],
            [-12, 15, 5], [-10, 0, 0], [10, 40, 0], [12, 15, 5], [10, 0, 0]
        ])
    },
    {
        'time': 0.7, 'offset': np.array([-150.0, 10.0, 20.0]),
        'pose': np.array([ # Take-off
            [5, 115, -8], [5, 100, -5], [5, 80, -5], [-10, 92, -5], [-15, 80, -20],
            [-20, 65, -30], [20, 92, -5], [25, 80, -20], [30, 65, -30], [-5, 70, -5],
            [-8, 40, -5], [-8, 5, -5], [15, 70, -5], [18, 40, -5], [18, 5, -5]
        ])
    },
    {
        'time': 1.05, 'offset': np.array([-60.0, 75.0, -20.0]),
        'pose': np.array([ # Flight Apex
            [10, 105, -13], [10, 90, -10], [10, 70, -10], [-5, 84, -10], [0, 75, -20],
            [-5, 65, -25], [25, 84, -10], [30, 75, -20], [35, 65, -25], [0, 60, -10],
            [5, 45, -5], [2, 25, 0], [20, 60, -10], [25, 45, -5], [22, 25, 0]
        ])
    },
    {
        'time': 1.4, 'offset': np.array([30.0, 30.0, 20.0]),
        'pose': np.array([ # Landing Preparation
            [15, 110, -18], [15, 95, -15], [15, 75, -15], [0, 89, -15], [0, 70, -5],
            [0, 50, 5], [30, 89, -15], [30, 70, -5], [30, 50, 5], [5, 65, -15],
            [5, 35, -10], [5, 5, -5], [25, 65, -15], [25, 35, -10], [25, 5, -5]
        ])
    },
    {
        'time': 1.5, 'offset': np.array([60.0, 0.0, 40.0]),
        'pose': np.array([ # Impact
            [20, 85, -13], [20, 70, -10], [20, 50, -10], [5, 65, -10], [0, 55, -20],
            [-5, 45, -30], [35, 65, -10], [40, 55, -20], [45, 45, -30], [10, 40, -10],
            [10, 15, -5], [10, 0, 0], [30, 40, -10], [30, 15, -5], [30, 0, 0]
        ])
    },
    {
        'time': 2.2, 'offset': np.array([90.0, 0.0, 50.0]),
        'pose': np.array([ # Final Stance
            [20, 105, -2], [20, 90, 0], [20, 70, 0], [5, 87, 0], [4, 60, -2],
            [3, 32, 0], [35, 87, 0], [36, 60, -2], [37, 32, 0], [10, 60, 0],
            [9, 30, 0], [9, 0, 0], [30, 60, 0], [29, 30, 0], [29, 0, 0]
        ])
    }
]

# Add a pause at the end for a smooth loop
end_pause_time = 1.0
final_kf = keyframes[-1].copy()
final_kf['time'] += end_pause_time
keyframes.append(final_kf)

def get_current_animation_state(time_sec):
    """Finds the surrounding keyframes and interpolation factor for a given time."""
    if time_sec <= keyframes[0]['time']:
        return keyframes[0], keyframes[0], 0.0
    if time_sec >= keyframes[-1]['time']:
        return keyframes[-1], keyframes[-1], 1.0

    for i in range(len(keyframes) - 1):
        kf1 = keyframes[i]
        kf2 = keyframes[i+1]
        if kf1['time'] <= time_sec < kf2['time']:
            time_diff = kf2['time'] - kf1['time']
            # Apply ease-in-out for smoother transition
            t = (time_sec - kf1['time']) / time_diff if time_diff > 0 else 0
            t = t * t * (3 - 2 * t)
            return kf1, kf2, t
    
    return keyframes[-1], keyframes[-1], 1.0

def interpolate(val1, val2, t):
    """Linearly interpolates between two numpy arrays or values."""
    return val1 * (1 - t) + val2 * t

def project_3d_to_2d(point_3d):
    """Projects a 3D point to 2D screen coordinates with perspective."""
    x, y, z = point_3d
    
    # Perspective projection: objects farther away (higher z) appear smaller
    scale_factor = VIEWER_DISTANCE / (VIEWER_DISTANCE + z)
    
    # Apply global scaling and center on screen
    # Pygame's y-axis is inverted (0 is at the top)
    screen_x = SCREEN_WIDTH / 2 + x * scale_factor * GLOBAL_SCALE
    screen_y = SCREEN_HEIGHT / 2 - y * scale_factor * GLOBAL_SCALE
    
    return int(screen_x), int(screen_y)

def main():
    """Main function to run the Pygame animation."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman Jumping Forward")
    clock = pygame.time.Clock()

    start_ticks = pygame.time.get_ticks()
    animation_duration = keyframes[-1]['time']

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Animation Update ---
        elapsed_sec = (pygame.time.get_ticks() - start_ticks) / 1000.0
        cycle_time = elapsed_sec % animation_duration
        
        kf1, kf2, t = get_current_animation_state(cycle_time)
        
        current_pose = interpolate(kf1['pose'], kf2['pose'], t)
        current_offset = interpolate(kf1['offset'], kf2['offset'], t)
        
        # Combine pose and offset for final 3D points
        final_points_3d = current_pose + current_offset

        # --- Drawing ---
        screen.fill(BLACK)
        
        for point_3d in final_points_3d:
            screen_pos = project_3d_to_2d(point_3d)
            pygame.draw.circle(screen, WHITE, screen_pos, POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
