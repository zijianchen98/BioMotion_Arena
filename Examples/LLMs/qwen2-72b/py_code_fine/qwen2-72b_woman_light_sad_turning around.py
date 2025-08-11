
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the drawing window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the points
points = [{'x': random.randint(0, screen_width), 'y': random.randint(0, screen_height),
           'vx': random.uniform(-1, 1), 'vy': random.uniform(-1, 1)} for _ in range(15)]

# Set up the clock
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

    # Update and draw the points
    for point in points:
        point['x'] += point['vx']
        point['y'] += point['vy']

        # Bounce off the edges of the screen
        if point['x'] < 0 or point['x'] > screen_width:
            point['vx'] *= -1
        if point['y'] < 0 or point['y'] > screen_height:
            point['vy'] *= -1

        # Draw the point
        pygame.draw.circle(screen, WHITE, [int(point['x']), int(point['y'])], 3)

    # Flip the display
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
