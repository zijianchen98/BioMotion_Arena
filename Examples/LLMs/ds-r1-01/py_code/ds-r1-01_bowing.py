
import pygame
import sys
import math

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Bowing")
clock = pygame.time.Clock()

# Color definitions
black = (0, 0, 0)
white = (255, 255, 255)

# Body parameters
hip_x, hip_y = width // 2, height // 2  # Center point
torso_length = 100
shoulder_width = 40
arm_length = 40
forearm_length = 40
thigh_length = 60
shin_length = 60
speed = 0.07

def calculate_positions(theta):
    # Head
    head_x = hip_x + torso_length * math.sin(theta)
    head_y = hip_y - torso_length * math.cos(theta)
    
    # Mid-torso
    mid_torso_x = hip_x + (torso_length/2) * math.sin(theta)
    mid_torso_y = hip_y - (torso_length/2) * math.cos(theta)
    
    # Shoulders
    left_shoulder_x = mid_torso_x - (shoulder_width/2) * math.cos(theta)
    left_shoulder_y = mid_torso_y + (shoulder_width/2) * math.sin(theta)
    right_shoulder_x = mid_torso_x + (shoulder_width/2) * math.cos(theta)
    right_shoulder_y = mid_torso_y - (shoulder_width/2) * math.sin(theta)
    
    # Arms
    elbow_angle = theta + math.pi/2
    # Left arm
    left_elbow_x = left_shoulder_x + arm_length * math.cos(elbow_angle)
    left_elbow_y = left_shoulder_y + arm_length * math.sin(elbow_angle)
    left_wrist_x = left_elbow_x + forearm_length * math.cos(elbow_angle)
    left_wrist_y = left_elbow_y + forearm_length * math.sin(elbow_angle)
    # Right arm
    right_elbow_x = right_shoulder_x + arm_length * math.cos(elbow_angle)
    right_elbow_y = right_shoulder_y + arm_length * math.sin(elbow_angle)
    right_wrist_x = right_elbow_x + forearm_length * math.cos(elbow_angle)
    right_wrist_y = right_elbow_y + forearm_length * math.sin(elbow_angle)
    
    # Hips (static)
    left_hip = (hip_x - 20, hip_y)
    right_hip = (hip_x + 20, hip_y)
    
    # Legs
    knee_offset = 20 * math.sin(theta)
    # Left leg
    left_knee = (left_hip[0] + knee_offset, left_hip[1] + thigh_length)
    left_ankle = (left_knee[0], left_knee[1] + shin_length)
    # Right leg
    right_knee = (right_hip[0] + knee_offset, right_hip[1] + thigh_length)
    right_ankle = (right_knee[0], right_knee[1] + shin_length)
    
    return [
        (head_x, head_y), (left_shoulder_x, left_shoulder_y),
        (right_shoulder_x, right_shoulder_y), (left_elbow_x, left_elbow_y),
        (right_elbow_x, right_elbow_y), (left_wrist_x, left_wrist_y),
        (right_wrist_x, right_wrist_y), (mid_torso_x, mid_torso_y),
        left_hip, right_hip, left_knee, right_knee,
        left_ankle, right_ankle, (hip_x, hip_y)
    ]

time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(black)
    
    # Calculate animation phase
    theta = (math.sin(time) + 1) * math.pi/4  # Get current positions
    points = calculate_positions(theta)
    
    # Draw all points
    for x, y in points:
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)
    
    pygame.display.flip()
    clock.tick(30)
    time += speed

pygame.quit()
sys.exit()
