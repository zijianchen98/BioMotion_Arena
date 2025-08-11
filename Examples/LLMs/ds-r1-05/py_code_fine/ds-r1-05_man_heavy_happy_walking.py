
import pygame
import math
import sys
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)  # Black background
POINT_COLOR = (255, 255, 255)  # White points
POINT_RADIUS = 6
NUM_POINTS = 15
FPS = 60

# Joint indices (matching biological motion literature)
HEAD = 0
NECK = 1
SHOULDER_R = 2
SHOULDER_L = 3
ELBOW_R = 4
ELBOW_L = 5
WRIST_R = 6
WRIST_L = 7
HIP_R = 8
HIP_L = 9
KNEE_R = 10
KNEE_L = 11
ANKLE_R = 12
ANKLE_L = 13
FOOT_R = 14
FOOT_L = 15

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Heavily Laden Walker")
clock = pygame.time.Clock()

class Walker:
    def __init__(self):
        self.scale = 100
        self.offset = np.array([WIDTH // 2, HEIGHT // 3])
        self.gravity = 0.6
        self.speed = 0.05
        self.t = 0
        self.foot_contact = [True, False]  # Right foot, left foot
        
    def get_joint_positions(self, phase):
        """Calculate realistic joint positions for heavy walker"""
        phase = phase % (2 * math.pi)
        
        # Core body motion (exaggerated for weight)
        torso_sway = 0.1 * math.sin(phase)
        vertical_bob = 0.5 * math.cos(2 * phase)  # Heavier bob
        
        # Body proportions
        positions = np.zeros((16, 2))  # More points than needed, we'll use 15
        
        # Head and torso
        positions[HEAD] = [0, -1.7 + vertical_bob]
        positions[NECK] = [0, -1.4 + vertical_bob]
        
        # Shoulders (wider for heavy person)
        positions[SHOULDER_R] = [0.7 - torso_sway, -1.3 + vertical_bob]
        positions[SHOULDER_L] = [-0.7 - torso_sway, -1.3 + vertical_bob]
        
        # Arms (shorter swing for heavy weight)
        arm_swing_r = 0.15 * math.sin(phase + math.pi/2)
        arm_swing_l = 0.15 * math.sin(phase + 3*math.pi/2)
        
        positions[ELBOW_R] = [0.7 - 0.4 - torso_sway, -0.8 + arm_swing_r]
        positions[ELBOW_L] = [-0.7 + 0.4 - torso_sway, -0.8 + arm_swing_l]
        
        # Hips (wider stance for heavy weight)
        positions[HIP_R] = [0.5 + torso_sway/2, 0 + vertical_bob]
        positions[HIP_L] = [-0.5 + torso_sway/2, 0 + vertical_bob]
        
        # Leg motion physics (shorter strides)
        leg_phase = phase if phase < math.pi else 2*math.pi - phase
        knee_angle = 1.2 - 0.4 * math.sin(leg_phase)
        thigh_r = 1.0 * math.sin(leg_phase - 0.2)
        thigh_l = 1.0 * math.sin(leg_phase + math.pi/2 + 0.2)
        
        # Right leg
        positions[KNEE_R] = [
            0.5 + 0.3 * math.sin(phase) + torso_sway/2, 
            0.7 - thigh_r
        ]
        positions[ANKLE_R] = [
            positions[KNEE_R][0] + 0.2 * math.sin(phase/2),
            positions[KNEE_R][1] + 0.8 + thigh_r/2
        ]
        
        # Left leg
        positions[KNEE_L] = [
            -0.5 + 0.3 * math.sin(phase + math.pi) + torso_sway/2, 
            0.7 - thigh_l
        ]
        positions[ANKLE_L] = [
            positions[KNEE_L][0] + 0.2 * math.sin((phase+math.pi)/2),
            positions[KNEE_L][1] + 0.8 + thigh_l/2
        ]
        
        # Feet placement
        positions[FOOT_R] = [positions[ANKLE_R][0] + 0.2, positions[ANKLE_R][1] + 0.1]
        positions[FOOT_L] = [positions[ANKLE_L][0] + 0.2, positions[ANKLE_L][1] + 0.1]
        
        return positions * self.scale + self.offset

    def update(self):
        """Update walker's state"""
        self.t += self.speed
        return self.get_joint_positions(self.t)[:NUM_POINTS]

# Create walker
walker = Walker()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BG_COLOR)
    
    # Get and draw points
    points = walker.update()
    for point in points:
        pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), POINT_RADIUS)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
