
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30
POINT_RADIUS = 8

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sitting Down")
clock = pygame.time.Clock()

# Define 15 body joints for biological motion
class BodyJoint:
    def __init__(self, x, y, name):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.name = name

# Initialize body joints in standing position (centered)
center_x, center_y = WIDTH // 2, HEIGHT // 2 - 100

joints = [
    BodyJoint(center_x, center_y - 100, "head"),           # 0
    BodyJoint(center_x, center_y - 60, "neck"),            # 1
    BodyJoint(center_x - 30, center_y - 40, "left_shoulder"), # 2
    BodyJoint(center_x + 30, center_y - 40, "right_shoulder"), # 3
    BodyJoint(center_x - 40, center_y, "left_elbow"),      # 4
    BodyJoint(center_x + 40, center_y, "right_elbow"),     # 5
    BodyJoint(center_x - 50, center_y + 40, "left_hand"),  # 6
    BodyJoint(center_x + 50, center_y + 40, "right_hand"), # 7
    BodyJoint(center_x, center_y - 20, "spine"),           # 8
    BodyJoint(center_x, center_y + 40, "pelvis"),          # 9
    BodyJoint(center_x - 20, center_y + 80, "left_hip"),   # 10
    BodyJoint(center_x + 20, center_y + 80, "right_hip"),  # 11
    BodyJoint(center_x - 25, center_y + 140, "left_knee"), # 12
    BodyJoint(center_x + 25, center_y + 140, "right_knee"), # 13
    BodyJoint(center_x, center_y + 200, "pelvis_base"),    # 14
]

def interpolate(start, end, t):
    """Linear interpolation between start and end values"""
    return start + (end - start) * t

def ease_in_out(t):
    """Smooth easing function"""
    return t * t * (3.0 - 2.0 * t)

def update_sitting_animation(frame, total_frames):
    """Update joint positions for sitting down animation"""
    progress = ease_in_out(frame / total_frames)
    
    # Heavy person sitting down - more pronounced movements
    for i, joint in enumerate(joints):
        if joint.name == "head":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 40, progress)
            
        elif joint.name == "neck":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 45, progress)
            
        elif joint.name == "left_shoulder":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 50, progress)
            joints[i].x = interpolate(joint.start_x, joint.start_x - 10, progress)
            
        elif joint.name == "right_shoulder":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 50, progress)
            joints[i].x = interpolate(joint.start_x, joint.start_x + 10, progress)
            
        elif joint.name == "left_elbow":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 60, progress)
            joints[i].x = interpolate(joint.start_x, joint.start_x - 5, progress)
            
        elif joint.name == "right_elbow":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 60, progress)
            joints[i].x = interpolate(joint.start_x, joint.start_x + 5, progress)
            
        elif joint.name == "left_hand":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 70, progress)
            
        elif joint.name == "right_hand":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 70, progress)
            
        elif joint.name == "spine":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 55, progress)
            
        elif joint.name == "pelvis":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 80, progress)
            
        elif joint.name == "left_hip":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 85, progress)
            joints[i].x = interpolate(joint.start_x, joint.start_x - 10, progress)
            
        elif joint.name == "right_hip":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 85, progress)
            joints[i].x = interpolate(joint.start_x, joint.start_x + 10, progress)
            
        elif joint.name == "left_knee":
            # Knees bend significantly when sitting
            joints[i].y = interpolate(joint.start_y, joint.start_y + 30, progress)
            joints[i].x = interpolate(joint.start_x, joint.start_x - 15, progress)
            
        elif joint.name == "right_knee":
            joints[i].y = interpolate(joint.start_y, joint.start_y + 30, progress)
            joints[i].x = interpolate(joint.start_x, joint.start_x + 15, progress)
            
        elif joint.name == "pelvis_base":
            # Feet/ankles stay relatively stable
            joints[i].y = interpolate(joint.start_y, joint.start_y - 20, progress)

def draw_points():
    """Draw all joint points"""
    for joint in joints:
        pygame.draw.circle(screen, WHITE, (int(joint.x), int(joint.y)), POINT_RADIUS)

# Main animation loop
running = True
frame = 0
total_frames = 90  # 3 seconds at 30 FPS
cycle_complete = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Update animation
    if not cycle_complete:
        update_sitting_animation(frame, total_frames)
        frame += 1
        
        if frame >= total_frames:
            cycle_complete = True
            frame = 0
    else:
        # Hold final position for a moment, then restart
        frame += 1
        if frame > 30:  # Hold for 1 second
            frame = 0
            cycle_complete = False
            # Reset joints to starting positions
            for i, joint in enumerate(joints):
                joint.x = joint.start_x
                joint.y = joint.start_y
    
    # Draw points
    draw_points()
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
