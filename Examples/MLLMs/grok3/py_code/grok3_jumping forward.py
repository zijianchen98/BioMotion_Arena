
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Joint positions for a jumping forward motion (simplified 2D representation)
# These are relative positions that will animate over time
joint_positions = [
    (0, -50),   # Head
    (-10, -20), # Left shoulder
    (10, -20),  # Right shoulder
    (-15, 0),   # Left elbow
    (15, 0),    # Right elbow
    (-20, 20),  # Left hip
    (20, 20),   # Right hip
    (-15, 40),  # Left knee
    (15, 40),   # Right knee
    (-10, 60),  # Left ankle
    (10, 60),   # Right ankle
    (-5, 10),   # Left wrist
    (5, 10),    # Right wrist
    (-5, 30),   # Left toe
    (5, 30)     # Right toe
]

# Animation parameters
frame_rate = 60
jump_height = 100
jump_duration = 120  # frames for one jump cycle
current_frame = 0

# Function to calculate vertical position during jump
def get_jump_height(frame):
    if frame < jump_duration / 2:
        return -jump_height * math.sin((2 * math.pi * frame) / jump_duration)
    else:
        return -jump_height * math.sin((2 * math.pi * frame) / jump_duration)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Calculate vertical offset for jump
    vertical_offset = get_jump_height(current_frame)
    
    # Draw point-lights
    for x, y in joint_positions:
        # Add forward motion and jump motion
        forward_offset = 2 * (current_frame / jump_duration)  # Simple forward movement
        adjusted_y = y + vertical_offset
        pygame.draw.circle(screen, WHITE, 
                          (int(WIDTH/2 + x + forward_offset), int(HEIGHT/2 + adjusted_y)), 5)

    # Update frame
    current_frame = (current_frame + 1) % jump_duration
    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()
