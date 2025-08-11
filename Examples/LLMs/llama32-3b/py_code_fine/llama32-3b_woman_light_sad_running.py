
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the point lights
point_lights = [
    {"x": 100, "y": 100, "radius": 5, "color": RED, "dx": 1, "dy": 0, "angle": 0},
    {"x": 150, "y": 100, "radius": 5, "color": ORANGE, "dx": 1, "dy": 0, "angle": 0},
    {"x": 200, "y": 100, "radius": 5, "color": YELLOW, "dx": 1, "dy": 0, "angle": 0},
    {"x": 250, "y": 100, "radius": 5, "color": GREEN, "dx": 1, "dy": 0, "angle": 0},
    {"x": 300, "y": 100, "radius": 5, "color": BLUE, "dx": 1, "dy": 0, "angle": 0},
    {"x": 350, "y": 100, "radius": 5, "color": PURPLE, "dx": 1, "dy": 0, "angle": 0},
    {"x": 400, "y": 100, "radius": 5, "color": CYAN, "dx": 1, "dy": 0, "angle": 0},
    {"x": 450, "y": 100, "radius": 5, "color": MAGENTA, "dx": 1, "dy": 0, "angle": 0},
    {"x": 500, "y": 100, "radius": 5, "color": RED, "dx": 1, "dy": 1, "angle": 0},
    {"x": 550, "y": 100, "radius": 5, "color": ORANGE, "dx": 1, "dy": 1, "angle": 0},
    {"x": 600, "y": 100, "radius": 5, "color": YELLOW, "dx": 1, "dy": 1, "angle": 0},
    {"x": 650, "y": 100, "radius": 5, "color": GREEN, "dx": 1, "dy": 1, "angle": 0},
    {"x": 700, "y": 100, "radius": 5, "color": BLUE, "dx": 1, "dy": 1, "angle": 0},
    {"x": 750, "y": 100, "radius": 5, "color": PURPLE, "dx": 1, "dy": 1, "angle": 0},
]

# Set up the animation
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.fill(BLACK)

    # Draw the point lights
    for point_light in point_lights:
        pygame.draw.circle(screen, point_light["color"], (point_light["x"], point_light["y"]), point_light["radius"])

    # Update the point lights
    for point_light in point_lights:
        point_light["x"] += point_light["dx"]
        point_light["y"] += point_light["dy"]
        point_light["angle"] += 0.01

    # Ensure the point lights don't move off the screen
    for point_light in point_lights:
        if point_light["x"] < 0 or point_light["x"] > WIDTH:
            point_light["dx"] = -point_light["dx"]
        if point_light["y"] < 0 or point_light["y"] > HEIGHT:
            point_light["dy"] = -point_light["dy"]

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
