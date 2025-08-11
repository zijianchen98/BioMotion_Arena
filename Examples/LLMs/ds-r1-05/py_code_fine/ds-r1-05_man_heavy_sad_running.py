
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Point-Light Stimulus")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 30
cycle_duration = 1.5  # seconds per gait cycle

# Point size
POINT_RADIUS = 5

# Function to compute positions of 15 points for running motion
def get_point_positions(t):
    t_frac = t / cycle_duration
    phase = 2 * math.pi * t_frac
    
    # Core body motion (vertical bounce)
    bounce = 0.6 * math.sin(phase * 2)  # Body bounce
    torso_y_offset = 50 + 70 * bounce
    
    # Head motion
    head_x = 0
    head_y = torso_y_offset - 75
    
    # Torso and hips
    torso_x = 0
    torso_y = torso_y_offset
    
    mid_hip_x = 0
    mid_hip_y = torso_y_offset + 20
    
    shoulder_y = torso_y - 15
    hip_y = torso_y + 15
    
    # Limb swing parameters (legs and arms counter-phase)
    leg_swing = 0.8 * math.sin(phase)
    arm_swing = 0.9 * math.sin(phase + math.pi)  # Arms counter legs
    
    # Arm and leg flexion
    arm_flex = 0.4 * (1 + math.sin(phase * 2 + math.pi/2))
    leg_flex = 0.3 * (1 - math.sin(phase * 2))  # Leg flexion during swing
    
    # Left side points
    shoulder_left_x = -30
    elbow_left_x = shoulder_left_x - 35 * arm_flex
    hand_left_x = elbow_left_x - 30 * arm_flex
    elbow_left_y = shoulder_y + 45 + 15 * (1 - arm_swing)
    hand_left_y = elbow_left_y + 20
    
    hip_left_x = -18
    knee_left_x = hip_left_x - 15 * math.cos(leg_swing * math.pi/2)
    ankle_left_x = knee_left_x - 30 * math.sin(leg_swing * math.pi/2)
    knee_left_y = hip_y + 35 - 40 * leg_flex
    ankle_left_y = knee_left_y + 45
    
    # Right side points
    shoulder_right_x = 30
    elbow_right_x = shoulder_right_x + 35 * arm_flex
    hand_right_x = elbow_right_x + 30 * arm_flex
    elbow_right_y = shoulder_y + 45 - 15 * arm_swing
    hand_right_y = elbow_right_y + 20
    
    hip_right_x = 18
    knee_right_x = hip_right_x + 15 * math.cos(leg_swing * math.pi/2)
    ankle_right_x = knee_right_x + 30 * math.sin(leg_swing * math.pi/2)
    knee_right_y = hip_y + 35 - 40 * leg_flex
    ankle_right_y = knee_right_y + 45
    
    # Return points: head, torso, mid-hip, shoulders, elbows, hands, hips, knees, ankles
    return [
        (head_x, head_y),            # 0: head
        (torso_x, torso_y),           # 1: torso
        (mid_hip_x, mid_hip_y),       # 2: mid-hip
        (shoulder_left_x, shoulder_y),  # 3: left shoulder
        (shoulder_right_x, shoulder_y), # 4: right shoulder
        (elbow_left_x, elbow_left_y), # 5: left elbow
        (elbow_right_x, elbow_right_y),# 6: right elbow
        (hand_left_x, hand_left_y),   # 7: left hand
        (hand_right_x, hand_right_y), # 8: right hand
        (hip_left_x, hip_y),          # 9: left hip
        (hip_right_x, hip_y),         # 10: right hip
        (knee_left_x, knee_left_y),   # 11: left knee
        (knee_right_x, knee_right_y), # 12: right knee
        (ankle_left_x, ankle_left_y), # 13: left ankle
        (ankle_right_x, ankle_right_y) # 14: right ankle
    ]

# Main animation loop
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Calculate time
    current_time = (pygame.time.get_ticks() - start_time) / 1000.0
    
    # Get positions for current frame
    points = get_point_positions(current_time)
    
    # Draw each point on screen (scaled and centered)
    for (x, y) in points:
        screen_x = WIDTH // 2 + int(x * 3)  # Scale horizontal movement
        screen_y = HEIGHT // 2 + int(y)     # Vertical position with offset
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), POINT_RADIUS)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
