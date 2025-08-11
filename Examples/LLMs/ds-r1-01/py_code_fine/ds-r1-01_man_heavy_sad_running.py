
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Heavy Running")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
speed = 0.04  # Slower speed for heavier movement
torso_amplitude = 25  # Increased vertical movement for torso
arm_amplitude = 40    # Larger arm swing for effort
leg_amplitude = 60    # More pronounced leg movements

def calculate_positions(time):
    points = []
    hip_center_x = width // 2
    hip_center_y = height // 2 + 30  # Lower center for hunched posture

    # Torso/Head movement
    torso_phase = time * speed
    head_y = hip_center_y - 80 + torso_amplitude * math.sin(torso_phase - math.pi/8)
    head_x = hip_center_x + 15 * math.sin(torso_phase)  # Swaying side to side

    # Shoulders (hunched forward)
    shoulder_y = head_y + 45
    shoulder_spread = 35 + 10 * math.sin(torso_phase)
    left_shoulder_x = hip_center_x - shoulder_spread
    right_shoulder_x = hip_center_x + shoulder_spread

    # Arms (exaggerated swing)
    arm_phase = time * speed * 2 + math.pi
    left_elbow_x = left_shoulder_x + arm_amplitude * math.sin(arm_phase)
    left_elbow_y = shoulder_y + 50 * math.cos(arm_phase)
    right_elbow_x = right_shoulder_x - arm_amplitude * math.sin(arm_phase)
    right_elbow_y = shoulder_y + 50 * math.cos(arm_phase)
    
    # Hands (loose following motion)
    hand_phase = arm_phase + 0.5
    left_hand_x = left_elbow_x + 25 * math.sin(hand_phase)
    left_hand_y = left_elbow_y + 20 * math.cos(hand_phase)
    right_hand_x = right_elbow_x - 25 * math.sin(hand_phase)
    right_hand_y = right_elbow_y + 20 * math.cos(hand_phase)

    # Legs (deep knee bends)
    leg_phase = time * speed * 2
    left_knee_x = hip_center_x - 25 - leg_amplitude * math.sin(leg_phase)
    left_knee_y = hip_center_y + 50 + abs(30 * math.cos(leg_phase))
    right_knee_x = hip_center_x + 25 + leg_amplitude * math.sin(leg_phase)
    right_knee_y = hip_center_y + 50 + abs(30 * math.cos(leg_phase + math.pi))

    # Feet (flat, heavy steps)
    foot_phase = leg_phase + math.pi/2
    left_foot_x = left_knee_x - 15 * math.sin(foot_phase)
    left_foot_y = left_knee_y + 50 + 10 * abs(math.cos(foot_phase))
    right_foot_x = right_knee_x + 15 * math.sin(foot_phase)
    right_foot_y = right_knee_y + 50 + 10 * abs(math.cos(foot_phase + math.pi))

    # Compile all points (15 total)
    points.extend([
        (head_x, head_y),                    # Head
        (left_shoulder_x, shoulder_y),       # Left shoulder
        (right_shoulder_x, shoulder_y),      # Right shoulder
        (left_elbow_x, left_elbow_y),        # Left elbow
        (right_elbow_x, right_elbow_y),      # Right elbow
        (left_hand_x, left_hand_y),          # Left hand
        (right_hand_x, right_hand_y),        # Right hand
        (hip_center_x - 20, hip_center_y),   # Left hip
        (hip_center_x + 20, hip_center_y),   # Right hip
        (left_knee_x, left_knee_y),          # Left knee
        (right_knee_x, right_knee_y),        # Right knee
        (left_foot_x, left_foot_y),          # Left ankle
        (right_foot_x, right_foot_y),        # Right ankle
        (left_foot_x - 10, left_foot_y + 5), # Left foot
        (right_foot_x + 10, right_foot_y + 5) # Right foot
    ])
    
    return points

# Main loop
time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    points = calculate_positions(time)
    
    # Draw points
    for point in points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 6)
    
    pygame.display.flip()
    time += 1
    clock.tick(30)

pygame.quit()
