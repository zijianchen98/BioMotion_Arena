
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Clock for limiting frame rate
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Parameters for the running woman
point_lights = [(WIDTH // 2, HEIGHT // 2)] * 15  # Starting positions
radius = 100
speed = 0.05
time_elapsed = 0

# Function to simulate running motion
def running_motion(t):
    return math.sin(t * 2 * math.pi * speed) * radius + WIDTH // 2, math.cos(t * 2 * math.pi * speed) * radius + HEIGHT // 2

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update point-light positions
    for i in range(len(point_lights)):
        time_elapsed += 0.01
        angle = 2 * math.pi * i / len(point_lights)
        x, y = running_motion(time_elapsed + angle)
        point_lights[i] = (int(x), int(y))

    # Draw point-lights
    for point in point_lights:
        pygame.draw.circle(screen, WHITE, point, 5)

    # Update display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
