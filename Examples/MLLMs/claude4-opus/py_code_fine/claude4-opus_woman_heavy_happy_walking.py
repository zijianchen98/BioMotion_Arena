
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 4

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Walking Woman")
clock = pygame.time.Clock()

class PointLightWalker:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.time = 0
        self.step_frequency  # Slower for heavy weight walking
        self.step_amplitude = 25    # Smaller steps for heavy walking
        self.body_sway = 8          # More body sway for heavy walking
        
        # Define 15 joint positions (simplified human skeleton)
        self.joint_names = [
            'head', 'neck', 'spine_upper', 'spine_lower', 'pelvis',
            'left_shoulder', 'left_elbow', 'left_hand',
            'right_shoulder', 'right_elbow', 'right_hand',
            'left_hip', 'left_knee', 'left_foot',
            'right_hip', 'right_knee', 'right_foot'
        ][:15]
        
        # Base positions relative to center
        self.base_positions = {
            'head': (0, -120),
            'neck': (0, -100),
            'spine_upper': (0, -80),
            'spine_lower': (0, -40),
            'pelvis': (0, 0),
            'left_shoulder': (-20, -90),
            'left_elbow': (-35, -60),
            'left_hand': (-45, -30),
            'right_shoulder': (20, -90),
            'right_elbow': (35, -60),
            'right_hand': (45, -30),
            'left_hip': (-15, 10),
            'left_knee': (-18, 50),
            'left_foot': (-20, 90),
            'right_hip': (15, 10)
        }
        
        self.positions = {}
        
    def update(self):
        self.time += self.step_frequency
        
        # Walking cycle phase
        left_phase = math.sin(self.time)
        right_phase = math.sin(self.time + math.pi)  # Opposite phase
        
        # Body sway (heavy walking characteristic)
        body_sway_x = math.sin(self.time * 2) * self.body_sway
        
        # Calculate positions for each joint
        for joint in self.joint_names:
            if joint in self.base_positions:
                base_x, base_y = self.base_positions[joint]
                
                # Apply body sway to torso
                if joint in ['head', 'neck', 'spine_upper', 'spine_lower', 'pelvis']:
                    sway_mult = 1.0 if joint in ['head', 'neck'] else 0.7
                    x = self.center_x + base_x + body_sway_x * sway_mult
                    
                    # Slight vertical bobbing
                    bob = math.sin(self.time * 4) * 3
                    y = self.center_y + base_y + bob
                    
                # Left arm swing (opposite to left leg)
                elif 'left' in joint and joint in ['left_shoulder', 'left_elbow', 'left_hand']:
                    arm_swing = -right_phase * 15  # Opposite to left leg
                    if joint == 'left_shoulder':
                        x = self.center_x + base_x + body_sway_x * 0.5
                        y = self.center_y + base_y + arm_swing * 0.3
                    elif joint == 'left_elbow':
                        x = self.center_x + base_x + arm_swing + body_sway_x * 0.3
                        y = self.center_y + base_y
                    else:  # left_hand
                        x = self.center_x + base_x + arm_swing * 1.5 + body_sway_x * 0.2
                        y = self.center_y + base_y + arm_swing * 0.5
                
                # Right arm swing (opposite to right leg)
                elif 'right' in joint and joint in ['right_shoulder', 'right_elbow', 'right_hand']:
                    arm_swing = -left_phase * 15  # Opposite to right leg
                    if joint == 'right_shoulder':
                        x = self.center_x + base_x + body_sway_x * 0.5
                        y = self.center_y + base_y + arm_swing * 0.3
                    elif joint == 'right_elbow':
                        x = self.center_x + base_x + arm_swing + body_sway_x * 0.3
                        y = self.center_y + base_y
                    else:  # right_hand
                        x = self.center_x + base_x + arm_swing * 1.5 + body_sway_x * 0.2
                        y = self.center_y + base_y + arm_swing * 0.5
                
                # Left leg
                elif 'left' in joint and 'hip' in joint:
                    x = self.center_x + base_x + body_sway_x * 0.3
                    y = self.center_y + base_y
                elif 'left' in joint and 'knee' in joint:
                    knee_bend = max(0, left_phase) * 20  # Knee lift
                    x = self.center_x + base_x + left_phase * self.step_amplitude * 0.5
                    y = self.center_y + base_y - knee_bend
                elif 'left' in joint and 'foot' in joint:
                    foot_lift = max(0, left_phase) * 15
                    x = self.center_x + base_x + left_phase * self.step_amplitude
                    y = self.center_y + base_y - foot_lift
                
                # Right leg  
                elif 'right' in joint and 'hip' in joint:
                    x = self.center_x + base_x + body_sway_x * 0.3
                    y = self.center_y + base_y
                elif 'right' in joint and 'knee' in joint:
                    knee_bend = max(0, right_phase) * 20
                    x = self.center_x + base_x + right_phase * self.step_amplitude * 0.5
                    y = self.center_y + base_y - knee_bend
                elif 'right' in joint and 'foot' in joint:
                    foot_lift = max(0, right_phase) * 15
                    x = self.center_x + base_x + right_phase * self.step_amplitude
                    y = self.center_y + base_y - foot_lift
                
                else:
                    x = self.center_x + base_x + body_sway_x * 0.1
                    y = self.center_y + base_y
                
                self.positions[joint] = (int(x), int(y))
    
    def draw(self, surface):
        for joint in self.joint_names:
            if joint in self.positions:
                pygame.draw.circle(surface, WHITE, self.positions[joint], POINT_RADIUS)

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
    walker.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
