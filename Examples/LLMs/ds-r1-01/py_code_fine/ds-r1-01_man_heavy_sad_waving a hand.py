
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Center coordinates
center_x, center_y = width // 2, height // 2

# Arm parameters
UPPER_ARM_LENGTH = 40
LOWER_ARM_LENGTH = 30
AMPLITUDE = math.pi / 2.5  # Reduced amplitude for heavier movement
SPEED = 0.04
PHASE_SHIFT = -math.pi / 1.7  # Adjusted for heavier movement

# Time tracking
time = 0

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate arm angles with damped movement
    theta = AMPLITUDE * math.sin(time)  # Main arm movement
    phi = PHASE_SHIFT + AMPLITUDE * 0.7 * math.sin(time + 1.5)  # Secondary arm movement

    # Right arm joint calculations
    shoulder_x, shoulder_y = 50, -30
    elbow_x = shoulder_x + UPPER_ARM_LENGTH * math.cos(theta)
    elbow_y = shoulder_y + UPPER_ARM_LENGTH * math.sin(theta)
    wrist_x = elbow_x + LOWER_ARM_LENGTH * math.cos(theta + phi)
    wrist_y = elbow_y + LOWER_ARM_LENGTH * math.sin(theta + phi)

    # Define all 15 points
    points = [
        # Body (5 points)
        (0, -100), (0, -50), (0, 0), (-30, 50), (30, 50),
        
        # Left arm (3 points - static)
        (-50, -30), (-70, -10), (-90, 10),
        
        # Right arm (3 points - dynamic)
        (shoulder_x, shoulder_y), (elbow_x, elbow_y), (wrist_x, wrist_y),
        
        # Legs (4 points - static)
        (-30, 50), (-30, 80), (30, 50), (30, 80)
    ]

    # Draw frame
    screen.fill(BLACK)
    for (x, y) in points:
        pygame.draw.circle(screen, WHITE, 
                         (int(center_x + x), int(center_y + y)), 6)

    pygame.display.flip()
    time += SPEED
    clock.tick(30)

pygame.quit()
sys.exit()
