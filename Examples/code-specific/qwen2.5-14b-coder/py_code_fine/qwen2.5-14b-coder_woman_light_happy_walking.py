
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Woman Walking Animation")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to calculate the position of each light
def calculate_light_positions(frame):
    positions = []
    # Example of a simple walking motion
    for i in range(NUM_LIGHTS):
        x_offset = i * 50
        y_offset = math.sin((frame + i * 10) * 0.1) * 50 + 200
        positions.append((x_offset, y_offset))
    return positions

# Main loop
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Calculate and draw lights
    light_positions = calculate_light_positions(frame)
    for pos in light_positions:
        pygame.draw.circle(screen, LIGHT_COLOR, pos, 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    # Increment frame counter
    frame += 1

# Quit Pygame
pygame.quit()
sys.exit()
