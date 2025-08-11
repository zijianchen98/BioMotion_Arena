
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Sad Woman Lying Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 30
clock = pygame.time.Clock()

# Point-light locations (15 points)
num_points = 15
points = np.zeros((num_points, 2), dtype=float)

# Biomechanical parameters
time = 0.0
speed = 0.05
amplitude = 80
vertical_offset = height // 2

# Body part indices for easier reference
HEAD, NECK = 0, 1
L_SHOULDER, R_SHOULDER = 2, 3
L_ELBOW, R_ELBOW = 4, 5
L_WRIST, R_WRIST = 6, 7
TORSO = 8
L_HIP, R_HIP = 9, 10
L_KNEE, R_KNEE = 11, 12
L_ANKLE, R_ANKLE = 13, 14

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Update time for animation
    time += speed
    
    # Core body position (simulates breathing/movement)
    core_y = vertical_offset + 5 * math.sin(time * 0.5)
    
    # Update body points with biomechanically plausible positions
    
    # Torso (center of motion)
    points[TORSO] = [width/2, core_y]
    
    # Head and neck (subtle movement)
    points[HEAD] = [width/2, core_y - 70 + 2 * math.sin(time)]
    points[NECK] = [width/2, core_y - 50 + 1 * math.sin(time + 0.3)]
    
    # Shoulders (breathing pattern)
    points[L_SHOULDER] = [width/2 - 35 + 5 * math.sin(time*1.2), core_y - 30]
    points[R_SHOULDER] = [width/2 + 35 - 5 * math.sin(time*1.2), core_y - 30]
    
    # Arms and hands (relaxed, downward movement)
    points[L_ELBOW] = [width/2 - 60, core_y]
    points[R_ELBOW] = [width/2 + 60, core_y]
    points[L_WRIST] = [width/2 - 70, core_y + 30 + 3 * math.sin(time)]
    points[R_WRIST] = [width/2 + 70, core_y + 30 - 3 * math.sin(time)]
    
    # Hips (base structure)
    points[L_HIP] = [width/2 - 25, core_y + 30]
    points[R_HIP] = [width/2 + 25, core_y + 30]
    
    # Legs and feet (lying position with slight movement)
    points[L_KNEE] = [width/2 - 40, core_y + 80 + 4 * math.sin(time + 0.2)]
    points[R_KNEE] = [width/2 + 40, core_y + 80 - 4 * math.sin(time + 0.2)]
    points[L_ANKLE] = [width/2 - 55, core_y + 130 + 2 * math.sin(time + 0.4)]
    points[R_ANKLE] = [width/2 + 55, core_y + 130 - 2 * math.sin(time + 0.4)]
    
    # Draw all points
    for i in range(num_points):
        pygame.draw.circle(screen, WHITE, (int(points[i][0]), int(points[i][1])), 6)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
