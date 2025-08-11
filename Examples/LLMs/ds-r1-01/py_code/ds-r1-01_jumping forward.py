
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Jumping Forward")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
jump_duration = 1.5  # Seconds per jump cycle
num_points = 15
body_scale = 2.5  # Scale factor for body proportions

def calculate_positions(t):
    """Calculate 15 point-light positions for a jumping figure at time t (0-1)"""
    positions = []
    
    # Main body trajectory (parabolic)
    phase = t * 2 * math.pi
    vertical = -math.cos(phase * 2) * 100  # Vertical movement
    horizontal = math.sin(phase) * 30      # Horizontal sway
    
    # Body segments
    torso_y = height//2 + vertical
    torso_x = width//2 + horizontal
    
    # Head
    head_y = torso_y - 40 * body_scale
    positions.append((torso_x, head_y))

    # Shoulders
    shoulder_offset = 25 * body_scale
    positions.extend([(torso_x - shoulder_offset, torso_y),
                     (torso_x + shoulder_offset, torso_y)])

    # Arms
    arm_phase = phase + math.pi/2
    arm_length = 40 * body_scale
    for side in [-1, 1]:
        elbow_x = torso_x + side * (shoulder_offset + math.cos(arm_phase) * arm_length)
        elbow_y = torso_y + math.sin(arm_phase) * arm_length
        positions.append((elbow_x, elbow_y))
        
        wrist_x = elbow_x + side * math.cos(arm_phase) * arm_length
        wrist_y = elbow_y + math.sin(arm_phase) * arm_length
        positions.append((wrist_x, wrist_y))

    # Hips
    hip_offset = 20 * body_scale
    positions.extend([(torso_x - hip_offset, torso_y + 30),
                     (torso_x + hip_offset, torso_y + 30)])

    # Legs
    leg_phase = phase * 2
    leg_length = 50 * body_scale
    for side in [-1, 1]:
        knee_x = torso_x + side * hip_offset + math.cos(leg_phase) * 30
        knee_y = torso_y + 60 + math.sin(leg_phase) * leg_length
        positions.append((knee_x, knee_y))
        
        ankle_x = knee_x + math.cos(leg_phase) * 30
        ankle_y = knee_y + math.sin(leg_phase) * leg_length
        positions.append((ankle_x, ankle_y))
        
        foot_offset = 20 * body_scale
        math.sin(leg_phase) > 0 else -20
        foot_x = ankle_x + foot_offset
        foot_y = ankle_y + 10
        positions.append((foot_x, foot_y))

    return positions

running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate normalized time (0-1)
    current_time = (pygame.time.get_ticks() - start_time) / 1000
    t = (current_time % jump_duration) / jump_duration

    # Get current positions
    points = calculate_positions(t)

    # Draw frame
    screen.fill(BLACK)
    for (x, y) in points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 8)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
