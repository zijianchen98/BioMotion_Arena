
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the position and speed of the point
x, y = WIDTH // 2, HEIGHT // 2
speed = 2
angle = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the point
    pygame.draw.circle(screen, WHITE, (x, y), 5)

    # Update the position of the point
    x += math.cos(math.radians(angle)) * speed
    y += math.sin(math.radians(angle)) * speed

    # Update the angle
    angle += 1

    # If the point goes off the screen, reset it
    if x < 0 or x > WIDTH or y < 0 or y > HEIGHT:
        x, y = WIDTH // 2, HEIGHT // 2
        angle = 0

    # Update the display
    pygame.display.flip()

    # Delay to control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
