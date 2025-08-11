
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Walking Woman")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 60
clock = pygame.time.Clock()

class PointLightWalker:
    def __init__(self):
        # 15 key joint positions for biological motion
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder',
            'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
            'torso', 'left_hip', 'right_hip', 'left_knee', 'right_knee',
            'left_ankle', 'right_ankle'
        ]
        
        # Base positions (normalized, will be scaled)
        self.base_positions = {
            'head': (0, -0.45),
            'neck': (0, -0.35),
            'left_shoulder': (-0.08, -0.3),
            'right_shoulder': (0.08, -0.3),
            'left_elbow': (-0.12, -0.15),
            'right_elbow': (0.12, -0.15),
            'left_wrist': (-0.15, 0),
            'right_wrist': (0.15, 0),
            'torso': (0, -0.1),
            'left_hip': (-0.05, 0.05),
            'right_hip': (0.05, 0.05),
            'left_knee': (-0.06, 0.25),
            'right_knee': (0.06, 0.25),
            'left_ankle': (-0.04, 0.45),
            'right_ankle': (0.04, 0.45)
        }
        
        self.scale = 200
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        self.frame = 0
        self.walking_speed = 0.1
        
    def get_walking_motion(self, frame):
        positions = {}
        t = frame * self.walking_speed
        
        # Walking cycle parameters
        step_cycle = math.sin(t)
        step_cycle_offset = math.sin(t + math.pi)
        
        # Head bob
        head_bob = 0.02 * math.sin(t * 2)
        
        # Arm swing (opposite to legs)
        left_arm_swing = 0.05 * math.sin(t + math.pi)
        right_arm_swing = 0.05 * math.sin(t)
        
        # Leg movement
        left_leg_forward = 0.04 * step_cycle
        right_leg_forward = 0.04 * step_cycle_offset
        
        left_knee_bend = max(0, 0.03 * step_cycle)
        right_knee_bend = max(0, 0.03 * step_cycle_offset)
        
        # Apply movements to base positions
        for joint in self.joint_names:
            x, y = self.base_positions[joint]
            
            # Head movements
            if joint == 'head':
                y += head_bob
            elif joint == 'neck':
                y += head_bob * 0.5
                
            # Arm movements
            elif 'left' in joint and ('shoulder' in joint or 'elbow' in joint or 'wrist' in joint):
                if 'elbow' in joint:
                    x += left_arm_swing * 0.8
                    y += abs(left_arm_swing) * 0.3
                elif 'wrist' in joint:
                    x += left_arm_swing
                    y += abs(left_arm_swing) * 0.5
                    
            elif 'right' in joint and ('shoulder' in joint or 'elbow' in joint or 'wrist' in joint):
                if 'elbow' in joint:
                    x += right_arm_swing * 0.8
                    y += abs(right_arm_swing) * 0.3
                elif 'wrist' in joint:
                    x += right_arm_swing
                    y += abs(right_arm_swing) * 0.5
                    
            # Leg movements
            elif joint == 'left_hip':
                x += left_leg_forward * 0.3
            elif joint == 'right_hip':
                x += right_leg_forward * 0.3
            elif joint == 'left_knee':
                x += left_leg_forward
                y += left_knee_bend
            elif joint == 'right_knee':
                x += right_leg_forward
                y += right_knee_bend
            elif joint == 'left_ankle':
                x += left_leg_forward * 1.5
                if step_cycle > 0:  # Foot lift
                    y -= 0.02 * step_cycle
            elif joint == 'right_ankle':
                x += right_leg_forward * 1.5
                if step_cycle_offset > 0:  # Foot lift
                    y -= 0.02 * step_cycle_offset
                    
            # Torso slight movement
            elif joint == 'torso':
                x += (left_leg_forward + right_leg_forward) * 0.1
                y += head_bob * 0.3
                
            positions[joint] = (
                self.center_x + x * self.scale,
                self.center_y + y * self.scale
            )
            
        return positions
    
    def draw(self, screen, frame):
        positions = self.get_walking_motion(frame)
        
        # Draw all 15 point lights
        for joint in self.joint_names:
            x, y = positions[joint]
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 4)

def main():
    walker = PointLightWalker()
    frame = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill(BLACK)
        walker.draw(screen, frame)
        
        pygame.display.flip()
        clock.tick(FPS)
        frame += 1
        
    pygame.quit()

if __name__ == "__main__":
    main()
