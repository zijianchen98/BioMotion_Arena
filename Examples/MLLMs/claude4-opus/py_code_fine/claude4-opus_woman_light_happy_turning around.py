
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 30
POINT_RADIUS = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Woman Turning Around")
clock = pygame.time.Clock()

class Joint:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

class BioMotionFigure:
    def __init__(self):
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        self.angle = 0
        self.turn_speed = 0.05
        
        # Define 15 joint positions for a human figure (relative positions)
        self.base_joints = [
            Joint(0, -80),      # 0: head
            Joint(0, -50),      # 1: neck
            Joint(-15, -30),    # 2: left shoulder
            Joint(15, -30),     # 3: right shoulder
            Joint(-25, -5),     # 4: left elbow
            Joint(25, -5),      # 5: right elbow
            Joint(-30, 20),     # 6: left hand
            Joint(30, 20),      # 7: right hand
            Joint(0, -20),      # 8: spine/torso
            Joint(-8, 10),      # 9: left hip
            Joint(8, 10),       # 10: right hip
            Joint(-12, 50),     # 11: left knee
            Joint(12, 50),      # 12: right knee
            Joint(-10, 90),     # 13: left foot
            Joint(10, 90),      # 14: right foot
        ]
        
        self.joints = [Joint(0, 0) for _ in range(15)]
        
    def update(self):
        self.angle += self.turn_speed
        
        # Calculate depth effect as figure turns
        cos_angle = math.cos(self.angle)
        sin_angle = math.sin(self.angle)
        
        for i, base_joint in enumerate(self.base_joints):
            # Apply 3D rotation around Y-axis (turning)
            rotated_x = base_joint.x * cos_angle - base_joint.z * sin_angle
            rotated_z = base_joint.x * sin_angle + base_joint.z * cos_angle
            
            # Add natural walking motion for legs and arms
            if i in [4, 6]:  # left arm
                swing = math.sin(self.angle * 4) * 10
                rotated_x += swing
            elif i in [5, 7]:  # right arm
                swing = -math.sin(self.angle * 4) * 10
                rotated_x += swing
            elif i in [11, 13]:  # left leg
                swing = math.sin(self.angle * 3) * 5
                rotated_x += swing
            elif i in [12, 14]:  # right leg
                swing = -math.sin(self.angle * 3) * 5
                rotated_x += swing
            
            # Add slight up-down motion for natural movement
            bounce = math.sin(self.angle * 6) * 2
            
            # Apply perspective scaling based on depth
            scale_factor = max(0.3, 1 - abs(rotated_z) * 0.01)
            
            self.joints[i].x = self.center_x + rotated_x * scale_factor
            self.joints[i].y = self.center_y + (base_joint.y + bounce) * scale_factor
            self.joints[i].z = rotated_z
    
    def draw(self, surface):
        # Sort joints by depth (z-coordinate) for proper rendering
        joint_data = [(i, joint) for i, joint in enumerate(self.joints)]
        joint_data.sort(key=lambda x: x[1].z, reverse=True)
        
        for i, joint in joint_data:
            # Vary point size based on depth for 3D effect
            depth_factor = max(0.3, 1 - abs(joint.z) * 0.01)
            point_size = int(POINT_RADIUS * depth_factor)
            
            # Draw the point
            pygame.draw.circle(surface, WHITE, 
                             (int(joint.x), int(joint.y)), 
                             point_size)

# Create figure
figure = BioMotionFigure()

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
    figure.update()
    
    # Draw
    screen.fill(BLACK)
    figure.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
