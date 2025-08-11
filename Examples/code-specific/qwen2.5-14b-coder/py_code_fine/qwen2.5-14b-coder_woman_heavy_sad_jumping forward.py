
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sad Woman Jumping Forward")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
num_lights = 15
lights = []

# Initial positions and velocities for the lights
for i in range(num_lights):
    x = width // 2 + (i - num_lights // 2) * 10
    y = height // 2
    vx = 0
    vy = 0
    lights.append({'x': x, 'y': y, 'vx': vx, 'vy': vy})

# Gravity and jump force
gravity = 0.5
jump_force = -15

# Animation loop
clock = pygame.time.Clock()
running = True
jumping = False
jump_start_time = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle jumping logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        jump_start_time = pygame.time.get_ticks()

    if jumping:
        elapsed_time = (pygame.time.get_ticks() - jump_start_time) / 1000.0
        for light in lights:
            light['vy'] = jump_force + gravity * elapsed_time
            light['y'] += light['vy']

        # Check if the jump has ended
        if all(light['vy'] >= 0 for light in lights):
            jumping = False
            for light in lights:
                light['vy'] = 0

    # Update light positions
    for light in lights:
        light['x'] += light['vx']

    # Clear screen
    screen.fill(BLACK)

    # Draw point lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light['x']), int(light['y'])), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
