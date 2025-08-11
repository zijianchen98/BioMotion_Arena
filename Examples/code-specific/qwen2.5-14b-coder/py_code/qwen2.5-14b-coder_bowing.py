
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bowing Animation")

# Clock to control frame rate
clock = pygame.time.Clock()

# Number of point-lights
NUM_LIGHTS = 15

# Define the positions of the point-lights
lights = [
    {"x": 400, "y": 300, "angle": 0, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 0.1, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 0.2, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 0.3, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 0.4, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 0.5, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 0.6, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 0.7, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 0.8, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 0.9, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 1.0, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 1.1, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 1.2, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 1.3, "speed": 0.02},
    {"x": 400, "y": 300, "angle": 1.4, "speed": 0.02},
]

# Bowing parameters
bowing_angle = 0
bowing_speed = 0.05

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update bowing angle
    bowing_angle += bowing_speed
    if bowing_angle > math.pi / 4 or bowing_angle < -math.pi / 4:
        bowing_speed *= -1

    # Update light positions
    for light in lights:
        light["angle"] += light["speed"]
        light["x"] = 400 + 150 * math.cos(bowing_angle + light["angle"])
        light["y"] = 300 + 150 * math.sin(bowing_angle + light["angle"])

    # Clear screen
    screen.fill(BLACK)

    # Draw point-lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light["x"]), int(light["y"])), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
