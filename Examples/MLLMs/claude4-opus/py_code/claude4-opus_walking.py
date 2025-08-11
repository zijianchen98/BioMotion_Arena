
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 4

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Walking")
clock = pygame.time.Clock()

# Define joint positions for a walking human (15 points)
# Based on typical biomechanical model
class WalkingHuman:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.time = 0
        
        # Define relative positions of 15 body points
        # Head, shoulders, elbows, wrists, hips, knees, ankles, feet
        self.joint_offsets = {
            'head': (0, -60),
            'left_shoulder': (-15, -40),
            'right_shoulder': (15, -40),
            'left_elbow': (-25, -20),
            'right_elbow': (25, -20),
            'left_wrist': (-30, 0),
            'right_wrist': (30, 0),
            'left_hip': (-10, 0),
            'right_hip': (10, 0),
            'left_knee': (-12, 25),
            'right_knee': (12, 25),
            'left_ankle': (-10, 50),
            'right_ankle': (10, 50),
            'left_foot': (-8, 55),
            'right_foot': (8, 55)
        }
        
    def update(self, dt):
        self.time += dt
        
    def get_joint_positions(self):
        positions = []
        
        # Walking cycle parameters
        cycle_speed = 2.0
        step_amplitude = 20
        arm_swing = 15
        vertical_bob = 3
        
        # Calculate phase for each leg (opposite phases)
        left_phase = math.sin(self.time * cycle_speed)
        right_phase = math.sin(self.time * cycle_speed + math.pi)
        
        # Body center vertical bobbing
        body_y_offset = math.sin(self.time * cycle_speed * 2) * vertical_bob
        
        for joint, (base_x, base_y) in self.joint_offsets.items():
            x = self.center_x + base_x
            y = self.center_y + base_y + body_y_offset
            
            if 'left' in joint:
                if 'hip' in joint:
                    x += left_phase * 3
                elif 'knee' in joint:
                    x += left_phase * step_amplitude * 0.3
                    y += abs(left_phase) * 8
                elif 'ankle' in joint or 'foot' in joint:
                    x += left_phase * step_amplitude * 0.5
                    y += max(0, left_phase * 12)
                elif 'shoulder' in joint:
                    x += right_phase * arm_swing * 0.3
                elif 'elbow' in joint:
                    x += right_phase * arm_swing * 0.6
                    y += abs(right_phase) * 5
                elif 'wrist' in joint:
                    x += right_phase * arm_swing * 0.8
                    y += abs(right_phase) * 8
                    
            elif 'right' in joint:
                if 'hip' in joint:
                    x += right_phase * 3
                elif 'knee' in joint:
                    x += right_phase * step_amplitude * 0.3
                    y += abs(right_phase) * 8
                elif 'ankle' in joint or 'foot' in joint:
                    x += right_phase * step_amplitude * 0.5
                    y += max(0, right_phase * 12)
                elif 'shoulder' in joint:
                    x += left_phase * arm_swing * 0.3
                elif 'elbow' in joint:
                    x += left_phase * arm_swing * 0.6
                    y += abs(left_phase) * 5
                elif 'wrist' in joint:
                    x += left_phase * arm_swing * 0.8
                    y += abs(left_phase) * 8
            
            positions.append((int(x), int(y)))
            
        return positions

# Create walking human
walker = WalkingHuman(WIDTH // 2, HEIGHT // 2)

# Main game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000.0
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Update
    walker.update(dt)
    
    # Draw
    screen.fill(BACKGROUND_COLOR)
    
    # Get joint positions and draw points
    joint_positions = walker.get_joint_positions()
    for pos in joint_positions:
        pygame.draw.circle(screen, POINT_COLOR, pos, POINT_RADIUS)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
