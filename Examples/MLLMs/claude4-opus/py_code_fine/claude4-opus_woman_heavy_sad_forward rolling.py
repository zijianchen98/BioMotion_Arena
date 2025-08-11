
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Forward Rolling")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, joint_name):
        self.x = x
        self.y = y
        self.joint_name = joint_name
        
    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), 5)

def get_rolling_motion_frame(frame, total_frames):
    """Generate positions for 15 joint points during forward rolling motion"""
    # Base position that moves forward during roll
    base_x = WIDTH // 2 + (frame / total_frames) * 200 - 100
    base_y = HEIGHT // 2
    
    # Rolling angle
    roll_angle = (frame / total_frames) * 4 * math.pi  # 2 full rotations
    
    # Body center offset during roll
    body_center_y = base_y - 30 + 40 * math.sin(roll_angle * 0.5)
    
    # Define relative positions for 15 joints
    joint_positions = []
    
    # Phase of rolling motion
    phase = roll_angle
    
    # Head
    head_offset_x = 25 * math.cos(phase + math.pi)
    head_offset_y = 25 * math.sin(phase + math.pi)
    joint_positions.append((base_x + head_offset_x, body_center_y + head_offset_y))
    
    # Neck
    neck_offset_x = 15 * math.cos(phase + math.pi)
    neck_offset_y = 15 * math.sin(phase + math.pi)
    joint_positions.append((base_x + neck_offset_x, body_center_y + neck_offset_y))
    
    # Shoulders
    shoulder_width = 20
    left_shoulder_x = base_x + shoulder_width * math.cos(phase + math.pi/2)
    left_shoulder_y = body_center_y + shoulder_width * math.sin(phase + math.pi/2)
    right_shoulder_x = base_x + shoulder_width * math.cos(phase - math.pi/2)
    right_shoulder_y = body_center_y + shoulder_width * math.sin(phase - math.pi/2)
    joint_positions.append((left_shoulder_x, left_shoulder_y))
    joint_positions.append((right_shoulder_x, right_shoulder_y))
    
    # Elbows
    elbow_extend = 25
    left_elbow_x = left_shoulder_x + elbow_extend * math.cos(phase + math.pi/4)
    left_elbow_y = left_shoulder_y + elbow_extend * math.sin(phase + math.pi/4)
    right_elbow_x = right_shoulder_x + elbow_extend * math.cos(phase - math.pi/4)
    right_elbow_y = right_shoulder_y + elbow_extend * math.sin(phase - math.pi/4)
    joint_positions.append((left_elbow_x, left_elbow_y))
    joint_positions.append((right_elbow_x, right_elbow_y))
    
    # Hands
    hand_extend = 20
    left_hand_x = left_elbow_x + hand_extend * math.cos(phase + math.pi/6)
    left_hand_y = left_elbow_y + hand_extend * math.sin(phase + math.pi/6)
    right_hand_x = right_elbow_x + hand_extend * math.cos(phase - math.pi/6)
    right_hand_y = right_elbow_y + hand_extend * math.sin(phase - math.pi/6)
    joint_positions.append((left_hand_x, left_hand_y))
    joint_positions.append((right_hand_x, right_hand_y))
    
    # Spine/torso
    spine_offset_x = 5 * math.cos(phase + math.pi)
    spine_offset_y = 5 * math.sin(phase + math.pi)
    joint_positions.append((base_x + spine_offset_x, body_center_y + spine_offset_y))
    
    # Hips
    hip_width = 15
    left_hip_x = base_x + hip_width * math.cos(phase + math.pi/2)
    left_hip_y = body_center_y + hip_width * math.sin(phase + math.pi/2) + 20
    right_hip_x = base_x + hip_width * math.cos(phase - math.pi/2)
    right_hip_y = body_center_y + hip_width * math.sin(phase - math.pi/2) + 20
    joint_positions.append((left_hip_x, left_hip_y))
    joint_positions.append((right_hip_x, right_hip_y))
    
    # Knees
    knee_extend = 30
    left_knee_x = left_hip_x + knee_extend * math.cos(phase + 3*math.pi/4)
    left_knee_y = left_hip_y + knee_extend * math.sin(phase + 3*math.pi/4)
    right_knee_x = right_hip_x + knee_extend * math.cos(phase - 3*math.pi/4)
    right_knee_y = right_hip_y + knee_extend * math.sin(phase - 3*math.pi/4)
    joint_positions.append((left_knee_x, left_knee_y))
    joint_positions.append((right_knee_x, right_knee_y))
    
    # Feet
    foot_extend = 25
    left_foot_x = left_knee_x + foot_extend * math.cos(phase + math.pi/3)
    left_foot_y = left_knee_y + foot_extend * math.sin(phase + math.pi/3)
    right_foot_x = right_knee_x + foot_extend * math.cos(phase - math.pi/3)
    right_foot_y = right_knee_y + foot_extend * math.sin(phase - math.pi/3)
    joint_positions.append((left_foot_x, left_foot_y))
    joint_positions.append((right_foot_x, right_foot_y))
    
    return joint_positions

def main():
    running = True
    frame = 0
    total_frames = 120  # 2 seconds at 60 FPS
    
    joint_names = [
        "head", "neck", "left_shoulder", "right_shoulder",
        "left_elbow", "right_elbow", "left_hand", "right_hand",
        "spine", "left_hip", "right_hip", "left_knee", "right_knee",
        "left_foot", "right_foot"
    ]
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(BLACK)
        
        # Get current frame positions
        positions = get_rolling_motion_frame(frame, total_frames)
        
        # Create and draw point lights
        point_lights = []
        for i, (x, y) in enumerate(positions):
            point_light = PointLight(x, y, joint_names[i])
            point_lights.append(point_light)
            point_light.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Update frame
        frame = (frame + 1) % total_frames
        
        # Control frame rate
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
