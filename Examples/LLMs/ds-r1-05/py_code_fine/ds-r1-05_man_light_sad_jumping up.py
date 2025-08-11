
import pygame
import sys
import math

pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
torso_y_center = height // 2
jump_height = 100
period = 2.0
dt = 0.05
time = 0.0

def calculate_positions(phase):
    """Calculate positions of 15 points based on animation phase (0-1)"""
    torso_x = width // 2
    torso_y = torso_y_center - jump_height * (4 * phase * (1 - phase))
    
    # Head
    head = (torso_x, torso_y - 50)
    
    # Shoulders
    left_shoulder = (torso_x - 40, torso_y + 20)
    right_shoulder = (torso_x + 40, torso_y + 20)
    
    # Arms
    arm_angle = math.pi/4 * math.sin(2 * math.pi * phase)
    left_elbow = (
        left_shoulder[0] - 50 * math.cos(arm_angle),
        left_shoulder[1] + 50 * math.sin(arm_angle)
    )
    left_hand = (
        left_elbow[0] - 50 * math.cos(arm_angle),
        left_elbow[1] + 50 * math.sin(arm_angle)
    )
    right_elbow = (
        right_shoulder[0] + 50 * math.cos(arm_angle),
        right_shoulder[1] + 50 * math.sin(arm_angle)
    )
    right_hand = (
        right_elbow[0] + 50 * math.cos(arm_angle),
        right_elbow[1] + 50 * math.sin(arm_angle)
    )
    
    # Hips
    left_hip = (torso_x - 30, torso_y + 60)
    right_hip = (torso_x + 30, torso_y + 60)
    
    # Legs
    leg_angle = math.pi/6 * (1 + math.sin(2 * math.pi * phase))
    left_knee = (
        left_hip[0] - 60 * math.sin(leg_angle),
        left_hip[1] + 60 * math.cos(leg_angle)
    )
    left_ankle = (
        left_knee[0] - 60 * math.sin(leg_angle),
        left_knee[1] + 60 * math.cos(leg_angle)
    )
    right_knee = (
        right_hip[0] + 60 * math.sin(leg_angle),
        right_hip[1] + 60 * math.cos(leg_angle)
    )
    right_ankle = (
        right_knee[0] + 60 * math.sin(leg_angle),
        right_knee[1] + 60 * math.cos(leg_angle)
    )
    
    # Additional points for natural motion
    neck = (torso_x, torso_y - 25)
    mid_back = (torso_x, torso_y + 40)
    waist = (torso_x, torso_y + 80)
    
    return [
        head, neck, left_shoulder, right_shoulder,
        left_elbow, right_elbow, left_hand, right_hand,
        mid_back, left_hip, right_hip, left_knee,
        right_knee, left_ankle, right_ankle
    ]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Calculate animation phase
    phase = (time % period) / period
    points = calculate_positions(phase)
    
    # Draw frame
    screen.fill(black)
    for point in points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 6)
    
    pygame.display.flip()
    clock.tick(30)
    time += dt

pygame.quit()
sys.exit()
