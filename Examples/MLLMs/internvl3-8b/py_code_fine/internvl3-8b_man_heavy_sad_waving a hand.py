
import pygame
import sys

# Configuration
WIDTH, HEIGHT = 800, 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initializing Pygame
pygame.init()

# Setting up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Point-light positions
points = [
    [100, 100], [150, 125], [200, 85], [175, 50], [85, 30], [125, 25],
    [160, 10], [210, 75], [245, 50], [230, 25], [145, 10], [85, 50],
    [130, 125], [170, 70], [205, 50]
]

def animate(points):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        for coord in points:
            pygame.draw.circle(screen, WHITE, coord, 4)
        pygame.display.flip()
        clock.tick(FPS)
        pygame.time.delay(int(1000 / FPS))

    pygame.quit()
    sys.exit()

# Start the animation
animate(points)
