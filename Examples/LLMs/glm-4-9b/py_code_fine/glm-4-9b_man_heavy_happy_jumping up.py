
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Parameters for the "happyman" jumping
radius = 20
amplitude = 100
frequency = 0.5
phase_shift = math.pi / 4

# Function to simulate the jumping motion of the "happyman"
def jumping_motion(t, amplitude, frequency, phase_shift):
    x = width // 2
    y = height - amplitude * math.sin(t * frequency + phase_shift) - 50
    return x, y

# Main loop
running = True
t = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(black)

    # Update the jumping motion
    x, y = jumping_motion(t, amplitude, frequency, phase_shift)

    # Draw 15 point-lights around the "happyman"
    for i in range(15):
        angle = 2 * math.pi * i / 15
        offset_x = radius * math.cos(angle)
        offset_y = radius * math.sin(angle)
        point_light_x = x + offset_x
        point_light_y = y + offset_y
        pygame.draw.circle(screen, white, (int(point_light_x), int(point_light_y)), 5)

    # Update the display
    pygame.display.flip()

    # Increment time
    t += 0.1

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()
