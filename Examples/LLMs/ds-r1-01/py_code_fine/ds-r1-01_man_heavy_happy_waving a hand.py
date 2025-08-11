
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
L1 = 50  # Upper arm length
L2 = 50  # Lower arm length
amplitude = math.radians(30)  # 30 degrees in radians
omega = 2  # Angular velocity (radians per second)
sway_amplitude = 20  # Body sway magnitude

def calculate_positions(t):
    """Calculate positions for all 15 points based on time"""
    theta = amplitude * math.sin(omega * t)
    torso_x = 400 + (-sway_amplitude * math.sin(omega * t))
    
    # Right arm components
    right_shoulder = (torso_x + 50, 150)
    elbow = (
        right_shoulder[0] + L1 * math.sin(theta),
        right_shoulder[1] + L1 * math.cos(theta)
    )
    hand = (
        elbow[0] + L2 * math.cos(theta),
        elbow[1] - L2 * math.sin(theta)
    )
    
    # Left arm components (static)
    left_shoulder = (torso_x - 50, 150)
    left_elbow = (left_shoulder[0], left_shoulder[1] + L1)
    left_hand = (left_elbow[0] + L2, left_elbow[1])
    
    # Lower body components
    right_hip = (torso_x + 30, 250)
    left_hip = (torso_x - 30, 250)
    
    return [
        (torso_x, 100),          # Head
        right_shoulder,          # Right shoulder
        left_shoulder,           # Left shoulder
        elbow,                   # Right elbow
        left_elbow,              # Left elbow
        hand,                    # Right hand
        left_hand,               # Left hand
        (torso_x, 200),          # Torso
        right_hip,               # Right hip
        left_hip,                # Left hip
        (right_hip[0], 300),     # Right knee
        (left_hip[0], 300),      # Left knee
        (right_hip[0], 350),     # Right ankle
        (left_hip[0], 350),      # Left ankle
        (torso_x, 250)           # Mid-hip
    ]

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    
    current_time = pygame.time.get_ticks() / 1000
    points = calculate_positions(current_time)
    
    # Draw all points
    for point in points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 5)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
