
import pygame
import sys
import math

def interpolate_points(start_points, end_points, t):
    return [((1 - t) * start[0] + t * end[0], 
             (1 - t) * start[1] + t * end[1]) 
            for start, end in zip(start_points, end_points)]

def norm_to_screen(pos, screen_width, screen_height):
    return (int(pos[0] * screen_width), int(pos[1] * screen_height))

def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Point-Light Biological Motion: Sitting Down")
    
    background_color = (0, 0, 0)
    point_color = (255, 255, 255)
    point_radius = 6
    
    # Keyframes [Start, Mid1, Mid2, End]
    keyframes = [
        # Frame 0: Start (standing)
        [
            (0.50, 0.20), # Head
            (0.50, 0.30), # Neck
            (0.40, 0.35), # Left shoulder
            (0.60, 0.35), # Right shoulder
            (0.35, 0.45), # Left elbow
            (0.65, 0.45), # Right elbow
            (0.30, 0.55), # Left wrist
            (0.70, 0.55), # Right wrist
            (0.50, 0.45), # Spine
            (0.40, 0.55), # Left hip
            (0.60, 0.55), # Right hip
            (0.40, 0.75), # Left knee
            (0.60, 0.75), # Right knee
            (0.40, 0.90), # Left ankle
            (0.60, 0.90)  # Right ankle
        ],
        # Frame 1: Mid1 (begin descent)
        [
            (0.50, 0.23), # Head
            (0.50, 0.32), # Neck
            (0.41, 0.38), # Left shoulder
            (0.59, 0.38), # Right shoulder
            (0.37, 0.48), # Left elbow
            (0.63, 0.48), # Right elbow
            (0.32, 0.58), # Left wrist
            (0.68, 0.58), # Right wrist
            (0.50, 0.48), # Spine
            (0.42, 0.60), # Left hip
            (0.58, 0.60), # Right hip
            (0.43, 0.78), # Left knee
            (0.57, 0.78), # Right knee
            (0.43, 0.92), # Left ankle
            (0.57, 0.92)  # Right ankle
        ],
        # Frame 2: Mid2 (mid-sit)
        [
            (0.50, 0.33), # Head
            (0.50, 0.40), # Neck
            (0.43, 0.45), # Left shoulder
            (0.57, 0.45), # Right shoulder
            (0.40, 0.53), # Left elbow
            (0.60, 0.53), # Right elbow
            (0.35, 0.63), # Left wrist
            (0.65, 0.63), # Right wrist
            (0.50, 0.52), # Spine
            (0.45, 0.70), # Left hip
            (0.55, 0.70), # Right hip
            (0.47, 0.83), # Left knee
            (0.53, 0.83), # Right knee
            (0.46, 0.95), # Left ankle
            (0.54, 0.95)  # Right ankle
        ],
        # Frame 3: End (fully seated)
        [
            (0.50, 0.40), # Head
            (0.50, 0.46), # Neck
            (0.45, 0.50), # Left shoulder
            (0.55, 0.50), # Right shoulder
            (0.42, 0.58), # Left elbow
            (0.58, 0.58), # Right elbow
            (0.38, 0.68), # Left wrist
            (0.62, 0.68), # Right wrist
            (0.50, 0.58), # Spine
            (0.47, 0.78), # Left hip
            (0.53, 0.78), # Right hip
            (0.49, 0.88), # Left knee
            (0.51, 0.88), # Right knee
            (0.48, 0.98), # Left ankle
            (0.52, 0.98)  # Right ankle
        ]
    ]
    
    num_keyframes = len(keyframes)
    total_frames = 120  # 4 seconds at 30 FPS
    clock = pygame.time.Clock()
    frame_count = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(background_color)
        
        t = frame_count / (total_frames - 1)
        segment = t * (num_keyframes - 1)
        segment_idx = min(int(segment), num_keyframes - 2)
        segment_t = segment - segment_idx
        
        start_points = keyframes[segment_idx]
        end_points = keyframes[segment_idx + 1]
        current_points = interpolate_points(start_points, end_points, segment_t)
        
        for point in current_points:
            screen_x, screen_y = norm_to_screen(point, screen_width, screen_height)
            pygame.draw.circle(screen, point_color, (screen_x, screen_y), point_radius)
        
        pygame.display.flip()
        clock.tick(30)
        frame_count = (frame_count + 1) % total_frames
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
