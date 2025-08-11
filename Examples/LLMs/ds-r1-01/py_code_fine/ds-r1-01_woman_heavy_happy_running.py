
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Biological Motion")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Center of the screen
center_x, center_y = width // 2, height // 2

# Motion parameters for heavy runner
speed = 0.05
amplitude_vertical = 20
arm_swing = 1.5
leg_swing = 1.0

def get_head_pos(t):
    x = center_x
    y = center_y - 100 + 5 * math.sin(t * 0.5)
    return (x, y)

def get_neck_pos(t):
    x = center_x
    y = center_y - 80
    return (x, y)

def get_left_shoulder_pos(t):
    x = center_x - 40 + 15 * math.sin(t * arm_swing)
    y = center_y - 60 + 10 * math.sin(t * arm_swing + math.pi/2)
    return (x, y)

def get_right_shoulder_pos(t):
    x = center_x + 40 - 15 * math.sin(t * arm_swing)
    y = center_y - 60 + 10 * math.sin(t * arm_swing + math.pi/2)
    return (x, y)

def get_left_elbow_pos(t):
    shoulder_x, shoulder_y = get_left_shoulder_pos(t)
    angle = math.sin(t * arm_swing) * math.pi/2.5
    x = shoulder_x + 30 * math.cos(angle)
    y = shoulder_y + 30 * math.sin(angle)
    return (x, y)

def get_right_elbow_pos(t):
    shoulder_x, shoulder_y = get_right_shoulder_pos(t)
    angle = math.sin(t * arm_swing + math.pi) * math.pi/2.5
    x = shoulder_x - 30 * math.cos(angle)
    y = shoulder_y + 30 * math.sin(angle)
    return (x, y)

def get_left_wrist_pos(t):
    elbow_x, elbow_y = get_left_elbow_pos(t)
    angle = math.sin(t * arm_swing + math.pi/2) * math.pi/3
    x = elbow_x + 25 * math.cos(angle)
    y = elbow_y + 25 * math.sin(angle)
    return (x, y)

def get_right_wrist_pos(t):
    elbow_x, elbow_y = get_right_elbow_pos(t)
    angle = math.sin(t * arm_swing + math.pi/2 + math.pi) * math.pi/3
    x = elbow_x - 25 * math.cos(angle)
    y = elbow_y + 25 * math.sin(angle)
    return (x, y)

def get_torso_pos(t):
    x = center_x
    y = center_y - 20 + 5 * math.sin(t * 0.5)
    return (x, y)

def get_left_hip_pos(t):
    x = center_x - 30 + 20 * math.sin(t * leg_swing)
    y = center_y + 30 + amplitude_vertical * math.sin(2 * t * leg_swing)
    return (x, y)

def get_right_hip_pos(t):
    x = center_x + 30 - 20 * math.sin(t * leg_swing)
    y = center_y + 30 + amplitude_vertical * math.sin(2 * t * leg_swing + math.pi)
    return (x, y)

def get_left_knee_pos(t):
    hip_x, hip_y = get_left_hip_pos(t)
    angle = math.sin(t * leg_swing * 2) * math.pi/2.5
    x = hip_x + 40 * math.cos(angle)
    y = hip_y + 40 * math.sin(angle)
    return (x, y)

def get_right_knee_pos(t):
    hip_x, hip_y = get_right_hip_pos(t)
    angle = math.sin(t * leg_swing * 2 + math.pi) * math.pi/2.5
    x = hip_x - 40 * math.cos(angle)
    y = hip_y + 40 * math.sin(angle)
    return (x, y)

def get_left_ankle_pos(t):
    knee_x, knee_y = get_left_knee_pos(t)
    angle = math.sin(t * leg_swing * 2 + math.pi/2) * math.pi/3
    x = knee_x + 35 * math.cos(angle)
    y = knee_y + 35 * math.sin(angle)
    return (x, y)

def get_right_ankle_pos(t):
    knee_x, knee_y = get_right_knee_pos(t)
    angle = math.sin(t * leg_swing * 2 + math.pi/2 + math.pi) * math.pi/3
    x = knee_x - 35 * math.cos(angle)
    y = knee_y + 35 * math.sin(angle)
    return (x, y)

point_functions = [
    get_head_pos,
    get_neck_pos,
    get_left_shoulder_pos,
    get_right_shoulder_pos,
    get_left_elbow_pos,
    get_right_elbow_pos,
    get_left_wrist_pos,
    get_right_wrist_pos,
    get_torso_pos,
    get_left_hip_pos,
    get_right_hip_pos,
    get_left_knee_pos,
    get_right_knee_pos,
    get_left_ankle_pos,
    get_right_ankle_pos
]

# Main loop
t = 0.0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for func in point_functions:
        x, y = func(t)
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)
    t += speed

pygame.quit()
sys.exit()
