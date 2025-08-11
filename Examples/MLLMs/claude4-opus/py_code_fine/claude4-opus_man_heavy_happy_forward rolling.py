
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 4

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Forward Rolling")
clock = pygame.time.Clock()

class PointLightFigure:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.angle = 0
        self.roll_distance = 0
        self.body_height = 120
        self.body_width = 40
        
        # Define 15 joint positions relative to center
        # Head, shoulders, elbows, wrists, torso, hips, knees, ankles, feet
        self.joints = {
            'head': (0, -self.body_height//2),
            'left_shoulder': (-self.body_width//3, -self.body_height//3),
            'right_shoulder': (self.body_width//3, -self.body_height//3),
            'left_elbow': (-self.body_width//2, -self.body_height//6),
            'right_elbow': (self.body_width//2, -self.body_height//6),
            'left_wrist': (-self.body_width//1.5, 0),
            'right_wrist': (self.body_width//1.5, 0),
            'torso_upper': (0, -self.body_height//6),
            'torso_middle': (0, 0),
            'torso_lower': (0, self.body_height//6),
            'left_hip': (-self.body_width//4, self.body_height//4),
            'right_hip': (self.body_width//4, self.body_height//4),
            'left_knee': (-self.body_width//3, self.body_height//2),
            'right_knee': (self.body_width//3, self.body_height//2),
            'left_ankle': (-self.body_width//4, self.body_height//1.5)
        }
        
    def update(self, time):
        # Rolling motion parameters
        roll_speed = 0.1
        self.angle += roll_speed
        self.roll_distance += 2
        
        # Reset position when rolling off screen
        if self.roll_distance > WIDTH + 100:
            self.roll_distance = -100
            
        # Calculate current center position
        current_center_x = self.roll_distance
        current_center_y = self.center_y
        
        # Update joint positions with rolling transformation
        self.current_positions = {}
        
        for joint_name, (rel_x, rel_y) in self.joints.items():
            # Apply rotation for rolling motion
            rotated_x = rel_x * math.cos(self.angle) - rel_y * math.sin(self.angle)
            rotated_y = rel_x * math.sin(self.angle) + rel_y * math.cos(self.angle)
            
            # Add some dynamic motion for realism
            wave_offset = math.sin(time * 0.05 + hash(joint_name) % 10) * 2
            
            # Final position
            final_x = current_center_x + rotated_x
            final_y = current_center_y + rotated_y + wave_offset
            
            self.current_positions[joint_name] = (int(final_x), int(final_y))
    
    def draw(self, surface):
        for pos in self.current_positions.values():
            if 0 <= pos[0] <= WIDTH and 0 <= pos[1] <= HEIGHT:
                pygame.draw.circle(surface, WHITE, pos, POINT_RADIUS)

def main():
    figure = PointLightFigure(WIDTH // 4, HEIGHT // 2)
    running = True
    time = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update
        time += 1
        figure.update(time)
        
        # Draw
        screen.fill(BLACK)
        figure.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
