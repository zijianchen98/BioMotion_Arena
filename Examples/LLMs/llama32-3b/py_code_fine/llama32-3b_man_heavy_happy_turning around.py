
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Set up the points of interest
points_of_interest = [
    {"x": 100, "y": 100, "angle": 0},
    {"x": 200, "y": 200, "angle": 0},
    {"x": 300, "y": 300, "angle": 0},
    {"x": 400, "y": 400, "angle": 0},
    {"x": 500, "y": 500, "angle": 0},
    {"x": 600, "y": 600, "angle": 0},
    {"x": 700, "y": 700, "angle": 0},
    {"x": 800, "y": 800, "angle": 0},
    {"x": 300, "y": 100, "angle": 0},
    {"x": 300, "y": 200, "angle": 0},
    {"x": 300, "y": 300, "angle": 0},
    {"x": 300, "y": 400, "angle": 0},
    {"x": 300, "y": 500, "angle": 0},
    {"x": 300, "y": 600, "angle": 0},
    {"x": 300, "y": 700, "angle": 0},
]

# Set up the animation
angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.fill(BLACK)

    # Draw the point lights
    for point in points_of_interest:
        # Calculate the position of the point light
        x = int(WIDTH / 2 + point["x"] * math.cos(angle) - point["y"] * math.sin(angle))
        y = int(HEIGHT / 2 + point["x"] * math.sin(angle) + point["y"] * math.cos(angle))

        # Draw the point light
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    # Increase the angle
    angle += 0.01

    # Update the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
