
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
pygame.display.set_caption("Biological Motion - Woman Waving Hand")
clock = pygame.time.Clock()

# Joint positions for a human figure (15 points)
# Based on typical biomechanical model
class BiologicalMotion:
    def __init__(self):
        self.frame = 0
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        
        # Define 15 key body points
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder',
            'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
            'spine_mid', 'hip_center', 'left_hip', 'right_hip',
            'left_knee', 'right_knee', 'left_ankle', 'right_ankle'
        ]
        
        # Base positions relative to center
        self.base_positions = {
            'head': (0, -120),
            'neck': (0, -100),
            'left_shoulder': (-25, -85),
            'right_shoulder': (25, -85),
            'left_elbow': (-45, -55),
            'right_elbow': (45, -55),
            'left_wrist': (-60, -25),
            'right_wrist': (60, -25),
            'spine_mid': (0, -50),
            'hip_center': (0, 0),
            'left_hip': (-15, 5),
            'right_hip': (15, 5),
            'left_knee': (-18, 60),
            'right_knee': (18, 60),
            'left_ankle': (-20, 120),
            'right_ankle': (20, 120)
        }
    
    def get_waving_positions(self):
        positions = []
        time = self.frame * 0.2
        
        # Wave parameters
        wave_amplitude = 40
        wave_frequency = 2.0
        
        for joint in self.joint_names:
            base_x, base_y = self.base_positions[joint]
            x = self.center_x + base_x
            y = self.center_y + base_y
            
            # Apply waving motion primarily to right arm
            if joint == 'right_shoulder':
                y += math.sin(time * wave_frequency) * 5
            elif joint == 'right_elbow':
                x += math.sin(time * wave_frequency) * wave_amplitude * 0.8
                y += math.sin(time * wave_frequency) * 15 - 10
            elif joint == 'right_wrist':
                x += math.sin(time * wave_frequency) * wave_amplitude
                y += math.sin(time * wave_frequency) * 25 - 20
            
            # Slight body sway
            elif joint in ['spine_mid', 'hip_center']:
                x += math.sin(time * wave_frequency * 0.5) * 3
            
            # Head slight movement
            elif joint == 'head':
                x += math.sin(time * wave_frequency * 0.3) * 2
                y += math.cos(time * wave_frequency * 0.3) * 1
            
            # Left arm subtle counter-movement
            elif joint == 'left_elbow':
                x += math.sin(time * wave_frequency + math.pi) * 5
            elif joint == 'left_wrist':
                x += math.sin(time * wave_frequency + math.pi) * 8
            
            # Leg slight weight shift
            elif joint in ['left_knee', 'left_ankle']:
                x += math.sin(time * wave_frequency * 0.4) * 2
            elif joint in ['right_knee', 'right_ankle']:
                x += math.sin(time * wave_frequency * 0.4 + math.pi) * 2
            
            positions.append((int(x), int(y)))
        
        self.frame += 1
        return positions

# Create biological motion instance
bio_motion = BiologicalMotion()

# Main loop
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
    
    # Get current positions
    positions = bio_motion.get_waving_positions()
    
    # Draw points
    for pos in positions:
        pygame.draw.circle(screen, WHITE, pos, 4)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
