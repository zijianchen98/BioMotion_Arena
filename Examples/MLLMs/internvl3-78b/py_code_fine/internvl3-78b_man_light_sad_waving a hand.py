
import pygame
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sadman Waving Hand Animation')

# Variables
points = [
    (WIDTH // 2 + 50, HEIGHT // 4),      # Head
    (WIDTH // 2, HEIGHT // 4 + 50),      # Body
    (WIDTH // 2 + 50, HEIGHT // 2),      # Left shoulder
    (WIDTH // 2 + 100, HEIGHT // 2),     # Left elbow
    (WIDTH // 2 + 150, HEIGHT // 2),     # Left hand
    (WIDTH // 2 - 50, HEIGHT // 2),      # Right shoulder
    (WIDTH // 2 - 50, HEIGHT // 2 + 50), # Waist
    (WIDTH // 2 - 100, HEIGHT // 2),     # Right elbow
    (WIDTH // 2 - 150, HEIGHT // 2),     # Right hand
    (WIDTH // 2, HEIGHT // 2 + 200),     # Left leg
    (WIDTH // 2, HEIGHT // 2 + 300),     # Left foot
    (WIDTH // 2 - 50, HEIGHT // 2 + 200),# Right leg
    (WIDTH // 2 - 50, HEIGHT // 2 + 300),# Right foot
    (WIDTH // 2 - 10, HEIGHT // 2 + 50), # Left eye
    (WIDTH // 2 + 10, HEIGHT // 2 + 50), # Right eye
]
wave_angle = 0
wave_offset = 10

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    new_points = []
    for x, y in points:
        if 150 <= x <= 200 or -50 <= x <= 0:
            x += math.sin(wave_angle) * wave_offset
        new_points.append((x, y))
    
    for x, y in new_points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)
    
    pygame.display.flip()
    wave_angle += 0.05
    clock.tick(FPS)

# Quit
pygame.quit()
