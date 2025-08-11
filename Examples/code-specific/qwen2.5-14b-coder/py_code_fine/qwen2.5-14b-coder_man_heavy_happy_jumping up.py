
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
GRAVITY = 0.5
JUMP_HEIGHT = 200
JUMP_DURATION = 1.5  # seconds
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Function to calculate position based on time
def calculate_position(t):
    if t < JUMP_DURATION / 2:
        return -GRAVITY * (t ** 2) + JUMP_HEIGHT
    else:
        return GRAVITY * ((t - JUMP_DURATION) ** 2) - JUMP_HEIGHT

# Main loop
clock = pygame.time.Clock()
running = True
start_time = pygame.time.get_ticks() / 1000

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks() / 1000 - start_time
    if current_time >= JUMP_DURATION:
        start_time = pygame.time.get_ticks() / 1000

    screen.fill(BACKGROUND_COLOR)

    for i in range(NUM_LIGHTS):
        angle = (i / NUM_LIGHTS) * 2 * math.pi
        x_offset = 50 * math.cos(angle)
        y_offset = 50 * math.sin(angle)

        light_x = WIDTH // 2 + x_offset
        light_y = HEIGHT // 2 + y_offset

        jump_progress = current_time / JUMP_DURATION
        vertical_offset = calculate_position(current_time)
        light_y += vertical_offset

        pygame.draw.circle(screen, LIGHT_COLOR, (int(light_x), int(light_y)), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
