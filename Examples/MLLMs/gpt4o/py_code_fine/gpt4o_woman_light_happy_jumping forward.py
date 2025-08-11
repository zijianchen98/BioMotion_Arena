
import pygame
import math

# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Biological Motion: Jumping Forward")
clock = pygame.time.Clock()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_RADIUS = 5
FPS = 30

# Sadman's joint positions for jumping motion
def sadman_motion(frame):
    """Generate frame-specific motion for sadman jumping forward."""
    jump_height = 80
    forward_motion = 5
    speed = 0.1

    t = frame * speed  # time parameter

    # Base positions for joints
    positions = [
        [screen_width // 2, screen_height // 2 - 150],  # Head
        [screen_width // 2 - 20, screen_height // 2 - 100],  # Left shoulder
        [screen_width // 2 + 20, screen_height // 2 - 100],  # Right shoulder
        [screen_width // 2 - 40, screen_height // 2 - 50],  # Left elbow
        [screen_width // 2 + 40, screen_height // 2 - 50],  # Right elbow
        [screen_width // 2 - 5, screen_height // 2 - 80],   # Spine top
        [screen_width // 2 - 5, screen_height // 2 - 30],   # Spine bottom
        [screen_width // 2 - 40, screen_height // 2 + 10],  # Left hip
        [screen_width // 2 + 40, screen_height // 2 + 10],  # Right hip
        [screen_width // 2 - 60, screen_height // 2 + 80],  # Left knee
        [screen_width // 2 + 60, screen_height // 2 + 80],  # Right knee
        [screen_width // 2 - 40, screen_height // 2 + 150], # Left foot
        [screen_width // 2 + 40, screen_height // 2 + 150], # Right foot
    ]

    # Apply jumping and forward motion
    for i, pos in enumerate(positions):
        # Vertical jump aspect based on sine wave
        pos[1] -= int(jump_height * math.sin(t + i / 2))

        # Forward motion aspect
        pos[0] += int(forward_motion * t)

    return positions

def draw_sadman(positions):
    """Render sadman points on the screen."""
    for x, y in positions:
        pygame.draw.circle(screen, WHITE, (x, y), POINT_RADIUS)

# Main loop
running = True
frame = 0
while running:
    screen.fill(BLACK)  # Clear the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current motion positions
    positions = sadman_motion(frame)

    # Draw sadman on screen
    draw_sadman(positions)
    
    # Update screen
    pygame.display.flip()

    # Advance frame and regulate FPS
    frame += 1
    clock.tick(FPS)

pygame.quit()
