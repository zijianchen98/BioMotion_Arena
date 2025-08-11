
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Biological Motion - Forward Roll")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Animation parameters
radius = 40  # Body tucked radius
speed = 2    # Pixels per frame
cx = 0       # Initial horizontal center
cy = screen_height - 50  # Vertical center position

# Define 15 points with varying angular offsets and radii to simulate body parts
points = [
    {'theta0': -math.pi/2, 'r': radius},      # Head
    {'theta0': -math.pi/2.2, 'r': radius*0.9},# Upper back
    {'theta0': -math.pi/2.4, 'r': radius*0.8},# Mid back
    {'theta0': -math.pi/1.8, 'r': radius*0.9},# Shoulder left
    {'theta0': -math.pi/1.6, 'r': radius*0.7},# Elbow left
    {'theta0': -math.pi/1.4, 'r': radius*0.5},# Hand left
    {'theta0': -math.pi/2.8, 'r': radius*0.9},# Shoulder right
    {'theta0': -math.pi/3.0, 'r': radius*0.7},# Elbow right
    {'theta0': -math.pi/3.2, 'r': radius*0.5},# Hand right
    {'theta0': math.pi/2, 'r': radius},       # Hips
    {'theta0': math.pi/1.8, 'r': radius*0.9}, # Thigh left
    {'theta0': math.pi/1.6, 'r': radius*0.7}, # Knee left
    {'theta0': math.pi/1.4, 'r': radius*0.5}, # Ankle left
    {'theta0': math.pi/2.2, 'r': radius*0.9}, # Thigh right
    {'theta0': math.pi/2.4, 'r': radius*0.7}, # Knee right
]

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    
    # Update center position and rotation angle
    cx += speed
    theta = cx / radius
    
    # Reset position for continuous animation
    if cx > screen_width + radius*2:
        cx = -radius*2

    for point in points:
        # Calculate positions with vertical offset for ground contact
        x = cx + point['r'] * math.cos(point['theta0'] + theta)
        y = cy - point['r'] * math.sin(point['theta0'] + theta)  # Inverted Y-axis
        
        # Draw point-light
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
