
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Woman Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light configuration for initial standing pose (15 points)
# Points represent: head, neck, shoulders (2), elbows (2), wrists (2), torso, hips (2), knees (2), ankles (2)
initial_points = [
    (400, 150),  # Head
    (400, 190),  # Neck
    (360, 220),  # Left shoulder
    (440, 220),  # Right shoulder
    (340, 270),  # Left elbow
    (460, 270),  # Right elbow
    (320, 320),  # Left wrist
    (480, 320),  # Right wrist
    (400, 250),  # Torso
    (380, 320),  # Left hip
    (420, 320),  # Right hip
    (380, 420),  # Left knee
    (420, 420),  # Right knee
    (380, 520),  # Left ankle
    (420, 520)   # Right ankle
]

# Initialize point positions
points = initial_points.copy()

# Animation parameters
period = 2.0  # Seconds for one complete bow
u_scale = 0.5  # Upper body movement scaling
hip_center_initial = (initial_points[9][0] + initial_points[10][0]) / 2, (initial_points[9][1] + initial_points[10][1]) / 2
head_y_initial = initial_points[0][1]

# Start time tracking
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Calculate time-based movement
    elapsed = (pygame.time.get_ticks() - start_time) / 1000.0
    normalized_time = (elapsed % period) / period
    f_normalized = (1 - math.cos(2 * math.pi * normalized_time)) / 2.0
    
    # Calculate hip movement and apply to all points
    drop_hips = 0.3 * (hip_center_initial[1] - head_y_initial) * f_normalized
    
    # Update points based on time for bowing motion
    for i, (x, y) in enumerate(initial_points):
        if i < 9:  # Upper body points (head to torso)
            additional_drop = (hip_center_initial[1] - y) * f_normalized * u_scale
            new_y = y + drop_hips + additional_drop
            points[i] = (x, new_y)
        else:  # Lower body points (hips to ankles)
            new_y = y + drop_hips
            points[i] = (x, new_y)
    
    # Draw the point-light stimulus
    for x, y in points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 8)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
