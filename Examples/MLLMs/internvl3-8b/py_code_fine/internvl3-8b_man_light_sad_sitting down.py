
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sadman Sitting Down Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define point-light stimuli
points = [
    [(WIDTH//2 - 25, HEIGHT//2 - 25), (WIDTH//2 + 25, HEIGHT//2 - 25), (WIDTH//2, HEIGHT//2 + 25)],
    [(WIDTH//2, HEIGHT//2 - 25), (WIDTH//2 - 10, HEIGHT//2 - 15), (WIDTH//2 + 10, HEIGHT//2 - 15)],
    [(WIDTH//2, HEIGHT//2 + 25), (WIDTH//2 - 10, HEIGHT//2 + 15), (WIDTH//2 + 10, HEIGHT//2 + 15)],
    [(WIDTH//2 - 25, HEIGHT//2 - 20), (WIDTH//2 + 25, HEIGHT//2 - 20), (WIDTH//2, HEIGHT//2 + 20)],
    [(WIDTH//2 - 25, HEIGHT//2 + 20), (WIDTH//2 + 25, HEIGHT//2 + 20), (WIDTH//2, HEIGHT//2 - 20)],
]

# Define delta for movement
delta = 2

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)
    current_frame = pygame.time.get_ticks() // 30

    # Update and draw point-lights
    for point_set in points:
        for point in point_set:
            point[0] += random.uniform(-delta, delta)
            point[1] += random.uniform(-delta, delta)
            screen.set_at((int(point[0]), int(point[1])), WHITE)

    # Present the frame
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(30)

pygame.quit()
