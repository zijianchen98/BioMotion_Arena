
import pygame
import sys
import math

pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Jumping")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
amplitude = 50  # Vertical jump height
speed = 0.6     # Horizontal movement speed
cycle_duration = 1.5  # Jump cycle duration in seconds
phase_shift = 0.25    # Phase shift for limb movements

def calculate_positions(t):
    """Calculate positions for all 15 points based on normalized time (0-1)"""
    # Body center coordinates (hips)
    x_center = width * 0.2 + (t * speed) * width * 0.6
    y_center = height//2 + amplitude * (1 - (2*(t - 0.5))**2)
    
    points = []
    
    # Head (1 point)
    points.append((x_center, y_center - 50))
    
    # Shoulders (2 points)
    points.append((x_center - 30, y_center - 40))
    points.append((x_center + 30, y_center - 40))
    
    # Arms (4 points: elbows and hands)
    arm_phase = 2 * math.pi * t
    for side in [-1, 1]:
        # Elbows
        elbow_x = x_center + side * (30 + 25 * math.sin(arm_phase))
        elbow_y = y_center - 40 + 30 * math.cos(arm_phase)
        points.append((elbow_x, elbow_y))
        
        # Hands
        hand_x = elbow_x + side * 25 * math.sin(arm_phase)
        hand_y = elbow_y + 30 * math.cos(arm_phase)
        points.append((hand_x, hand_y))
    
    # Hips (2 points)
    points.append((x_center - 20, y_center))
    points.append((x_center + 20, y_center))
    
    # Legs (6 points: knees, ankles, feet)
    leg_phase = 2 * math.pi * (t + phase_shift)
    for side in [-1, 1]:
        # Knees
        knee_x = x_center + side * 20 - side * 15 * math.sin(leg_phase)
        knee_y = y_center + 50 + 30 * math.cos(leg_phase)
        points.append((knee_x, knee_y))
        
        # Ankles
        ankle_x = knee_x - side * 15 * math.sin(leg_phase)
        ankle_y = knee_y + 40 + 20 * math.cos(leg_phase)
        points.append((ankle_x, ankle_y))
        
        # Feet
        foot_x = ankle_x - side * 10 * math.sin(leg_phase)
        foot_y = ankle_y + 20 * math.cos(leg_phase)
        points.append((foot_x, foot_y))
    
    return points, (x_center, y_center)

# Animation control
t = 0.0
dt = 0.02  # Time increment per frame

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    
    # Calculate positions
    points, center = calculate_positions(t % 1.0)
    
    # Draw all points
    for x, y in points:
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)
    
    # Update display
    pygame.display.flip()
    clock.tick(30)
    t += dt / cycle_duration
