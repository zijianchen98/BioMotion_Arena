
import pygame
import numpy as np
from math import sin, cos, radians

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Man Sitting Down")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define initial positions for 15 point-lights (simplified human skeleton)
# Head, shoulders, elbows, wrists, hips, knees, ankles, torso points
base_positions = [
    (WIDTH//2, 100),    # Head
    (WIDTH//2-40, 150), # Left shoulder
    (WIDTH//2+40, 150), # Right shoulder
    (WIDTH//2-80, 200), # Left elbow
    (WIDTH//2+80, 200), # Right elbow
    (WIDTH//2-100, 250),# Left wrist
    (WIDTH//2+100, 250),# Right wrist
    (WIDTH//2-30, 300), # Left hip
    (WIDTH//2+30, 300), # Right hip
    (WIDTH//2-30, 400), # Left knee
    (WIDTH//2+30, 400), # Right knee
    (WIDTH//2-30, 500), # Left ankle
    (WIDTH//2+30, 500), # Right ankle
    (WIDTH//2-15, 200), # Upper torso
    (WIDTH//2+15, 200)  # Upper torso
]

# Animation parameters
duration = 2000  # Total duration in milliseconds (2 seconds for one cycle)
frames = 60      # Frames per cycle
frame_time = duration / frames
t = 0

# Sitting down motion (simplified angles and offsets)
def get_positions(t):
    positions = base_positions.copy()
    progress = min(1.0, t / duration)  # Normalize time (0 to 1)
    
    # Torso angle (tilts forward then straightens)
    torso_angle = -30 * (1 - progress) * progress  # Parabola-like motion
    # Leg angles (bend knees and lower)
    knee_angle = 90 * progress  # Bend knees from 0 to 90 degrees
    hip_offset_y = 200 * progress  # Lower hips by 200 pixels
    
    # Update positions based on motion
    for i, (x, y) in enumerate(positions):
        if i in [7, 8]:  # Hips
            y += hip_offset_y
        elif i in [9, 10]:  # Knees
            angle = radians(knee_angle)
            if i == 9:  # Left knee
                x = positions[7][0] - 30 * cos(angle)
                y = positions[7][1] + 100 * sin(angle)
            else:  # Right knee
                x = positions[8][0] + 30 * cos(angle)
                y = positions[8][1] + 100 * sin(angle)
        elif i in [11, 12]:  # Ankles
            if i == 11:  # Left ankle
                x = positions[9][0]
                y = positions[9][1] + 100
            else:  # Right ankle
                x = positions[10][0]
                y = positions[10][1] + 100
        elif i in [13, 14]:  # Torso points
            angle = radians(torso_angle)
            dx = (x - WIDTH//2) * cos(angle) - (y - 200) * sin(angle) + WIDTH//2
            dy = (x - WIDTH//2) * sin(angle) + (y - 200) * cos(angle) + 200
            x, y = dx, dy + hip_offset_y
    
    return positions

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update time
    t += clock.get_rawtime()
    if t > duration:
        t = 0  # Reset cycle
    
    # Clear screen
    screen.fill(BLACK)
    
    # Get current positions
    positions = get_positions(t)
    
    # Draw point-lights
    for x, y in positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

# Quit Pygame
pygame.quit()
