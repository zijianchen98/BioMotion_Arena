
import pygame
import sys
import math

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

# PointLight class to store each point's properties
class PointLight:
    def __init__(self, base_x, base_y, amplitude, phase):
        self.base_x = base_x
        self.base_y = base_y
        self.amplitude = amplitude
        self.phase = phase

# Create 15 point-lights representing body joints
points = [
    # Head
    PointLight(0, -50, 5, 0),
    # Shoulders
    PointLight(-15, -40, 10, 0.2), PointLight(15, -40, 10, 0.2),
    # Elbows
    PointLight(-30, -30, 15, 0.4), PointLight(30, -30, 15, 0.4),
    # Hands
    PointLight(-40, -20, 20, 0.6), PointLight(40, -20, 20, 0.6),
    # Hips
    PointLight(-10, 0, 10, 0.8), PointLight(10, 0, 10, 0.8),
    # Knees
    PointLight(-20, 20, 15, 1.0), PointLight(20, 20, 15, 1.0),
    # Ankles
    PointLight(-25, 40, 20, 1.2), PointLight(25, 40, 20, 1.2),
    # Feet
    PointLight(-30, 50, 25, 1.4), PointLight(30, 50, 25, 1.4)
]

# Initial position parameters
initial_x = width // 2
initial_y = height // 2
period = 1.2  # Jump cycle duration in seconds
jump_height = 60  # Maximum jump height
forward_speed = 120  # Horizontal speed (pixels per second)

# Main animation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    
    # Calculate normalized time
    current_time = pygame.time.get_ticks() / 1000  # Convert to seconds
    cycle_time = current_time % period
    
    # Calculate body center position
    x_center = initial_x + forward_speed * cycle_time
    vertical_progress = 4 * (cycle_time/period) * (1 - cycle_time/period)
    y_center = initial_y - jump_height * vertical_progress
    
    # Update and draw points
    for point in points:
        # Calculate dynamic vertical offset
        dynamic_y = point.amplitude * math.sin(2 * math.pi * (cycle_time/period) + point.phase)
        x = x_center + point.base_x
        y = y_center + point.base_y + dynamic_y
        
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)
