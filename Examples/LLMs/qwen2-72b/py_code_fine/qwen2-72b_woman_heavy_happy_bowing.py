
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Happy Woman Bowing Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the clock
clock = pygame.time.Clock()

# Set the number of points
num_points = 15

# Define initial positions for the points
points = [(random.randint(0, screen_width), random.randint(0, screen_height)) for _ in range(num_points)]

# Define velocities for the points
velocities = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(num_points)]

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update positions and velocities based on the action (bowing)
    for i in range(num_points):
        x, y = points[i]
        vx, vy = velocities[i]

        # Simulate a simple bowing motion
        if y > screen_height // 2:
            vy -= 0.1  # Move upwards
        else:
            vy += 0.1  # Move downwards

        # Limit velocity to prevent points from moving too fast
        if abs(vy) > 5:
            vy *= -0.9  # Reverse direction and slow down

        # Update position
        x += vx
        y += vy

        # Wrap around the screen
        if x > screen_width:
            x = 0
        elif x < 0:
            x = screen_width
        if y > screen_height:
            y = 0
        elif y < 0:
            y = screen_height

        # Update the point's position and velocity
        points[i] = (x, y)
        velocities[i] = (vx, vy)

        # Draw the point
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
