
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Jumping")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
fps = 30
clock = pygame.time.Clock()

def calculate_positions(t):
    """Calculate 15 point-light positions for a jumping figure at time t"""
    points = []
    
    # Core body parameters
    main_amplitude = 80
    hip_center_x = width // 2
    hip_center_y = height // 2 + main_amplitude * math.sin(t * 2)
    
    # Hips (2 points)
    points.append((hip_center_x - 15, hip_center_y))  # Left hip
    points.append((hip_center_x + 15, hip_center_y))  # Right hip

    # Head (1 point)
    head_offset = 100 + 20 * math.sin(t * 2 + 0.5)
    points.insert(0, (hip_center_x, hip_center_y - head_offset))

    # Shoulders (2 points)
    shoulder_y = hip_center_y - 60 + 25 * math.sin(t * 2 + 1)
    points.append((hip_center_x - 40, shoulder_y_))  # Left shoulder
    points.append((hip_center_x + 40, shoulder_y_))  # Right shoulder

    # Arms (4 points: elbows and hands)
    arm_phase = math.sin(t * 4)
    # Left arm
    points.append((hip_center_x - 40 - 35 * arm_phase, shoulder_y_ + 40))  # Elbow
    points.append((hip_center_x - 40 - 50 * arm_phase, shoulder_y_ + 80))  # Hand
    # Right arm
    points.append((hip_center_x + 40 + 35 * arm_phase, shoulder_y_ + 40))  # Elbow
    points.append((hip_center_x + 40 + 50 * arm_phase, shoulder_y_ + 80))  # Hand

    # Torso (1 point)
    points.insert(7, (hip_center_x, (shoulder_y_ + hip_center_y) // 2))

    # Legs (4 points: knees and feet)
    leg_phase = math.sin(t * 2 + 1.5)
    # Left leg
    points.append((hip_center_x - 15 - 25 * leg_phase, hip_center_y + 60))  # Knee
    points.append((hip_center_x - 15 - 40 * leg_phase, hip_center_y + 120))  # Foot
    # Right leg
    points.append((hip_center_x + 15 + 25 * leg_phase, hip_center_y + 60))  # Knee
    points.append((hip_center_x + 15 + 40 * leg_phase, hip_center_y + 120))  # Foot

    # Additional spine point (1 point)
    points.append((hip_center_x, hip_center_y - head_offset // 2))

    return points

# Main animation loop
time = 0.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    
    # Get current positions
    points = calculate_positions(time)
    
    # Draw all points
    for (x, y) in points:
        pygame.draw.circle(screen, white, (int(x), int(y)), 6)
    
    pygame.display.flip()
    time += 0.05
    clock.tick(fps)

pygame.quit()
