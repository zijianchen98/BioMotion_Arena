
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Running")
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
phase = 0
speed = 0.05
amplitude_torso = 20  # Vertical movement of torso
amplitude_arm = 50    # Horizontal arm swing
amplitude_leg = 60    # Horizontal leg swing

def get_points(phase):
    points = []
    center_x = width // 2
    center_y = height // 2 + 50  # Initial vertical position

    # Torso (point 0)
    torso_y = center_y + amplitude_torso * math.sin(phase)
    points.append((center_x, torso_y))

    # Head (point 1)
    head_y = torso_y - 40
    points.append((center_x, head_y))

    # Shoulders (points 2, 3)
    shoulder_dx = 30
    shoulder_y = torso_y - 20
    points.append((center_x - shoulder_dx, shoulder_y))
    points.append((center_x + shoulder_dx, shoulder_y))

    # Arms (points 4-7)
    arm_phase = phase + math.pi  # Arms opposite to legs
    # Left arm
    left_elbow_x = points[2][0] - amplitude_arm * math.sin(arm_phase)
    left_elbow_y = shoulder_y + 20 * math.cos(arm_phase)
    points.append((left_elbow_x, left_elbow_y))
    left_hand_x = left_elbow_x - 30 * math.sin(arm_phase)
    left_hand_y = left_elbow_y + 15 * math.cos(arm_phase)
    points.append((left_hand_x, left_hand_y))
    # Right arm
    right_elbow_x = points[3][0] + amplitude_arm * math.sin(arm_phase)
    right_elbow_y = shoulder_y + 20 * math.cos(arm_phase)
    points.append((right_elbow_x, right_elbow_y))
    right_hand_x = right_elbow_x + 30 * math.sin(arm_phase)
    right_hand_y = right_elbow_y + 15 * math.cos(arm_phase)
    points.append((right_hand_x, right_hand_y))

    # Hips (points 8, 9)
    hip_dx = 30
    hip_y = torso_y + 30
    points.append((center_x - hip_dx, hip_y))
    points.append((center_x + hip_dx, hip_y))

    # Legs (points 10-13)
    # Right leg
    right_knee_x = points[9][0] + amplitude_leg * math.sin(phase)
    right_knee_y = points[9][1] + 30 * math.cos(phase)
    points.append((right_knee_x, right_knee_y))
    right_ankle_x = right_knee_x + amplitude_leg * math.sin(phase + 0.5*math.pi)
    right_ankle_y = right_knee_y + 30 * math.cos(phase + 0.5*math.pi)
    points.append((right_ankle_x, right_ankle_y))
    # Left leg
    left_knee_x = points[8][0] - amplitude_leg * math.sin(phase)
    left_knee_y = points[8][1] + 30 * math.cos(phase)
    points.append((left_knee_x, left_knee_y))
    left_ankle_x = left_knee_x - amplitude_leg * math.sin(phase + 0.5*math.pi)
    left_ankle_y = left_knee_y + 30 * math.cos(phase + 0.5*math.pi)
    points.append((left_ankle_x, left_ankle_y))

    # Neck (point 14)
    neck_y = (head_y + torso_y) / 2
    points.append((center_x, neck_y))

    return points

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    current_phase = phase % (2 * math.pi)  # Keep phase cyclical
    current_points = get_points(current_phase)

    # Draw all 15 points
    for (x, y) in current_points:
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    pygame.display.flip()
    phase += speed
    clock.tick(30)

pygame.quit()
sys.exit()
