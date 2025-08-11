
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Define screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happyman Running Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Parameters for the running motion
num_points = 15
radius = 50
center = (WIDTH // 2, HEIGHT // 2)
joints = [
    (0, 0), (radius, 0), (radius + 30, -radius), (radius * 2 + 30, -radius), 
    (radius * 3 + 60, 0), (radius * 4 + 60, radius), (radius * 5 + 60, 0), 
    (radius * 6 + 90, -radius), (radius * 7 + 90, -radius), (radius * 8 + 120, 0),
    (radius * 9 + 120, radius), (radius * 10 + 120, 0), (radius * 11 + 150, -radius),
    (radius * 12 + 150, -radius), (radius * 13 + 180, 0)
]

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

def update_joints(time):
    t = time / 1000.0
    updated_joints = []
    for x, y in joints:
        # Apply a running motion to the joints
        new_x = x + 2 * math.sin(t)
        new_y = y + 3 * math.cos(t) * math.sin(t)
        updated_joints.append((new_x, new_y))
    return updated_joints

running = True
time_elapsed = 0

while running:
    time_elapsed += clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update joint positions
    updated_joints = update_joints(time_elapsed)
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw the point-lights
    for joint in updated_joints:
        pygame.draw.circle(screen, WHITE, joint, 5)
    
    # Update the display
    pygame.display.flip()

pygame.quit()
