
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Heavy Walking")
clock = pygame.time.Clock()

class PointLightWalker:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.frame = 0
        self.walking_speed = 0.8  # Slower for heavy walking
        
        # Define 15 joint positions (head, torso, arms, legs)
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder',
            'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
            'spine', 'left_hip', 'right_hip',
            'left_knee', 'right_knee', 'left_ankle', 'right_ankle'
        ]
        
        # Base positions relative to center
        self.base_positions = {
            'head': (0, -80),
            'neck': (0, -60),
            'left_shoulder': (-20, -50),
            'right_shoulder': (20, -50),
            'left_elbow': (-35, -20),
            'right_elbow': (35, -20),
            'left_wrist': (-40, 10),
            'right_wrist': (40, 10),
            'spine': (0, -20),
            'left_hip': (-15, 20),
            'right_hip': (15, 20),
            'left_knee': (-18, 60),
            'right_knee': (18, 60),
            'left_ankle': (-20, 100),
            'right_ankle': (20, 100)
        }
        
    def get_walking_motion(self, t):
        # Heavy walking characteristics
        cycle = t * self.walking_speed
        
        # Vertical bob (more pronounced for heavy walking)
        vertical_bob = 8 * math.sin(cycle * 2)
        
        # Lateral sway (side-to-side motion)
        lateral_sway = 5 * math.sin(cycle)
        
        # Arm swing (less pronounced for heavy walking)
        left_arm_swing = 15 * math.sin(cycle)
        right_arm_swing = -15 * math.sin(cycle)
        
        # Leg motion (alternating steps)
        left_leg_phase = math.sin(cycle)
        right_leg_phase = math.sin(cycle + math.pi)
        
        # Hip motion
        hip_rotation = 3 * math.sin(cycle)
        
        motions = {
            'head': (lateral_sway * 0.3, vertical_bob * 0.8),
            'neck': (lateral_sway * 0.4, vertical_bob * 0.9),
            'left_shoulder': (lateral_sway * 0.6 + left_arm_swing * 0.3, vertical_bob),
            'right_shoulder': (lateral_sway * 0.6 + right_arm_swing * 0.3, vertical_bob),
            'left_elbow': (lateral_sway * 0.4 + left_arm_swing * 0.8, vertical_bob * 0.7),
            'right_elbow': (lateral_sway * 0.4 + right_arm_swing * 0.8, vertical_bob * 0.7),
            'left_wrist': (lateral_sway * 0.2 + left_arm_swing * 1.2, vertical_bob * 0.5),
            'right_wrist': (lateral_sway * 0.2 + right_arm_swing * 1.2, vertical_bob * 0.5),
            'spine': (lateral_sway, vertical_bob),
            'left_hip': (lateral_sway + hip_rotation, vertical_bob * 1.1),
            'right_hip': (lateral_sway - hip_rotation, vertical_bob * 1.1),
            'left_knee': (lateral_sway + left_leg_phase * 12, vertical_bob + abs(left_leg_phase) * 15),
            'right_knee': (lateral_sway + right_leg_phase * 12, vertical_bob + abs(right_leg_phase) * 15),
            'left_ankle': (lateral_sway + left_leg_phase * 20, vertical_bob + abs(left_leg_phase) * 8),
            'right_ankle': (lateral_sway + right_leg_phase * 20, vertical_bob + abs(right_leg_phase) * 8)
        }
        
        return motions
    
    def get_joint_positions(self):
        t = self.frame * 0.1
        motions = self.get_walking_motion(t)
        
        positions = []
        for joint in self.joint_names:
            base_x, base_y = self.base_positions[joint]
            motion_x, motion_y = motions[joint]
            
            final_x = self.center_x + base_x + motion_x
            final_y = self.center_y + base_y + motion_y
            
            positions.append((int(final_x), int(final_y)))
        
        return positions
    
    def update(self):
        self.frame += 1

# Create walker
walker = PointLightWalker(WIDTH // 2, HEIGHT // 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Update
    walker.update()
    
    # Draw
    screen.fill(BLACK)
    
    # Get joint positions and draw points
    positions = walker.get_joint_positions()
    for pos in positions:
        pygame.draw.circle(screen, WHITE, pos, 4)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
