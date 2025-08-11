
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Number of point-lights
num_lights = 15

# Initial positions and velocities for point-lights
lights = []
for _ in range(num_lights):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    vx = random.uniform(-2, 2)
    vy = random.uniform(-2, 2)
    lights.append({"pos": [x, y], "vel": [vx, vy]})

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update light positions
    for light in lights:
        light["pos"][0] += light["vel"][0]
        light["pos"][1] += light["vel"][1]

        # Bounce off walls
        if light["pos"][0] < 0 or light["pos"][0] > screen_width:
            light["vel"][0] *= -1
        if light["pos"][1] < 0 or light["pos"][1] > screen_height:
            light["vel"][1] *= -1

    # Clear the screen
    screen.fill(black)

    # Draw point-lights
    for light in lights:
        pygame.draw.circle(screen, white, light["pos"], 2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
