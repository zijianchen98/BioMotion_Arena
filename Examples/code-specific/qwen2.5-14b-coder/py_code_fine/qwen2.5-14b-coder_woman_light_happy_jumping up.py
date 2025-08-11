
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
LIGHT_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Woman Jumping Animation")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Light properties
lights = []
for i in range(NUM_LIGHTS):
    x = WIDTH // 2 + (i - NUM_LIGHTS // 2) * 10
    y = HEIGHT - JUMP_HEIGHT
    velocity_y = 0
    lights.append({'x': x, 'y': y, 'velocity_y': velocity_y})

# Animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update light positions
    for light in lights:
        light['velocity_y'] += GRAVITY
        light['y'] += light['velocity_y']

        # Check for ground collision
        if light['y'] >= HEIGHT - JUMP_HEIGHT:
            light['y'] = HEIGHT - JUMP_HEIGHT
            light['velocity_y'] = -math.sqrt(2 * GRAVITY * JUMP_HEIGHT)

    # Clear screen
    screen.fill(BACKGROUND_COLOR)

    # Draw lights
    for light in lights:
        pygame.draw.circle(screen, LIGHT_COLOR, (int(light['x']), int(light['y'])), LIGHT_RADIUS)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
