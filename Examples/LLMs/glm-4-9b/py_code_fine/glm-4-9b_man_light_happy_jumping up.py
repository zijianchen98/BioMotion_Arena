
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Clock to control the speed of the animation
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-lights positions for 'happyman' jumping
points = []
for _ in range(15):
    x = width // 2
    y = height - 100 + 200 * math.sin(math.pi * 2 * 0.1 * _)
    points.append([x, y])

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # User event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update point-lights positions to simulate jumping
    t = pygame.time.get_ticks() / 1000.0
    for i, point in enumerate(points):
        x = width // 2 + 20 * math.sin(t + i * 0.1)
        y = height - 100 + 100 * math.sin(t * 2 * math.pi) + 200 * math.sin(math.pi * 2 * 0.1 * i)
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 4)

    # Update display
    pygame.display.flip()

    # Maintain frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()
