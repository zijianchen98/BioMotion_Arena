
import pygame
import random
import time

# Define the window dimensions
width, height = 800, 600

# Initialize Pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Sad Woman Animation")

# Define the positions of the 15 points
points = [(100, 600), (120, 200), (130, 270), (110, 150), (90, 210), (70, 290), (50, 330),
          (60, 360), (40, 420), (20, 480), (150, 420), (170, 360), (155, 300), (125, 210),
          (115, 180), (85, 150)]

# Define the speed of the movement
speed = 1

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the 15 points
    for point in points:
        point[0] += speed
        if point[0] > width:
            point[0] = -50
            point[1] = random.randint(180, 280)

    # Clear the screen with a black background
    screen.fill((0, 0, 0))

    # Draw white points at the positions defined
    for p in points:
        pygame.draw.circle(screen, (255, 255, 255), p, 10)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
