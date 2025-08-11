
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Biological Motion - Point-light Stimulus")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configuration parameters
SCALE = 200  # Scaling factor for visualization
CENTER_X = screen_width // 2
CENTER_Y = screen_height // 2
ANGULAR_SPEED = 0.03  # Slower speed for heavier appearance

# Define 3D coordinates for body points (x, y, z)
body_points = [
    # Upper body
    (0.00, 0.50, 0.00),   # Head
    (0.00, 0.45, 0.00),   # Neck
    (-0.20, 0.40, 0.00),  # Left shoulder
    (0.20, 0.40, 0.00),   # Right shoulder
    (-0.30, 0.30, 0.10),  # Left elbow
    (0.30, 0.30, 0.10),   # Right elbow
    (-0.40, 0.20, 0.20),  # Left hand
    (0.40, 0.20, 0.20),   # Right hand
    
    # Lower body
    (-0.15, 0.20, 0.00),  # Left hip
    (0.15, 0.20, 0.00),   # Right hip
    (-0.15, 0.00, 0.10),  # Left knee
    (0.15, 0.00, 0.10),   # Right knee
    (-0.15, -0.20, 0.20), # Left ankle
    (0.15, -0.20, 0.20),  # Right ankle
    (0.00, 0.30, 0.00)    # Torso (mid-hip)
]

clock = pygame.time.Clock()
theta = 0  # Rotation angle

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Update rotation angle
    theta += ANGULAR_SPEED
    
    # Draw all body points
    for point in body_points:
        x, y, z = point
        
        # 3D rotation around Y-axis (vertical axis)
        x_rot = x * math.cos(theta) - z * math.sin(theta)
        
        # Convert to screen coordinates (invert Y-axis for proper display)
        screen_x = int(x_rot * SCALE + CENTER_X)
        screen_y = int(-y * SCALE + CENTER_Y)  # Negative Y for proper orientation
        
        # Draw point with size 5
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), 5)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
