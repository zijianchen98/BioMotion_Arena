
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 4

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Man Turning Around")
clock = pygame.time.Clock()

class PointLightWalker:
    def __init__(self):
        # Define 15 body joints for point-light display
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder', 'left_elbow', 
            'right_elbow', 'left_wrist', 'right_wrist', 'torso', 'left_hip', 
            'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle'
        ]
        
        # Base positions (normalized, will be scaled)
        self.base_positions = {
            'head': (0, -0.9),
            'neck': (0, -0.7),
            'left_shoulder': (-0.15, -0.65),
            'right_shoulder': (0.15, -0.65),
            'left_elbow': (-0.25, -0.4),
            'right_elbow': (0.25, -0.4),
            'left_wrist': (-0.3, -0.15),
            'right_wrist': (0.3, -0.15),
            'torso': (0, -0.3),
            'left_hip': (-0.1, 0.0),
            'right_hip': (0.1, 0.0),
            'left_knee': (-0.12, 0.35),
            'right_knee': (0.12, 0.35),
            'left_ankle': (-0.1, 0.7),
            'right_ankle': (0.1, 0.7)
        }
        
        self.scale = 200
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.angle = 0
        self.time = 0
        
    def get_sad_heavy_modifications(self, t):
        """Apply sad, heavy movement characteristics"""
        # Sad posture: head down, shoulders drooped, slower movements
        modifications = {}
        
        # Head slightly down
        modifications['head'] = (0, 0.05)
        modifications['neck'] = (0, 0.03)
        
        # Drooped shoulders
        modifications['left_shoulder'] = (0, 0.08)
        modifications['right_shoulder'] = (0, 0.08)
        
        # Arms hanging lower, less swing
        arm_swing = 0.03 * math.sin(t * 0.5)
        modifications['left_elbow'] = (-0.05 + arm_swing, 0.1)
        modifications['right_elbow'] = (0.05 - arm_swing, 0.1)
        modifications['left_wrist'] = (-0.03 + arm_swing * 0.8, 0.15)
        modifications['right_wrist'] = (0.03 - arm_swing * 0.8, 0.15)
        
        # Torso slightly forward
        modifications['torso'] = (0, 0.05)
        
        # Heavy, slow leg movement
        leg_lift = 0.02 * abs(math.sin(t * 0.3))
        modifications['left_knee'] = (-0.02, -leg_lift)
        modifications['right_knee'] = (0.02, leg_lift * 0.5)
        modifications['left_ankle'] = (-0.01, -leg_lift * 0.5)
        modifications['right_ankle'] = (0.01, leg_lift * 0.3)
        
        return modifications
    
    def get_turning_rotation(self, t):
        """Calculate rotation for turning around motion"""
        # Slow, continuous turn
        return t * 0.02  # Slow rotation speed
    
    def get_positions(self):
        """Get current positions of all joints"""
        positions = []
        
        # Get sad/heavy modifications
        sad_mods = self.get_sad_heavy_modifications(self.time)
        
        # Get turning rotation
        turn_angle = self.get_turning_rotation(self.time)
        
        for joint in self.joint_names:
            # Base position
            base_x, base_y = self.base_positions[joint]
            
            # Apply sad/heavy modifications
            if joint in sad_mods:
                mod_x, mod_y = sad_mods[joint]
                base_x += mod_x
                base_y += mod_y
            
            # Apply turning rotation
            rotated_x = base_x * math.cos(turn_angle) - base_y * math.sin(turn_angle) * 0.3
            rotated_y = base_y
            
            # Scale and position
            screen_x = self.center_x + rotated_x * self.scale
            screen_y = self.center_y + rotated_y * self.scale
            
            positions.append((screen_x, screen_y))
        
        return positions
    
    def update(self, dt):
        """Update animation"""
        self.time += dt

def main():
    walker = PointLightWalker()
    running = True
    
    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update walker
        walker.update(dt)
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw point lights
        positions = walker.get_positions()
        for pos in positions:
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)
        
        # Update display
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
