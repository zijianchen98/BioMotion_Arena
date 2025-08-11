
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Man Forward Rolling")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Number of point lights
num_lights = 15

# Initial positions and velocities of point lights
lights = []
for i in range(num_lights):
    angle = 2 * math.pi * i / num_lights
    x = width // 2 + 100 * math.cos(angle)
    y = height // 2 + 100 * math.sin(angle)
    lights.append([x, y, 0, 0])

# Animation loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update light positions
    for light in lights:
        light[0] += light[2]
        light[1] += light[3]

        # Apply forward rolling motion
        light[2] = 5 * math.cos(math.radians(light[0] - width // 2))
        light[3] = 5 * math.sin(math.radians(light[1] - height // 2))

        # Wrap around screen edges
        if light[0] < 0:
            light[0] += width
        elif light[0] > width:
            light[0] -= width
        if light[1] < 0:
            light[1] += height
        elif light[1] > height:
            light[1] -= height

    # Clear screen
    screen.fill(black)

    # Draw point lights
    for light in lights:
        pygame.draw.circle(screen, white, (int(light[0]), int(light[1])), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
