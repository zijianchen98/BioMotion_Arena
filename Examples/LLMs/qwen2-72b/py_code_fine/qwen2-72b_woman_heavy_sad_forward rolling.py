
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Point Light Animation')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Simulation parameters
num_points = 15
points = []
gravity = 0.05
friction = 0.99
max_speed = 5

# Initialize points
for _ in range(num_points):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    vx = random.uniform(-2, 2)
    vy = random.uniform(-2, 2)
    points.append({'pos': [x, y], 'vel': [vx, vy]})

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update physics
    for point in points:
        point['vel'][1] += gravity
        point['vel'][0] *= friction
        point['vel'][1] *= friction
        point['vel'][0] = max(min(point['vel'][0], max_speed), -max_speed)
        point['vel'][1] = max(min(point['vel'][1], max_speed), -max_speed)
        point['pos'][0] += point['vel'][0]
        point['pos'][1] += point['vel'][1]

        # Wrap around the screen
        if point['pos'][0] > screen_width:
            point['pos'][0] = 0
        elif point['pos'][0] < 0:
            point['pos'][0] = screen_width
        if point['pos'][1] > screen_height:
            point['pos'][1] = 0
        elif point['pos'][1] < 0:
            point['pos'][1] = screen_height

    # Draw everything
    screen.fill(BLACK)
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point['pos'][0]), int(point['pos'][1])), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
