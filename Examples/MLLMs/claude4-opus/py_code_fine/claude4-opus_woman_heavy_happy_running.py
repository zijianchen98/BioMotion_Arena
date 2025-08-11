
import pygame
import math
import numpy as np

pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Heavy Woman Running")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 30
clock = pygame.time.Clock()

# Center position
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Point-light positions for a human figure (15 points)
# Head, shoulders, elbows, wrists, hips, knees, ankles, torso points
point_names = [
    "head", "neck", "left_shoulder", "right_shoulder", 
    "left_elbow", "right_elbow", "left_wrist", "right_wrist",
    "left_hip", "right_hip", "left_knee", "right_knee", 
    "left_ankle", "right_ankle", "torso"
]

# Base positions relative to center (for a standing figure)
base_positions = {
    "head": (0, -80),
    "neck": (0, -60),
    "left_shoulder": (-20, -50),
    "right_shoulder": (20, -50),
    "left_elbow": (-35, -20),
    "right_elbow": (35, -20),
    "left_wrist": (-45, 10),
    "right_wrist": (45, 10),
    "torso": (0, -25),
    "left_hip": (-15, 20),
    "right_hip": (15, 20),
    "left_knee": (-20, 60),
    "right_knee": (20, 60),
    "left_ankle": (-25, 100),
    "right_ankle": (25, 100)
}

def get_running_motion(frame, heavy_weight=True):
    """Calculate point positions for running motion with heavy weight characteristics"""
    time = frame * 0.1
    
    # Running cycle parameters
    cycle_speed = 1.8 if heavy_weight else 2.5  # Slower for heavy weight
    leg_lift = 25 if heavy_weight else 35  # Less leg lift for heavy weight
    arm_swing = 30 if heavy_weight else 40  # Less arm swing
    torso_lean = 8 if heavy_weight else 5  # More forward lean
    
    # Phase calculations for different body parts
    leg_phase = time * cycle_speed
    arm_phase = leg_phase + math.pi  # Arms opposite to legs
    
    # Vertical bobbing (more pronounced for heavy weight)
    vertical_bob = math.sin(leg_phase * 2) * (8 if heavy_weight else 5)
    
    # Horizontal sway (more for heavy weight)
    horizontal_sway = math.sin(leg_phase) * (4 if heavy_weight else 2)
    
    positions = {}
    
    # Head and neck with bobbing and forward lean
    positions["head"] = (
        base_positions["head"][0] + horizontal_sway + torso_lean,
        base_positions["head"][1] + vertical_bob
    )
    positions["neck"] = (
        base_positions["neck"][0] + horizontal_sway + torso_lean,
        base_positions["neck"][1] + vertical_bob
    )
    
    # Torso with lean and bob
    positions["torso"] = (
        base_positions["torso"][0] + horizontal_sway + torso_lean,
        base_positions["torso"][1] + vertical_bob
    )
    
    # Arms swinging
    left_arm_swing = math.sin(arm_phase) * arm_swing
    right_arm_swing = -left_arm_swing
    
    # Shoulders
    positions["left_shoulder"] = (
        base_positions["left_shoulder"][0] + horizontal_sway + torso_lean,
        base_positions["left_shoulder"][1] + vertical_bob
    )
    positions["right_shoulder"] = (
        base_positions["right_shoulder"][0] + horizontal_sway + torso_lean,
        base_positions["right_shoulder"][1] + vertical_bob
    )
    
    # Elbows
    positions["left_elbow"] = (
        base_positions["left_elbow"][0] + left_arm_swing/2 + horizontal_sway + torso_lean,
        base_positions["left_elbow"][1] + vertical_bob - abs(left_arm_swing)/4
    )
    positions["right_elbow"] = (
        base_positions["right_elbow"][0] + right_arm_swing/2 + horizontal_sway + torso_lean,
        base_positions["right_elbow"][1] + vertical_bob - abs(right_arm_swing)/4
    )
    
    # Wrists
    positions["left_wrist"] = (
        base_positions["left_wrist"][0] + left_arm_swing + horizontal_sway + torso_lean,
        base_positions["left_wrist"][1] + vertical_bob - abs(left_arm_swing)/3
    )
    positions["right_wrist"] = (
        base_positions["right_wrist"][0] + right_arm_swing + horizontal_sway + torso_lean,
        base_positions["right_wrist"][1] + vertical_bob - abs(right_arm_swing)/3
    )
    
    # Legs running motion
    left_leg_phase = leg_phase
    right_leg_phase = leg_phase + math.pi
    
    # Hips
    positions["left_hip"] = (
        base_positions["left_hip"][0] + horizontal_sway,
        base_positions["left_hip"][1] + vertical_bob
    )
    positions["right_hip"] = (
        base_positions["right_hip"][0] + horizontal_sway,
        base_positions["right_hip"][1] + vertical_bob
    )
    
    # Knees with running motion
    left_knee_lift = max(0, math.sin(left_leg_phase)) * leg_lift
    right_knee_lift = max(0, math.sin(right_leg_phase)) * leg_lift
    
    positions["left_knee"] = (
        base_positions["left_knee"][0] + horizontal_sway + math.sin(left_leg_phase) * 5,
        base_positions["left_knee"][1] + vertical_bob - left_knee_lift
    )
    positions["right_knee"] = (
        base_positions["right_knee"][0] + horizontal_sway + math.sin(right_leg_phase) * 5,
        base_positions["right_knee"][1] + vertical_bob - right_knee_lift
    )
    
    # Ankles with running stride
    left_ankle_lift = max(0, math.sin(left_leg_phase + 0.3)) * (leg_lift * 0.7)
    right_ankle_lift = max(0, math.sin(right_leg_phase + 0.3)) * (leg_lift * 0.7)
    
    positions["left_ankle"] = (
        base_positions["left_ankle"][0] + horizontal_sway + math.sin(left_leg_phase) * 10,
        base_positions["left_ankle"][1] + vertical_bob - left_ankle_lift
    )
    positions["right_ankle"] = (
        base_positions["right_ankle"][0] + horizontal_sway + math.sin(right_leg_phase) * 10,
        base_positions["right_ankle"][1] + vertical_bob - right_ankle_lift
    )
    
    return positions

def main():
    running = True
    frame = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Clear screen
        screen.fill(BLACK)
        
        # Get current frame positions
        positions = get_running_motion(frame, heavy_weight=True)
        
        # Draw point-lights
        for point_name in point_names:
            if point_name in positions:
                x = center_x + positions[point_name][0]
                y = center_y + positions[point_name][1]
                pygame.draw.circle(screen, WHITE, (int(x), int(y)), 4)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
        frame += 1
    
    pygame.quit()

if __name__ == "__main__":
    main()
