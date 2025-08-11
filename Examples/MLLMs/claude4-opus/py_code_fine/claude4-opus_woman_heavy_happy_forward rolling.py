
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30
POINT_RADIUS = 8

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Forward Rolling")
clock = pygame.time.Clock()

class PointLightWoman:
    def __init__(self):
        # 15 key body points for biological motion
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder',
            'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
            'torso', 'left_hip', 'right_hip',
            'left_knee', 'right_knee', 'left_ankle', 'right_ankle'
        ]
        
        # Initial positions relative to center (scaled for heavier build)
        self.base_positions = {
            'head': (0, -80),
            'neck': (0, -60),
            'left_shoulder': (-25, -50),
            'right_shoulder': (25, -50),
            'left_elbow': (-40, -25),
            'right_elbow': (40, -25),
            'left_wrist': (-50, 0),
            'right_wrist': (50, 0),
            'torso': (0, -20),
            'left_hip': (-20, 10),
            'right_hip': (20, 10),
            'left_knee': (-25, 50),
            'right_knee': (25, 50),
            'left_ankle': (-30, 80),
            'right_ankle': (30, 80)
        }
        
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        self.roll_angle = 0
        self.roll_speed = 0.15
        self.horizontal_speed = 2.0
        self.phase = 0
        
    def get_rolling_positions(self):
        positions = []
        
        # Rolling motion involves rotation around changing centers
        roll_radius = 90
        
        # Calculate center of rotation (moves forward during roll)
        roll_center_x = self.center_x + math.sin(self.roll_angle) * 20
        roll_center_y = self.center_y + roll_radius
        
        for joint in self.joint_names:
            base_x, base_y = self.base_positions[joint]
            
            # Apply rolling rotation
            cos_roll = math.cos(self.roll_angle)
            sin_roll = math.sin(self.roll_angle)
            
            # Rotate around rolling center
            rotated_x = base_x * cos_roll - base_y * sin_roll
            rotated_y = base_x * sin_roll + base_y * cos_roll
            
            # Add some organic deformation during roll
            compression = 1.0 + 0.3 * math.sin(self.roll_angle * 2)
            stretch_factor = math.cos(self.roll_angle) * 0.2
            
            # Apply compression/stretch
            if joint in ['torso', 'left_hip', 'right_hip']:
                rotated_y *= compression
            
            # Add limb flexion during roll
            limb_flex = 0
            if joint in ['left_elbow', 'right_elbow']:
                limb_flex = math.sin(self.roll_angle + math.pi/4) * 15
                rotated_x += limb_flex * (1 if 'left' in joint else -1)
            
            if joint in ['left_knee', 'right_knee']:
                limb_flex = math.sin(self.roll_angle + math.pi/2) * 20
                rotated_x += limb_flex * (1 if 'left' in joint else -1)
                rotated_y -= abs(limb_flex)
            
            # Final position
            final_x = roll_center_x + rotated_x
            final_y = roll_center_y + rotated_y
            
            # Add slight secondary motion for realism
            wobble_x = math.sin(self.phase + hash(joint) % 100) * 2
            wobble_y = math.cos(self.phase * 1.2 + hash(joint) % 100) * 1
            
            positions.append((
                final_x + wobble_x,
                final_y + wobble_y
            ))
        
        return positions
    
    def update(self):
        # Update rolling motion
        self.roll_angle += self.roll_speed
        self.center_x += self.horizontal_speed
        self.phase += 0.2
        
        # Reset position when off screen
        if self.center_x > WIDTH + 100:
            self.center_x = -100
            
        # Keep vertical position roughly centered
        target_y = HEIGHT // 2
        self.center_y += (target_y - self.center_y) * 0.02

def main():
    woman = PointLightWoman()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update
        woman.update()
        
        # Draw
        screen.fill(BLACK)
        
        # Get current positions and draw points
        positions = woman.get_rolling_positions()
        for pos in positions:
            x, y = pos
            if 0 <= x <= WIDTH and 0 <= y <= HEIGHT:
                pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
