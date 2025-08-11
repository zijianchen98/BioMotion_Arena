
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Woman Lying Down")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, joint_name):
        self.base_x = x
        self.base_y = y
        self.x = x
        self.y = y
        self.joint_name = joint_name
        
    def update(self, time):
        # Subtle breathing motion for lying down position
        breath_amplitude = 2 if self.joint_name in ['chest', 'shoulder_left', 'shoulder_right'] else 1
        breath_freq = 0.05
        
        # Minor relaxed movements
        relax_amplitude = 1.5
        relax_freq = 0.02
        
        # Breathing motion (vertical)
        breath_offset = math.sin(time * breath_freq) * breath_amplitude
        
        # Relaxed shifting motion
        relax_x = math.sin(time * relax_freq + hash(self.joint_name) % 10) * relax_amplitude
        relax_y = math.cos(time * relax_freq * 1.1 + hash(self.joint_name) % 10) * relax_amplitude * 0.5
        
        self.x = self.base_x + relax_x
        self.y = self.base_y + breath_offset + relax_y
        
    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), 4)

# Create 15 point lights representing a woman lying down (side view)
# Arranged to show a relaxed lying position
points = [
    PointLight(WIDTH//2 + 20, HEIGHT//2 - 120, 'head'),           # Head
    PointLight(WIDTH//2, HEIGHT//2 - 100, 'neck'),               # Neck
    PointLight(WIDTH//2 - 15, HEIGHT//2 - 80, 'shoulder_left'),  # Left shoulder
    PointLight(WIDTH//2 + 15, HEIGHT//2 - 80, 'shoulder_right'), # Right shoulder
    PointLight(WIDTH//2, HEIGHT//2 - 60, 'chest'),               # Chest
    PointLight(WIDTH//2 - 25, HEIGHT//2 - 40, 'elbow_left'),     # Left elbow
    PointLight(WIDTH//2 + 25, HEIGHT//2 - 40, 'elbow_right'),    # Right elbow
    PointLight(WIDTH//2 - 35, HEIGHT//2 - 20, 'hand_left'),      # Left hand
    PointLight(WIDTH//2 + 35, HEIGHT//2 - 20, 'hand_right'),     # Right hand
    PointLight(WIDTH//2, HEIGHT//2, 'hip_center'),               # Hip center
    PointLight(WIDTH//2 - 10, HEIGHT//2 + 20, 'hip_left'),       # Left hip
    PointLight(WIDTH//2 + 10, HEIGHT//2 + 20, 'hip_right'),      # Right hip
    PointLight(WIDTH//2 - 15, HEIGHT//2 + 80, 'knee_left'),      # Left knee
    PointLight(WIDTH//2 + 15, HEIGHT//2 + 80, 'knee_right'),     # Right knee
    PointLight(WIDTH//2, HEIGHT//2 + 140, 'foot_center'),        # Feet area
]

# Main animation loop
time = 0
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
    
    # Update and draw points
    for point in points:
        point.update(time)
        point.draw(screen)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)
    time += 1

# Quit
pygame.quit()
sys.exit()
