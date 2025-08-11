
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Bowing")
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define initial joint positions (standing pose)
points = [
    # Head (0)
    {'base_x': 400, 'base_y': 100, 'amp_y': 40, 'amp_x': 0},
    # Neck (1)
    {'base_x': 400, 'base_y': 130, 'amp_y': 50, 'amp_x': 0},
    # Shoulders (2, 3)
    {'base_x': 370, 'base_y': 150, 'amp_y': 50, 'amp_x': 15},
    {'base_x': 430, 'base_y': 150, 'amp_y': 50, 'amp_x': -15},
    # Elbows (4, 5)
    {'base_x': 350, 'base_y': 180, 'amp_y': 30, 'amp_x': 10},
    {'base_x': 450, 'base_y': 180, 'amp_y': 30, 'amp_x': -10},
    # Hands (6, 7)
    {'base_x': 330, 'base_y': 210, 'amp_y': 20, 'amp_x': 5},
    {'base_x': 470, 'base_y': 210, 'amp_y': 20, 'amp_x': -5},
    # Torso (8)
    {'base_x': 400, 'base_y': 180, 'amp_y': 60, 'amp_x': 0},
    # Hips (9, 10)
    {'base_x': 380, 'base_y': 250, 'amp_y': 20, 'amp_x': 0},
    {'base_x': 420, 'base_y': 250, 'amp_y': 20, 'amp_x': 0},
    # Knees (11, 12)
    {'base_x': 380, 'base_y': 300, 'amp_y': 10, 'amp_x': 0},
    {'base_x': 420, 'base_y': 300, 'amp_y': 10, 'amp_x': 0},
    # Feet (13, 14)
    {'base_x': 380, 'base_y': 350, 'amp_y': 0, 'amp_x': 0},
    {'base_x': 420, 'base_y': 350, 'amp_y': 0, 'amp_x': 0},
]

# Define connections between joints
connections = [
    (0, 1), (1, 2), (1, 3), (2, 4), (3, 5),
    (4, 6), (5, 7), (1, 8), (8, 9), (8, 10),
    (9, 10), (9, 11), (10, 12), (11, 13), (12, 14)
]

running = True
time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Calculate animation phase
    phase = math.sin(time * 0.02)  # Controls animation speed
    
    # Update joint positions
    current_points = []
    for point in points:
        x = point['base_x'] + point['amp_x'] * phase
        y = point['base_y'] + point['amp_y'] * abs(phase)  # Absolute value for downward motion
        current_points.append((x, y))
    
    # Draw connections
    for connection in connections:
        start_pos = current_points[connection[0]]
        end_pos = current_points[connection[1]]
        pygame.draw.line(screen, WHITE, start_pos, end_pos, 2)
    
    # Draw joints
    for (x, y) in current_points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS
    time += 1

pygame.quit()
