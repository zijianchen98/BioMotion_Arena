
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Forward Roll")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
num_points = 15
ellipse_rx = 60    # Horizontal radius of body ellipse
ellipse_ry = 40    # Vertical radius of body ellipse
angular_vel = 0.04  # Angular velocity (radians/frame)
linear_vel = ellipse_rx * angular_vel  # Linear velocity (pixels/frame)

# Phase offsets for points around the ellipse
phases = [(2 * math.pi * i) / num_points for i in range(num_points)]

# Initial position
center_x = -ellipse_rx  # Start off-screen left
center_y = height * 0.6  # Vertical position

clock = pygame.time.Clock()
angle = 0  # Rotation angle

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update position and angle
    center_x += linear_vel
    angle += angular_vel

    # Reset position when off-screen right
    if center_x - ellipse_rx > width:
        center_x = -ellipse_rx
        angle = 0

    # Draw each point-light
    for phase in phases:
        x = center_x + ellipse_rx * math.cos(angle + phase)
        y = center_y + ellipse_ry * math.sin(angle + phase)
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
