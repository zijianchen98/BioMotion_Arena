
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 8

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Woman Jumping Forward")
clock = pygame.time.Clock()

class PointLightWalker:
    def __init__(self):
        # 15 key points for human body
        self.joint_names = [
            'head', 'neck', 'torso', 'hip',
            'left_shoulder', 'left_elbow', 'left_wrist',
            'right_shoulder', 'right_elbow', 'right_wrist',
            'left_hip', 'left_knee', 'left_ankle',
            'right_hip', 'right_knee', 'right_ankle'
        ]
        
        # Base positions relative to center (torso)
        self.base_positions = {
            'head': (0, -120),
            'neck': (0, -90),
            'torso': (0, -40),
            'hip': (0, 20),
            'left_shoulder': (-25, -80),
            'left_elbow': (-40, -50),
            'left_wrist': (-50, -20),
            'right_shoulder': (25, -80),
            'right_elbow': (40, -50),
            'right_wrist': (50, -20),
            'left_hip': (-15, 20),
            'left_knee': (-20, 80),
            'left_ankle': (-25, 140),
            'right_hip': (15, 20),
            'right_knee': (20, 80),
            'right_ankle': (25, 140)
        }
        
        self.positions = {}
        self.center_x = WIDTH // 2 - 100
        self.center_y = HEIGHT // 2
        self.time = 0
        
    def update(self, dt):
        self.time += dt
        
        # Jump cycle - approximately 1 second per jump
        jump_cycle = 2.0
        t = (self.time % jump_cycle) / jump_cycle
        
        # Phases: crouch (0-0.2), takeoff (0.2-0.4), flight (0.4-0.8), landing (0.8-1.0)
        if t < 0.2:  # Crouch phase
            phase = "crouch"
            phase_t = t / 0.2
        elif t < 0.4:  # Takeoff phase
            phase = "takeoff"
            phase_t = (t - 0.2) / 0.2
        elif t < 0.8:  # Flight phase
            phase = "flight"
            phase_t = (t - 0.4) / 0.4
        else:  # Landing phase
            phase = "landing"
            phase_t = (t - 0.8) / 0.2
        
        # Calculate vertical displacement and forward movement
        if phase == "crouch":
            vertical_offset = -20 * math.sin(phase_t * math.pi)
            forward_offset = phase_t * 10
        elif phase == "takeoff":
            vertical_offset = -20 * (1 - phase_t) - 60 * phase_t
            forward_offset = 10 + phase_t * 30
        elif phase == "flight":
            # Parabolic flight path
            vertical_offset = -60 - 40 * math.sin(phase_t * math.pi)
            forward_offset = 40 + phase_t * 80
        else:  # landing
            vertical_offset = -60 * (1 - phase_t) - 15 * phase_t
            forward_offset = 120 + phase_t * 20
        
        # Update center position
        base_center_x = WIDTH // 2 - 100 + forward_offset
        base_center_y = HEIGHT // 2 + vertical_offset
        
        # Calculate limb movements
        for joint in self.joint_names:
            base_x, base_y = self.base_positions[joint]
            
            # Apply phase-specific modifications
            if phase == "crouch":
                if "knee" in joint:
                    base_y -= 30 * phase_t
                if "ankle" in joint:
                    base_y -= 20 * phase_t
                if "elbow" in joint:
                    base_y += 15 * phase_t
                if "hip" in joint:
                    base_y += 10 * phase_t
                    
            elif phase == "takeoff":
                if "knee" in joint:
                    base_y -= 30 * (1 - phase_t)
                if "ankle" in joint:
                    base_y -= 20 * (1 - phase_t) + 10 * phase_t
                if "elbow" in joint:
                    base_y += 15 * (1 - phase_t) - 25 * phase_t
                if "wrist" in joint:
                    base_y -= 20 * phase_t
                    
            elif phase == "flight":
                # Extended pose during flight
                if "knee" in joint:
                    base_y += 10 * math.sin(phase_t * math.pi)
                if "ankle" in joint:
                    base_y += 20 * math.sin(phase_t * math.pi)
                if "elbow" in joint:
                    base_y -= 25
                if "wrist" in joint:
                    base_y -= 20
                    
            elif phase == "landing":
                # Prepare for landing
                if "knee" in joint:
                    base_y -= 25 * phase_t
                if "ankle" in joint:
                    base_y -= 15 * phase_t
                if "elbow" in joint:
                    base_y -= 25 * (1 - phase_t)
                if "wrist" in joint:
                    base_y -= 20 * (1 - phase_t)
            
            # Add slight asymmetry for more natural movement
            if "left" in joint:
                base_x -= 2 * math.sin(self.time * 3)
            elif "right" in joint:
                base_x += 2 * math.sin(self.time * 3 + math.pi)
            
            # Store final position
            self.positions[joint] = (
                base_center_x + base_x,
                base_center_y + base_y
            )
    
    def draw(self, surface):
        for joint in self.joint_names:
            if joint in self.positions:
                x, y = self.positions[joint]
                pygame.draw.circle(surface, WHITE, (int(x), int(y)), POINT_RADIUS)

def main():
    walker = PointLightWalker()
    running = True
    
    while running:
        dt = clock.tick(FPS) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
