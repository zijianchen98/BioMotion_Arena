
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set dimensions and colors
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sadman with Heavy Weight Forward Rolling")

# Define parameters for the point lights
num_points = 15
point_radius = 5
fps = 60
clock = pygame.time.Clock()

# Define a function for generating the positions of point lights
def get_positions(frame):
    positions = []
    for i in range(num_points):
        # Calculate the angle for each point light
        angle = (i * (math.pi / 7) + frame * 0.1) % (2 * math.pi)

        # Calculate positions based on a rolling motion
        x = WIDTH // 2 + 100 * math.sin(angle)  # X position oscillates in a sine wave
        y = HEIGHT // 2 + (i - num_points // 2) * 15 + 100 * math.cos(angle)  # Y position nearly linear, with oscillation

        positions.append((x, y))
    return positions

# Main loop
frame = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Get positions and draw point lights
    positions = get_positions(frame)
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), point_radius)

    # Update the display
    pygame.display.flip()

    # Increment frame count and control frame rate
    frame += 1
    clock.tick(fps)
