
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 5

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Running Woman")
clock = pygame.time.Clock()

# Define 15 body points for a human figure
# [head, neck, left_shoulder, right_shoulder, left_elbow, right_elbow, 
#  left_wrist, right_wrist, torso_mid, left_hip, right_hip, 
#  left_knee, right_knee, left_ankle, right_ankle]

class BioMotionRunner:
    def __init__(self):
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        self.time = 0
        self.running_speed = 8  # Animation speed
        
        # Base positions relative to center (scaled for visibility)
        self.base_positions = {
            'head': (0, -80),
            'neck': (0, -60),
            'left_shoulder': (-20, -50),
            'right_shoulder': (20, -50),
            'left_elbow': (-35, -25),
            'right_elbow': (35, -25),
            'left_wrist': (-45, 0),
            'right_wrist': (45, 0),
            'torso_mid': (0, -20),
            'left_hip': (-15, 10),
            'right_hip': (15, 10),
            'left_knee': (-20, 50),
            'right_knee': (20, 50),
            'left_ankle': (-25, 90),
            'right_ankle': (25, 90)
        }
        
    def get_running_motion(self, t):
        positions = {}
        
        # Running cycle parameters
        leg_cycle = math.sin(t * self.running_speed)
        arm_cycle = math.sin(t * self.running_speed + math.pi)  # Arms opposite to legs
        
        # Head - slight bobbing
        head_bob = 3 * math.sin(t * self.running_speed * 2)
        positions['head'] = (self.base_positions['head'][0], 
                           self.base_positions['head'][1] + head_bob)
        
        # Neck follows head with slight delay
        positions['neck'] = (self.base_positions['neck'][0], 
                           self.base_positions['neck'][1] + head_bob * 0.7)
        
        # Torso - slight forward lean and vertical movement
        torso_lean = 8
        torso_bob = 2 * math.sin(t * self.running_speed * 2)
        positions['torso_mid'] = (self.base_positions['torso_mid'][0] + torso_lean, 
                                self.base_positions['torso_mid'][1] + torso_bob)
        
        # Shoulders - follow torso with arm swing
        shoulder_swing = 15 * math.sin(t * self.running_speed)
        positions['left_shoulder'] = (self.base_positions['left_shoulder'][0] - shoulder_swing, 
                                    self.base_positions['left_shoulder'][1] + torso_bob)
        positions['right_shoulder'] = (self.base_positions['right_shoulder'][0] + shoulder_swing, 
                                     self.base_positions['right_shoulder'][1] + torso_bob)
        
        # Arms - running motion
        left_arm_swing = 25 * arm_cycle
        right_arm_swing = -25 * arm_cycle
        
        positions['left_elbow'] = (self.base_positions['left_elbow'][0] + left_arm_swing, 
                                 self.base_positions['left_elbow'][1] + torso_bob - 10 * math.sin(t * self.running_speed))
        positions['right_elbow'] = (self.base_positions['right_elbow'][0] + right_arm_swing, 
                                  self.base_positions['right_elbow'][1] + torso_bob + 10 * math.sin(t * self.running_speed))
        
        positions['left_wrist'] = (self.base_positions['left_wrist'][0] + left_arm_swing * 1.5, 
                                 self.base_positions['left_wrist'][1] + torso_bob - 15 * math.sin(t * self.running_speed))
        positions['right_wrist'] = (self.base_positions['right_wrist'][0] + right_arm_swing * 1.5, 
                                  self.base_positions['right_wrist'][1] + torso_bob + 15 * math.sin(t * self.running_speed))
        
        # Hips - stable base with slight movement
        hip_sway = 3 * math.sin(t * self.running_speed * 2)
        positions['left_hip'] = (self.base_positions['left_hip'][0] + hip_sway, 
                               self.base_positions['left_hip'][1] + torso_bob)
        positions['right_hip'] = (self.base_positions['right_hip'][0] + hip_sway, 
                                self.base_positions['right_hip'][1] + torso_bob)
        
        # Legs - running stride
        left_leg_phase = leg_cycle
        right_leg_phase = -leg_cycle
        
        # Knees
        left_knee_lift = 20 * max(0, left_leg_phase)
        right_knee_lift = 20 * max(0, right_leg_phase)
        
        positions['left_knee'] = (self.base_positions['left_knee'][0] + 5 * left_leg_phase, 
                                self.base_positions['left_knee'][1] - left_knee_lift + torso_bob)
        positions['right_knee'] = (self.base_positions['right_knee'][0] + 5 * right_leg_phase, 
                                 self.base_positions['right_knee'][1] - right_knee_lift + torso_bob)
        
        # Ankles - ground contact and lift
        left_ankle_forward = 15 * left_leg_phase
        right_ankle_forward = 15 * right_leg_phase
        left_ankle_lift = 25 * max(0, left_leg_phase)
        right_ankle_lift = 25 * max(0, right_leg_phase)
        
        positions['left_ankle'] = (self.base_positions['left_ankle'][0] + left_ankle_forward, 
                                 self.base_positions['left_ankle'][1] - left_ankle_lift + torso_bob)
        positions['right_ankle'] = (self.base_positions['right_ankle'][0] + right_ankle_forward, 
                                  self.base_positions['right_ankle'][1] - right_ankle_lift + torso_bob)
        
        return positions
    
    def draw(self, screen):
        positions = self.get_running_motion(self.time)
        
        # Draw all 15 points
        for joint, (rel_x, rel_y) in positions.items():
            x = self.center_x + rel_x
            y = self.center_y + rel_y
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)
        
        self.time += 1/FPS

# Main animation loop
def main():
    runner = BioMotionRunner()
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
        
        # Draw the running figure
        runner.draw(screen)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
