
import pygame
import math

# Initialize Pygame
pygame.init()

# Colors and frame rate
black = (0, 0, 0)
white = (255, 255, 255)
fps = 60

# Screen resolution
width, height = 500, 400
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Happyman Bowing Animation")

# Clock to control frame rate
clock = pygame.time.Clock()

# Function to draw a dot
def draw_dot(x, y):
    pygame.draw.circle(screen, white, (x, y), 4)

# Calculate position for each dot based on the bowing action
def calculate_dot_positions(angle):
    positions = []
    # Define basic positions as offsets from a center
    base_positions = [
        (-50, -100), (-40, -40), (-30, 0), (-20, 30), (-10, 50),
        (0, 0), (10, 50), (20, 30), (30, 0), (40, -40), (50, -100),
        (-10, -200), (10, -200), (-5, -300), (5, -300)
    ]
    
    # Convert angle to radians for trigonometric calculations
    radian_angle = math.radians(angle)
    
    # Calculate final positions after bowing transformation
    sin_angle = math.sin(radian_angle)
    cos_angle = math.cos(radian_angle)
    
    for x, y in base_positions:
        # Apply rotation matrix transformation
        new_x = x * cos_angle - y * sin_angle
        new_y = x * sin_angle + y * cos_angle
        # Move to center position on the screen
        positions.append((int(new_x + width/2), int(new_y + height/2)))
    
    return positions

# Main loop
angle = 0
increasing = True

running = True
while running:
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update angle for the bowing motion
    if increasing:
        angle += 5
        if angle >= 20:
            increasing = False
    else:
        angle -= 5
        if angle <= -20:
            increasing = True
    
    # Get the positions for the dots
    dot_positions = calculate_dot_positions(angle)
    
    # Draw the dots
    for x, y in dot_positions:
        draw_dot(x, y)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
