
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 4

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Walking")
clock = pygame.time.Clock()

class BiologicalMotion:
    def __init__(self):
        self.frame = 0
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        
        # Define 15 key points for human body
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder',
            'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
            'spine', 'left_hip', 'right_hip',
            'left_knee', 'right_knee', 'left_ankle', 'right_ankle'
        ]
        
        # Base positions relative to center (proportional to human body)
        self.base_positions = {
            'head': (0, -120),
            'neck': (0, -100),
            'left_shoulder': (-25, -95),
            'right_shoulder': (25, -95),
            'left_elbow': (-35, -70),
            'right_elbow': (35, -70),
            'left_wrist': (-30, -45),
            'right_wrist': (30, -45),
            'spine': (0, -50),
            'left_hip': (-15, -10),
            'right_hip': (15, -10),
            'left_knee': (-18, 40),
            'right_knee': (18, 40),
            'left_ankle': (-20, 90),
            'right_ankle': (20, 90)
        }
    
    def get_walking_animation(self, frame):
        # Walking cycle parameters
        cycle_length = 60  # frames for one complete walking cycle
        phase = (frame % cycle_length) / cycle_length * 2 * math.pi
        
        positions = {}
        
        # Head - slight vertical bob
        head_bob = math.sin(phase * 2) * 3
        positions['head'] = (self.center_x, self.center_y + self.base_positions['head'][1] + head_bob)
        positions['neck'] = (self.center_x, self.center_y + self.base_positions['neck'][1] + head_bob)
        
        # Shoulders - slight sway
        shoulder_sway = math.sin(phase) * 2
        positions['left_shoulder'] = (
            self.center_x + self.base_positions['left_shoulder'][0] + shoulder_sway,
            self.center_y + self.base_positions['left_shoulder'][1] + head_bob * 0.5
        )
        positions['right_shoulder'] = (
            self.center_x + self.base_positions['right_shoulder'][0] - shoulder_sway,
            self.center_y + self.base_positions['right_shoulder'][1] + head_bob * 0.5
        )
        
        # Arms - swinging opposite to legs
        left_arm_swing = math.sin(phase + math.pi) * 15
        right_arm_swing = math.sin(phase) * 15
        
        positions['left_elbow'] = (
            self.center_x + self.base_positions['left_elbow'][0] + left_arm_swing * 0.7,
            self.center_y + self.base_positions['left_elbow'][1]
        )
        positions['right_elbow'] = (
            self.center_x + self.base_positions['right_elbow'][0] + right_arm_swing * 0.7,
            self.center_y + self.base_positions['right_elbow'][1]
        )
        
        positions['left_wrist'] = (
            self.center_x + self.base_positions['left_wrist'][0] + left_arm_swing,
            self.center_y + self.base_positions['left_wrist'][1]
        )
        positions['right_wrist'] = (
            self.center_x + self.base_positions['right_wrist'][0] + right_arm_swing,
            self.center_y + self.base_positions['right_wrist'][1]
        )
        
        # Spine - slight movement
        positions['spine'] = (
            self.center_x + shoulder_sway * 0.3,
            self.center_y + self.base_positions['spine'][1] + head_bob * 0.3
        )
        
        # Hips - counter-rotation and vertical movement
        hip_rotation = math.sin(phase) * 3
        hip_bob = math.sin(phase * 2) * 2
        
        positions['left_hip'] = (
            self.center_x + self.base_positions['left_hip'][0] - hip_rotation,
            self.center_y + self.base_positions['left_hip'][1] + hip_bob
        )
        positions['right_hip'] = (
            self.center_x + self.base_positions['right_hip'][0] + hip_rotation,
            self.center_y + self.base_positions['right_hip'][1] + hip_bob
        )
        
        # Legs - walking motion
        left_leg_forward = math.sin(phase) * 25
        right_leg_forward = math.sin(phase + math.pi) * 25
        
        left_leg_lift = max(0, math.sin(phase) * 15)
        right_leg_lift = max(0, math.sin(phase + math.pi) * 15)
        
        # Knees
        positions['left_knee'] = (
            self.center_x + self.base_positions['left_knee'][0] + left_leg_forward * 0.5,
            self.center_y + self.base_positions['left_knee'][1] - left_leg_lift
        )
        positions['right_knee'] = (
            self.center_x + self.base_positions['right_knee'][0] + right_leg_forward * 0.5,
            self.center_y + self.base_positions['right_knee'][1] - right_leg_lift
        )
        
        # Ankles
        positions['left_ankle'] = (
            self.center_x + self.base_positions['left_ankle'][0] + left_leg_forward,
            self.center_y + self.base_positions['left_ankle'][1] - left_leg_lift * 0.3
        )
        positions['right_ankle'] = (
            self.center_x + self.base_positions['right_ankle'][0] + right_leg_forward,
            self.center_y + self.base_positions['right_ankle'][1] - right_leg_lift * 0.3
        )
        
        return positions
    
    def update(self):
        self.frame += 1
        return self.get_walking_animation(self.frame)

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
    
    # Clear screen
    screen.fill(BLACK)
    
    # Get current frame positions
    positions = bio_motion.update()
    
    # Draw all 15 points
    for joint_name in bio_motion.joint_names:
        pos = positions[joint_name]
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit
pygame.quit()
sys.exit()
