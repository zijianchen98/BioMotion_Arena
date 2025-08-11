
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Woman Bowing Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Number of point lights
num_lights = 15

# Function to calculate point light positions for bowing motion
def calculate_light_positions(frame):
    positions = []
    # Calculate angles for each light based on frame number
    for i in range(num_lights):
        angle = (i / num_lights) * 2 * math.pi + (frame / 60.0) * math.pi
        radius = 200 + 50 * math.sin(angle)  # Radius changes to simulate bowing motion
        x = width // 2 + radius * math.cos(angle)
        y = height // 2 + radius * math.sin(angle)
        positions.append((x, y))
    return positions

# Main loop
clock = pygame.time.Clock()
running = True
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with black
    screen.fill(black)

    # Calculate and draw point lights
    light_positions = calculate_light_positions(frame)
    for pos in light_positions:
        pygame.draw.circle(screen, white, pos, 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

    # Increment frame counter
    frame += 1

# Quit Pygame
pygame.quit()
sys.exit()
