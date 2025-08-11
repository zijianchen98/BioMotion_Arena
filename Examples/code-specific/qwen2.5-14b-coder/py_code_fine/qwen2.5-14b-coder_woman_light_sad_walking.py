
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sad Woman Walking Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light properties
num_lights = 15
lights = []

# Initial positions of the lights
for i in range(num_lights):
    x = width // 2 + (i - num_lights // 2) * 10
    y = height // 2
    lights.append((x, y))

# Animation parameters
frame_rate = 60
clock = pygame.time.Clock()
angle = 0
step = 0.1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update light positions
    for i, (x, y) in enumerate(lights):
        offset_x = (i - num_lights // 2) * 5
        offset_y = math.sin(angle + i * 0.5) * 10
        new_x = x + offset_x + step * math.cos(angle)
        new_y = y + offset_y + step * math.sin(angle)
        lights[i] = (new_x, new_y)
        pygame.draw.circle(screen, WHITE, (int(new_x), int(new_y)), 3)

    angle += 0.05
    step += 0.01

    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()
