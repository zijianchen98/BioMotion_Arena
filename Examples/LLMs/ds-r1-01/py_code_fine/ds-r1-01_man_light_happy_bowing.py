
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Bowing")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
time = 0.0
speed = 0.08  # Controls animation speed
radius = 5    # Point-light radius

def calculate_positions(phase):
    """Calculate positions of 15 point-lights based on bowing phase (0-1)"""
    points = []
    
    # Head (1)
    points.append((50 * phase, -150 + 200 * phase))
    
    # Shoulders (2-3)
    points.append((-50 + 20 * phase, -100 + 50 * phase))  # Left
    points.append((50 - 20 * phase, -100 + 50 * phase))   # Right
    
    # Elbows (4-5)
    points.append((-70 - 20 * phase, -50 + 50 * phase))   # Left
    points.append((70 - 20 * phase, -50 + 50 * phase))    # Right
    
    # Hands (6-7)
    points.append((-90 - 30 * phase, 0 + 50 * phase))     # Left
    points.append((90 - 30 * phase, 0 + 50 * phase))      # Right
    
    # Hips (8-9, stationary
    points.append((-30, 0))   # Left
    points.append((30, 0))    # Right
    
    # Knees (10-11)
    points.append((-20, 50 + 30 * phase))  # Left
    points.append((20, 50 + 30 * phase))   # Right
    
    # Feet (12-13, stationary)
    points.append((-30, 100))  # Left
    points.append((30, 100))   # Right
    
    # Mid-back points (14-15)
    points.append((0, -50 + 50 * phase))  # Upper
    points.append((0, 0))                 # Lower
    
    return points

# Main animation loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    
    # Update animation phase
    time += 1
    phase = (math.sin(time * speed) + 1) / 2  # Smooth 0-1 oscillation
    
    # Get current point positions
    points = calculate_positions(phase)
    
    # Draw all points
    center_x, center_y = width//2, height//2
    for (x, y) in points:
        screen_x = int(center_x + x)
        screen_y = int(center_y + y)
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), radius)
    
    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS
