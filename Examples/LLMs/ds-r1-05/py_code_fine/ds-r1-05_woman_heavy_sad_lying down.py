
import pygame
import math
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Woman Lying Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Initialize joint positions (15 points for the human form)
joints = [
    # Head and neck (2 points)
    [0, -200], [0, -170],
    # Shoulders and torso (4 points)
    [-40, -150], [40, -150], [-20, -120], [20, -120],
    # Arms (2 points)
    [-60, -120], [60, -120],
    # Hips (2 points)
    [-25, -50], [25, -50],
    # Legs (3 points)
    [-45, -20], [45, -20], [0, 20],
    # Feet (2 points)
    [-35, 50], [35, 50]
]

# Parameters for the lying down motion
motion_progress = 0.0
motion_speed = 0.005
gravity_influence = 0.1

def apply_motion(joints, progress):
    """Apply lying down motion to the joints with biomechanical realism"""
    new_joints = []
    
    # Base angles for lying down motion
    body_angle = math.pi * progress
    leg_angle = 0.4 * math.sin(progress * math.pi * 4)  # Subtle leg movement
    
    for i, (x, y) in enumerate(joints):
        # Center of rotation - approximate pelvis position
        center_x, center_y = 0, -50
        
        # Calculate distance from center
        dx = x - center_x
        dy = y - center_y
        
        # Apply rotational movement around the body center
        if i < 6:  # Upper body
            angle = body_angle * 0.7
            new_x = center_x + dx * math.cos(angle) - dy * math.sin(angle)
            new_y = center_y + dx * math.sin(angle) + dy * math.cos(angle)
        elif i < 12:  # Lower body
            angle = body_angle * 0.3 + leg_angle
            new_x = center_x + dx * math.cos(angle) - dy * math.sin(angle)
            new_y = center_y + dx * math.sin(angle) + dy * math.cos(angle)
        else:  # Feet
            new_x = center_x + dx * math.cos(body_angle * 0.2)
            new_y = center_y + dy + progress * 80  # Sliding feet movement
            # Heavy weight effect - feet move slower
            new_x += math.sin(progress * math.pi) * 5
            new_y += math.sin(progress * math.pi) * 3
            
        # Apply gravity influence to simulate heavy weight
        new_y += progress * 10 * gravity_influence
        
        # Apply subtle secondary movements for realism
        if i == 0:  # Head
            new_y += 5 * math.sin(progress * math.pi * 3)
        elif i in [2, 3]:  # Shoulders
            new_x += 2 * math.sin(progress * math.pi * 4)
        elif i in [8, 9]:  # Hips
            new_y += 3 * math.sin(progress * math.pi * 2)
        elif i in [6, 7]:  # Arms
            new_y += 2 * math.sin(progress * math.pi * 4)
            
        new_joints.append((new_x, new_y))
    
    return new_joints

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Update motion progress
    motion_progress += motion_speed
    if motion_progress > 1.0:
        motion_progress = 0.0  # Reset for continuous animation
    
    # Apply motion to joints
    current_joints = apply_motion(joints, motion_progress)
    
    # Draw joints (15 point-lights)
    for x, y in current_joints:
        pygame.draw.circle(screen, WHITE, (int(WIDTH/2 + x), int(HEIGHT/2 + y)), 5)
    
    # Draw connecting lines for visual reference (optional for form recognition)
    for i in range(len(current_joints)):
        if i in [0, 2, 4, 6, 8, 10, 12]:
            pygame.draw.line(screen, WHITE, 
                            (int(WIDTH/2 + current_joints[i][0]), int(HEIGHT/2 + current_joints[i][1])),
                            (int(WIDTH/2 + current_joints[i+1][0]), int(HEIGHT/2 + current_joints[i+1][1])), 1)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
