
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 8

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sitting Down")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, joint_name):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.joint_name = joint_name

# Define the 15 point-lights for human figure (standing position)
def create_initial_points():
    center_x, center_y = WIDTH // 2, HEIGHT // 2 - 50
    
    points = [
        PointLight(center_x, center_y - 120, "head"),
        PointLight(center_x, center_y - 80, "neck"),
        PointLight(center_x - 30, center_y - 60, "left_shoulder"),
        PointLight(center_x + 30, center_y - 60, "right_shoulder"),
        PointLight(center_x - 50, center_y - 20, "left_elbow"),
        PointLight(center_x + 50, center_y - 20, "right_elbow"),
        PointLight(center_x - 60, center_y + 20, "left_wrist"),
        PointLight(center_x + 60, center_y + 20, "right_wrist"),
        PointLight(center_x, center_y - 40, "spine"),
        PointLight(center_x, center_y + 20, "hip_center"),
        PointLight(center_x - 20, center_y + 20, "left_hip"),
        PointLight(center_x + 20, center_y + 20, "right_hip"),
        PointLight(center_x - 25, center_y + 80, "left_knee"),
        PointLight(center_x + 25, center_y + 80, "right_knee"),
        PointLight(center_x - 30, center_y + 140, "left_ankle"),
        PointLight(center_x + 30, center_y + 140, "right_ankle")
    ]
    return points

def animate_sitting_motion(points, frame):
    # Animation duration in frames
    total_frames = 180
    
    # Normalize frame to 0-1 range
    t = min(frame / total_frames, 1.0)
    
    # Easing function for smooth motion
    ease_t = 0.5 * (1 - math.cos(t * math.pi))
    
    center_x, center_y = WIDTH // 2, HEIGHT // 2 - 50
    
    # Define target positions for sitting
    sitting_positions = {
        "head": (center_x, center_y - 80),
        "neck": (center_x, center_y - 40),
        "left_shoulder": (center_x - 30, center_y - 20),
        "right_shoulder": (center_x + 30, center_y - 20),
        "left_elbow": (center_x - 45, center_y + 10),
        "right_elbow": (center_x + 45, center_y + 10),
        "left_wrist": (center_x - 50, center_y + 40),
        "right_wrist": (center_x + 50, center_y + 40),
        "spine": (center_x, center_y),
        "hip_center": (center_x, center_y + 60),
        "left_hip": (center_x - 20, center_y + 60),
        "right_hip": (center_x + 20, center_y + 60),
        "left_knee": (center_x - 25, center_y + 80),
        "right_knee": (center_x + 25, center_y + 80),
        "left_ankle": (center_x - 25, center_y + 90),
        "right_ankle": (center_x + 25, center_y + 90)
    }
    
    # Interpolate between starting and sitting positions
    for point in points:
        if point.joint_name in sitting_positions:
            target_x, target_y = sitting_positions[point.joint_name]
            point.x = point.start_x + (target_x - point.start_x) * ease_t
            point.y = point.start_y + (target_y - point.start_y) * ease_t

def main():
    points = create_initial_points()
    frame = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    frame = 0  # Reset animation
        
        # Clear screen
        screen.fill(BLACK)
        
        # Animate the sitting motion
        animate_sitting_motion(points, frame)
        
        # Draw point-lights
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), POINT_RADIUS)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
        
        # Increment frame counter
        frame += 1
        
        # Loop animation after completion
        if frame > 240:  # Add some pause at the end
            frame = 0
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
