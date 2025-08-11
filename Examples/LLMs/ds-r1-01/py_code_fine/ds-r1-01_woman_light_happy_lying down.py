
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define 15 points with base positions and movement parameters
points = [
    # Head (subtle vertical movement)
    {'base_x': 400, 'base_y': 250, 'amp_x': 0, 'amp_y': 1, 'freq': 0.05, 'phase': 0},
    # Neck (connects to head and chest)
    {'base_x': 400, 'base_y': 260, 'amp_x': 0, 'amp_y': 1.5, 'freq': 0.06, 'phase': 0.2},
    # Right Shoulder (horizontal sway)
    {'base_x': 420, 'base_y': 270, 'amp_x': 0.5, 'amp_y': 2, 'freq': 0.1, 'phase': 0.5},
    # Left Shoulder
    {'base_x': 380, 'base_y': 270, 'amp_x': 0.5, 'amp_y': 2, 'freq': 0.1, 'phase': 0.5},
    # Right Elbow (arm movement)
    {'base_x': 440, 'base_y': 290, 'amp_x': 1, 'amp_y': 2.5, 'freq': 0.12, 'phase': 0.3},
    # Left Elbow
    {'base_x': 360, 'base_y': 290, 'amp_x': 1, 'amp_y': 2.5, 'freq': 0.12, 'phase': 0.3},
    # Right Wrist (hand movement)
    {'base_x': 460, 'base_y': 310, 'amp_x': 1.5, 'amp_y': 2, 'freq': 0.15, 'phase': 0.6},
    # Left Wrist
    {'base_x': 340, 'base_y': 310, 'amp_x': 1.5, 'amp_y': 2, 'freq': 0.15, 'phase': 0.6},
    # Chest (main breathing motion)
    {'base_x': 400, 'base_y': 280, 'amp_x': 0, 'amp_y': 4, 'freq': 0.08, 'phase': 0.0},
    # Abdomen (secondary breathing)
    {'base_x': 400, 'base_y': 300, 'amp_x': 0, 'amp_y': 2, 'freq': 0.09, 'phase': 0.1},
    # Hips (pelvic movement)
    {'base_x': 400, 'base_y': 320, 'amp_x': 0, 'amp_y': 2, 'freq': 0.1, 'phase': 0.2},
    # Right Knee (leg movement)
    {'base_x': 420, 'base_y': 340, 'amp_x': 0.5, 'amp_y': 3, 'freq': 0.12, 'phase': 0.4},
    # Left Knee
    {'base_x': 380, 'base_y': 340, 'amp_x': 0.5, 'amp_y': 3, 'freq': 0.12, 'phase': 0.4},
    # Right Ankle (foot movement)
    {'base_x': 440, 'base_y': 360, 'amp_x': 1, 'amp_y': 2.5, 'freq': 0.14, 'phase': 0.5},
    # Left Ankle
    {'base_x': 360, 'base_y': 360, 'amp_x': 1, 'amp_y': 2.5, 'freq': 0.14, 'phase': 0.5},
]

clock = pygame.time.Clock()
t = 0  # Time variable for animation

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update and draw each point
    for point in points:
        # Calculate displacement using sine waves
        dx = point['amp_x'] * math.sin(t * point['freq'] + point['phase'])
        dy = point['amp_y'] * math.sin(t * point['freq'] + point['phase'])
        x = point['base_x'] + dx
        y = point['base_y'] + dy
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 3)

    pygame.display.flip()
    t += 0.1  # Adjust animation speed
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
sys.exit()
