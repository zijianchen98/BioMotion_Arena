
import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point Light Animation")

# Set up clock
clock = pygame.time.Clock()

# Number of points
num_points = 15

# Create a list of points with random positions and velocities
points = []
for _ in range(num_points):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)
    points.append({'pos': [x, y], 'vel': [vx, vy]})

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update points
    for point in points:
        point['pos'][0] += point['vel'][0]
        point['pos'][1] += point['vel'][1]

        # Bounce off walls
        if point['pos'][0] < 0 or point['pos'][0] > screen_width:
            point['vel'][0] *= -1
        if point['pos'][1] < 0 or point['pos'][1] > screen_height:
            point['vel'][1] *= -1

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw points
    for point in points:
        pygame.draw.circle(screen, (255, 255, 255), (int(point['pos'][0]), int(point['pos'][1])), 3)

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
