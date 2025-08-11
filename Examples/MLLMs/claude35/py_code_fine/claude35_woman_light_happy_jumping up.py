
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
POINT_LIGHTS = 15
JUMP_HEIGHT = 100

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Animation of a Happy Woman Jumping')

# Function to generate point light positions
def get_jump_positions(t, total_time):
    t_norm = t / total_time
    positions = []
    
    # Create a simple upward jump motion
    for i in range(POINT_LIGHTS):
        # X position across the width of the screen
        x = (WIDTH / POINT_LIGHTS) * i + 100
        
        # Y position based on a sinusoidal function for smooth jump
        y = HEIGHT // 2 + (math.sin(t_norm * math.pi) * JUMP_HEIGHT - (JUMP_HEIGHT / 2))
        
        positions.append((x, y))
    
    return positions

# Main loop
running = True
clock = pygame.time.Clock()
total_time = 2  # Total time for the jump in seconds
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)
    
    # Get the current time
    current_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert to seconds

    # If the jump is over, reset the movement
    if current_time >= total_time:
        start_time = pygame.time.get_ticks()
    
    # Get point light positions
    positions = get_jump_positions(current_time, total_time)

    # Draw point lights
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    # Update the display
    pygame.display.flip()
    
    # Maintain the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
