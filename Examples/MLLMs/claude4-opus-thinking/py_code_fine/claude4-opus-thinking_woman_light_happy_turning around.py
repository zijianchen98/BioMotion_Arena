
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light positions (adjust these values for a realistic representation)
# Each tuple represents the (x, y) coordinates of a point-light
points = [
    (400, 150), (370, 130), (430, 130),  # Head (3 points)
    (360, 220), (440, 220), (380, 300), (420, 300),  # Shoulders (4 points)
    (350, 400), (450, 400), (380, 470), (420, 470),  # Hips and Knees (4 points)
    (362, 540), (438, 540),  # Feet (2 points)
]

# Animation parameters
clock = pygame.time.Clock()
running = True
angle = 0

def move_points(points, angle):
    """Rotate points around the center (400, 300) based on the angle."""
    center_x = 400
    center_y = 300
    rotated_points = []
    
    for (x, y) in points:
        # Translate point to origin
        translated_x = x - center_x
        translated_y = y - center_y
        
        # Rotate point
        new_x = (translated_x * np.cos(angle)) - (translated_y * np.sin(angle))
        new_y = (translated_x * np.sin(angle)) + (translated_y * np.cos(angle))
        
        # Translate point back
        final_x = new_x + center_x
        final_y = new_y + center_y
        
        rotated_points.append((final_x, final_y))
    
    return rotated_points

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update the angle for rotation
    angle += 0.01  # Adjust rotation speed here if needed

    # Get rotated points
    rotated_points = move_points(points, angle)

    # Draw points
    for (x, y) in rotated_points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)  # Draw each point-light

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
