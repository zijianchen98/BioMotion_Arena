
import pygame
import math
import numpy as np

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Running Person")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

class PointLightWalker:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.frame = 0
        self.speed = 0.1
        
        # 15 joint positions representing a human figure
        # [head, neck, left_shoulder, right_shoulder, left_elbow, right_elbow,
        #  left_wrist, right_wrist, spine, left_hip, right_hip, left_knee, 
        #  right_knee, left_ankle, right_ankle]
        
        # Base positions for a standing person (relative to center)
        self.base_positions = [
            (0, -100),     # head
            (0, -80),      # neck
            (-20, -60),    # left shoulder
            (20, -60),     # right shoulder
            (-35, -40),    # left elbow
            (35, -40),     # right elbow
            (-45, -20),    # left wrist
            (45, -20),     # right wrist
            (0, -40),      # spine
            (-12, 0),      # left hip
            (12, 0),       # right hip
            (-15, 40),     # left knee
            (15, 40),      # right knee
            (-18, 80),     # left ankle
            (18, 80)       # right ankle
        ]
        
    def update(self):
        self.frame += self.speed * 2  # Running is faster than walking
        
    def get_positions(self):
        positions = []
        t = self.frame
        
        # Running cycle parameters
        leg_swing = 25 * math.sin(t)
        arm_swing = 20 * math.sin(t + math.pi)  # Arms opposite to legs
        torso_lean = 5 * math.sin(t * 2)
        vertical_bob = 8 * abs(math.sin(t))
        
        # Head - bobs with running
        head_x = self.center_x + torso_lean * 0.3
        head_y = self.center_y + self.base_positions[0][1] - vertical_bob
        positions.append((head_x, head_y))
        
        # Neck - follows head but less movement
        neck_x = self.center_x + torso_lean * 0.2
        neck_y = self.center_y + self.base_positions[1][1] - vertical_bob * 0.8
        positions.append((neck_x, neck_y))
        
        # Left shoulder - arm swing
        ls_x = self.center_x + self.base_positions[2][0] + arm_swing * 0.3
        ls_y = self.center_y + self.base_positions[2][1] - vertical_bob * 0.6
        positions.append((ls_x, ls_y))
        
        # Right shoulder - opposite arm swing
        rs_x = self.center_x + self.base_positions[3][0] - arm_swing * 0.3
        rs_y = self.center_y + self.base_positions[3][1] - vertical_bob * 0.6
        positions.append((rs_x, rs_y))
        
        # Left elbow - more pronounced arm swing
        le_x = self.center_x + self.base_positions[4][0] + arm_swing * 0.8
        le_y = self.center_y + self.base_positions[4][1] - vertical_bob * 0.4
        positions.append((le_x, le_y))
        
        # Right elbow - opposite swing
        re_x = self.center_x + self.base_positions[5][0] - arm_swing * 0.8
        re_y = self.center_y + self.base_positions[5][1] - vertical_bob * 0.4
        positions.append((re_x, re_y))
        
        # Left wrist - maximum arm swing
        lw_x = self.center_x + self.base_positions[6][0] + arm_swing * 1.2
        lw_y = self.center_y + self.base_positions[6][1] - vertical_bob * 0.2
        positions.append((lw_x, lw_y))
        
        # Right wrist - opposite maximum swing
        rw_x = self.center_x + self.base_positions[7][0] - arm_swing * 1.2
        rw_y = self.center_y + self.base_positions[7][1] - vertical_bob * 0.2
        positions.append((rw_x, rw_y))
        
        # Spine - slight forward lean and bobbing
        spine_x = self.center_x + torso_lean
        spine_y = self.center_y + self.base_positions[8][1] - vertical_bob * 0.5
        positions.append((spine_x, spine_y))
        
        # Left hip - leg swing
        lh_x = self.center_x + self.base_positions[9][0] + leg_swing * 0.2
        lh_y = self.center_y + self.base_positions[9][1] - vertical_bob * 0.3
        positions.append((lh_x, lh_y))
        
        # Right hip - opposite leg swing
        rh_x = self.center_x + self.base_positions[10][0] - leg_swing * 0.2
        rh_y = self.center_y + self.base_positions[10][1] - vertical_bob * 0.3
        positions.append((rh_x, rh_y))
        
        # Left knee - pronounced leg swing with bend
        knee_bend = 15 * abs(math.sin(t))
        lk_x = self.center_x + self.base_positions[11][0] + leg_swing * 0.8
        lk_y = self.center_y + self.base_positions[11][1] - knee_bend
        positions.append((lk_x, lk_y))
        
        # Right knee - opposite swing
        rk_x = self.center_x + self.base_positions[12][0] - leg_swing * 0.8
        rk_y = self.center_y + self.base_positions[12][1] - knee_bend * math.cos(t)
        positions.append((rk_x, rk_y))
        
        # Left ankle - maximum leg swing with lift
        foot_lift = 20 * max(0, math.sin(t))
        la_x = self.center_x + self.base_positions[13][0] + leg_swing * 1.2
        la_y = self.center_y + self.base_positions[13][1] - foot_lift
        positions.append((la_x, la_y))
        
        # Right ankle - opposite maximum swing
        ra_x = self.center_x + self.base_positions[14][0] - leg_swing * 1.2
        ra_y = self.center_y + self.base_positions[14][1] - foot_lift * math.cos(t)
        positions.append((ra_x, ra_y))
        
        return positions

# Create walker instance
walker = PointLightWalker(WIDTH // 2, HEIGHT // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Update
    walker.update()
    
    # Draw
    screen.fill(BLACK)
    
    # Get current positions and draw points
    positions = walker.get_positions()
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 4)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
