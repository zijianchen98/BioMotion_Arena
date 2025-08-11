
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Biological Motion Animation")

# Define point parameters for 15 points
points = [
    # Head (0)
    {'base_x': 400, 'base_y': 100, 'amp_x': 0, 'amp_y': 0, 'freq': 1.0, 'phase_x': 0.0, 'phase_y': 0.0},
    # Right Shoulder (1)
    {'base_x': 350, 'base_y': 150, 'amp_x': 5, 'amp_y': 0, 'freq': 1.0, 'phase_x': 0.0, 'phase_y': 0.0},
    # Right Elbow (2)
    {'base_x': 330, 'base_y': 200, 'amp_x': 15, 'amp_y': 5, 'freq': 1.0, 'phase_x': 0.5, 'phase_y': 0.5},
    # Right Hand (3) - Main waving point
    {'base_x': 310, 'base_y': 250, 'amp_x': 30, 'amp_y': 10, 'freq': 1.0, 'phase_x': 1.0, 'phase_y': 1.0},
    # Left Shoulder (4)
    {'base_x': 450, 'base_y': 150, 'amp_x': 0, 'amp_y': 0, 'freq': 1.0, 'phase_x': 0.0, 'phase_y': 0.0},
    # Left Elbow (5)
    {'base_x': 470, 'base_y': 200, 'amp_x': 0, 'amp_y': 0, 'freq': 1.0, 'phase_x': 0.0, 'phase_y': 0.0},
    # Left Hand (6)
    {'base_x': 490, 'base_y': 250, 'amp_x': 0, 'amp_y': 0, 'freq': 1.0, 'phase_x': 0.0, 'phase_y': 0.0},
    # Upper Torso (7) - Counterbalance movement
    {'base_x': 400, 'base_y': 200, 'amp_x': -5, 'amp_y': 0, 'freq': 1.0, 'phase_x': 1.0, 'phase_y': 0.0},
    # Right Hip (8)
    {'base_x': 350, 'base_y': 250, 'amp_x': 5, 'amp_y': 0, 'freq': 1.0, 'phase_x': 0.3, 'phase_y': 0.0},
    # Right Knee (9)
    {'base_x': 330, 'base_y': 300, 'amp_x': 5, 'amp_y': 5, 'freq': 1.0, 'phase_x': 0.6, 'phase_y': 0.0},
    # Right Foot (10)
    {'base_x': 310, 'base_y': 350, 'amp_x': 5, 'amp_y': 5, 'freq': 1.0, 'phase_x': 0.6, 'phase_y': 0.0},
    # Left Hip (11)
    {'base_x': 450, 'base_y': 250, 'amp_x': 5, 'amp_y': 0, 'freq': 1.0, 'phase_x': 0.3, 'phase_y': 0.0},
    # Left Knee (12)
    {'base_x': 470, 'base_y': 300, 'amp_x': 5, 'amp_y': 0, 'freq': 1.0, 'phase_x': 0.6, 'phase_y': 0.0},
    # Left Foot (13)
    {'base_x': 490, 'base_y': 350, 'amp_x': 5, 'amp_y': 0, 'freq': 1.0, 'phase_x': 0.6, 'phase_y': 0.0},
    # Lower Torso (14) - Counterbalance movement
    {'base_x': 400, 'base_y': 250, 'amp_x': -5, 'amp_y': 0, 'freq': 1.0, 'phase_x': 1.0, 'phase_y': 0.0}
]

# Main animation loop
clock = pygame.time.Clock()
time = 0.0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Update and draw points
    for point in points:
        x = base_x + amp_x * sin(freq * time + phase_x)
        x = point['base_x'] + point['amp_x'] * math.sin(point['freq'] * time + point['phase_x'])
        y = point['base_y'] + point['amp_y'] * math.sin(point['freq'] * time + point['phase_y'])
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    pygame.display.flip()
    time += 0.05  # Control animation speed
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
