import pygame
import sys

# Define the 15 keypoints for a standing pose (x, y)
# Order: [head, chest, pelvis,
#         L_shoulder, L_elbow, L_wrist,
#         R_shoulder, R_elbow, R_wrist,
#         L_hip, L_knee, L_ankle,
#         R_hip, R_knee, R_ankle]
standing_points = [
    (0, -50),   # head
    (0, -30),   # chest
    (0, -10),   # pelvis
    (-10, -30), # L_shoulder
    (-15, -20), # L_elbow
    (-15, -10), # L_wrist
    (10, -30),  # R_shoulder
    (15, -20),  # R_elbow
    (15, -10),  # R_wrist
    (-5, -10),  # L_hip
    (-5, 0),    # L_knee
    (-5, 10),   # L_ankle
    (5, -10),   # R_hip
    (5, 0),     # R_knee
    (5, 10)     # R_ankle
]

# Define the 15 keypoints for a lying-down pose
lying_points = [
    (-50, 0),   # head
    (-30, 0),   # chest
    (-10, 0),   # pelvis
    (-30, -10), # L_shoulder
    (-20, -15), # L_elbow
    (-10, -15), # L_wrist
    (-30, 10),  # R_shoulder
    (-20, 15),  # R_elbow
    (-10, 15),  # R_wrist
    (-10, -5),  # L_hip
    (0, -5),    # L_knee
    (10, -5),   # L_ankle
    (-10, 5),   # R_hip
    (0, 5),     # R_knee
    (10, 5)     # R_ankle
]

def interpolate_points(p1, p2, alpha):
    """Linear interpolation between two points p1 and p2."""
    return (p1[0] + alpha * (p2[0] - p1[0]),
            p1[1] + alpha * (p2[1] - p1[1]))

def main():
    pygame.init()
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Biological Motion: Lying Down")
    clock = pygame.time.Clock()
    
    # Number of frames to transition from standing to lying
    total_frames = 120
    frame_count = 0
    
    running = True
    while running:
        clock.tick(30)  # 30 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen (black background)
        screen.fill((0, 0, 0))
        
        # Compute interpolation alpha from 0.0 to 1.0
        alpha = min(frame_count / float(total_frames - 1), 1.0)
        
        # Interpolate each point between standing_points and lying_points
        current_points = [
            interpolate_points(standing_points[i], lying_points[i], alpha)
            for i in range(15)
        ]
        
        # Draw 15 white circles at each of the current_points
        center_x, center_y = screen_width // 2, screen_height // 2
        for (x, y) in current_points:
            px = int(center_x + x)
            py = int(center_y + y)
            pygame.draw.circle(screen, (255, 255, 255), (px, py), 5)
        
        pygame.display.flip()
        
        # Increment frame counter until the animation stops or finishes
        if frame_count < total_frames - 1:
            frame_count += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()