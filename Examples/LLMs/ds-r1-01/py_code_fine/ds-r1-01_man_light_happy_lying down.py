
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Lying Down")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define body points in standing position (relative to hips at origin)
points = [
    (0, -100),   # Head
    (0, -80),    # Neck
    (-40, -60),  # Left shoulder
    (40, -60),   # Right shoulder
    (-60, -40),  # Left elbow
    (60, -40),   # Right elbow
    (-80, -20),  # Left wrist
    (80, -20),   # Right wrist
    (0, -40),    # Torso (chest)
    (-20, 0),    # Left hip
    (20, 0),     # Right hip
    (-20, 20),   # Left knee
    (20, 20),    # Right knee
    (-20, 40),   # Left ankle
    (20, 40)     # Right ankle
]

# Animation parameters
angle = 0
speed = 1  # Degrees per frame
clock = pygame.time.Clock()
running = True

# Main animation loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    current_angle = math.radians(angle)
    
    # Calculate and draw each point
    for (x, y) in points:
        # Apply rotation matrix (counter-clockwise)
        rot_x = x * math.cos(current_angle) - y * math.sin(current_angle)
        rot_y = x * math.sin(current_angle) + y * math.cos(current_angle)
        
        # Convert to screen coordinates
        screen_x = int(rot_x) + width // 2
        screen_y = int(rot_y) + height // 2
        
        # Draw point
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), 4)
    
    pygame.display.flip()
    
    # Update angle with smooth oscillation
    angle += speed
    if angle >= 90 or angle <= 0:
        speed = -speed
    
    clock.tick(30)

pygame.quit()
