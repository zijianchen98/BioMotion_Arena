
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen configuration
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Sitting Down")
clock = pygame.time.Clock()

# Animation parameters
duration = 2000  # Animation duration in milliseconds
current_time = 0

# Define 15 point-light positions (standing and sitting configurations)
standing_pos = [
    (400, 100), (400, 150), (350, 150), (450, 150),
    (350, 200), (450, 200), (350, 250), (450, 250),
    (400, 250), (350, 300), (450, 300), (350, 400),
    (450, 400), (350, 500), (450, 500)
]

sitting_pos = [
    (400, 200), (400, 250), (350, 250), (450, 250),
    (350, 300), (450, 300), (350, 350), (450, 350),
    (400, 400), (350, 450), (450, 450), (350, 450),
    (450, 450), (350, 500), (450, 500)
]

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate normalized time with smooth easing
    current_time = pygame.time.get_ticks() % duration
    progress = current_time / duration
    t = (1 - math.cos(progress * math.pi * 2)) / 2  # Smooth oscillating motion

    # Interpolate positions
    current_pos = []
    for i in range(15):
        x = standing_pos[i][0] + (sitting_pos[i][0] - standing_pos[i][0]) * t
        y = standing_pos[i][1] + (sitting_pos[i][1] - standing_pos[i][1]) * t
        current_pos.append((int(x), int(y)))

    # Render frame
    screen.fill((0, 0, 0))  # Black background
    for pos in current_pos:
        pygame.draw.circle(screen, (255, 255, 255), pos, 5)  # White points

    pygame.display.flip()
    clock.tick(60)  # 60 FPS for smooth animation

pygame.quit()
sys.exit()
