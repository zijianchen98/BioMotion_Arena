
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sad Man Jumping Animation")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Number of points
num_points = 15

# Create a list to store points' positions and velocities
points = []
for _ in range(num_points):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    vy = random.uniform(-10, -20)  # Initial vertical velocity upwards
    points.append({"x": x, "y": y, "vy": vy})

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the positions of the points
    for point in points:
        point["y"] += point["vy"]
        if point["y"] < 0 or point["y"] > screen_height:
            point["vy"] *= -0.9  # Bounce back with some energy loss
        else:
            point["vy"] += 0.5  # Gravity effect

    # Fill the screen with black
    screen.fill(black)

    # Draw the points
    for point in points:
        pygame.draw.circle(screen, white, (point["x"], point["y"]), 3)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
