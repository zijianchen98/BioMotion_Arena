
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Running")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 30
time = 0
speed = 0.1  # Overall speed modifier

# Body points parameters (15 points)
points = [
    # Head (1)
    {"phase": 0, "amp_y": 0.1, "amp_x": 0},
    # Shoulders (2)
    {"phase": 0, "amp_y": 0.05, "amp_x": 0.15},
    {"phase": 0, "amp_y": 0.05, "amp_x": -0.15},
    # Elbows (2)
    {"phase": 0.5, "amp_y": 0.1, "amp_x": 0.25},
    {"phase": 0.5, "amp_y": 0.1, "amp_x": -0.25},
    # Hands (2)
    {"phase": 0.7, "amp_y": 0.15, "amp_x": 0.3},
    {"phase": 0.7, "amp_y": 0.15, "amp_x": -0.3},
    # Hips (2)
    {"phase": 0.2, "amp_y": 0.05, "amp_x": 0.1},
    {"phase": 0.2, "amp_y": 0.05, "amp_x": -0.1},
    # Knees (2)
    {"phase": 0.3, "amp_y": 0.2, "amp_x": 0.15},
    {"phase": 0.8, "amp_y": 0.2, "amp_x": -0.15},
    # Ankles (2)
    {"phase": 0.4, "amp_y": 0.25, "amp_x": 0.2},
    {"phase": 0.9, "amp_y": 0.25, "amp_x": -0.2},
    # Feet (2)
    {"phase": 0.5, "amp_y": 0.3, "amp_x": 0.25},
    {"phase": 1.0, "amp_y": 0.3, "amp_x": -0.25},
]

def calculate_position(point, time):
    """Calculate position for a body point with dampened movement"""
    phase = time + point["phase"]
    x = math.sin(phase * 2) * point["amp_x"] * 0.8  # Reduced horizontal movement
    y = (math.cos(phase * 2) * point["amp_y"] + 
         abs(math.sin(phase)) * 0.1)  # Subtle bounce
    return (x * WIDTH/3 + WIDTH/2, 
            y * HEIGHT/3 + HEIGHT/2 + 50)  # Lower center position

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    time += speed * 0.5  # Slower movement for sad effect

    # Draw all points
    for point in points:
        x, y = calculate_position(point, time)
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 8)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
