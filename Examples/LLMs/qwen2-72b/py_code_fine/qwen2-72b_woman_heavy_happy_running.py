
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point light parameters
num_points = 15
points = []
for _ in range(num_points):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    points.append([x, y])

# Simulation parameters
speed = 5
angle = 0
angle_change = 0.05

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update points based on running motion
    for i, point in enumerate(points):
        angle += angle_change
        if i % 3 == 0:  # Legs
            point[0] += speed * math.cos(angle)
            point[1] += speed * math.sin(angle)
        elif i % 3 == 1:  # Body
            point[0] += speed * math.cos(angle + math.pi / 4)
            point[1] += speed * math.sin(angle + math.pi / 4)
        else:  # Arms
            point[0] += speed * math.cos(angle - math.pi / 4)
            point[1] += speed * math.sin(angle - math.pi / 4)

        # Draw point
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 3)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
