
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30
POINT_RADIUS = 5

# Create the display window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Man Sitting Down")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, name):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.name = name

# Define 15 key body points for a human figure
points = [
    PointLight(200, 100, "head"),           # 0 - head
    PointLight(200, 140, "neck"),           # 1 - neck
    PointLight(200, 180, "torso_top"),      # 2 - upper torso
    PointLight(200, 220, "torso_mid"),      # 3 - mid torso
    PointLight(200, 260, "torso_bottom"),   # 4 - lower torso
    PointLight(170, 160, "left_shoulder"),  # 5 - left shoulder
    PointLight(230, 160, "right_shoulder"), # 6 - right shoulder
    PointLight(150, 200, "left_elbow"),     # 7 - left elbow
    PointLight(250, 200, "right_elbow"),    # 8 - right elbow
    PointLight(140, 240, "left_hand"),      # 9 - left hand
    PointLight(260, 240, "right_hand"),     # 10 - right hand
    PointLight(180, 280, "left_hip"),       # 11 - left hip
    PointLight(220, 280, "right_hip"),      # 12 - right hip
    PointLight(160, 350, "left_knee"),      # 13 - left knee
    PointLight(240, 350, "right_knee"),     # 14 - right knee
]

def update_sitting_animation(frame):
    # Animation parameters
    total_frames = 120
    progress = frame / total_frames
    
    # Sitting motion progress (0 to 1)
    sit_progress = min(1.0, progress * 1.5)
    
    # Ease-out function for natural movement
    eased_progress = 1 - (1 - sit_progress) ** 3
    
    # Head movement - slight forward lean and down
    points[0].x = points[0].start_x + math.sin(eased_progress * math.pi * 0.3) * 8
    points[0].y = points[0].start_y + eased_progress * 15
    
    # Neck follows head
    points[1].x = points[1].start_x + math.sin(eased_progress * math.pi * 0.3) * 6
    points[1].y = points[1].start_y + eased_progress * 12
    
    # Torso - bends forward and compresses vertically
    bend_amount = eased_progress * 0.4
    points[2].x = points[2].start_x + math.sin(bend_amount * math.pi) * 10
    points[2].y = points[2].start_y + eased_progress * 8
    
    points[3].x = points[3].start_x + math.sin(bend_amount * math.pi) * 12
    points[3].y = points[3].start_y + eased_progress * 6
    
    points[4].x = points[4].start_x + math.sin(bend_amount * math.pi) * 8
    points[4].y = points[4].start_y + eased_progress * 4
    
    # Shoulders - droop and move forward with sad posture
    droop_amount = eased_progress * 15
    points[5].x = points[5].start_x - eased_progress * 5  # left shoulder
    points[5].y = points[5].start_y + droop_amount
    
    points[6].x = points[6].start_x + eased_progress * 5  # right shoulder
    points[6].y = points[6].start_y + droop_amount
    
    # Arms - hang down heavily
    arm_hang = eased_progress * 20
    points[7].x = points[7].start_x - eased_progress * 8   # left elbow
    points[7].y = points[7].start_y + arm_hang
    
    points[8].x = points[8].start_x + eased_progress * 8   # right elbow
    points[8].y = points[8].start_y + arm_hang
    
    points[9].x = points[9].start_x - eased_progress * 10  # left hand
    points[9].y = points[9].start_y + arm_hang + 10
    
    points[10].x = points[10].start_x + eased_progress * 10 # right hand
    points[10].y = points[10].start_y + arm_hang + 10
    
    # Hips - move down and slightly back
    hip_drop = eased_progress * 40
    points[11].x = points[11].start_x - eased_progress * 3  # left hip
    points[11].y = points[11].start_y + hip_drop
    
    points[12].x = points[12].start_x + eased_progress * 3  # right hip
    points[12].y = points[12].start_y + hip_drop
    
    # Knees - bend significantly for sitting position
    knee_bend = eased_progress * 80
    knee_forward = eased_progress * 25
    
    points[13].x = points[13].start_x - knee_forward  # left knee
    points[13].y = points[13].start_y + knee_bend
    
    points[14].x = points[14].start_x - knee_forward  # right knee
    points[14].y = points[14].start_y + knee_bend
    
    # Add subtle breathing motion for realism
    breath = math.sin(frame * 0.2) * 2 * (1 - eased_progress * 0.7)
    for i in range(2, 5):  # torso points
        points[i].y += breath

def main():
    running = True
    frame = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(BLACK)
        
        # Update animation
        update_sitting_animation(frame)
        
        # Draw points
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), POINT_RADIUS)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
        
        frame += 1
        if frame > 180:  # Reset animation after completion
            frame = 0
    
    pygame.quit()

if __name__ == "__main__":
    main()
