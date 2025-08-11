
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of point-lights
num_lights = 15

# Define the positions and velocities for the point-lights
lights = []
for _ in range(num_lights):
    angle = math.radians(360 / num_lights * _)
    x = width // 2 + int(math.cos(angle) * 100)
    y = height // 2 + int(math.sin(angle) * 100)
    dx = math.cos(angle) * 2
    dy = math.sin(angle) * 2
    lights.append([x, y, dx, dy])

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update and draw the point-lights
    for light in lights:
        light[0] += light[2]
        light[1] += light[3]

        # Reverse direction if the light hits the screen boundary
        if light[0] <= 0 or light[0] >= width:
            light[2] *= -1
        if light[1] <= 0 or light[1] >= height:
            light[3] *= -1

        # Draw the light
        pygame.draw.circle(screen, WHITE, (light[0], light[1]), 5)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
