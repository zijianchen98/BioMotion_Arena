
import pygame
import math

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define base positions for 15 points (relative to center)
points_base = [
    (0, -50),    # Head
    (-20, -40),  # Left shoulder
    (20, -40),   # Right shoulder
    (-30, -30),  # Left elbow
    (30, -30),   # Right elbow
    (-40, -20),  # Left hand
    (40, -20),   # Right hand
    (0, -20),    # Upper torso
    (-15, 0),    # Left hip
    (15, 0),     # Right hip
    (-20, 20),   # Left knee
    (20, 20),    # Right knee
    (-25, 40),   # Left ankle
    (25, 40),    # Right ankle
    (0, 10)      # Lower torso
]

# Main loop
running = True
t = 0
center_x, center_y = width//2, height//2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    
    # Calculate rotation angle with continuous rotation
    theta = t * 0.02 % (2 * math.pi)
    
    for i, (x_base, y_base) in enumerate(points_base):
        # Apply rotation
        x_rot = x_base * math.cos(theta) - y_base * math.sin(theta)
        y_rot = x_base * math.sin(theta) + y_base * math.cos(theta)
        
        # Add limb movements
        if i in [5, 6]:  # Hands
            swing = math.sin(t * 0.1) * 12
            x_rot += swing * (-1 if i == 5 else 1)
        elif i in [12, 13]:  # Ankles
            swing = math.sin(t * 0.1 + math.pi) * 8
            y_rot += swing
        
        # Calculate screen position
        x = x_rot + center_x
        y = y_rot + center_y
        
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    pygame.display.flip()
    t += 1
    clock.tick(30)

pygame.quit()
