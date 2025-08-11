
import pygame
import math
import numpy as np

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
pygame.display.set_caption("Biological Motion - Sad Woman Jumping Forward")
clock = pygame.time.Clock()

class PointLightWalker:
    def __init__(self):
        # 15 body points representing major joints and body parts
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder',
            'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
            'spine', 'left_hip', 'right_hip', 'left_knee', 'right_knee',
            'left_ankle', 'right_ankle'
        ]
        
        # Base positions (standing pose)
        self.base_positions = {
            'head': (0, -90),
            'neck': (0, -70),
            'left_shoulder': (-15, -60),
            'right_shoulder': (15, -60),
            'left_elbow': (-25, -30),
            'right_elbow': (25, -30),
            'left_wrist': (-30, 0),
            'right_wrist': (30, 0),
            'spine': (0, -20),
            'left_hip': (-10, 20),
            'right_hip': (10, 20),
            'left_knee': (-12, 60),
            'right_knee': (12, 60),
            'left_ankle': (-10, 100),
            'right_ankle': (10, 100)
        }
        
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        self.time = 0
        self.jump_height = 0
        self.forward_position = 0
        
    def get_jump_phase(self, t):
        """Calculate jump phase - modified for sad, heavy motion"""
        # Slower, more labored jumping motion
        cycle_time = 3.0  # Slower cycle for heavy motion
        phase = (t % cycle_time) / cycle_time
        
        if phase < 0.3:  # Preparation phase (longer)
            return 'prep', phase / 0.3
        elif phase < 0.5:  # Takeoff phase
            return 'takeoff', (phase - 0.3) / 0.2
        elif phase < 0.7:  # Flight phase
            return 'flight', (phase - 0.5) / 0.2
        else:  # Landing phase (longer recovery)
            return 'landing', (phase - 0.7) / 0.3
    
    def calculate_positions(self):
        jump_phase, sub_phase = self.get_jump_phase(self.time)
        positions = {}
        
        # Calculate vertical displacement (reduced for heavy motion)
        if jump_phase == 'prep':
            self.jump_height = -15 * sub_phase  # Crouch down more
            self.forward_position += 0.3  # Minimal forward during prep
        elif jump_phase == 'takeoff':
            self.jump_height = -15 + 35 * sub_phase  # Rise up
            self.forward_position += 1.5  # Forward motion during takeoff
        elif jump_phase == 'flight':
            self.jump_height = 20 - 10 * sub_phase  # Peak and start descent
            self.forward_position += 2.0  # Continue forward
        else:  # landing
            self.jump_height = 10 - 25 * sub_phase  # Land and compress
            self.forward_position += 0.5  # Slow down
        
        # Apply sad/heavy motion characteristics
        for joint, (base_x, base_y) in self.base_positions.items():
            x = base_x + self.forward_position
            y = base_y + self.jump_height
            
            # Add specific joint movements for jumping
            if jump_phase in ['prep', 'takeoff']:
                # Arm swing for momentum (less energetic)
                if 'elbow' in joint or 'wrist' in joint:
                    if 'left' in joint:
                        x -= 10 * sub_phase
                        y += 5 * sub_phase
                    else:
                        x += 10 * sub_phase
                        y += 5 * sub_phase
                
                # Leg preparation
                if jump_phase == 'prep':
                    if 'knee' in joint:
                        y += 15 * sub_phase  # Bend knees more
                    if 'ankle' in joint:
                        y += 10 * sub_phase
                
            elif jump_phase == 'flight':
                # Legs tuck up slightly (less dynamic for sad motion)
                if 'knee' in joint:
                    y -= 8 * (1 - abs(2 * sub_phase - 1))
                if 'ankle' in joint:
                    y -= 12 * (1 - abs(2 * sub_phase - 1))
                
                # Arms move less dramatically
                if 'elbow' in joint or 'wrist' in joint:
                    y -= 3 * (1 - abs(2 * sub_phase - 1))
            
            elif jump_phase == 'landing':
                # Landing impact - more pronounced for heavy motion
                if 'knee' in joint or 'ankle' in joint:
                    y += 8 * sub_phase
                
                # Arms drop down
                if 'elbow' in joint or 'wrist' in joint:
                    y += 10 * sub_phase
            
            # Add slight body sway for sad motion
            sway = 3 * math.sin(self.time * 0.8)
            x += sway * 0.3
            
            # Add slight head droop for sad expression
            if joint == 'head':
                y += 5
                x += sway * 0.1
            
            positions[joint] = (
                self.center_x + x,
                self.center_y + y
            )
        
        return positions
    
    def update(self, dt):
        self.time += dt
    
    def draw(self, screen):
        positions = self.calculate_positions()
        
        # Draw all 15 points
        for joint_name in self.joint_names:
            if joint_name in positions:
                x, y = positions[joint_name]
                # Ensure points stay within screen bounds
                x = max(POINT_RADIUS, min(WIDTH - POINT_RADIUS, x))
                y = max(POINT_RADIUS, min(HEIGHT - POINT_RADIUS, y))
                pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

# Main game loop
def main():
    walker = PointLightWalker()
    running = True
    
    while running:
        dt = clock.tick(FPS) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update
        walker.update(dt)
        
        # Draw
        screen.fill(BLACK)
        walker.draw(screen)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
