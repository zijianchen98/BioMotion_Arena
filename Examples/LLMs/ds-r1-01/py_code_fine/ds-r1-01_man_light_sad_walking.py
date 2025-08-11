
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Point-light Walker")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
PERIOD = 2.0  # Seconds per walk cycle
AMPLITUDE_LEG = 40  # Horizontal leg movement
AMPLITUDE_LIFT = 20  # Vertical foot lift
SHOULDER_WIDTH = 80
HIP_WIDTH = 60
TORSO_HEIGHT = 100
AMPLITUDE_ARM = 30

# Base positions (relative to center)
BASE_HEAD_Y = -150
BASE_SHOULDER_Y = -50
BASE_HIP_Y = 50

def get_positions(t):
    points = []
    
    # Head
    head_y = BASE_HEAD_Y + 10 * math.sin(2 * math.pi * t / PERIOD)
    points.append((0, head_y))
    
    # Shoulders
    left_shoulder_x = -SHOULDER_WIDTH/2 + 10 * math.sin(2 * math.pi * t / PERIOD + math.pi)
    left_shoulder_y = BASE_SHOULDER_Y + 5 * math.cos(2 * math.pi * t / PERIOD)
    right_shoulder_x = SHOULDER_WIDTH/2 + 10 * math.sin(2 * math.pi * t / PERIOD + math.pi)
    right_shoulder_y = BASE_SHOULDER_Y + 5 * math.cos(2 * math.pi * t / PERIOD + math.pi)
    points.append((left_shoulder_x, left_shoulder_y))
    points.append((right_shoulder_x, right_shoulder_y))
    
    # Arms
    left_hand_x = -AMPLITUDE_ARM * math.sin(2 * math.pi * t / PERIOD)
    left_hand_y = BASE_SHOULDER_Y - 30 + 10 * math.cos(2 * math.pi * t / PERIOD)
    right_hand_x = AMPLITUDE_ARM * math.sin(2 * math.pi * t / PERIOD)
    right_hand_y = BASE_SHOULDER_Y - 30 + 10 * math.cos(2 * math.pi * t / PERIOD + math.pi)
    
    # Elbows
    left_elbow_x = (left_shoulder_x + left_hand_x) / 2
    left_elbow_y = (left_shoulder_y + left_hand_y) / 2 - 20
    right_elbow_x = (right_shoulder_x + right_hand_x) / 2
    right_elbow_y = (right_shoulder_y + right_hand_y) / 2 - 20
    points.extend([(left_elbow_x, left_elbow_y), (right_elbow_x, right_elbow_y),
                   (left_hand_x, left_hand_y), (right_hand_x, right_hand_y)])
    
    # Hips
    left_hip_x = -HIP_WIDTH/2 + 10 * math.sin(2 * math.pi * t / PERIOD)
    right_hip_x = HIP_WIDTH/2 + 10 * math.sin(2 * math.pi * t / PERIOD + math.pi)
    points.extend([(left_hip_x, BASE_HIP_Y), (right_hip_x, BASE_HIP_Y)])
    
    # Legs
    left_ankle_x = -AMPLITUDE_LEG * math.sin(2 * math.pi * t / PERIOD)
    left_ankle_y = AMPLITUDE_LIFT * (1 + math.cos(2 * math.pi * t / PERIOD))
    right_ankle_x = AMPLITUDE_LEG * math.sin(2 * math.pi * t / PERIOD)
    right_ankle_y = AMPLITUDE_LIFT * (1 - math.cos(2 * math.pi * t / PERIOD))
    
    # Knees
    left_knee_x = (left_hip_x + left_ankle_x) / 2
    left_knee_y = (BASE_HIP_Y + left_ankle_y) / 2 + 20
    right_knee_x = (right_hip_x + right_ankle_x) / 2
    right_knee_y = (BASE_HIP_Y + right_ankle_y) / 2 + 20
    points.extend([(left_knee_x, left_knee_y), (right_knee_x, right_knee_y),
                   (left_ankle_x, left_ankle_y), (right_ankle_x, right_ankle_y)])
    
    # Torso and mid-hip
    points.append((0, (BASE_SHOULDER_Y + BASE_HIP_Y) / 2))
    points.append(((left_hip_x + right_hip_x) / 2, BASE_HIP_Y))
    
    return points

# Main loop
time = 0.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    # Get and draw points
    for x, y in get_positions(time):
        pygame.draw.circle(screen, WHITE, 
                         (int(x + WIDTH/2), int(y + HEIGHT/2)), 5)
    
    pygame.display.flip()
    time += 0.02
    clock.tick(60)

pygame.quit()
sys.exit()
