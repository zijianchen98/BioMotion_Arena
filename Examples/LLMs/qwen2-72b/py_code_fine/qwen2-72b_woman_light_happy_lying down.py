
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the drawing window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption("Point-Light Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# List to store point positions
points = []

# Number of points
num_points = 15

# Add initial positions for points
for _ in range(num_points):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    points.append([x, y])

# Speed of each point
speeds = [random.randint(1, 5) for _ in range(num_points)]

# Clock object to control frame rate
clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill(BLACK)

    # Update point positions
    for i, point in enumerate(points):
        dx = random.choice([-1, 1]) * speeds[i]
        dy = random.choice([-1, 1]) * speeds[i]
        new_x = point[0] + dx
        new_y = point[1] + dy

        # Keep points within the screen boundaries
        if 0 <= new_x <= screen_width:
            point[0] = new_x
        else:
            point[0] = screen_width - (new_x - screen_width) if new_x > screen_width else -new_x

        if 0 <= new_y <= screen_height:
            point[1] = new_y
        else:
            point[1] = screen_height - (new_y - screen_height) if new_y > screen_height else -new_y

        # Draw the point
        pygame.draw.circle(screen, WHITE, (point[0], point[1]), 3)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
