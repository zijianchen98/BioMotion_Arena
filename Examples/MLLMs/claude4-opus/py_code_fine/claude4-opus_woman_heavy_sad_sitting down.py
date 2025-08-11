
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Woman Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for animation timing
clock = pygame.time.Clock()
FPS = 30

class PointLight:
    def __init__(self, x, y, joint_name):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.joint_name = joint_name

# Define the 15 key body joints for biological motion
# Based on standard point-light walker configuration
joints = [
    PointLight(WIDTH//2, HEIGHT//2 - 150, "head"),           # 1. Head
    PointLight(WIDTH//2, HEIGHT//2 - 120, "neck"),           # 2. Neck
    PointLight(WIDTH//2, HEIGHT//2 - 100, "torso_upper"),    # 3. Upper torso
    PointLight(WIDTH//2, HEIGHT//2 - 60, "torso_lower"),     # 4. Lower torso
    PointLight(WIDTH//2 - 40, HEIGHT//2 - 110, "left_shoulder"), # 5. Left shoulder
    PointLight(WIDTH//2 + 40, HEIGHT//2 - 110, "right_shoulder"), # 6. Right shoulder
    PointLight(WIDTH//2 - 60, HEIGHT//2 - 80, "left_elbow"),  # 7. Left elbow
    PointLight(WIDTH//2 + 60, HEIGHT//2 - 80, "right_elbow"), # 8. Right elbow
    PointLight(WIDTH//2 - 70, HEIGHT//2 - 40, "left_wrist"),  # 9. Left wrist
    PointLight(WIDTH//2 + 70, HEIGHT//2 - 40, "right_wrist"), # 10. Right wrist
    PointLight(WIDTH//2 - 20, HEIGHT//2 - 20, "left_hip"),    # 11. Left hip
    PointLight(WIDTH//2 + 20, HEIGHT//2 - 20, "right_hip"),   # 12. Right hip
    PointLight(WIDTH//2 - 25, HEIGHT//2 + 60, "left_knee"),   # 13. Left knee
    PointLight(WIDTH//2 + 25, HEIGHT//2 + 60, "right_knee"),  # 14. Right knee
    PointLight(WIDTH//2, HEIGHT//2 + 120, "pelvis")          # 15. Pelvis/base
]

def animate_sitting_motion(frame):
    """Animate the sitting down motion for a sad, heavy woman"""
    
    # Animation parameters
    duration = 180  # frames for complete sitting motion
    progress = min(frame / duration, 1.0)
    
    # Ease-out function for more natural, heavy movement
    ease_progress = 1 - math.pow(1 - progress, 3)
    
    # Sad posture adjustments
    shoulder_droop = 15 * ease_progress  # Shoulders droop down
    head_droop = 10 * ease_progress      # Head tilts down slightly
    
    for joint in joints:
        if joint.joint_name == "head":
            joint.x = joint.start_x
            joint.y = joint.start_y + 20 * ease_progress + head_droop
            
        elif joint.joint_name == "neck":
            joint.x = joint.start_x
            joint.y = joint.start_y + 25 * ease_progress + head_droop
            
        elif joint.joint_name == "torso_upper":
            # Slight forward lean when sitting
            joint.x = joint.start_x + 5 * ease_progress
            joint.y = joint.start_y + 30 * ease_progress
            
        elif joint.joint_name == "torso_lower":
            # Lower torso moves down and slightly forward
            joint.x = joint.start_x + 8 * ease_progress
            joint.y = joint.start_y + 45 * ease_progress
            
        elif joint.joint_name == "left_shoulder":
            joint.x = joint.start_x + 5 * ease_progress
            joint.y = joint.start_y + 25 * ease_progress + shoulder_droop
            
        elif joint.joint_name == "right_shoulder":
            joint.x = joint.start_x + 5 * ease_progress
            joint.y = joint.start_y + 25 * ease_progress + shoulder_droop
            
        elif joint.joint_name == "left_elbow":
            # Arms hang more naturally when sitting
            joint.x = joint.start_x + 10 * ease_progress
            joint.y = joint.start_y + 35 * ease_progress
            
        elif joint.joint_name == "right_elbow":
            joint.x = joint.start_x + 10 * ease_progress
            joint.y = joint.start_y + 35 * ease_progress
            
        elif joint.joint_name == "left_wrist":
            # Hands rest on thighs when sitting
            joint.x = joint.start_x + 30 * ease_progress
            joint.y = joint.start_y + 60 * ease_progress
            
        elif joint.joint_name == "right_wrist":
            joint.x = joint.start_x + 30 * ease_progress
            joint.y = joint.start_y + 60 * ease_progress
            
        elif joint.joint_name == "left_hip":
            joint.x = joint.start_x
            joint.y = joint.start_y + 40 * ease_progress
            
        elif joint.joint_name == "right_hip":
            joint.x = joint.start_x
            joint.y = joint.start_y + 40 * ease_progress
            
        elif joint.joint_name == "left_knee":
            # Knees bend significantly when sitting
            knee_bend_x = -15 * math.sin(ease_progress * math.pi * 0.5)
            joint.x = joint.start_x + knee_bend_x
            joint.y = joint.start_y - 20 * ease_progress
            
        elif joint.joint_name == "right_knee":
            knee_bend_x = -15 * math.sin(ease_progress * math.pi * 0.5)
            joint.x = joint.start_x + knee_bend_x
            joint.y = joint.start_y - 20 * ease_progress
            
        elif joint.joint_name == "pelvis":
            # Pelvis moves down significantly when sitting
            joint.x = joint.start_x
            joint.y = joint.start_y - 40 * ease_progress

def main():
    running = True
    frame = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset animation
                    frame = 0
        
        # Clear screen
        screen.fill(BLACK)
        
        # Animate the sitting motion
        animate_sitting_motion(frame)
        
        # Draw all point lights
        for joint in joints:
            pygame.draw.circle(screen, WHITE, (int(joint.x), int(joint.y)), 5)
        
        # Update display
        pygame.display.flip()
        
        # Update frame counter
        frame += 1
        if frame > 300:  # Reset after complete cycle + pause
            frame = 0
        
        # Control frame rate
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
