
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
POINT_RADIUS = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sitting Down")
clock = pygame.time.Clock()

# Body part indices for 15 points
# 0: head, 1: neck, 2: left shoulder, 3: right shoulder
# 4: left elbow, 5: right elbow, 6: left wrist, 7: right wrist
# 8: spine, 9: left hip, 10: right hip, 11: left knee, 12: right knee
# 13: left ankle, 14: right ankle

class BiologicalMotion:
    def __init__(self):
        self.frame = 0
        self.total_frames = 120  # 4 seconds at 30 fps
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2 - 50
        
        # Initial standing positions (relative to center)
        self.standing_positions = {
            0: (0, -120),    # head
            1: (0, -100),    # neck
            2: (-25, -85),   # left shoulder
            3: (25, -85),    # right shoulder
            4: (-40, -50),   # left elbow
            5: (40, -50),    # right elbow
            6: (-50, -15),   # left wrist
            7: (50, -15),    # right wrist
            8: (0, -60),     # spine
            9: (-15, -20),   # left hip
            10: (15, -20),   # right hip
            11: (-20, 20),   # left knee
            12: (20, 20),    # right knee
            13: (-25, 60),   # left ankle
            14: (25, 60)     # right ankle
        }
        
        # Final sitting positions
        self.sitting_positions = {
            0: (0, -80),     # head
            1: (0, -60),     # neck
            2: (-25, -45),   # left shoulder
            3: (25, -45),    # right shoulder
            4: (-35, -20),   # left elbow
            5: (35, -20),    # right elbow
            6: (-30, 5),     # left wrist
            7: (30, 5),      # right wrist
            8: (0, -30),     # spine
            9: (-15, 0),     # left hip
            10: (15, 0),     # right hip
            11: (-30, 30),   # left knee
            12: (30, 30),    # right knee
            13: (-35, 35),   # left ankle
            14: (35, 35)     # right ankle
        }
        
    def get_position(self, point_id, progress):
        # Smooth transition using easing function
        t = progress / self.total_frames
        # Ease in-out cubic for natural motion
        if t < 0.5:
            eased_t = 4 * t * t * t
        else:
            eased_t = 1 - pow(-2 * t + 2, 3) / 2
            
        start_pos = self.standing_positions[point_id]
        end_pos = self.sitting_positions[point_id]
        
        # Interpolate between standing and sitting positions
        x = start_pos[0] + (end_pos[0] - start_pos[0]) * eased_t
        y = start_pos[1] + (end_pos[1] - start_pos[1]) * eased_t
        
        # Add slight natural sway for realism
        sway = math.sin(progress * 0.1) * 2
        x += sway
        
        return (self.center_x + x, self.center_y + y)
    
    def update(self):
        self.frame += 1
        if self.frame >= self.total_frames:
            self.frame = 0  # Loop animation
    
    def draw(self, surface):
        surface.fill(BLACK)
        
        # Draw all 15 points
        for i in range(15):
            pos = self.get_position(i, self.frame)
            pygame.draw.circle(surface, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

# Main animation loop
motion = BiologicalMotion()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    motion.update()
    motion.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
