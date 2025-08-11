
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

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Man Turning Around")
clock = pygame.time.Clock()

class PointLightWalker:
    def __init__(self):
        # 15 body joints for a human figure
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
            'left_wrist', 'right_wrist', 'torso', 'left_hip', 'right_hip',
            'left_knee', 'right_knee', 'left_ankle', 'right_ankle'
        ]
        
        # Base positions relative to center (anatomically correct proportions)
        self.base_positions = {
            'head': (0, -90),
            'neck': (0, -70),
            'left_shoulder': (-20, -60),
            'right_shoulder': (20, -60),
            'left_elbow': (-25, -30),
            'right_elbow': (25, -30),
            'left_wrist': (-30, 0),
            'right_wrist': (30, 0),
            'torso': (0, -20),
            'left_hip': (-15, 20),
            'right_hip': (15, 20),
            'left_knee': (-15, 60),
            'right_knee': (15, 60),
            'left_ankle': (-15, 100),
            'right_ankle': (15, 100)
        }
        
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        self.angle = 0
        self.turn_speed = 2
        self.time = 0
        
    def get_joint_position(self, joint_name, angle):
        base_x, base_y = self.base_positions[joint_name]
        
        # Add subtle walking motion while turning
        walking_phase = self.time * 3
        
        # Walking motion adjustments for different body parts
        if 'left' in joint_name:
            if 'hip' in joint_name or 'knee' in joint_name or 'ankle' in joint_name:
                base_y += math.sin(walking_phase) * 3
                base_x += math.cos(walking_phase) * 2
            elif 'arm' in joint_name or 'elbow' in joint_name or 'wrist' in joint_name:
                base_x += math.sin(walking_phase) * 8
                
        elif 'right' in joint_name:
            if 'hip' in joint_name or 'knee' in joint_name or 'ankle' in joint_name:
                base_y += math.sin(walking_phase + math.pi) * 3
                base_x += math.cos(walking_phase + math.pi) * 2
            elif 'arm' in joint_name or 'elbow' in joint_name or 'wrist' in joint_name:
                base_x += math.sin(walking_phase + math.pi) * 8
        
        # Add sad posture - drooped shoulders and head
        if joint_name == 'head':
            base_y += 5
            base_x += math.sin(self.time * 0.5) * 2  # slight head movement
        elif 'shoulder' in joint_name:
            base_y += 8  # drooped shoulders
        elif 'wrist' in joint_name:
            base_y += 5  # arms hanging lower
            
        # Apply rotation for turning around
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        
        rotated_x = base_x * cos_a - base_y * sin_a * 0.3  # Perspective effect
        rotated_y = base_y
        
        # Add depth effect (points get smaller/larger as they rotate)
        depth_factor = 0.7 + 0.3 * cos_a
        
        return (
            self.center_x + rotated_x * depth_factor,
            self.center_y + rotated_y,
            depth_factor
        )
    
    def update(self, dt):
        self.time += dt
        self.angle += math.radians(self.turn_speed)
        if self.angle >= 2 * math.pi:
            self.angle = 0
    
    def draw(self, surface):
        for joint_name in self.joint_names:
            x, y, depth = self.get_joint_position(joint_name, self.angle)
            
            # Adjust point size based on depth
            radius = max(2, int(4 * depth))
            
            # Only draw if point is within screen bounds
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                pygame.draw.circle(surface, WHITE, (int(x), int(y)), radius)

# Create walker instance
walker = PointLightWalker()

# Main game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000.0
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Update
    walker.update(dt)
    
    # Draw
    screen.fill(BLACK)
    walker.draw(screen)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
