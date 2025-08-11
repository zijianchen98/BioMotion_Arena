
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60
RADIUS = 100
SPEED = 0.01

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create a list to hold the point-lights
point_lights = []
for i in range(15):
    angle = i * (2 * math.pi / 15)
    x = WIDTH // 2 + RADIUS * math.cos(angle)
    y = HEIGHT // 2 + RADIUS * math.sin(angle)
    point_lights.append((x, y))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the point-lights
    for i in range(15):
        angle = i * (2 * math.pi / 15) + SPEED
        x = WIDTH // 2 + RADIUS * math.cos(angle)
        y = HEIGHT // 2 + RADIUS * math.sin(angle)
        point_lights[i] = (x, y)

    # Draw the point-lights
    screen.fill((0, 0, 0))
    for x, y in point_lights:
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Clean up Pygame
pygame.quit()
