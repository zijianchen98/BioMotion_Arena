
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

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Walking Animation")

# Function to draw a point-light
def draw_point_light(x, y):
    pygame.draw.circle(screen, LIGHT_COLOR, (int(x), int(y)), 5)

# Function to get the position of each light based on time and frame
def get_light_positions(time, num_lights):
    positions = []
    step = 2 * math.pi / num_lights
    amplitude = 100
    frequency = 0.1
    for i in range(num_lights):
        angle = i * step + time * frequency
        x = WIDTH // 2 + amplitude * math.cos(angle)
        y = HEIGHT // 2 + amplitude * math.sin(angle) + 50 * math.sin(time * frequency * 2)
        positions.append((x, y))
    return positions

# Main loop
clock = pygame.time.Clock()
running = True
time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    positions = get_light_positions(time, NUM_LIGHTS)
    for pos in positions:
        draw_point_light(*pos)

    pygame.display.flip()
    clock.tick(FPS)
    time += 0.1

pygame.quit()
sys.exit()
