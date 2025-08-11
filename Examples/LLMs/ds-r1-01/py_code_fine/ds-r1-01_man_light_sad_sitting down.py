
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point positions (start, end) for 15 body points
points = [
    # Head
    ((400, 200), (400, 300)),
    # Neck
    ((400, 250), (400, 320)),
    # Left shoulder
    ((360, 280), (360, 350)),
    # Right shoulder
    ((440, 280), (440, 350)),
    # Left elbow
    ((340, 340), (340, 400)),
    # Right elbow
    ((460, 340), (460, 400)),
    # Left wrist
    ((320, 380), (320, 450)),
    # Right wrist
    ((480, 380), (480, 450)),
    # Hip center
    ((400, 400), (400, 500)),
    # Left hip
    ((380, 400), (380, 500)),
    # Right hip
    ((420, 400), (420, 500)),
    # Left knee
    ((380, 500), (380, 560)),
    # Right knee
    ((420, 500), (420, 560)),
    # Left ankle
    ((380, 580), (380, 580)),
    # Right ankle
    ((420, 580), (420, 580)),
]

# Animation parameters
DURATION = 2000  # 2 seconds in milliseconds

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate normalized time with easing
    current_time = pygame.time.get_ticks() - start_time
    tt = (current_time % DURATION) / DURATION
    eased_tt = (math.sin(math.pi * tt - math.pi/2) + 1) / 2  # Smooth easing

    screen.fill(BLACK)

    # Draw each point-light
    for start, end in points:
        x = start[0] + (end[0] - start[0]) * eased_tt
        y = start[1] + (end[1] - start[1]) * eased_tt
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()
sys.exit()
