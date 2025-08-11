
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
RADIUS = 10
DURATION = 10000  # milliseconds

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")
clock = pygame.time.Clock()

# Point positions for a sad woman forward rolling
def get_point_positions(t):
    # Example positions (simplified); adjust for smoothness and realism
    angle = t / 100
    positions = [
        (WIDTH // 2, HEIGHT // 2 + 50 * math.sin(angle)),
        (WIDTH // 2 - 30, HEIGHT // 2 + 40 * math.sin(angle + math.pi / 4)),
        (WIDTH // 2 + 30, HEIGHT // 2 + 40 * math.sin(angle + math.pi / 4)),
        (WIDTH // 2 - 50, HEIGHT // 2 + 30 * math.sin(angle + math.pi / 2)),
        (WIDTH // 2 + 50, HEIGHT // 2 + 30 * math.sin(angle + math.pi / 2)),
        (WIDTH // 2 - 30, HEIGHT // 2 - 40 * math.sin(angle + 3 * math.pi / 4)),
        (WIDTH // 2 + 30, HEIGHT // 2 - 40 * math.sin(angle + 3 * math.pi / 4)),
        (WIDTH // 2 - 70, HEIGHT // 2 - 30 * math.sin(angle + math.pi)),
        (WIDTH // 2 + 70, HEIGHT // 2 - 30 * math.sin(angle + math.pi)),
        (WIDTH // 2 - 30, HEIGHT // 2 + 70 * math.sin(angle + 5 * math.pi / 4)),
        (WIDTH // 2 + 30, HEIGHT // 2 + 70 * math.sin(angle + 5 * math.pi / 4)),
        (WIDTH // 2 - 100, HEIGHT // 2 + 40 * math.sin(angle + 3 * math.pi / 2)),
        (WIDTH // 2 + 100, HEIGHT // 2 + 40 * math.sin(angle + 3 * math.pi / 2)),
        (WIDTH // 2 - 50, HEIGHT // 2 + 60 * math.sin(angle + 7 * math.pi / 4)),
        (WIDTH // 2 + 50, HEIGHT // 2 + 60 * math.sin(angle + 7 * math.pi / 4)),
        (WIDTH // 2, HEIGHT // 2 + 80 * math.sin(angle + 2 * math.pi))
    ]
    return positions

# Main loop
start_ticks = pygame.time.get_ticks()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_ticks = pygame.time.get_ticks()
    elapsed_time = current_ticks - start_ticks

    if elapsed_time >= DURATION:
        running = False

    screen.fill(BLACK)

    t = elapsed_time % (2 * math.pi * 100)
    for pos in get_point_positions(t):
        pygame.draw.circle(screen, WHITE, pos, RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
