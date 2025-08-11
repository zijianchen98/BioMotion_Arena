
import pygame
import sys

def main():
    pygame.init()
    
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Point-light Biological Motion: Sitting Down")
    
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # Define 15 body points in 3D space for standing pose
    standing_pose = [
        (0, -1.0, 0.0),       # Head
        (0, -0.8, -0.1),       # Neck
        (-0.25, -0.75, 0.0),   # Left Shoulder
        (0.25, -0.75, 0.0),    # Right Shoulder
        (-0.5, -0.6, 0.0),     # Left Elbow
        (0.5, -0.6, 0.0),      # Right Elbow
        (-0.6, -0.3, 0.0),     # Left Wrist
        (0.6, -0.3, 0.0),      # Right Wrist
        (0, -0.55, 0.0),       # Waist
        (-0.2, -0.55, 0.0),    # Left Hip
        (0.2, -0.55, 0.0),     # Right Hip
        (-0.2, -0.1, 0.1),     # Left Knee
        (0.2, -0.1, 0.1),      # Right Knee
        (-0.15, 0.4, 0.0),     # Left Ankle
        (0.15, 0.4, 0.0)       # Right Ankle
    ]
    
    # Define 15 body points for sitting pose
    sitting_pose = [
        (0, -0.6, 0.2),        # Head
        (0, -0.4, 0.1),        # Neck
        (-0.25, -0.35, 0.0),   # Left Shoulder
        (0.25, -0.35, 0.0),    # Right Shoulder
        (-0.45, -0.1, 0.0),    # Left Elbow
        (0.45, -0.1, 0.0),     # Right Elbow
        (-0.5, 0.0, 0.0),      # Left Wrist
        (0.5, 0.0, 0.0),       # Right Wrist
        (0, -0.1, 0.0),        # Waist
        (-0.2, -0.1, -0.1),    # Left Hip
        (0.2, -0.1, -0.1),     # Right Hip
        (-0.35, 0.3, -0.1),    # Left Knee
        (0.35, 0.3, -0.1),     # Right Knee
        (-0.3, 0.4, 0.0),      # Left Ankle
        (0.3, 0.4, 0.0)        # Right Ankle
    ]
    
    # Projection function to 2D (orthographic with offset for z-depth)
    def project_to_2d(x, y, z):
        # Convert 3D coordinates to 2D screen coordinates
        screen_x = int(width/2 + (x - z * 0.3) * 200)  # x and z contribute to horizontal
        screen_y = int(height - (y - z) * 200)          # y and z contribute to vertical
        return (screen_x, screen_y)
    
    # Smoothstep interpolation function
    def smoothstep(t):
        return t * t * (3 - 2 * t)
    
    total_frames = 120
    frame_index = 0
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        t = frame_index / (total_frames - 1)
        eased_t = smoothstep(t)
        
        # Interpolate each point between standing and sitting poses
        current_pose = []
        for i in range(15):
            sx, sy, sz = standing_pose[i]
            ex, ey, ez = sitting_pose[i]
            x = sx + eased_t * (ex - sx)
            y = sy + eased_t * (ey - sy)
            z = sz + eased_t * (ez - sz)
            current_pose.append((x, y, z))
        
        # Draw everything
        screen.fill(BLACK)
        
        for point in current_pose:
            x, y, z = point
            screen_x, screen_y = project_to_2d(x, y, z)
            pygame.draw.circle(screen, WHITE, (screen_x, screen_y), 5)
        
        pygame.display.flip()
        clock.tick(30)
        
        # Update frame index (loop continuously)
        frame_index = (frame_index + 1) % total_frames
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
