
import pygame
import numpy as np
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Parameters for the "happyman sitting down" motion
PERSON_CENTRAL_X = WIDTH // 2
PERSON_CENTRAL_Y = HEIGHT // 2 - 50
BODY_LENGTH = 120
HEAD_RADIUS = 20
-arm_angle_range = math.pi / 2  # 90 degrees range for arm movement
-leg_angle_range = math.pi / 4  # 45 degrees range for leg movement
-body_angle_range = math.pi / 6  # 30 degrees range for body movement

# Define the 15 light positions (ratio of body parts to light distribution)
light_distribution = {
    "head": 3,
    "left shoulder": 2,
    "right shoulder": 2,
    "left elbow": 3,
    "right elbow": 3,
    "left wrist": 2,
    "right wrist": 2,
    "left hip": 2,
    "right hip": 2,
    "left knee": 3,
    "right knee": 3,
    "left ankle": 2,
    "right ankle": 2,
    "tail": 1  # Small light at the back
}

total_lights = sum(light_distribution.values())
light_positions = []

# Initialize angles for animation
body_angle = 0
left_arm_angle = -arm_angle_range / 2
right_arm_angle = arm_angle_range / 2
left_leg_angle = -leg_angle_range / 2
right_leg_angle = leg_angle_range / 2

def calculate_light_positions(time_elapsed):
    global body_angle, left_arm_angle, right_arm_angle, left_leg_angle, right_leg_angle
    
    # Update angles with smooth oscillation
    body_angle = math.sin(time_elapsed * 0.5) * body_angle_range * 0.3
    
    # Arm swing with slight delay between arms
    left_arm_angle = math.sin(time_elapsed * 0.7) * arm_angle_range * 0.4
    right_arm_angle = math.sin(time_elapsed * 0.7 + math.pi) * arm_angle_range * 0.4
    
    # Leg movement while sitting
    leg_swing = math.sin(time_elapsed * 0.3) * leg_angle_range * 0.6
    left_leg_angle = leg_swing
    right_leg_angle = -leg_swing
    
    # Calculate positions based on angles
    positions = []
    
    # Head lights (3 lights around the head)
    for i in range(3):
        angle = (time_elapsed * 0.2 + i * 2 * math.pi / 3) % (2 * math.pi)
        x = PERSON_CENTRAL_X + math.cos(angle) * HEAD_RADIUS * 1.1
        y = PERSON_CENTRAL_Y + math.sin(angle) * HEAD_RADIUS * 1.1
        positions.append((x, y))
    
    # Main body lights
    # Crown of head
    positions.append((PERSON_CENTRAL_X, PERSON_CENTRAL_Y - HEAD_RADIUS * 1.5))
    
    # Shoulders
    left_shoulder_x = PERSON_CENTRAL_X - BODY_LENGTH * 0.3 * math.cos(body_angle)
    left_shoulder_y = PERSON_CENTRAL_Y - BODY_LENGTH * 0.3 * math.sin(body_angle)
    right_shoulder_x = PERSON_CENTRAL_X + BODY_LENGTH * 0.3 * math.cos(body_angle)
    right_shoulder_y = PERSON_CENTRAL_Y - BODY_LENGTH * 0.3 * math.sin(body_angle)
    
    positions.append((left_shoulder_x, left_shoulder_y))
    positions.append((right_shoulder_x, right_shoulder_y))
    
    # Elbows
    left_elbow_x = left_shoulder_x - 70 * math.cos(left_arm_angle + body_angle)
    left_elbow_y = left_shoulder_y - 70 * math.sin(left_arm_angle + body_angle)
    right_elbow_x = right_shoulder_x - 70 * math.cos(right_arm_angle + body_angle)
    right_elbow_y = right_shoulder_y - 70 * math.sin(right_arm_angle + body_angle)
    
    positions.append((left_elbow_x, left_elbow_y))
    positions.append((right_elbow_x, right_elbow_y))
    
    # Wrist
    left_wrist_x = left_elbow_x - 60 * math.cos(left_arm_angle * 1.5 + body_angle)
    left_wrist_y = left_elbow_y - 60 * math.sin(left_arm_angle * 1.5 + body_angle)
    right_wrist_x = right_elbow_x - 60 * math.cos(right_arm_angle * 1.5 + body_angle)
    right_wrist_y = right_elbow_y - 60 * math.sin(right_arm_angle * 1.5 + body_angle)
    
    positions.append((left_wrist_x, left_wrist_y))
    positions.append((right_wrist_x, right_wrist_y))
    
    # Hips
    left_hip_x = PERSON_CENTRAL_X - 40 * math.cos(body_angle)
    left_hip_y = PERSON_CENTRAL_Y + 30 * math.sin(body_angle)
    right_hip_x = PERSON_CENTRAL_X + 40 * math.cos(body_angle)
    right_hip_y = PERSON_CENTRAL_Y + 30 * math.sin(body_angle)
    
    positions.append((left_hip_x, left_hip_y))
    positions.append((right_hip_x, right_hip_y))
    
    # Knees
    left_knee_x = left_hip_x - 60 * math.cos(left_leg_angle + body_angle)
    left_knee_y = left_hip_y + 60 * math.sin(left_leg_angle + body_angle)
    right_knee_x = right_hip_x - 60 * math.cos(right_leg_angle + body_angle)
    right_knee_y = right_hip_y + 60 * math.sin(right_leg_angle + body_angle)
    
    positions.append((left_knee_x, left_knee_y))
    positions.append((right_knee_x, right_knee_y))
    
    # Ankle
    left_ankle_x = left_knee_x - 50 * math.cos(left_leg_angle * 1.5 + body_angle)
    left_ankle_y = left_knee_y + 50 * math.sin(left_leg_angle * 1.5 + body_angle)
    right_ankle_x = right_knee_x - 50 * math.cos(right_leg_angle * 1.5 + body_angle)
    right_ankle_y = right_knee_y + 50 * math.sin(right_leg_angle * 1.5 + body_angle)
    
    positions.append((left_ankle_x, left_ankle_y))
    positions.append((right_ankle_x, right_ankle_y))
    
    # Tail light (behind the person)
    tail_x = PERSON_CENTRAL_X - 100 * math.cos(body_angle)
    tail_y = PERSON_CENTRAL_Y + 100 * math.sin(body_angle)
    positions.append((tail_x, tail_y))
    
    return positions

# Main animation loop
running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Calculate time elapsed in seconds
    time_elapsed = (pygame.time.get_ticks() - start_time) / 1000.0
    
    # Calculate new light positions
    light_positions = calculate_light_positions(time_elapsed)
    
    # Draw lights
    for pos in light_positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 3)
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

pygame.quit()
