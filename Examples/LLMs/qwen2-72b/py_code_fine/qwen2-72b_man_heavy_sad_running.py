
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the clock
clock = pygame.time.Clock()

# Number of points
num_points = 15

# Initialize point positions and velocities
points = []
for _ in range(num_points):
    x = random.randint(0, width)
    y = random.randint(0, height)
    vx = random.uniform(-2, 2)
    vy = random.uniform(-2, 2)
    points.append({"pos": [x, y], "vel": [vx, vy]})

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Update and draw points
    for point in points:
        # Update position
        point["pos"][0] += point["vel"][0]
        point["pos"][1] += point["vel"][1]

        # Keep points on screen
        if point["pos"][0] < 0 or point["pos"][0] > width:
            point["vel"][0] *= -1
        if point["pos"][1] < 0 or point["pos"][1] > height:
            point["vel"][1] *= -1

        # Draw point
        pygame.draw.circle(screen, white, (int(point["pos"][0]), int(point["pos"][1])), 5)

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
