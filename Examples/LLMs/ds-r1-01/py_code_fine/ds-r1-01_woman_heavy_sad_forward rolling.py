
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define 15 points in a human figure pattern (relative to center)
points_relative = [
    (0, -35),    # Head
    (15, -25),   # Right shoulder
    (-15, -25),  # Left shoulder
    (25, -10),    # Right elbow
    (-25, -10),   # Left elbow
    (30, 5),      # Right hand
    (-30, 5),     # Left hand
    (0, 0),       # Hips (center)
    (15, 15),     # Right knee
    (-15, 15),    # Left knee
    (20, 30),     # Right ankle
    (-20, 30),    # Left ankle
    (25, 40),     # Right foot
    (-25, 40),    # Left foot
    (0, -10)      # Chest
]

# Movement parameters
speed = 1.2        # Slower forward speed for heavy weight
angular_speed = 0.03  # Slower rotation for realistic motion
radius = 40         # Compact radius for tucked position

# Initial position
center_x, center_y = 100, height//2

# Main loop
running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Update positions
    center_x += speed
    angle += angular_speed
    
    # Vertical oscillation for weight transfer
    vertical_offset = 10 * math.sin(angle)
    
    for (x, y) in points_relative:
        # Apply rotation and vertical offset
        rot_x = x * math.cos(angle) - y * math.sin(angle)
        rot_y = x * math.sin(angle) + y * math.cos(angle)
        
        # Calculate screen position
        pos_x = int(center_x + rot_x)
        pos_y = int(center_y + rot_y + vertical_offset)
        
        # Draw
        pygame.draw.circle(screen, WHITE, (pos_x, pos_y), 4)

    pygame.display.flip()
    clock.tick(40)  # Smooth frame rate

pygame.quit()
sys.exit()
