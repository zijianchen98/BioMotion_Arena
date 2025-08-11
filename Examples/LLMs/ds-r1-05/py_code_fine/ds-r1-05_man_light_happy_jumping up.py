
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Jumping Point-Light Figure")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
JUMP_AMPLITUDE = 60
BASE_FREQ = 1.5
ARM_FREQ = BASE_FREQ * 3
LEG_FREQ = BASE_FREQ * 2
PHASE_OFFSET = math.pi/2

# Body part offsets
HEAD_OFFSET = 35
SHOULDER_WIDTH = 50
UPPER_ARM = 35
LOWER_ARM = 30
HIP_WIDTH = 40
THIGH_LENGTH = 50
CALF_LENGTH = 45

def calculate_positions(t):
    torso_y = height//2 + JUMP_AMPLITUDE * math.sin(t * BASE_FREQ)
    torso_x = width//2

    # Upper body points
    head = (torso_x, torso_y - HEAD_OFFSET)
    l_shoulder = (torso_x - SHOULDER_WIDTH, torso_y)
    r_shoulder = (torso_x + SHOULDER_WIDTH, torso_y)
    
    arm_phase = math.sin(t * ARM_FREQ)
    l_elbow = (l_shoulder[0] - UPPER_ARM, l_shoulder[1] + arm_phase * 25)
    r_elbow = (r_shoulder[0] + UPPER_ARM, r_shoulder[1] + arm_phase * 25)
    l_wrist = (l_elbow[0] - LOWER_ARM, l_elbow[1] + math.cos(t * ARM_FREQ) * 30)
    r_wrist = (r_elbow[0] + LOWER_ARM, r_elbow[1] + math.cos(t * ARM_FREQ) * 30)

    # Lower body points
    leg_phase = math.sin(t * LEG_FREQ + PHASE_OFFSET)
    l_hip = (torso_x - HIP_WIDTH, torso_y + 35)
    r_hip = (torso_x + HIP_WIDTH, torso_y + 35)
    l_knee = (l_hip[0], l_hip[1] + THIGH_LENGTH + leg_phase * 25)
    r_knee = (r_hip[0], r_hip[1] + THIGH_LENGTH + leg_phase * 25)
    l_ankle = (l_knee[0], l_knee[1] + CALF_LENGTH - leg_phase * 20)
    r_ankle = (r_knee[0], r_knee[1] + CALF_LENGTH - leg_phase * 20)
    l_foot = (l_ankle[0] - 15, l_ankle[1] + 10)
    r_foot = (r_ankle[0] + 15, r_ankle[1] + 10)

    return [
        head, l_shoulder, r_shoulder, l_elbow, r_elbow,
        l_wrist, r_wrist, l_hip, r_hip, l_knee,
        r_knee, l_ankle, r_ankle, l_foot, r_foot
    ]

# Main animation loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = pygame.time.get_ticks() / 1000
    points = calculate_positions(t)

    screen.fill(BLACK)
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 6)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
