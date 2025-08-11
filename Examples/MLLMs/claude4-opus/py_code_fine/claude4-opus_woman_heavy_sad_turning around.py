
import pygame
import math
import sys

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
pygame.display.set_caption("Biological Motion - Sad Woman Turning Around")
clock = pygame.time.Clock()

class Joint:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.screen_x = 0
        self.screen_y = 0
    
    def project_to_screen(self, center_x, center_y):
        # Simple perspective projection
        scale = 300 / (300 + self.z)
        self.screen_x = center_x + self.x * scale
        self.screen_y = center_y + self.y * scale

class BiologicalMotion:
    def __init__(self):
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2 - 50
        self.time = 0
        self.turning_speed = 0.02  # Slow turning for sad, heavy movement
        
        # Define 15 key joints for human figure
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder',
            'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
            'spine', 'left_hip', 'right_hip',
            'left_knee', 'right_knee', 'left_ankle', 'right_ankle'
        ]
        
        # Base positions (front-facing)
        self.base_positions = {
            'head': (0, -120),
            'neck': (0, -100),
            'left_shoulder': (-25, -85),
            'right_shoulder': (25, -85),
            'left_elbow': (-35, -50),
            'right_elbow': (35, -50),
            'left_wrist': (-30, -15),
            'right_wrist': (30, -15),
            'spine': (0, -40),
            'left_hip': (-15, 0),
            'right_hip': (15, 0),
            'left_knee': (-18, 50),
            'right_knee': (18, 50),
            'left_ankle': (-15, 100),
            'right_ankle': (15, 100)
        }
        
        self.joints = {}
        for name in self.joint_names:
            x, y = self.base_positions[name]
            self.joints[name] = Joint(x, y)
    
    def update_pose(self):
        angle = self.time * self.turning_speed
        
        # Rotation matrix for Y-axis (turning around)
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        
        for name in self.joint_names:
            base_x, base_y = self.base_positions[name]
            
            # Add subtle swaying and drooping for sad, heavy movement
            sway_offset = math.sin(self.time * 0.01) * 3
            droop_factor = 1 + math.sin(self.time * 0.008) * 0.02
            
            # Apply sad posture modifications
            if 'shoulder' in name:
                base_y += 5  # Dropped shoulders
                base_x *= 0.9  # Narrower stance
            elif name == 'head':
                base_y += 8  # Head slightly down
                base_x += sway_offset * 0.5
            elif 'elbow' in name or 'wrist' in name:
                base_y += 10  # Arms hang lower
            
            # Apply heavy, slow movement
            base_y *= droop_factor
            base_x += sway_offset
            
            # 3D rotation (turning around)
            rotated_x = base_x * cos_a
            rotated_z = base_x * sin_a
            
            self.joints[name].x = rotated_x
            self.joints[name].y = base_y
            self.joints[name].z = rotated_z
            
            # Project to screen
            self.joints[name].project_to_screen(self.center_x, self.center_y)
    
    def draw(self, screen):
        for joint in self.joints.values():
            # Only draw if joint is visible (not too far back in z)
            if joint.z > -100:
                alpha = max(0.3, 1 - (joint.z / 200))  # Fade with distance
                color = (int(255 * alpha), int(255 * alpha), int(255 * alpha))
                pygame.draw.circle(screen, color, 
                                 (int(joint.screen_x), int(joint.screen_y)), 
                                 POINT_RADIUS)

# Create biological motion instance
bio_motion = BiologicalMotion()

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
    bio_motion.time += 1
    bio_motion.update_pose()
    
    # Draw
    screen.fill(BLACK)
    bio_motion.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
