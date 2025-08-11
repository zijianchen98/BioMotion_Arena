
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
PERIOD = 2.0  # Jump cycle duration in seconds
BODY_AMPLITUDE = 60  # Vertical body movement amplitude
ARM_AMPLITUDE = 40   # Arm swing amplitude
LEG_AMPLITUDE = 30   # Leg movement amplitude

def calculate_positions(phase):
    """Calculate positions of 15 points based on jump phase (0-1)"""
    body_y = HEIGHT//2 - BODY_AMPLITUDE * math.sin(2 * math.pi * phase)
    points = []

    # Head (1 point)
    points.append((WIDTH//2, body_y - 40))

    # Shoulders (2 points)
    shoulder_offset = 35 + 10 * math.sin(2 * math.pi * phase)
    points.append((WIDTH//2 - shoulder_offset, body_y - 20))
    points.append((WIDTH//2 + shoulder_offset, body_y - 20))

    # Arms (4 points: elbows and hands)
    arm_angle = math.pi * 0.5 * (1 + math.sin(4 * math.pi * phase))
    for side in [-1, 1]:
        elbow_x = WIDTH//2 + side * (shoulder_offset + 25 * math.cos(arm_angle))
        elbow_y = body_y - 20 + 25 * math.sin(arm_angle)
        points.append((elbow_x, elbow_y))
        
        hand_x = elbow_x + side * 35 * math.cos(arm_angle - math.pi/4)
        hand_y = elbow_y + 35 * math.sin(arm_angle - math.pi/4)
        points.append((hand_x, hand_y))

    # Hips (2 points)
    hip_offset = 20 - 10 * math.sin(2 * math.pi * phase)
    points.append((WIDTH//2 - hip_offset, body_y + 10))
    points.append((WIDTH//2 + hip_offset, body_y + 10))

    # Legs (6 points: knees, ankles, feet)
    leg_phase = phase + 0.2 if phase < 0.8 else phase - 0.8
    leg_angle = math.pi * 0.3 * (1 + math.sin(4 * math.pi * leg_phase))
    for side in [-1, 1]:
        knee_x = WIDTH//2 + side * (20 - 15 * math.cos(leg_angle))
        knee_y = body_y + 50 + 40 * math.sin(leg_angle)
        points.append((knee_x, knee_y))
        
        ankle_x = knee_x + side * 30 * math.cos(leg_angle)
        ankle_y = knee_y + 40 * math.sin(leg_angle)
        points.append((ankle_x, ankle_y))
        
        foot_x = ankle_x + side * 15 * math.cos(leg_angle - math.pi/6)
        foot_y = ankle_y + 15 * math.sin(leg_angle - math.pi/6)
        points.append((foot_x, foot_y))

    return points

# Main animation loop
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate current phase
    current_time = (pygame.time.get_ticks() - start_time) / 1000
    phase = (current_time % PERIOD) / PERIOD

    # Get current positions
    points = calculate_positions(phase)

    # Draw frame
    screen.fill(BLACK)
    for (x, y) in points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 6)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
