
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Happy Woman Waving")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Body parameters
body_points = {
    # Upper body
    'head': (width//2, 150),
    'neck': (width//2, 200),
    'left_shoulder': (width//2 - 60, 220),
    'right_shoulder': (width//2 + 60, 220),
    # Left arm (static)
    'left_elbow': (width//2 - 90, 260),
    'left_wrist': (width//2 - 120, 300),
    'left_hand': (width//2 - 130, 320),
    # Right arm (dynamic points will be calculated)
    'right_elbow': (0, 0),
    'right_wrist': (0, 0),
    'right_hand': (0, 0),
    # Lower body
    'hip_left': (width//2 - 40, 400),
    'hip_right': (width//2 + 40, 400),
    'knee_left': (width//2 - 40, 500),
    'knee_right': (width//2 + 40, 500),
    'ankle_left': (width//2 - 40, 580),
    'ankle_right': (width//2 + 40, 580)
}

# Arm animation parameters
shoulder_pos = body_points['right_shoulder']
upper_arm_length = 60
forearm_length = 50
hand_length = 20
wave_amplitude = math.radians(35)  # Reduced amplitude for more natural movement
wave_speed = 0.5  # Seconds per wave cycle
elbow_flex = math.radians(80)  # Slightly bent elbow

def calculate_arm_position(t):
    # Shoulder angle with smooth sinusoidal movement
    shoulder_angle = wave_amplitude * math.sin(2 * math.pi * t / wave_speed)
    
    # Elbow position
    elbow_x = shoulder_pos[0] + upper_arm_length * math.cos(shoulder_angle)
    elbow_y = shoulder_pos[1] + upper_arm_length * math.sin(shoulder_angle)
    
    # Wrist position with natural forearm movement
    wrist_angle = shoulder_angle - elbow_flex + math.radians(10) * math.sin(4 * math.pi * t / wave_speed)
    wrist_x = elbow_x + forearm_length * math.cos(wrist_angle)
    wrist_y = elbow_y + forearm_length * math.sin(wrist_angle)
    
    # Hand position with slight natural rotation
    hand_angle = wrist_angle + math.radians(15) * math.sin(2 * math.pi * t / wave_speed)
    hand_x = wrist_x + hand_length * math.cos(hand_angle)
    hand_y = wrist_y + hand_length * math.sin(hand_angle)
    
    return (elbow_x, elbow_y), (wrist_x, wrist_y), (hand_x, hand_y)

# Main animation loop
time = 0.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Update arm positions
    elbow, wrist, hand = calculate_arm_position(time)
    body_points['right_elbow'] = elbow
    body_points['right_wrist'] = wrist
    body_points['right_hand'] = hand
    
    # Draw all 15 points
    for point in body_points.values():
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 6)
    
    pygame.display.flip()
    
    # Update time and maintain 60 FPS
    time += clock.tick(60) / 1000.0

pygame.quit()
sys.exit()
