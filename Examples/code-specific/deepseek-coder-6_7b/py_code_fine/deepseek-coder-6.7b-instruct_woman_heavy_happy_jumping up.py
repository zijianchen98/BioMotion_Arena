
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
NUM_LIGHTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the lights
lights = []
for _ in range(NUM_LIGHTS):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    color = (255, 255, 255)  # White
    radius = 5
    speed = 1
    direction = random.choice([-1, 1])
    lights.append({'x': x, 'y': y, 'color': color, 'radius': radius, 'speed': speed, 'direction': direction})

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the lights
    for light in lights:
        pygame.draw.circle(screen, light['color'], (light['x'], light['y']), light['radius'])

        # Update the light position
        light['x'] += light['speed'] * light['direction']

        # Bounce the light off the edges
        if light['x'] - light['radius'] < 0 or light['x'] + light['radius'] > WIDTH:
            light['direction'] *= -1

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
