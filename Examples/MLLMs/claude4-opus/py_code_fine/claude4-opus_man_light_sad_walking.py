
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30
POINT_SIZE = 8

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Walking")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.name = name

def create_walker_points():
    """Create 15 point-lights representing key body joints for walking animation"""
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    
    points = [
        PointLight(center_x, center_y - 120, "head"),
        PointLight(center_x, center_y - 100, "neck"),
        PointLight(center_x - 40, center_y - 80, "left_shoulder"),
        PointLight(center_x + 40, center_y - 80, "right_shoulder"),
        PointLight(center_x - 60, center_y - 40, "left_elbow"),
        PointLight(center_x + 60, center_y - 40, "right_elbow"),
        PointLight(center_x - 80, center_y, "left_hand"),
        PointLight(center_x + 80, center_y, "right_hand"),
        PointLight(center_x, center_y - 60, "torso"),
        PointLight(center_x, center_y, "hip"),
        PointLight(center_x - 20, center_y + 40, "left_knee"),
        PointLight(center_x + 20, center_y + 40, "right_knee"),
        PointLight(center_x - 40, center_y + 80, "left_ankle"),
        PointLight(center_x + 40, center_y + 80, "right_ankle"),
        PointLight(center_x, center_y + 100, "center_foot")
    ]
    
    return points

def update_walking_motion(points, frame):
    """Update point positions for walking motion with sad/tired characteristics"""
    t = frame * 0.1
    
    # Slower, more labored walking cycle
    walk_cycle = math.sin(t * 0.8) 
    step_phase = math.sin(t * 1.6)
    
    # Sad posture adjustments
    head_droop = 15
    shoulder_sag = 10
    reduced_arm_swing = 0.6
    
    for point in points:
        if point.name == "head":
            point.x = point.base_x + math.sin(t * 0.5) * 2
            point.y = point.base_y + head_droop + math.sin(t * 0.3) * 3
            
        elif point.name == "neck":
            point.x = point.base_x + math.sin(t * 0.5) * 1.5
            point.y = point.base_y + head_droop * 0.7
            
        elif point.name == "left_shoulder":
            point.x = point.base_x - shoulder_sag + walk_cycle * 8
            point.y = point.base_y + shoulder_sag + math.sin(t * 0.8) * 3
            
        elif point.name == "right_shoulder":
            point.x = point.base_x + shoulder_sag - walk_cycle * 8
            point.y = point.base_y + shoulder_sag + math.sin(t * 0.8 + math.pi) * 3
            
        elif point.name == "left_elbow":
            arm_swing = math.sin(t * 0.8) * 25 * reduced_arm_swing
            point.x = point.base_x + arm_swing
            point.y = point.base_y + shoulder_sag * 0.5
            
        elif point.name == "right_elbow":
            arm_swing = math.sin(t * 0.8 + math.pi) * 25 * reduced_arm_swing
            point.x = point.base_x + arm_swing
            point.y = point.base_y + shoulder_sag * 0.5
            
        elif point.name == "left_hand":
            hand_swing = math.sin(t * 0.8) * 35 * reduced_arm_swing
            point.x = point.base_x + hand_swing
            point.y = point.base_y + shoulder_sag * 0.3
            
        elif point.name == "right_hand":
            hand_swing = math.sin(t * 0.8 + math.pi) * 35 * reduced_arm_swing
            point.x = point.base_x + hand_swing
            point.y = point.base_y + shoulder_sag * 0.3
            
        elif point.name == "torso":
            point.x = point.base_x + walk_cycle * 3
            point.y = point.base_y + math.sin(t * 1.6) * 2 + shoulder_sag * 0.3
            
        elif point.name == "hip":
            point.x = point.base_x + walk_cycle * 4
            point.y = point.base_y + math.sin(t * 1.6) * 3
            
        elif point.name == "left_knee":
            knee_bend = max(0, math.sin(t * 0.8) * 20)
            point.x = point.base_x - 10 + walk_cycle * 6
            point.y = point.base_y - knee_bend + math.sin(t * 1.6) * 2
            
        elif point.name == "right_knee":
            knee_bend = max(0, math.sin(t * 0.8 + math.pi) * 20)
            point.x = point.base_x + 10 + walk_cycle * 6
            point.y = point.base_y - knee_bend + math.sin(t * 1.6) * 2
            
        elif point.name == "left_ankle":
            step_height = max(0, math.sin(t * 0.8) * 15)
            point.x = point.base_x - 20 + walk_cycle * 8
            point.y = point.base_y - step_height
            
        elif point.name == "right_ankle":
            step_height = max(0, math.sin(t * 0.8 + math.pi) * 15)
            point.x = point.base_x + 20 + walk_cycle * 8
            point.y = point.base_y - step_height
            
        elif point.name == "center_foot":
            point.x = point.base_x + walk_cycle * 5
            point.y = point.base_y + math.sin(t * 1.6) * 1

def main():
    points = create_walker_points()
    frame = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Clear screen
        screen.fill(BLACK)
        
        # Update motion
        update_walking_motion(points, frame)
        
        # Draw point lights
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), POINT_SIZE)
        
        pygame.display.flip()
        clock.tick(FPS)
        frame += 1
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
