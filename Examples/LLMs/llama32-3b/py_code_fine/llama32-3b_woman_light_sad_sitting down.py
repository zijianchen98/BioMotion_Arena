
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the point-lights
point_lights = [
    {"x": 100, "y": 100, "angle": 0, "radius": 10},
    {"x": 200, "y": 100, "angle": 0, "radius": 10},
    {"x": 300, "y": 100, "angle": 0, "radius": 10},
    {"x": 400, "y": 100, "angle": 0, "radius": 10},
    {"x": 500, "y": 100, "angle": 0, "radius": 10},
    {"x": 600, "y": 100, "angle": 0, "radius": 10},
    {"x": 100, "y": 200, "angle": 0, "radius": 10},
    {"x": 200, "y": 200, "angle": 0, "radius": 10},
    {"x": 300, "y": 200, "angle": 0, "radius": 10},
    {"x": 400, "y": 200, "angle": 0, "radius": 10},
    {"x": 500, "y": 200, "angle": 0, "radius": 10},
    {"x": 600, "y": 200, "angle": 0, "radius": 10},
    {"x": 100, "y": 300, "angle": 0, "radius": 10},
    {"x": 200, "y": 300, "angle": 0, "radius": 10},
    {"x": 300, "y": 300, "angle": 0, "radius": 10},
]

# Set up the clock
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the background
    screen.fill(BLACK)

    # Draw the point-lights
    for light in point_lights:
        angle = light["angle"]
        radius = light["radius"]
        x = light["x"] + radius * math.cos(angle)
        y = light["y"] + radius * math.sin(angle)
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 2)

        # Update the angle
        light["angle"] += 0.01

    # Draw the sad woman
    # For simplicity, we will just draw a circle
    pygame.draw.circle(screen, WHITE, (400, 400), 100)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
