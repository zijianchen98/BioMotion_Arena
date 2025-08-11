
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Waving Hand")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point definitions
class Point:
    def __init__(self, x, y, fixed=False):
        self.x = x
        self.y = y
        self.fixed = fixed
        self.ox = x
        self.oy = y
        
    def update(self, wave_offset):
        if not self.fixed:
            self.x = self.ox + wave_offset

# Body points
points = [
    # Head (1)
    Point(0, -100, fixed=True),
    
    # Neck/Upper spine (1)
    Point(0, -70, fixed=True),
    
    # Shoulders (2)
    Point(-40, -70), Point(40, -70),
    
    # Elbows (2)
    Point(-60, -20), Point(60, -20),
    
    # Hands (2)
    Point(-70, 30), Point(70, 30),
    
    # Hips (2)
    Point(-20, 0, fixed=True), Point(20, 0, fixed=True),
    
    # Knees (2)
    Point(-30, 70), Point(30, 70),
    
    # Feet (2)
    Point(-40, 120), Point(40, 120),
    
    # Torso (1)
    Point(0, -30, fixed=True)
]

# Animation parameters
clock = pygame.time.Clock()
amplitude = 20
wave_period = 2.0  # seconds per full wave cycle
running = True

# Main animation loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Calculate wave offset
    time_ms = pygame.time.get_ticks()
    phase = (time_ms / 1000) * (2 * math.pi) / wave_period
    wave_offset = math.sin(phase) * amplitude
    
    # Update right arm points (shoulder, elbow, hand)
    points[2].update(-wave_offset/2)  # Right shoulder
    points[4].update(wave_offset)     # Right elbow
    points[6].update(wave_offset*2)  # Right hand
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw all points
    for point in points:
        pygame.draw.circle(screen, WHITE, 
                          (int(WIDTH/2 + point.x), 
                           int(HEIGHT/2 + point.y)), 5)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
