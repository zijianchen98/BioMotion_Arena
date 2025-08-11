
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Biological Motion Animation')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define parameters
num_points = 15
radius = 100
center = (width // 2, height // 2)
speed = 0.05
time = 0

# Define the points for the waving hand (simplified to an arc for this example)
points = []
for i in range(num_points):
    angle = 2 * math.pi * i / num_points - math.pi / 2
    points.append([center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle)])

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the positions of the points to simulate waving
    for i, point in enumerate(points):
        angle = 2 * math.pi * i / num_points - math.pi / 2 + math.sin(time + i * 0.2) * 0.5
        point[0] = center[0] + radius * math.cos(angle)
        point[1] = center[1] + radius * math.sin(angle)

    # Fill the screen with black
    display.fill(BLACK)

    # Draw the points
    for point in points:
        pygame.draw.circle(display, WHITE, point, 5)

    # Update the display
    pygame.display.flip()

    # Control the speed of the animation
    time += speed
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
