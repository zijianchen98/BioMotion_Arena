
import pygame
import math
import sys

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Sad Jump")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
amplitude = 40  # Reduced jump height for heavy appearance
period = 2.5    # Slower movement period
dt = 0.02

# Define 15 points with their relative positions and movement characteristics
points = [
    # Head (0)
    {'x_offset': 0, 'y_offset': -50, 'swing_x': 0, 'swing_x_phase': 0,
     'swing_y_amp': 0, 'swing_y_phase': 0},
    
    # Shoulders (1-2)
    {'x_offset': -20, 'y_offset': -30, 'swing_x': 8, 'swing_x_phase': 0,
     'swing_y_amp': 5, 'swing_y_phase': 0},
    {'x_offset': 20, 'y_offset': -30, 'swing_x': 8, 'swing_x_phase': math.pi,
     'swing_y_amp': 5, 'swing_y_phase': 0},
    
    # Elbows (3-4)
    {'x_offset': -35, 'y_offset': -10, 'swing_x': 12, 'swing_x_phase': 0.5*math.pi,
     'swing_y_amp': 10, 'swing_y_phase': 0.5*math.pi},
    {'x_offset': 35, 'y_offset': -10, 'swing_x': 12, 'swing_x_phase': 1.5*math.pi,
     'swing_y_amp': 10, 'swing_y_phase': 0.5*math.pi},
    
    # Hands (5-6)
    {'x_offset': -50, 'y_offset': 10, 'swing_x': 15, 'swing_x_phase': math.pi,
     'swing_y_amp': 15, 'swing_y_phase': math.pi},
    {'x_offset': 50, 'y_offset': 10, 'swing_x': 15, 'swing_x_phase': 0,
     'swing_y_amp': 15, 'swing_y_phase': math.pi},
    
    # Hips (7-8)
    {'x_offset': -15, 'y_offset': 20, 'swing_x': 4, 'swing_x_phase': 0,
     'swing_y_amp': 3, 'swing_y_phase': 0},
    {'x_offset': 15, 'y_offset': 20, 'swing_x': 4, 'swing_x_phase': math.pi,
     'swing_y_amp': 3, 'swing_y_phase': 0},
    
    # Knees (9-10)
    {'x_offset': -25, 'y_offset': 50, 'swing_x': 8, 'swing_x_phase': 0.5*math.pi,
     'swing_y_amp': 8, 'swing_y_phase': 0.5*math.pi},
    {'x_offset': 25, 'y_offset': 50, 'swing_x': 8, 'swing_x_phase': 1.5*math.pi,
     'swing_y_amp': 8, 'swing_y_phase': 0.5*math.pi},
    
    # Ankles (11-12)
    {'x_offset': -30, 'y_offset': 80, 'swing_x': 10, 'swing_x_phase': math.pi,
     'swing_y_amp': 10, 'swing_y_phase': math.pi},
    {'x_offset': 30, 'y_offset': 80, 'swing_x': 10, 'swing_x_phase': 0,
     'swing_y_amp': 10, 'swing_y_phase': math.pi},
    
    # Feet (13-14)
    {'x_offset': -35, 'y_offset': 90, 'swing_x': 4, 'swing_x_phase': 0,
     'swing_y_amp': 4, 'swing_y_phase': 0},
    {'x_offset': 35, 'y_offset': 90, 'swing_x': 4, 'swing_x_phase': math.pi,
     'swing_y_amp': 4, 'swing_y_phase': 0},
]

# Main loop
time = 0.0
center_x, center_y = width//2, height//2 + 100  # Lower center for heavy appearance

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    
    # Update time with modulo to keep it within period
    time = (time + dt) % period
    
    # Calculate body vertical displacement
    body_vertical = amplitude * (1 - math.cos(2 * math.pi * time / period))
    
    # Draw all points
    for point in points:
        # Horizontal movement
        x_swing = point['swing_x'] * math.sin(2 * math.pi * time / period + point['swing_x_phase'])
        x = center_x + point['x_offset'] + x_swing
        
        # Vertical movement
        y_swing = point['swing_y_amp'] * math.sin(2 * math.pi * time / period + point['swing_y_phase'])
        y = (center_y - body_vertical) + point['y_offset'] + y_swing
        
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
