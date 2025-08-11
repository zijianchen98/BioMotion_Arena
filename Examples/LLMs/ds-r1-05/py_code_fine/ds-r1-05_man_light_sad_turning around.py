
import pygame
import math
import sys

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Biological Motion - Turning Figure")

center_x, center_y = screen_width // 2, screen_height // 2

# Define the 3D points for a human figure (15 points)
points = [
    # Head (0)
    (0, -200, 0),
    # Neck (1)
    (0, -170, 0),
    # Left shoulder (2)
    (-50, -170, -20),
    # Right shoulder (3)
    (50, -170, 20),
    # Left elbow (4)
    (-90, -90, -30),
    # Right elbow (5)
    (90, -90, 30),
    # Left hand (6)
    (-120, -10, -50),
    # Right hand (7)
    (120, -10, 50),
    # Hip center (8)
    (0, 0, 0),
    # Left hip (9)
    (-25, 0, -20),
    # Right hip (10)
    (25, 0, 20),
    # Left knee (11)
    (-30, 100, -25),
    # Right knee (12)
    (30, 100, 25),
    # Left foot (13)
    (-40, 200, -30),
    # Right foot (14)
    (40, 200, 30)
]

angle = 0.0
clock = pygame.time.Clock()
fps = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    
    radians = math.radians(angle)
    cos_angle = math.cos(radians)
    sin_angle = math.sin(radians)
    
    for point in points:
        x0, y0, z0 = point
        x_new = x0 * cos_angle - z0 * sin_angle
        y_new = y0
        x_screen = center_x + x_new
        y_screen = center_y + y_new
        pygame.draw.circle(screen, (255, 255, 255), (int(x_screen), int(y_screen)), 6)
    
    angle = (angle + 1.5) % 360
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
