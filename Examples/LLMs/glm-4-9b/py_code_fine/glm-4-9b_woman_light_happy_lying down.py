
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Define the dimensions of the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the parameters for the animation
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
FRAME_RATE = 60
ANIMATION_DURATION = 10  # seconds

# Define the function to simulate the woman's lying motion
def get_light_positions(time):
    # The positions will follow a sinusoidal pattern to simulate a natural movement
    # while the woman is lying down.
    positions = []
    base_y = HEIGHT // 2  # Base horizontal position for the lights (across the woman's body)
    for i in range(NUM_LIGHTS):
        # Calculate the vertical position to simulate a lying down posture
        vertical_offset = math.sin(time + i * math.pi / NUM_LIGHTS) * 50
        x = WIDTH // 2 + (i - NUM_LIGHTS // 2) * (WIDTH // NUM_LIGHTS)
        y = base_y + vertical_offset
        positions.append((x, y))
    return positions

# Main animation loop
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the elapsed time in seconds
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0

    # Calculate the positions of the lights
    light_positions = get_light_positions(elapsed_time)

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the point-lights
    for pos in light_positions:
        pygame.draw.circle(screen, WHITE, pos, LIGHT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FRAME_RATE)

# Quit Pygame
pygame.quit()
sys.exit()
