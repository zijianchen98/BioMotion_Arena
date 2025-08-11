
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Jumping Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
fps = 30
clock = pygame.time.Clock()
jump_height = 70  # Reduced jump height for heavy person
cycle_duration = 1800  # ms per jump cycle (slower movement)

def calculate_positions(phase, center_x, center_y):
    """Calculate positions of 15 points based on jump phase (0-1)"""
    torso_y = center_y + 50 - jump_height * 4 * (phase - 0.5)**2  # Parabolic jump
    
    # Head and neck
    head_y = torso_y - 40
    neck_y = (torso_y + head_y) / 2

    # Shoulders with slight lateral movement
    shoulder_phase = math.sin(phase * 2 * math.pi)
    right_shoulder_x = center_x + 35 + 5 * shoulder_phase
    left_shoulder_x = center_x - 35 - 5 * shoulder_phase
    shoulder_y = torso_y + 15

    # Arms with coordinated swing
    arm_swing = 60 * math.sin(phase * math.pi)
    right_elbow_x = right_shoulder_x + 25 * math.cos(phase * math.pi)
    right_elbow_y = shoulder_y - arm_swing
    right_wrist_x = right_elbow_x + 25 * math.cos(phase * math.pi)
    right_wrist_y = right_elbow_y - arm_swing * 0.8

    left_elbow_x = left_shoulder_x - 25 * math.cos(phase * math.pi)
    left_elbow_y = shoulder_y - arm_swing
    left_wrist_x = left_elbow_x - 25 * math.cos(phase * math.pi)
    left_wrist_y = left_elbow_y - arm_swing * 0.8

    # Hips with weight shift
    hip_shift = 10 * math.sin(phase * 2 * math.pi)
    right_hip_x = center_x + 25 + hip_shift
    left_hip_x = center_x - 25 - hip_shift
    hip_y = torso_y + 40

    # Legs with realistic knee bend
    leg_phase = 0.5 * (1 + math.sin(2 * math.pi * (phase - 0.1)))
    knee_bend = 50 * leg_phase
    right_knee_y = hip_y + knee_bend
    right_ankle_y = right_knee_y + 70 - 30 * leg_phase
    left_knee_y = hip_y + knee_bend
    left_ankle_y = left_knee_y + 70 - 30 * leg_phase

    return [
        (center_x, head_y),        # Head
        (center_x, neck_y),        # Neck
        (right_shoulder_x, shoulder_y),  # Right shoulder
        (right_elbow_x, right_elbow_y),  # Right elbow
        (right_wrist_x, right_wrist_y),  # Right wrist
        (left_shoulder_x, shoulder_y),   # Left shoulder
        (left_elbow_x, left_elbow_y),    # Left elbow
        (left_wrist_x, left_wrist_y),    # Left wrist
        (center_x, torso_y),       # Torso
        (right_hip_x, hip_y),      # Right hip
        (right_hip_x, right_knee_y),    # Right knee
        (right_hip_x, right_ankle_y),   # Right ankle
        (left_hip_x, hip_y),       # Left hip
        (left_hip_x, left_knee_y),      # Left knee
        (left_hip_x, left_ankle_y)      # Left ankle
    ]

# Main loop
running = True
center = (width//2, height//2 + 80)  # Lower center for heavy figure

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate normalized phase (0-1)
    phase = (pygame.time.get_ticks() % cycle_duration) / cycle_duration
    
    # Get current positions
    points = calculate_positions(phase, *center)

    # Draw frame
    screen.fill(BLACK)
    for (x, y) in points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 7)
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
