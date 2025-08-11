#!/usr/bin/env python3
import pygame
import math
import sys

pygame.init()

# ---------------------------------------------
# Window setup
# ---------------------------------------------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Point-Light Stimulus")

# ---------------------------------------------
# Clock for controlling frame rate
# ---------------------------------------------
clock = pygame.time.Clock()
FPS = 60

# ---------------------------------------------
# Define 3D skeleton points (15 total)
# Each tuple is (x, y, z)
# ---------------------------------------------
skeleton_3d = [
    (0.0, 1.7, 0.0),   # Head
    (0.0, 1.5, 0.0),   # Neck
    (-0.2, 1.5, 0.0),  # Left shoulder
    ( 0.2, 1.5, 0.0),  # Right shoulder
    (-0.4, 1.3, 0.0),  # Left elbow
    ( 0.4, 1.3, 0.0),  # Right elbow
    (-0.6, 1.1, 0.0),  # Left wrist
    ( 0.6, 1.1, 0.0),  # Right wrist
    ( 0.0, 1.2, 0.0),  # Mid torso
    (-0.2, 1.0, 0.0),  # Left hip
    ( 0.2, 1.0, 0.0),  # Right hip
    (-0.2, 0.6, 0.0),  # Left knee
    ( 0.2, 0.6, 0.0),  # Right knee
    (-0.2, 0.2, 0.0),  # Left ankle
    ( 0.2, 0.2, 0.0),  # Right ankle
]

# ---------------------------------------------
# Rotation around y-axis in 3D (heading)
# angle in radians
# ---------------------------------------------
def rotate_y(point, angle):
    x, y, z = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    # rotation around y-axis
    x_rot = x * cos_a + z * sin_a
    z_rot = -x * sin_a + z * cos_a
    return (x_rot, y, z_rot)

# ---------------------------------------------
# Main loop
# ---------------------------------------------
def main():
    angle = 0.0
    running = True
    
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update angle for continuous turning
        angle += math.radians(1)  # 1 degree per frame
        
        # Clear screen (black background)
        screen.fill((0, 0, 0))
        
        # Compute and draw each point
        for pt in skeleton_3d:
            # Rotate around y-axis
            rx, ry, rz = rotate_y(pt, angle)
            
            # Project to 2D (orthographic)
            scale = 150
            # shifting to screen center
            sx = int(rx * scale + WIDTH // 2)
            sy = int(HEIGHT // 2 - ry * scale)
            
            # Draw the point (white)
            pygame.draw.circle(screen, (255, 255, 255), (sx, sy), 5)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()