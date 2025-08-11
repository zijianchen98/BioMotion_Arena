
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-light Happy Man Walking")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Initialize positions for 15 point lights
num_lights = 15
lights = [[random.randint(50, width - 50), random.randint(100, height - 100)] for _ in range(num_lights)]

# Position offsets for walking motion
motion_offsets = [
    (-2, 3), (-1, 4), (0, 5), (1, 4), (2, 3), 
    (2, -3), (1, -4), (0, -5), (-1, -4), (-2, -3), 
    (-2, 3), (-1, 4), (0, 5), (1, 4), (2, 3)
]

# Clock for controlling frame rate
clock = pygame.time.Clock()
fps = 30

# Animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(black)

    # Update positions
    for i in range(num_lights):
        lights[i][0] += motion_offsets[i][0]
        lights[i][1] += motion_offsets[i][1]

        # Keep lights within screen bounds
        if lights[i][0] < 50: lights[i][0] = 50
        if lights[i][0] > width - 50: lights[i][0] = width - 50
        if lights[i][1] < 100: lights[i][1] = 100
        if lights[i][1] > height - 100: lights[i][1] = height - 100

    # Draw lights
    for light in lights:
        pygame.draw.circle(screen, white, light, 10)

    # Update display
    pygame.display.flip()

    # Cap frame rate
    clock.tick(fps)

pygame.quit()
