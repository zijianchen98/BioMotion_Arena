
import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set background color to black
background_color = (0, 0, 0)

# Set point-light color to white
point_light_color = (255, 255, 255)

# Number of point-lights
num_points = 15

# Create a list to store point positions
points = [(random.randint(0, screen_width), random.randint(0, screen_height)) for _ in range(num_points)]

# Set frame rate
clock = pygame.time.Clock()
fps = 30

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(background_color)

    # Update point positions
    for i, (x, y) in enumerate(points):
        # Simple random movement
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        new_x = min(max(x + dx, 0), screen_width)
        new_y = min(max(y + dy, 0), screen_height)
        points[i] = (new_x, new_y)

    # Draw points
    for x, y in points:
        pygame.draw.circle(screen, point_light_color, (x, y), 2)

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(fps)

# Quit Pygame
pygame.quit()
