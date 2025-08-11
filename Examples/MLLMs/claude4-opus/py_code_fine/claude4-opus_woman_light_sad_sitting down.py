
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for frame rate
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, joint_name):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.joint_name = joint_name

# Define the 15 body joints for biological motion
def create_body_points():
    # Starting position (standing)
    center_x = WIDTH // 2
    center_y = HEIGHT // 2 - 50
    
    points = [
        PointLight(center_x, center_y - 120, "head"),
        PointLight(center_x, center_y - 80, "neck"),
        PointLight(center_x - 30, center_y - 60, "left_shoulder"),
        PointLight(center_x + 30, center_y - 60, "right_shoulder"),
        PointLight(center_x - 45, center_y - 20, "left_elbow"),
        PointLight(center_x + 45, center_y - 20, "right_elbow"),
        PointLight(center_x - 55, center_y + 20, "left_hand"),
        PointLight(center_x + 55, center_y + 20, "right_hand"),
        PointLight(center_x, center_y - 40, "torso_upper"),
        PointLight(center_x, center_y + 20, "torso_lower"),
        PointLight(center_x - 15, center_y + 40, "left_hip"),
        PointLight(center_x + 15, center_y + 40, "right_hip"),
        PointLight(center_x - 20, center_y + 100, "left_knee"),
        PointLight(center_x + 20, center_y + 100, "right_knee"),
        PointLight(center_x - 25, center_y + 160, "left_foot"),
        PointLight(center_x + 25, center_y + 160, "right_foot")
    ]
    return points

def animate_sitting_motion(points, frame):
    # Animation parameters
    total_frames = 120
    progress = min(frame / total_frames, 1.0)
    
    # Smooth easing function
    ease_progress = 0.5 * (1 - math.cos(progress * math.pi))
    
    center_x = WIDTH // 2
    center_y = HEIGHT // 2 - 50
    
    # Define target positions for sitting
    sitting_positions = {
        "head": (center_x, center_y - 80),
        "neck": (center_x, center_y - 40),
        "left_shoulder": (center_x - 25, center_y - 20),
        "right_shoulder": (center_x + 25, center_y - 20),
        "left_elbow": (center_x - 35, center_y + 10),
        "right_elbow": (center_x + 35, center_y + 10),
        "left_hand": (center_x - 40, center_y + 40),
        "right_hand": (center_x + 40, center_y + 40),
        "torso_upper": (center_x, center_y),
        "torso_lower": (center_x, center_y + 40),
        "left_hip": (center_x - 15, center_y + 60),
        "right_hip": (center_x + 15, center_y + 60),
        "left_knee": (center_x - 20, center_y + 80),
        "right_knee": (center_x + 20, center_y + 80),
        "left_foot": (center_x - 25, center_y + 90),
        "right_foot": (center_x + 25, center_y + 90)
    }
    
    # Interpolate between starting and sitting positions
    for point in points:
        start_x, start_y = point.start_x, point.start_y
        target_x, target_y = sitting_positions[point.joint_name]
        
        point.x = start_x + (target_x - start_x) * ease_progress
        point.y = start_y + (target_y - start_y) * ease_progress

def main():
    points = create_body_points()
    frame = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset animation
                    frame = 0
        
        # Clear screen
        screen.fill(BLACK)
        
        # Animate the sitting motion
        animate_sitting_motion(points, frame)
        
        # Draw all points
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), 4)
        
        # Update frame
        frame += 1
        if frame > 240:  # Reset after full cycle
            frame = 0
        
        pygame.display.flip()
        clock.tick(30)  # 30 FPS

if __name__ == "__main__":
    main()
