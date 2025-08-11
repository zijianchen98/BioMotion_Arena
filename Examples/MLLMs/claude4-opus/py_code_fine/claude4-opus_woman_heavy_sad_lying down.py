
import pygame
import math
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 5

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Woman Lying Down")
clock = pygame.time.Clock()

class PointLightWalker:
    def __init__(self):
        self.frame = 0
        self.total_frames = 120
        
        # Define 15 joint positions for a lying down pose
        # Arranged as: head, neck, shoulders, elbows, wrists, torso, hips, knees, ankles
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder', 
            'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
            'torso', 'left_hip', 'right_hip', 'left_knee', 'right_knee',
            'left_ankle', 'right_ankle'
        ]
        
        # Base positions for lying down pose (horizontal orientation)
        self.base_positions = {
            'head': (WIDTH//2 + 120, HEIGHT//2 - 20),
            'neck': (WIDTH//2 + 100, HEIGHT//2 - 10),
            'left_shoulder': (WIDTH//2 + 80, HEIGHT//2 - 25),
            'right_shoulder': (WIDTH//2 + 80, HEIGHT//2 + 5),
            'left_elbow': (WIDTH//2 + 60, HEIGHT//2 - 45),
            'right_elbow': (WIDTH//2 + 60, HEIGHT//2 + 25),
            'left_wrist': (WIDTH//2 + 40, HEIGHT//2 - 55),
            'right_wrist': (WIDTH//2 + 40, HEIGHT//2 + 35),
            'torso': (WIDTH//2 + 40, HEIGHT//2 - 10),
            'left_hip': (WIDTH//2 - 20, HEIGHT//2 - 20),
            'right_hip': (WIDTH//2 - 20, HEIGHT//2),
            'left_knee': (WIDTH//2 - 60, HEIGHT//2 - 25),
            'right_knee': (WIDTH//2 - 60, HEIGHT//2 + 5),
            'left_ankle': (WIDTH//2 - 100, HEIGHT//2 - 30),
            'right_ankle': (WIDTH//2 - 100, HEIGHT//2 + 10)
        }
        
    def get_positions(self):
        positions = []
        
        # Calculate breathing and subtle movement
        breathing = math.sin(self.frame * 0.3) * 3
        slow_drift = math.sin(self.frame * 0.1) * 2
        head_drift = math.sin(self.frame * 0.05) * 1
        
        for joint_name in self.joint_names:
            base_x, base_y = self.base_positions[joint_name]
            
            # Add breathing motion (mainly torso and chest area)
            if joint_name in ['torso', 'left_shoulder', 'right_shoulder', 'neck']:
                y_offset = breathing * 0.5
            else:
                y_offset = breathing * 0.2
                
            # Add subtle random movement for sadness/fatigue
            if joint_name == 'head':
                # Occasional head movement
                head_sway = head_drift
                x = base_x + head_sway + slow_drift * 0.3
                y = base_y + y_offset + math.sin(self.frame * 0.08) * 1
            elif joint_name in ['left_wrist', 'right_wrist']:
                # Slight hand tremor/movement
                tremor = math.sin(self.frame * 0.4 + hash(joint_name) % 100) * 0.8
                x = base_x + tremor + slow_drift * 0.2
                y = base_y + y_offset + tremor * 0.5
            elif joint_name in ['left_ankle', 'right_ankle']:
                # Minimal foot movement
                x = base_x + slow_drift * 0.1
                y = base_y + y_offset + math.sin(self.frame * 0.15) * 0.5
            else:
                # General body sway
                x = base_x + slow_drift * 0.3
                y = base_y + y_offset
            
            positions.append((int(x), int(y)))
            
        return positions
    
    def update(self):
        self.frame = (self.frame + 1) % self.total_frames

def main():
    walker = PointLightWalker()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(BLACK)
        
        # Get current joint positions
        positions = walker.get_positions()
        
        # Draw points
        for pos in positions:
            pygame.draw.circle(screen, WHITE, pos, POINT_RADIUS)
        
        # Update animation
        walker.update()
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
