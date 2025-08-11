
import pygame
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
POINT_COUNT = 15
FPS = 60
JUMP_HEIGHT = 100
FORWARD_DISTANCE = 300
JUMP_STEPS = 30

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Point Lights Jumping Forward')
clock = pygame.time.Clock()

# Define point light positions
def get_point_positions(step):
    angle = (2 * math.pi / JUMP_STEPS) * step
    positions = []
    
    # Define point light coordinates based on a simple jumping motion
    for i in range(POINT_COUNT):
        # Sample points in a vertical and horizontal jumping path
        x = SCREEN_WIDTH // 2 + (FORWARD_DISTANCE / JUMP_STEPS) * step
        y = SCREEN_HEIGHT // 2 + JUMP_HEIGHT * math.sin(angle) + (i % 5) * 20 - 40
        positions.append((x, y))
        
    return positions

# Animation Loop
running = True
step = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill((0, 0, 0))
    
    # Get current point positions
    point_positions = get_point_positions(step)
    
    # Draw points
    for pos in point_positions:
        pygame.draw.circle(screen, (255, 255, 255), (int(pos[0]), int(pos[1])), 5)
    
    # Update display
    pygame.display.flip()
    
    # Increment step
    step += 1
    if step >= JUMP_STEPS:
        step = 0

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
