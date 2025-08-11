
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Number of point lights
NUM_LIGHTS = 15

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Sadman Running Animation")

# Clock to control frame rate
clock = pygame.time.Clock()

# Function to calculate positions of point lights
def calculate_light_positions(frame):
    positions = []
    # Example pattern for running motion
    for i in range(NUM_LIGHTS):
        angle = (i / NUM_LIGHTS) * 2 * math.pi + frame * 0.1
        x = SCREEN_WIDTH // 2 + 100 * math.cos(angle)
        y = SCREEN_HEIGHT // 2 + 100 * math.sin(angle)
        positions.append((x, y))
    return positions

# Main loop
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate and draw point lights
    light_positions = calculate_light_positions(frame)
    for pos in light_positions:
        pygame.draw.circle(screen, WHITE, pos, 5)

    # Update the display
    pygame.display.flip()

    # Increment frame
    frame += 1

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
