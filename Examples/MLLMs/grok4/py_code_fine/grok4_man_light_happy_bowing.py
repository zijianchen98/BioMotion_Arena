
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_POINTS = 15
RADIUS = 5

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Function to calculate positions of point-lights for a bowing motion
def calculate_bowing_positions(time):
    positions = []
    for i in range(NUM_POINTS):
        # Calculate the position based on a sine wave for smooth motion
        angle = (2 * math.pi * (i / NUM_POINTS) + time) % (2 * math.pi)
        y = HEIGHT // 2 + math.sin(angle) * 30 * (i / NUM_POINTS)
        x = WIDTH // 2 - 50 + (i % 5) * 20
        positions.append((x, y))
    return positions

# Main loop
running = True
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen to black
    screen.fill(BLACK)
    
    # Calculate current time for animation
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

    # Get positions for point-lights
    positions = calculate_bowing_positions(elapsed_time)

    # Draw point-lights
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), RADIUS)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
