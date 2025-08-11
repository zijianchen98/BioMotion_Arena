
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling FPS
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x_amp, x_phase, y_amp, y_phase, y_offset):
        self.x_amp = x_amp
        self.x_phase = x_phase
        self.y_amp = y_amp
        self.y_phase = y_phase
        self.y_offset = y_offset

    def get_position(self, t):
        x = width // 2 + self.x_amp * math.sin(t + self.x_phase)
        y = height // 2 + self.y_amp * math.sin(t + self.y_phase) + self.y_offset
        return (int(x), int(y))

# Configure 15 point-lights with biomechanical parameters
points = [
    # Head (vertical movement)
    PointLight(0, 0, 8, 0, -120),
    # Shoulders
    PointLight(25, 0, 15, math.pi/2, -60),
    PointLight(25, math.pi, 15, math.pi/2, -60),
    # Elbows
    PointLight(40, math.pi, 25, math.pi*1.1, -30),
    PointLight(40, 0, 25, math.pi*0.9, -30),
    # Hands
    PointLight(55, math.pi, 35, math.pi*1.2, 0),
    PointLight(55, 0, 35, math.pi*0.8, 0),
    # Hips
    PointLight(30, 0, 20, math.pi/2, 40),
    PointLight(30, math.pi, 20, math.pi/2, 40),
    # Knees
    PointLight(50, math.pi, 40, math.pi*1.1, 80),
    PointLight(50, 0, 40, math.pi*0.9, 80),
    # Ankles
    PointLight(60, math.pi, 50, math.pi*1.2, 120),
    PointLight(60, 0, 50, math.pi*0.8, 120),
    # Feet
    PointLight(70, math.pi, 60, math.pi*1.3, 160),
    PointLight(70, 0, 60, math.pi*0.7, 160)
]

time = 0.0
speed = 0.07  # Animation speed modifier

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update and draw all points
    for point in points:
        x, y = point.get_position(time)
        pygame.draw.circle(screen, WHITE, (x, y), 6)

    pygame.display.flip()
    time += speed
    clock.tick(40)  # Smooth 40 FPS

pygame.quit()
sys.exit()
