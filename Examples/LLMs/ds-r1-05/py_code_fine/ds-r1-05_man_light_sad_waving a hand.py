
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Body parameters
body_center = (width // 2, height // 2)
amplitude = math.radians(40)  # Waving amplitude
period = 0.8  # Wave period in seconds
frame_rate = 60

# Right arm segments
upper_arm_length = 50
forearm_length = 40
hand_length = 20

# Initialize positions
shoulder_pos = (body_center[0] + 40, body_center[1] - 50)
left_shoulder_pos = (body_center[0] - 40, body_center[1] - 50)
head_pos = (body_center[0], body_center[1] - 100)
left_hip = (body_center[0] - 40, body_center[1] + 50)
right_hip = (body_center[0] + 40, body_center[1] + 50)

# Static points positions
static_points = {
    'head': head_pos,
    'left_shoulder': left_shoulder_pos,
    'left_elbow': (left_shoulder_pos[0], left_shoulder_pos[1] + upper_arm_length),
    'left_wrist': (left_shoulder_pos[0], left_shoulder_pos[1] + upper_arm_length + forearm_length),
    'left_hand': (left_shoulder_pos[0], left_shoulder_pos[1] + upper_arm_length + forearm_length + hand_length),
    'left_hip': left_hip,
    'right_hip': right_hip,
    'left_knee': (left_hip[0], left_hip[1] + 50),
    'right_knee': (right_hip[0], right_hip[1] + 50),
    'left_foot': (left_hip[0], left_hip[1] + 100),
    'right_foot': (right_hip[0], right_hip[1] + 100)
}

clock = pygame.time.Clock()
time_elapsed = 0.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Calculate waving angle
    theta = amplitude * math.sin(2 * math.pi * time_elapsed / period)
    
    # Right arm points
    elbow_x = shoulder_pos[0] + upper_arm_length * math.cos(theta)
    elbow_y = shoulder_pos[1] - upper_arm_length * math.sin(theta)
    forearm_theta = theta - math.pi/2
    wrist_x = elbow_x + forearm_length * math.cos(forearm_theta)
    wrist_y = elbow_y - forearm_length * math.sin(forearm_theta)
    hand_theta = forearm_theta
    hand_x = wrist_x + hand_length * math.cos(hand_theta)
    hand_y = wrist_y - hand_length * math.sin(hand_theta)
    
    # Dynamic right arm points
    right_arm_points = [
        shoulder_pos,
        (int(elbow_x), int(elbow_y)),
        (int(wrist_x), int(wrist_y)),
        (int(hand_x), int(hand_y))
    ]
    
    # Draw all 15 points
    points = [
        static_points['head'],
        static_points['left_shoulder'],
        shoulder_pos,
        static_points['left_elbow'],
        right_arm_points[1],
        static_points['left_wrist'],
        right_arm_points[2],
        static_points['left_hand'],
        right_arm_points[3],
        static_points['left_hip'],
        static_points['right_hip'],
        static_points['left_knee'],
        static_points['right_knee'],
        static_points['left_foot'],
        static_points['right_foot']
    ]
    
    for point in points:
        pygame.draw.circle(screen, WHITE, point, 5)

    pygame.display.flip()
    time_elapsed += clock.get_time() / 1000.0
    clock.tick(frame_rate)

pygame.quit()
sys.exit()
