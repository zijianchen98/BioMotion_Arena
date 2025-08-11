
import pygame
import sys
import math

def interpolate_points(start, end, t):
    return [(s[0] + t * (e[0] - s[0]), (s[1] + t * (e[1] - s[1]))] for s, e in zip(start, end)]

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Stimulus: Sitting Down")
clock = pygame.time.Clock()
fps = 60

# Standing pose coordinates
standing = [
    (400, 100),    # Head
    (400, 150),    # Neck
    (450, 160),    # Right shoulder
    (480, 220),    # Right elbow
    (500, 300),    # Right hand
    (350, 160),    # Left shoulder
    (320, 220),    # Left elbow
    (300, 300),    # Left hand
    (400, 200),    # Torso
    (430, 350),    # Right hip
    (450, 500),    # Right knee
    (430, 550),    # Right foot
    (370, 350),    # Left hip
    (350, 500),    # Left knee
    (370, 550)     # Left foot
]

# Sitting pose coordinates
sitting = [
    (400, 250),    # Head (lowered)
    (400, 300),    # Neck (lowered)
    (430, 310),    # Right shoulder (lowered and slightly forward)
    (470, 350),    # Right elbow (lowered and forward)
    (500, 400),    # Right hand (lowered and slightly forward)
    (370, 310),    # Left shoulder (lowered and slightly forward)
    (330, 350),    # Left elbow (lowered and forward)
    (300, 400),    # Left hand (lowered and slightly forward)
    (400, 325),    # Torso (lowered and leaned back)
    (430, 450),    # Right hip (lowered and moved back)
    (480, 500),    # Right knee (bent, moved forward)
    (460, 550),    # Right foot (slightly forward)
    (370, 450),    # Left hip (lowered and moved back)
    (320, 500),    # Left knee (bent, moved forward)
    (340, 550)     # Left foot (slightly forward)
]

total_frames = 120  # Duration of sitting down animation in frames
frame_count = 0
direction = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))  # Clear with black background
    
    # Progress for interpolation (0 to 1 and back to 0)
    t = frame_count / total_frames
    current_pose = interpolate_points(standing, sitting, t)
    
    # Draw 15 white points
    for point in current_pose:
        pygame.draw.circle(screen, (255, 255, 255), (int(point[0]), int(point[1])), 5)
    
    # Update frame and direction for looping
    frame_count += direction
    if frame_count >= total_frames or frame_count <= 0:
        direction *= -1  # Reverse direction at limits
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
