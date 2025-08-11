
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
period = 3.0  # Longer period for heavier movement
amplitude = 30  # Reduced jump height
forward_speed = 50  # Slower forward movement
baseline_y = height // 2

# Time management
start_time = pygame.time.get_ticks() / 1000.0

def head_pos(phase):
    return (0, -50 + 5 * math.sin(2 * math.pi * phase))

def left_shoulder_pos(_):
    return (-35, -30)

def right_shoulder_pos(_):
    return (35, -30)

def left_elbow_pos(phase):
    arm_swing = 20 * math.sin(2 * math.pi * phase)
    return (-35 + arm_swing, -10)

def right_elbow_pos(phase):
    arm_swing = 20 * math.sin(2 * math.pi * phase)
    return (35 + arm_swing, -10)

def left_hand_pos(phase):
    arm_swing = 30 * math.sin(2 * math.pi * phase)
    return (-35 + arm_swing, 10)

def right_hand_pos(phase):
    arm_swing = 30 * math.sin(2 * math.pi * phase)
    return (35 + arm_swing, 10)

def left_hip_pos(_):
    return (-25, 20)

def right_hip_pos(_):
    return (25, 20)

def left_knee_pos(phase):
    knee_bend = 15 * math.cos(2 * math.pi * phase)
    return (-25, 60 + knee_bend)

def right_knee_pos(phase):
    knee_bend = 15 * math.cos(2 * math.pi * phase)
    return (25, 60 + knee_bend)

def left_ankle_pos(phase):
    knee_bend = 15 * math.cos(2 * math.pi * phase)
    return (-25, 100 + knee_bend)

def right_ankle_pos(phase):
    knee_bend = 15 * math.cos(2 * math.pi * phase)
    return (25, 100 + knee_bend)

def torso_upper_pos(_):
    return (0, -15)

def torso_lower_pos(_):
    return (0, 15)

point_functions = [
    head_pos,
    left_shoulder_pos,
    right_shoulder_pos,
    left_elbow_pos,
    right_elbow_pos,
    left_hand_pos,
    right_hand_pos,
    left_hip_pos,
    right_hip_pos,
    left_knee_pos,
    right_knee_pos,
    left_ankle_pos,
    right_ankle_pos,
    torso_upper_pos,
    torso_lower_pos
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    current_time = pygame.time.get_ticks() / 1000.0
    elapsed_time = current_time - start_time
    phase = (elapsed_time % period) / period

    # Calculate center position
    center_x = (forward_speed * elapsed_time) % width
    center_y = baseline_y + amplitude * math.sin(2 * math.pi * phase)

    # Draw all points
    for func in point_functions:
        dx, dy = func(phase)
        x = center_x + dx
        y = center_y + dy
        pygame.draw.circle(screen, white, (int(x % width), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
