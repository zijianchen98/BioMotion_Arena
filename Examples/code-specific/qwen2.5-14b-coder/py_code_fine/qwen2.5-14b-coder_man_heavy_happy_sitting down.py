
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to calculate light positions for sitting down with heavy weight
def get_light_positions(time):
    positions = []
    # Example positions for a sitting down motion with heavy weight
    for i in range(NUM_LIGHTS):
        x = WIDTH // 2 + math.sin(i * 0.5 + time * 0.1) * 50
        y = HEIGHT // 2 + math.cos(i * 0.5 + time * 0.1) * 50 + math.sin(time * 0.05) * 20
        positions.append((x, y))
    return positions

# Main loop
running = True
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    light_positions = get_light_positions(time)

    for pos in light_positions:
        pygame.draw.circle(screen, LIGHT_COLOR, pos, LIGHT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)
    time += 1

pygame.quit()
sys.exit()
