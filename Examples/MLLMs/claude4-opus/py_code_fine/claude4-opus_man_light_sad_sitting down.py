
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

class Joint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y

# Define 15 body joints for biological motion
joints = [
    Joint(WIDTH//2, HEIGHT//2 - 120),  # 0: head
    Joint(WIDTH//2, HEIGHT//2 - 80),   # 1: neck
    Joint(WIDTH//2 - 30, HEIGHT//2 - 60),  # 2: left shoulder
    Joint(WIDTH//2 + 30, HEIGHT//2 - 60),  # 3: right shoulder
    Joint(WIDTH//2 - 45, HEIGHT//2 - 20),  # 4: left elbow
    Joint(WIDTH//2 + 45, HEIGHT//2 - 20),  # 5: right elbow
    Joint(WIDTH//2 - 50, HEIGHT//2 + 10),  # 6: left wrist
    Joint(WIDTH//2 + 50, HEIGHT//2 + 10),  # 7: right wrist
    Joint(WIDTH//2, HEIGHT//2 - 40),   # 8: spine/torso
    Joint(WIDTH//2, HEIGHT//2 + 20),   # 9: pelvis
    Joint(WIDTH//2 - 20, HEIGHT//2 + 50),  # 10: left hip
    Joint(WIDTH//2 + 20, HEIGHT//2 + 50),  # 11: right hip
    Joint(WIDTH//2 - 25, HEIGHT//2 + 100),  # 12: left knee
    Joint(WIDTH//2 + 25, HEIGHT//2 + 100),  # 13: right knee
    Joint(WIDTH//2 - 30, HEIGHT//2 + 150),  # 14: left foot
]

def sitting_motion(frame, total_frames):
    """Calculate joint positions for sitting down motion"""
    progress = frame / total_frames
    
    # Smooth easing function
    ease = 1 - math.cos(progress * math.pi) / 2
    
    for i, joint in enumerate(joints):
        if i == 0:  # head - slight downward movement
            joint.y = joint.start_y + ease * 30
        elif i == 1:  # neck
            joint.y = joint.start_y + ease * 25
        elif i in [2, 3]:  # shoulders - slight drop
            joint.y = joint.start_y + ease * 20
        elif i in [4, 5]:  # elbows - move down and slightly inward
            joint.y = joint.start_y + ease * 35
            if i == 4:  # left elbow
                joint.x = joint.start_x + ease * 10
            else:  # right elbow
                joint.x = joint.start_x - ease * 10
        elif i in [6, 7]:  # wrists - rest on thighs
            joint.y = joint.start_y + ease * 60
            if i == 6:  # left wrist
                joint.x = joint.start_x + ease * 15
            else:  # right wrist
                joint.x = joint.start_x - ease * 15
        elif i == 8:  # spine/torso - lean slightly forward
            joint.y = joint.start_y + ease * 15
        elif i == 9:  # pelvis - move down significantly
            joint.y = joint.start_y + ease * 80
        elif i in [10, 11]:  # hips - move down
            joint.y = joint.start_y + ease * 75
        elif i in [12, 13]:  # knees - bend significantly
            joint.y = joint.start_y + ease * 20
            if i == 12:  # left knee
                joint.x = joint.start_x + ease * 15
            else:  # right knee
                joint.x = joint.start_x - ease * 15
        elif i == 14:  # left foot - move closer to body
            joint.y = joint.start_y - ease * 30
            joint.x = joint.start_x + ease * 20

    # Add right foot as 15th joint
    if len(joints) == 14:
        joints.append(Joint(WIDTH//2 + 30, HEIGHT//2 + 150))
    
    # Right foot movement
    joints[14].y = joints[14].start_y - ease * 30
    joints[14].x = joints[14].start_x - ease * 20

def main():
    running = True
    frame = 0
    total_frames = 90  # 3 seconds at 30 FPS
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(BLACK)
        
        # Update motion
        sitting_motion(frame % total_frames, total_frames)
        
        # Draw joints as white points
        for joint in joints:
            pygame.draw.circle(screen, WHITE, (int(joint.x), int(joint.y)), POINT_RADIUS)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
        
        frame += 1
    
    pygame.quit()

if __name__ == "__main__":
    main()
