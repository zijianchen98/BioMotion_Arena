
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Walker")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

def calculate_positions(t):
    points = []
    
    # Hip center movement
    hip_center_x = width/2 + 30 * math.sin(t)
    hip_center_y = height/2 + 10 * math.sin(2*t)
    
    # Hips
    left_hip_x = hip_center_x - 20
    left_hip_y = hip_center_y
    right_hip_x = hip_center_x + 20
    right_hip_y = hip_center_y
    
    # Left leg
    thigh_angle_left = math.sin(t) * 0.5
    knee_left_x = left_hip_x + 50 * math.sin(thigh_angle_left)
    knee_left_y = left_hip_y - 50 * math.cos(thigh_angle_left)
    lower_leg_angle_left = thigh_angle_left + math.sin(t + 0.5) * 0.3
    ankle_left_x = knee_left_x + 50 * math.sin(lower_leg_angle_left)
    ankle_left_y = knee_left_y - 50 * math.cos(lower_leg_angle_left)
    
    # Right leg
    thigh_angle_right = math.sin(t + math.pi) * 0.5
    knee_right_x = right_hip_x + 50 * math.sin(thigh_angle_right)
    knee_right_y = right_hip_y - 50 * math.cos(thigh_angle_right)
    lower_leg_angle_right = thigh_angle_right + math.sin(t + 0.5 + math.pi) * 0.3
    ankle_right_x = knee_right_x + 50 * math.sin(lower_leg_angle_right)
    ankle_right_y = knee_right_y - 50 * math.cos(lower_leg_angle_right)
    
    # Upper body
    neck_x = hip_center_x
    neck_y = hip_center_y - 100
    head_x = neck_x
    head_y = neck_y - 30 + 5 * math.sin(t * 2)
    
    # Shoulders
    left_shoulder_x = neck_x - 40
    left_shoulder_y = neck_y + 30
    right_shoulder_x = neck_x + 40
    right_shoulder_y = neck_y + 30
    
    # Left arm
    arm_angle_left = math.sin(t + math.pi) * 0.7
    elbow_left_x = left_shoulder_x + 40 * math.sin(arm_angle_left)
    elbow_left_y = left_shoulder_y + 40 * math.cos(arm_angle_left)
    lower_arm_angle_left = arm_angle_left + math.sin(t + 0.5) * 0.3
    hand_left_x = elbow_left_x + 40 * math.sin(lower_arm_angle_left)
    hand_left_y = elbow_left_y + 40 * math.cos(lower_arm_angle_left)
    
    # Right arm
    arm_angle_right = math.sin(t) * 0.7
    elbow_right_x = right_shoulder_x + 40 * math.sin(arm_angle_right)
    elbow_right_y = right_shoulder_y + 40 * math.cos(arm_angle_right)
    lower_arm_angle_right = arm_angle_right + math.sin(t + 0.5) * 0.3
    hand_right_x = elbow_right_x + 40 * math.sin(lower_arm_angle_right)
    hand_right_y = elbow_right_y + 40 * math.cos(lower_arm_angle_right)
    
    # Torso
    torso_x = hip_center_x
    torso_y = (neck_y + hip_center_y) / 2
    
    # Collect all 15 points
    points = [
        (head_x, head_y),          # Head
        (neck_x, neck_y),          # Neck
        (left_shoulder_x, left_shoulder_y),  # Left shoulder
        (right_shoulder_x, right_shoulder_y),# Right shoulder
        (elbow_left_x, elbow_left_y),        # Left elbow
        (elbow_right_x, elbow_right_y),      # Right elbow
        (hand_left_x, hand_left_y),          # Left hand
        (hand_right_x, hand_right_y),        # Right hand
        (torso_x, torso_y),                  # Torso
        (left_hip_x, left_hip_y),            # Left hip
        (right_hip_x, right_hip_y),          # Right hip
        (knee_left_x, knee_left_y),          # Left knee
        (knee_right_x, knee_right_y),        # Right knee
        (ankle_left_x, ankle_left_y),        # Left ankle
        (ankle_right_x, ankle_right_y)       # Right ankle
    ]
    
    return points

# Animation loop
t = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(black)
    points = calculate_positions(t)
    
    # Draw all points
    for point in points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 5)
    
    pygame.display.flip()
    clock.tick(30)
    t += 0.1
