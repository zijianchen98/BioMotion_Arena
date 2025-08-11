
import pygame
import sys
import math

def interpolate_points(pose0, pose1, fraction):
    """Interpolate between two poses by a given fraction."""
    return [((1 - fraction) * x0 + fraction * x1, 
             (1 - fraction) * y0 + fraction * y1) 
            for (x0, y0), (x1, y1) in zip(pose0, pose1)]

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Biological Motion: Lying Down")
    clock = pygame.time.Clock()

    screen_center_x = width // 2
    ground_level = height - 100
    
    # Standing pose (initial)
    pose_standing = [
        (0, 200),     # head
        (-40, 170),   # left shoulder
        (-70, 140),   # left elbow
        (-100, 110),  # left hand
        (40, 170),    # right shoulder
        (70, 140),    # right elbow
        (100, 110),   # right hand
        (0, 160),     # mid-torso
        (0, 120),     # mid-hip
        (-20, 120),   # left hip
        (-20, 60),    # left knee
        (-20, 0),     # left foot
        (20, 120),    # right hip
        (20, 60),     # right knee
        (20, 0)       # right foot
    ]
    
    # Lying pose (final)
    pose_lying = [
        (-100, 0),    # head
        (-85, 0),     # left shoulder
        (-60, 0),     # left elbow
        (-40, 0),     # left hand
        (-75, 0),     # right shoulder
        (-50, 0),     # right elbow
        (-30, 0),     # right hand
        (-50, 0),     # mid-torso
        (0, 0),       # mid-hip
        (-20, 0),     # left hip
        (40, 0),      # left knee
        (80, 0),      # left foot
        (20, 0),      # right hip
        (60, 0),      # right knee
        (100, 0)      # right foot
    ]
    
    total_frames = 100
    current_frame = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))
        
        if current_frame < total_frames:
            fraction = current_frame / (total_frames - 1)
            # Apply easing for more natural motion
            fraction = 0.5 - 0.5 * math.cos(fraction * math.pi)
            current_pose = interpolate_points(pose_standing, pose_lying, fraction)
            current_frame += 1
        else:
            current_pose = pose_lying
        
        for (x, y) in current_pose:
            screen_x = screen_center_x + x
            screen_y = ground_level - y
            pygame.draw.circle(screen, (255, 255, 255), (int(screen_x), int(screen_y)), 5)
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
