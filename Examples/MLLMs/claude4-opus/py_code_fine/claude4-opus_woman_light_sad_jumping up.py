
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
POINTS = 15
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Points' initial positions (Y-coordinates)
point_positions = [
    (WIDTH // 2, HEIGHT // 3 + i * 10) for i in range(POINTS)
]

# Main loop
running = True
clock = pygame.time.Clock()

# Animation parameters
jump_amplitude = 100  # Maximum height of jump
jump_duration = 1.0    # Total duration of jump in seconds
offset = 0             # Vertical offset for jumping motion

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BACKGROUND_COLOR)

    # Calculate the jumping motion
    t = (pygame.time.get_ticks() / 1000) % jump_duration  # Time from 0 to jump_duration
    if t <= jump_duration / 2:  # Ascending phase
        offset = (-4 * jump_amplitude * (t - jump_duration / 4)**2 + jump_amplitude)
    else:  # Descending phase
        offset = (4 * jump_amplitude * (t - 3 * jump_duration / 4)**2 - jump_amplitude)

    # Draw points
    for index in range(POINTS):
        x = point_positions[index][0]
        y = int(point_positions[index][1] - offset)
        pygame.draw.circle(screen, POINT_COLOR, (x, y), 5)

    # Update screen
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
