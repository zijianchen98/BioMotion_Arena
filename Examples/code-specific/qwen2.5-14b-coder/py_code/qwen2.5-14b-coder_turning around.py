
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Number of point-lights
num_lights = 15

# Initial positions of the point-lights
lights = []
for i in range(num_lights):
    angle = (2 * math.pi / num_lights) * i
    x = width // 2 + 150 * math.cos(angle)
    y = height // 2 + 150 * math.sin(angle)
    lights.append((x, y))

# Rotation parameters
rotation_speed = 0.01
angle_offset = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update light positions
    angle_offset += rotation_speed
    new_lights = []
    for i in range(num_lights):
        angle = (2 * math.pi / num_lights) * i + angle_offset
        x = width // 2 + 150 * math.cos(angle)
        y = height // 2 + 150 * math.sin(angle)
        new_lights.append((x, y))
    lights = new_lights

    # Draw background
    screen.fill(black)

    # Draw point-lights
    for light in lights:
        pygame.draw.circle(screen, white, light, 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
