
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BG_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5

# Animation settings
fps = 60
clock = pygame.time.Clock()
cycle_duration = 2.5  # Slower cycle for heavier appearance
jump_height = 50      # Reduced jump height

# Define points' relative positions and movement functions
points = []

# Torso (central point)
torso_x = screen_width // 2

# Define points with biomechanically plausible movements
points = [
    # Head
    {'x_offset': lambda p: 0, 'y_offset': lambda p: -25},
    
    # Shoulders
    {'x_offset': lambda p: -25*math.cos(2*math.pi*p), 'y_offset': lambda p: 0},
    {'x_offset': lambda p: 25*math.cos(2*math.pi*p), 'y_offset': lambda p: 0},
    
    # Elbows
    {'x_offset': lambda p: -40 + 15*math.sin(4*math.pi*p), 'y_offset': lambda p: 35},
    {'x_offset': lambda p: 40 - 15*math.sin(4*math.pi*p), 'y_offset': lambda p: 35},
    
    # Hands
    {'x_offset': lambda p: -50 + 30*math.sin(4*math.pi*p), 'y_offset': lambda p: 70},
    {'x_offset': lambda p: 50 - 30*math.sin(4*math.pi*p), 'y_offset': lambda p: 70},
    
    # Hips
    {'x_offset': lambda p: -20*math.cos(2*math.pi*p), 'y_offset': lambda p: 30},
    {'x_offset': lambda p: 20*math.cos(2*math.pi*p), 'y_offset': lambda p: 30},
    
    # Knees
    {'x_offset': lambda p: -30 + 10*math.sin(4*math.pi*p + math.pi/2), 'y_offset': lambda p: 60 + 20*abs(math.sin(2*math.pi*p))},
    {'x_offset': lambda p: 30 - 10*math.sin(4*math.pi*p + math.pi/2), 'y_offset': lambda p: 60 + 20*abs(math.sin(2*math.pi*p))},
    
    # Feet
    {'x_offset': lambda p: -40 + 20*math.sin(4*math.pi*p), 'y_offset': lambda p: 90 + 30*math.sin(2*math.pi*p)},
    {'x_offset': lambda p: 40 - 20*math.sin(4*math.pi*p), 'y_offset': lambda p: 90 + 30*math.sin(2*math.pi*p)},
    
    # Additional torso points for weight emphasis
    {'x_offset': lambda p: 0, 'y_offset': lambda p: 15},
    {'x_offset': lambda p: 0, 'y_offset': lambda p: 30},
    {'x_offset': lambda p: 0, 'y_offset': lambda p: -10}
]

# Main loop
running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate current time and phase
    current_time = pygame.time.get_ticks() - start_time
    phase = (current_time / 1000 % cycle_duration) / cycle_duration

    # Torso vertical position with heavier movement
    torso_y = screen_height//2 - jump_height*(1 - (2*phase - 1)**2) + 50  # Lower baseline

    # Clear screen
    screen.fill(BG_COLOR)

    # Draw all points
    for point in points:
        try:
            x = torso_x + point['x_offset'](phase)
            y = torso_y + point['y_offset'](phase)
        except:
            x = torso_x + point['x_offset']
            y = torso_y + point['y_offset']
        pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), POINT_RADIUS)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
