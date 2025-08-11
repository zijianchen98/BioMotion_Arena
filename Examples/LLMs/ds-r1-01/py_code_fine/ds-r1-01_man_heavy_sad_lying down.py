
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Define initial points for a standing figure
initial_points = [
    (400, 100),  # Head
    (400, 130),  # Neck
    (380, 160),  # Left shoulder
    (420, 160),  # Right shoulder
    (360, 200),  # Left elbow
    (440, 200),  # Right elbow
    (340, 240),  # Left hand
    (460, 240),  # Right hand
    (400, 200),  # Torso (mid)
    (380, 300),  # Left hip
    (420, 300),  # Right hip
    (360, 340),  # Left knee
    (440, 340),  # Right knee
    (340, 380),  # Left ankle
    (460, 380)   # Right ankle
]

pivot_x, pivot_y = 400, 380  # Midpoint between ankles

start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    current_time = pygame.time.get_ticks() - start_time

    # Calculate rotation angle and breathing offset
    if current_time < 2000:  # 2000 ms = 2 seconds for lying down
        theta = (current_time / 2000) * (math.pi / 2)
        breath_offset = 0
    else:
        theta = math.pi / 2
        # Breathing motion after lying down
        breath_phase = (current_time - 2000) * 0.001  # Convert to seconds
        breath_offset = math.sin(breath_phase * 2 * math.pi * 0.5) * 3  # 0.5 Hz, 3px amplitude

    # Calculate and draw points
    for point in initial_points:
        x, y = point

        # Apply rotation around pivot
        x_rot = (x - pivot_x) * math.cos(theta) - (y - pivot_y) * math.sin(theta) + pivot_x
        y_rot = (x - pivot_x) * math.sin(theta) + (y - pivot_y) * math.cos(theta) + pivot_y

        # Apply breathing offset
        y_rot += breath_offset

        # Draw the point
        pygame.draw.circle(screen, (255, 255, 255), (int(x_rot), int(y_rot)), 5)

    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()
sys.exit()
