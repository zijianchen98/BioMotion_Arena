
import pygame
import sys
import math
import numpy as np

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock to control the frame rate
clock = pygame.time.Clock()
FPS = 60

# Parameters for the jump motion
jump_height = 200
jump_duration = 1  # seconds
gravity = 9.8

# Function to get the position of a point-light at a given time
def get_position(t, phase_shift=0):
    t = t + phase_shift
    x = WIDTH // 2 + int(math.sin(t * 2 * math.pi / 5) * 100)
    y = HEIGHT // 2 + int(math.sin(t * 2 * math.pi / jump_duration) * jump_height - (gravity / 2) * (t ** 2))
    return x, y

# Function to get the velocity of a point-light at a given time
def get_velocity(t, phase_shift=0):
    t = t + phase_shift
    x = (2 * math.pi / 5) * math.cos(t * 2 * math.pi / 5)
    y = (2 * math.pi / jump_duration) * math.sin(t * 2 * math.pi / jump_duration) - gravity * t
    return x, y

# Function to get the acceleration of a point-light at a given time
def get_acceleration(t, phase_shift=0):
    t = t + phase_shift
    x = -(2 * math.pi / 5) * (2 * math.pi / 5) * math.sin(t * 2 * math.pi / 5)
    y = (2 * math.pi / jump_duration) * (2 * math.pi / jump_duration) * math.cos(t * 2 * math.pi / jump_duration) - gravity
    return x, y

# Number of point-lights
num_lights = 15

# Main loop
running = True
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Update the position of each point-light
    for i in range(num_lights):
        phase_shift = 2 * math.pi * i / num_lights
        x, y = get_position(t, phase_shift)
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    # Update the display
    pygame.display.flip()

    # Increment time
    t += 1 / FPS

    # Control the frame rate
    clock.tick(FPS)

 pygame.quit()
 sys.exit()
