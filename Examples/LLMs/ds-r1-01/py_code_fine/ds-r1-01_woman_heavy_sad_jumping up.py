
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the relative positions of the 15 points (dx, dy) from the center
points_relative = [
    (0, -50),    # Head
    (-20, -30),  # Left shoulder
    (20, -30),   # Right shoulder
    (-40, -20),  # Left elbow
    (40, -20),   # Right elbow
    (-50, -10),  # Left hand
    (50, -10),   # Right hand
    (0, 0),      # Torso (center)
    (-20, 20),   # Left hip
    (20, 20),    # Right hip
    (-30, 40),   # Left knee
    (30, 40),    # Right knee
    (-40, 60),   # Left ankle
    (40, 60),    # Right ankle
    (0, 30)      # Mid-spine
]

# Motion parameters
amplitude = 30        # Vertical jump height
frequency = 0.3       # Slower movement for heavy person
sway_amplitude = 5    # Horizontal body sway
hand_amplitude = 20   # Arm swing intensity
foot_amplitude = 30   # Foot lift intensity

# Main animation loop
running = True
time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate body center position with natural sway and jump
    center_x = width//2 + sway_amplitude * math.sin(2 * math.pi * frequency * time)
    center_y = height//2 + amplitude * math.sin(2 * math.pi * frequency * time)

    # Update point positions with secondary movements
    points = []
    for i, (dx, dy) in enumerate(points_relative):
        x = center_x + dx
        y = center_y + dy

        # Add arm swing with phase shift
        if i in [5, 6]:  # Hands
            y += hand_amplitude * math.sin(2 * math.pi * frequency * time + math.pi/2)
        
        # Add foot lift mechanics
        elif i in [12, 13]:  # Ankles
            y -= foot_amplitude * math.sin(2 * math.pi * frequency * time)

        points.append((int(x), int(y)))

    # Draw all points
    for (x, y) in points:
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    pygame.display.flip()
    time += 0.01
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
sys.exit()
