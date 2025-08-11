
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation: Happyman with Heavy Weight Sitting Down")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Parameters for the motion
center_x, center_y = WIDTH // 2, HEIGHT // 2
radius = 50
num_points = 15
speed = 0.02
time = 0

# Define the positions of the 15 point-lights
point_positions = [(center_x + radius * math.cos(2 * math.pi * i / num_points), center_y + radius * math.sin(2 * math.pi * i / num_points)) for i in range(num_points)]

# Define the motion pattern for sitting down
def sit_motion(t):
    # Adjust the angle based on time to simulate sitting down
    # The angle starts at a sitting position and gradually increases to a standing position
    angle = math.pi / 4 * (1 + math.cos(t))
    return angle

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update the time
    time += speed

    # Calculate new positions based on the sitting motion
    new_positions = []
    for i in range(num_points):
        angle = sit_motion(time + i * 2 * math.pi / num_points)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        new_positions.append((x, y))

    # Draw the point-lights
    for pos in new_positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
