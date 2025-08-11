
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Biological Motion")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Define the keypoints for the point-light representation of the human body (relative coordinates)
human_points = [
    (-10, -50),  # Head
    (-20, -40), (0, -40),  # Shoulders
    (-30, -20), (-10, -20),  # Left arm
    (0, -20), (20, -20),  # Right arm
    (-20, 0), (0, 0),  # Torso
    (-30, 30), (-10, 30),  # Left leg
    (10, 30), (30, 30),  # Right leg
    (-30, 50), (30, 50),  # Feet
]

# Scaling and positioning constants
scale = 5
center_x = screen_width // 2
center_y = screen_height // 2

def transform_points(points, angle):
    """Apply a rotation transformation to the points."""
    rotated_points = []
    rad_angle = math.radians(angle)  # Convert degrees to radians
    for x, y in points:
        rot_x = x * math.cos(rad_angle) - y * math.sin(rad_angle)
        rot_y = x * math.sin(rad_angle) + y * math.cos(rad_angle)
        rotated_points.append((center_x + rot_x * scale, center_y + rot_y * scale))
    return rotated_points

def draw_points(points):
    """Draw the points on the screen."""
    for x, y in points:
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

# Main loop
running = True
angle = 0  # Rotation angle to simulate turning around
while running:
    screen.fill(black)  # Fill the screen with black
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Transform and draw the points
    transformed_points = transform_points(human_points, angle)
    draw_points(transformed_points)
    
    # Update the angle to simulate rotation
    angle += 2
    if angle >= 360:  # Reset angle after a full rotation
        angle -= 360

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
