
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

# Point light properties
num_lights = 15
lights = []
for i in range(num_lights):
    angle = 2 * math.pi * i / num_lights
    x = width // 2 + 100 * math.cos(angle)
    y = height // 2 + 100 * math.sin(angle)
    lights.append([x, y])

# Animation parameters
frame_rate = 60
clock = pygame.time.Clock()
running = True

def update_positions(frame):
    for i, light in enumerate(lights):
        angle = 2 * math.pi * i / num_lights + frame * 0.01
        light[0] = width // 2 + 100 * math.cos(angle)
        light[1] = height // 2 + 100 * math.sin(angle) - 50 * math.sin(frame * 0.05)  # Slight vertical movement for lying down effect

frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    for light in lights:
        pygame.draw.circle(screen, white, (int(light[0]), int(light[1])), 5)

    pygame.display.flip()
    clock.tick(frame_rate)
    frame += 1

pygame.quit()
sys.exit()
