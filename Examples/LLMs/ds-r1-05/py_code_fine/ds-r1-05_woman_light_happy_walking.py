
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 3
FPS = 60

# Body parameters
torso_height = 100
thigh_length = 40
shin_length = 40
upper_arm_length = 30
forearm_length = 30
shoulder_width = 60
hip_width = 40
head_y_offset = 50
amplitude_leg = 0.8  # radians (max thigh angle)
amplitude_arm = 0.5  # radians (max arm angle)
speed = 200  # pixels per second
bounce_amplitude = 20
freq = 2.0  # steps per second

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Walker Animation")
clock = pygame.time.Clock()

# Initial positions
start_x = 0
base_y = SCREEN_HEIGHT // 2
t = 0.0

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Calculate time delta
    dt = clock.tick(FPS) / 1000.0
    t += dt
    
    # Update root position (hip center) with bounce
    root_x = start_x + speed * t
    root_y = base_y + bounce_amplitude * math.sin(2 * math.pi * freq * t)
    
    # Reset position when off-screen
    if root_x > SCREEN_WIDTH:
        t = 0.0
    
    # Calculate limb angles
    angle_left_leg = amplitude_leg * math.sin(2 * math.pi * freq * t)
    angle_right_leg = amplitude_leg * math.sin(2 * math.pi * freq * t + math.pi)
    angle_left_arm = amplitude_arm * math.sin(2 * math.pi * freq * t + math.pi)
    angle_right_arm = amplitude_arm * math.sin(2 * math.pi * freq * t)
    
    # Calculate limb bend angles
    knee_bend_left = -0.5 * abs(angle_left_leg)
    knee_bend_right = -0.5 * abs(angle_right_leg)
    elbow_bend_left = -0.3 * abs(angle_left_arm)
    elbow_bend_right = -0.3 * abs(angle_right_arm)
    
    # Torso points
    torso_upper = (root_x, root_y - torso_height)
    torso_lower = (root_x, root_y)
    
    # Head
    head = (root_x, torso_upper[1] - head_y_offset)
    
    # Shoulders
    left_shoulder = (root_x - shoulder_width / 2, torso_upper[1])
    right_shoulder = (root_x + shoulder_width / 2, torso_upper[1])
    
    # Hips
    left_hip = (root_x - hip_width / 2, root_y)
    right_hip = (root_x + hip_width / 2, root_y)
    
    # Left leg
    left_knee = (
        left_hip[0] + thigh_length * math.sin(angle_left_leg),
        left_hip[1] + thigh_length * math.cos(angle_left_leg)
    )
    left_ankle = (
        left_knee[0] + shin_length * math.sin(angle_left_leg + knee_bend_left),
        left_knee[1] + shin_length * math.cos(angle_left_leg + knee_bend_left)
    )
    
    # Right leg
    right_knee = (
        right_hip[0] + thigh_length * math.sin(angle_right_leg),
        right_hip[1] + thigh_length * math.cos(angle_right_leg)
    )
    right_ankle = (
        right_knee[0] + shin_length * math.sin(angle_right_leg + knee_bend_right),
        right_knee[1] + shin_length * math.cos(angle_right_leg + knee_bend_right)
    )
    
    # Left arm
    left_elbow = (
        left_shoulder[0] + upper_arm_length * math.sin(angle_left_arm),
        left_shoulder[1] + upper_arm_length * math.cos(angle_left_arm)
    )
    left_wrist = (
        left_elbow[0] + forearm_length * math.sin(angle_left_arm + elbow_bend_left),
        left_elbow[1] + forearm_length * math.cos(angle_left_arm + elbow_bend_left)
    )
    
    # Right arm
    right_elbow = (
        right_shoulder[0] + upper_arm_length * math.sin(angle_right_arm),
        right_shoulder[1] + upper_arm_length * math.cos(angle_right_arm)
    )
    right_wrist = (
        right_elbow[0] + forearm_length * math.sin(angle_right_arm + elbow_bend_right),
        right_elbow[1] + forearm_length * math.cos(angle_right_arm + elbow_bend_right)
    )
    
    # Neck
    neck = (root_x, root_y - torso_height // 2)
    
    # All 15 points
    points = [
        head, neck, 
        left_shoulder, right_shoulder, 
        left_elbow, right_elbow, 
        left_wrist, right_wrist, 
        left_hip, right_hip, 
        left_knee, right_knee, 
        left_ankle, right_ankle, 
        torso_lower
    ]
    
    # Draw background
    screen.fill(BACKGROUND_COLOR)
    
    # Draw points
    for point in points:
        pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), POINT_RADIUS)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
