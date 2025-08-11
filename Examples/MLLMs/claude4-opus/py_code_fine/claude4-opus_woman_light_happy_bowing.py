
import pygame
import math
import numpy as np

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Woman Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 60
clock = pygame.time.Clock()

class PointLightDisplay:
    def __init__(self):
        self.frame = 0
        self.max_frames = 180  # 3 seconds at 60 FPS
        
        # Define 15 joint positions for a human figure
        # Order: head, neck, shoulders(2), elbows(2), wrists(2), 
        #        torso center, hips(2), knees(2), ankles(2), feet(2)
        self.joint_names = [
            'head', 'neck', 'left_shoulder', 'right_shoulder',
            'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
            'torso', 'left_hip', 'right_hip', 'left_knee', 'right_knee',
            'left_ankle', 'right_ankle'
        ]
        
        # Base positions (standing upright, centered)
        self.base_positions = {
            'head': (0, -60),
            'neck': (0, -45),
            'left_shoulder': (-15, -40),
            'right_shoulder': (15, -40),
            'left_elbow': (-25, -15),
            'right_elbow': (25, -15),
            'left_wrist': (-30, 5),
            'right_wrist': (30, 5),
            'torso': (0, -20),
            'left_hip': (-10, 0),
            'right_hip': (10, 0),
            'left_knee': (-12, 25),
            'right_knee': (12, 25),
            'left_ankle': (-10, 50),
            'right_ankle': (10, 50)
        }
    
    def get_bow_animation_frame(self, progress):
        """Generate positions for bowing animation"""
        positions = {}
        
        # Bowing motion phases
        if progress < 0.3:  # Start bowing
            bow_angle = progress * math.pi / 6  # Up to 30 degrees
        elif progress < 0.7:  # Hold bow
            bow_angle = math.pi / 6
        else:  # Return to standing
            bow_angle = (1 - progress) * math.pi / 6 / 0.3
        
        # Calculate spine curvature for bowing
        spine_bend = math.sin(bow_angle) * 20
        forward_lean = math.sin(bow_angle) * 15
        
        # Slight weight shift and natural sway for a light woman
        sway_x = math.sin(progress * math.pi * 2) * 2
        gentle_bob = math.sin(progress * math.pi * 4) * 1
        
        for joint in self.joint_names:
            base_x, base_y = self.base_positions[joint]
            
            # Apply bowing transformation
            if joint in ['head', 'neck']:
                # Head and neck lean forward more
                new_x = base_x + forward_lean * 1.5 + sway_x
                new_y = base_y + spine_bend * 0.5 + gentle_bob
            elif 'shoulder' in joint or 'elbow' in joint or 'wrist' in joint:
                # Arms move naturally with bow, slight arm swing
                arm_swing = math.sin(progress * math.pi * 2) * 3
                new_x = base_x + forward_lean + sway_x + arm_swing
                new_y = base_y + spine_bend * 0.7 + gentle_bob
            elif joint == 'torso':
                # Torso bends forward
                new_x = base_x + forward_lean + sway_x
                new_y = base_y + spine_bend + gentle_bob
            else:
                # Legs stay relatively stable with slight weight shift
                leg_shift = math.sin(progress * math.pi) * 2
                new_x = base_x + leg_shift + sway_x * 0.5
                new_y = base_y + gentle_bob * 0.5
            
            # Convert to screen coordinates
            screen_x = WIDTH // 2 + new_x * 4
            screen_y = HEIGHT // 2 + new_y * 4
            positions[joint] = (screen_x, screen_y)
        
        return positions
    
    def draw(self, screen):
        screen.fill(BLACK)
        
        # Calculate animation progress (0 to 1)
        progress = (self.frame % self.max_frames) / self.max_frames
        
        # Get current frame positions
        positions = self.get_bow_animation_frame(progress)
        
        # Draw points
        for joint in self.joint_names:
            pos = positions[joint]
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 6)
        
        self.frame += 1
    
    def update(self):
        pass

def main():
    display = PointLightDisplay()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        display.update()
        display.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
