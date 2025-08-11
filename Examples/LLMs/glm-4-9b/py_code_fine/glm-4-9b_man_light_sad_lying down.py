
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Parameters for the sadman's motion
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
BODY_LENGTH = 150
BODY_WIDTH = 50
ARM_LENGTH = 60
LEG_LENGTH = 70

def get_point_light_positions(t):
    """
    Generate positions for 15 point lights representing a sadman lying down
    t is the time parameter for animation
    """
    positions = []
    
    # Center of the body (the main source of light)
    body_x = CENTER_X
    body_y = CENTER_Y
    
    # Main body points (5 lights - torso, head, legs)
    body_points = [
        (body_x, body_y - BODY_LENGTH // 2),  # Head
        (body_x, body_y),                    # Upper torso
        (body_x, body_y + BODY_LENGTH // 3), # Lower torso
        (body_x, body_y + BODY_LENGTH // 2)  # Pelvis
    ]
    
    # Arms (3 lights each arm)
    arm_points = [
        # Left arm
        (body_x - BODY_WIDTH, body_y - ARM_LENGTH // 2),      # Upper arm
        (body_x - BODY_WIDTH - 20, body_y),                   # Forearm
        (body_x - BODY_WIDTH - 30, body_y + 10),              # Hand
        
        # Right arm
        (body_x + BODY_WIDTH, body_y - ARM_LENGTH // 2),      # Upper arm
        (body_x + BODY_WIDTH + 20, body_y),                   # Forearm
        (body_x + BODY_WIDTH + 30, body_y + 10),              # Hand
    ]
    
    # Legs (3 lights each leg)
    leg_points = [
        # Left leg
        (body_x - 30, body_y + BODY_LENGTH // 2),             # Upper leg
        (body_x - 40, body_y + BODY_LENGTH),                  # Lower leg
        (body_x - 50, body_y + BODY_LENGTH + 20),             # Foot
        
        # Right leg
        (body_x + 30, body_y + BODY_LENGTH // 2),             # Upper leg
        (body_x + 40, body_y + BODY_LENGTH),                  # Lower leg
        (body_x + 50, body_y + BODY_LENGTH + 20),             # Foot
    ]
    
    # Add some movement to the lights to simulate biological motion
    for point in body_points + arm_points + leg_points:
        x, y = point
        
        # Make the body gently浮动
        dx = 5 * math.sin(t * 0.5)
        dy = 3 * math.cos(t * 0.7)
        
        # Add slight independent movement to different parts
        if point in arm_points:
            dx += 2 * math.sin(t * 1.1)
        if point in leg_points:
            dx -= 3 * math.sin(t * 0.9)
            dy += 1 * math.cos(t * 1.2)
        
        positions.append((x + dx, y + dy))
    
    return positions

# Main animation loop
running = True
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Get the current positions of the point lights
    light_positions = get_point_light_positions(t)
    
    # Draw the point lights
    for pos in light_positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 3)
    
    # Update the display
    pygame.display.flip()
    
    # Increment time parameter
    t += 0.02
    
    # Control the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()
