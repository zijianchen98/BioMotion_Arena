
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_SPEED = 5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sadman Forward Rolling")

# Function to calculate point positions for forward rolling
def calculate_point_positions(frame):
    points = []
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2
    radius = 100
    angle_increment = 2 * math.pi / NUM_LIGHTS
    
    for i in range(NUM_LIGHTS):
        angle = i * angle_increment + (frame / 10) % (2 * math.pi)
        x = center_x + radius * math.cos(angle) + (frame / 10) * LIGHT_SPEED
        y = center_y + radius * math.sin(angle)
        points.append((x, y))
    
    return points

# Main loop
running = True
clock = pygame.time.Clock()
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Calculate point positions
    points = calculate_point_positions(frame_count)
    
    # Draw the point-lights
    for point in points:
        pygame.draw.circle(screen, WHITE, point, LIGHT_RADIUS)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)
    
    # Increment frame count
    frame_count += 1

# Quit Pygame
pygame.quit()
