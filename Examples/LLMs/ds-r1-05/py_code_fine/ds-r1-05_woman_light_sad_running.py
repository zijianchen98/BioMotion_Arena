
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

# Define parameters for 15 points with coordinated motion
points_params = [
    # Head (vertical bob)
    {'dx': 0, 'dy': -50, 'ax': 0, 'ay': 5, 'freq': 2, 'phase': 0},
    # Left arm system (back when right leg forward)
    {'dx': -20, 'dy': -30, 'ax': 25, 'ay': 0, 'freq': 1, 'phase': math.pi},
    {'dx': -40, 'dy': -10, 'ax': 20, 'ay': 0, 'freq': 1, 'phase': math.pi},
    {'dx': -60, 'dy': 10, 'ax': 15, 'ay': 0, 'freq': 1, 'phase': math.pi},
    # Right arm system (forward when right leg forward)
    {'dx': 20, 'dy': -30, 'ax': 25, 'ay': 0, 'freq': 1, 'phase': 0},
    {'dx': 40, 'dy': -10, 'ax': 20, 'ay': 0, 'freq': 1, 'phase': 0},
    {'dx': 60, 'dy': 10, 'ax': 15, 'ay': 0, 'freq': 1, 'phase': 0},
    # Left leg system (forward when right leg back)
    {'dx': -15, 'dy': 0, 'ax': 0, 'ay': 0, 'freq': 0, 'phase': 0},
    {'dx': -15, 'dy': 30, 'ax': 30, 'ay': 0, 'freq': 1, 'phase': 0},
    {'dx': -15, 'dy': 60, 'ax': 45, 'ay': 0, 'freq': 1, 'phase': 0},
    # Right leg system (forward when left leg back)
    {'dx': 15, 'dy': 0, 'ax': 0, 'ay': 0, 'freq': 0, 'phase': math.pi},
    {'dx': 15, 'dy': 30, 'ax': 30, 'ay': 0, 'freq': 1, 'phase': math.pi},
    {'dx': 15, 'dy': 60, 'ax': 45, 'ay': 0, 'freq': 1, 'phase': math.pi},
    # Torso (static)
    {'dx': 0, 'dy': -25, 'ax': 0, 'ay': 0, 'freq': 0, 'phase': 0},
    # Neck (small vertical bob)
    {'dx': 0, 'dy': -40, 'ax': 0, 'ay': 3, 'freq': 2, 'phase': 0},
]

# Animation parameters
time = 0
base_speed = 0.8
root_x = width // 4
base_root_y = height // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    
    # Update root position with horizontal movement and vertical bob
    root_x = (root_x + base_speed) % (width * 1.2)
    root_y = base_root_y + 10 * math.sin(time * 2)
    
    # Calculate point positions
    points = []
    for param in points_params:
        x = root_x + param['dx'] + param['ax'] * math.sin(time * param['freq'] + param['phase'])
        y = root_y + param['dy'] + param['ay'] * math.sin(time * param['freq'] + param['phase'])
        points.append((int(x), int(y)))
    
    # Draw points
    for pos in points:
        pygame.draw.circle(screen, white, pos, 5)

    pygame.display.flip()
    clock.tick(30)
    time += 0.1

pygame.quit()
sys.exit()
