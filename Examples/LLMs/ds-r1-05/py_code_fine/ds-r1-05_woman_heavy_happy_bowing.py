
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation: Woman Bowing")

# Colors
BACKGROUND = (0, 0, 0)
POINT_COLOR = (255, 255, 255)

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 30

# Body point definitions in a neutral standing position (scaled to screen size)
points = [
    # Head points
    (0, -150),            # 0: Head top
    (0, -100),            # 1: Chin
    
    # Torso points
    (0, -60),             # 2: Neck
    (0, -30),             # 3: Mid-back
    (0, 0),               # 4: Lower back
    (25, -30),            # 5: Right shoulder
    (-25, -30),           # 6: Left shoulder
    
    # Arm points
    (40, 0),              # 7: Right elbow
    (-40, 0),             # 8: Left elbow
    (55, 30),             # 9: Right hand
    (-55, 30),            # 10: Left hand
    
    # Leg points
    (15, 35),             # 11: Right hip
    (-15, 35),            # 12: Left hip
    (20, 80),             # 13: Right knee
    (-20, 80),            # 14: Left knee
]

# Scale points to screen
SCALE_FACTOR = 0.7
def scale_point(point):
    x, y = point
    return (WIDTH // 2 + x * SCALE_FACTOR, HEIGHT // 2 + y * SCALE_FACTOR)

# Center point for bowing rotation (mid-back)
pivot_idx = 3

# Animation parameters
amplitude = 60            # Maximum forward tilt angle (degrees)
speed = 0.05              # Animation speed
frame_count = 0

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BACKGROUND)
    
    # Calculate forward tilt (bowing motion)
    tilt_angle = amplitude * math.sin(frame_count * speed)
    frame_count += 1
    
    # Draw each point
    for i, point in enumerate(points):
        # Get pivot position (mid-back)
        pivot_x, pivot_y = scale_point(points[pivot_idx])
        
        # Convert to radians and apply rotation
        angle_rad = math.radians(tilt_angle)
        x, y = point
        if i < 11:  # Apply rotation to upper body points
            # Calculate vector from pivot to point
            dx = x - points[pivot_idx][0]
            dy = y - points[pivot_idx][1]
            
            # Rotate point around pivot
            rotated_x = dx * math.cos(angle_rad) - dy * math.sin(angle_rad)
            rotated_y = dx * math.sin(angle_rad) + dy * math.cos(angle_rad)
            
            # Convert back to absolute position
            screen_x, screen_y = scale_point((points[pivot_idx][0] + rotated_x, points[pivot_idx][1] + rotated_y))
        else:  # Lower body remains relatively still
            screen_x, screen_y = scale_point(point)
        
        # Draw point light as a circle
        pygame.draw.circle(screen, POINT_COLOR, (int(screen_x), int(screen_y)), 8)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
