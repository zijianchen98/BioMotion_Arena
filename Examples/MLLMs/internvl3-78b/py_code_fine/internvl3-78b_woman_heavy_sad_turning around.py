
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sad Woman Turning Around Point-Light Animation")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Point positions for the sad woman turning around
points = [
    (225, 375), (450, 375), (675, 375),
    (225, 475), (450, 475), (675, 475),
    (300, 225), (580, 225),
    (225, 225), (450, 225), (675, 225),
    (300, 525), (580, 525),
    (450, 475), (450, 375), (450, 275)
]

# Number of points
num_points = len(points)

# Angles for rotations
angle = 0
rotation_speed = 0.02

# Radius for the arcs
radius = 200

# Main loop
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(black)
    
    # Calculate new points positions based on rotation angle
    rotated_points = []
    for point in points:
        # Translate point to origin
        x translated = point[0] - screen_width / 2
        y translated = point[1] - screen_height / 2
        # Rotate the point
        new x = x_translated * math.cos(angle) - y_translated * math.sin(angle)
        new_y = x_translated * math.sin(angle) + y_translated * math.cos(angle)
        # Translate back
        new_x += screen_width / 2 + radius * math.cos(angle)
        new_y += screen_height / 2 + radius * math.sin(angle)
        rotated_points.append((new_x, new_y))
    
    # Draw points
    for point in rotated_points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 5)
    
    pygame.display.flip()
    
    # Increment the rotation angle
    angle += rotation_speed
    
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
sys.exit()
