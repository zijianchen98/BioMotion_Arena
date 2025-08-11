
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Running Human")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for frame rate
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.base_x = x
        self.base_y = y

# Define the 15 point-light positions for a human figure
# Based on major joints and body parts
point_lights = [
    # Head
    PointLight(WIDTH//2, HEIGHT//2 - 120),
    
    # Torso
    PointLight(WIDTH//2, HEIGHT//2 - 80),      # Neck/shoulders
    PointLight(WIDTH//2 - 20, HEIGHT//2 - 60), # Left shoulder
    PointLight(WIDTH//2 + 20, HEIGHT//2 - 60), # Right shoulder
    PointLight(WIDTH//2, HEIGHT//2 - 20),      # Chest center
    PointLight(WIDTH//2, HEIGHT//2 + 20),      # Hip center
    
    # Left arm
    PointLight(WIDTH//2 - 35, HEIGHT//2 - 40), # Left elbow
    PointLight(WIDTH//2 - 50, HEIGHT//2 - 10), # Left hand
    
    # Right arm
    PointLight(WIDTH//2 + 35, HEIGHT//2 - 40), # Right elbow
    PointLight(WIDTH//2 + 50, HEIGHT//2 - 10), # Right hand
    
    # Left leg
    PointLight(WIDTH//2 - 15, HEIGHT//2 + 60), # Left knee
    PointLight(WIDTH//2 - 20, HEIGHT//2 + 120), # Left foot
    
    # Right leg
    PointLight(WIDTH//2 + 15, HEIGHT//2 + 60), # Right knee
    PointLight(WIDTH//2 + 20, HEIGHT//2 + 120), # Right foot
    
    # Additional torso point
    PointLight(WIDTH//2, HEIGHT//2)            # Waist
]

def update_running_motion(frame):
    # Running cycle parameters
    cycle_length = 60  # frames for one complete running cycle
    t = (frame % cycle_length) / cycle_length * 2 * math.pi
    
    # Vertical bobbing motion for the entire body
    body_bob = math.sin(t * 2) * 8
    
    # Horizontal progression (running forward)
    horizontal_shift = (frame * 2) % WIDTH
    
    for i, point in enumerate(point_lights):
        # Reset to base position
        point.x = point.base_x + horizontal_shift
        point.y = point.base_y + body_bob
        
        if i == 0:  # Head
            point.y += math.sin(t * 2) * 3
            
        elif i in [1, 2, 3, 4, 14]:  # Torso points
            point.y += math.sin(t * 2) * 2
            
        elif i == 5:  # Hip center
            point.y += math.sin(t) * 5
            
        elif i == 6:  # Left elbow
            point.x += math.sin(t + math.pi) * 25
            point.y += math.cos(t + math.pi) * 15
            
        elif i == 7:  # Left hand
            point.x += math.sin(t + math.pi) * 35
            point.y += math.cos(t + math.pi) * 25
            
        elif i == 8:  # Right elbow
            point.x += math.sin(t) * 25
            point.y += math.cos(t) * 15
            
        elif i == 9:  # Right hand
            point.x += math.sin(t) * 35
            point.y += math.cos(t) * 25
            
        elif i == 10:  # Left knee
            knee_angle = t + math.pi
            point.x += math.sin(knee_angle) * 20
            point.y += abs(math.cos(knee_angle)) * 30
            
        elif i == 11:  # Left foot
            foot_angle = t + math.pi
            point.x += math.sin(foot_angle) * 25
            point.y += max(0, math.cos(foot_angle)) * 50
            
        elif i == 12:  # Right knee
            knee_angle = t
            point.x += math.sin(knee_angle) * 20
            point.y += abs(math.cos(knee_angle)) * 30
            
        elif i == 13:  # Right foot
            foot_angle = t
            point.x += math.sin(foot_angle) * 25
            point.y += max(0, math.cos(foot_angle)) * 50
        
        # Wrap around horizontally
        if point.x > WIDTH + 50:
            point.x -= WIDTH + 100
            point.base_x -= WIDTH + 100
        elif point.base_x < -50:
            point.base_x += WIDTH + 100

# Main animation loop
frame = 0
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
    
    # Update point positions for running motion
    update_running_motion(frame)
    
    # Draw all point lights
    for point in point_lights:
        pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), 6)
    
    # Update display
    pygame.display.flip()
    clock.tick(30)  # 30 FPS
    frame += 1

pygame.quit()
