
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Point-light Walker")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Center position
center_x, center_y = width // 2, height // 2

# Define 15 body points (relative positions)
points = [
    (0, -100),  # Head
    (-40, -80), (40, -80),  # Shoulders
    (-60, -60), (60, -60),  # Elbows
    (-70, -40), (70, -40),  # Hands
    (-20, -50), (20, -50),  # Waist
    (-20, 0), (20, 0),      # Hips
    (-20, 40), (20, 40),    # Knees
    (-20, 80), (20, 80)     # Feet
]

# Verify point count
assert len(points) == 15, "Exactly 15 points required"

# Animation control
angle = 0
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update and draw points
    for dx, dy in points:
        # Apply rotation
        rot_x = dx * math.cos(angle) - dy * math.sin(angle)
        rot_y = dx * math.sin(angle) + dy * math.cos(angle)
        
        # Calculate screen position
        x = int(rot_x) + center_x
        y = int(rot_y) + center_y
        
        # Draw point
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    # Update rotation angle
    angle += 0.03
    if angle >= 2 * math.pi:
        angle -= 2 * math.pi

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
