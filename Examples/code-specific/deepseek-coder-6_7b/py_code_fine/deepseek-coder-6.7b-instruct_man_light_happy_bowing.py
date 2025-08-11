
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
NUM_LIGHTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a list to hold the light objects
lights = []

# Create the lights
for _ in range(NUM_LIGHTS):
    x = random.randint(LIGHT_RADIUS, WIDTH - LIGHT_RADIUS)
    y = random.randint(LIGHT_RADIUS, HEIGHT - LIGHT_RADIUS)
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    light = {'x': x, 'y': y, 'dx': dx, 'dy': dy}
    lights.append(light)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the lights
    for light in lights:
        pygame.draw.circle(screen, LIGHT_COLOR, (light['x'], light['y']), LIGHT_RADIUS)

    # Update the lights' positions
    for light in lights:
        light['x'] += light['dx']
        light['y'] += light['dy']

        # Bounce the lights off the edges of the screen
        if light['x'] - LIGHT_RADIUS < 0 or light['x'] + LIGHT_RADIUS > WIDTH:
            light['dx'] = -light['dx']
        if light['y'] - LIGHT_RADIUS < 0 or light['y'] + LIGHT_RADIUS > HEIGHT:
            light['dy'] = -light['dy']

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
