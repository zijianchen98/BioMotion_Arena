
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Point-light Walk")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
speed = 1.5  # Slower speed for heavier person
hip_sway_amplitude = 25  # Increased sway for weight
shoulder_sway_amplitude = 15
step_length = 35  # Shorter steps for heavier gait
step_height = 25
arm_swing_amplitude = 25
body_bob_amplitude = 4
leg_speed = 1.2  # Slower leg movement
arm_speed = 1.2
center_x, center_y = width // 2, height // 2 + 20  # Lower center for heavier build

def get_positions(t):
    positions = []
    
    # Head (slight vertical movement)
    head_x = center_x
    head_y = center_y - 80 + body_bob_amplitude * math.sin(t * 1.5)
    positions.append((head_x, head_y))
    
    # Shoulders (opposite sway to hips)
    shoulder_sway = shoulder_sway_amplitude * math.sin(t + math.pi)
    left_shoulder_x = center_x - 45 + shoulder_sway
    left_shoulder_y = center_y - 40 + 3 * math.sin(t * 2)
    right_shoulder_x = center_x + 45 + shoulder_sway
    right_shoulder_y = center_y - 40 + 3 * math.sin(t * 2 + math.pi)
    positions.append((left_shoulder_x, left_shoulder_y))
    positions.append((right_shoulder_x, right_shoulder_y))
    
    # Elbows (arm swing opposite to legs)
    arm_phase = t * arm_speed + math.pi  # Opposite phase to legs
    left_elbow_x = left_shoulder_x + arm_swing_amplitude * math.sin(arm_phase)
    left_elbow_y = left_shoulder_y + 25
    right_elbow_x = right_shoulder_x + arm_swing_amplitude * math.sin(arm_phase)
    right_elbow_y = right_shoulder_y + 25
    positions.append((left_elbow_x, left_elbow_y))
    positions.append((right_elbow_x, right_elbow_y))
    
    # Hands (follow elbows)
    left_hand_x = left_elbow_x + 0.8 * arm_swing_amplitude * math.sin(arm_phase)
    left_hand_y = left_elbow_y + 15
    right_hand_x = right_elbow_x + 0.8 * arm_swing_amplitude * math.sin(arm_phase)
    right_hand_y = right_elbow_y + 15
    positions.append((left_hand_x, left_hand_y))
    positions.append((right_hand_x, right_hand_y))
    
    # Hips (pronounced side-to-side movement)
    hip_sway = hip_sway_amplitude * math.sin(t)
    left_hip_x = center_x - 35 - hip_sway
    left_hip_y = center_y + 10
    right_hip_x = center_x + 35 + hip_sway
    right_hip_y = center_y + 10
    positions.append((left_hip_x, left_hip_y))
    positions.append((right_hip_x, right_hip_y))
    
    # Knees (calculated with foot positions)
    leg_phase = t * leg_speed
    # Right leg
    right_foot_x = right_hip_x + step_length * math.sin(leg_phase)
    right_foot_y = right_hip_y + step_height * (1 - abs(math.sin(leg_phase)))
    right_knee_x = (right_hip_x + right_foot_x)/2 - 10 * math.sin(leg_phase)
    right_knee_y = (right_hip_y + right_foot_y)/2 - 25
    # Left leg
    left_foot_x = left_hip_x + step_length * math.sin(leg_phase + math.pi)
    left_foot_y = left_hip_y + step_height * (1 - abs(math.sin(leg_phase + math.pi)))
    left_knee_x = (left_hip_x + left_foot_x)/2 - 10 * math.sin(leg_phase + math.pi)
    left_knee_y = (left_hip_y + left_foot_y)/2 - 25
    positions.append((left_knee_x, left_knee_y))
    positions.append((right_knee_x, right_knee_y))
    
    # Ankles and feet
    left_ankle_x, left_ankle_y = left_foot_x, left_foot_y + 10
    right_ankle_x, right_ankle_y = right_foot_x, right_foot_y + 10
    positions.append((left_ankle_x, left_ankle_y))
    positions.append((right_ankle_x, right_ankle_y))
    
    # Feet (toes)
    positions.append((left_ankle_x + 12, left_ankle_y))
    positions.append((right_ankle_x + 12, right_ankle_y))
    
    return positions

# Main animation loop
t = 0.0
dt = 0.04  # Controls animation speed

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(black)
    positions = get_positions(t)
    
    # Draw all 15 points
    for (x, y) in positions:
        pygame.draw.circle(screen, white, (int(x), int(y)), 6)
    
    pygame.display.flip()
    clock.tick(30)
    t += dt

pygame.quit()
sys.exit()
