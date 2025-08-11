
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
    light = pygame.rect.Rect(x, y, 10, 10)
    lights.append(light)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the lights
    for light in lights:
        light.x += random.randint(-5, 5)
        light.y += random.randint(-5, 5)

        # Wrap around the screen
        if light.x < 0:
            light.x = WIDTH
        if light.x > WIDTH:
            light.x = 0
        if light.y < 0:
            light.y = HEIGHT
        if light.y > HEIGHT:
            light.y = 0

    # Draw everything
    screen.fill((0, 0, 0))
    for light in lights:
        pygame.draw.rect(screen, (255, 255, 255), light)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
