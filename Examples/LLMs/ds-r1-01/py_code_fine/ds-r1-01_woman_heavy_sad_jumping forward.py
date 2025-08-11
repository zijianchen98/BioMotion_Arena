
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
black = (0, 0, 0)
white = (255, 255, 255)

# Point-light settings
points_offsets = [
    (0, -40),    # Head
    (-10, -30), (10, -30),  # Shoulders
    (-20, -20), (20, -20),  # Elbows
    (-30, -10), (30, -10),  # Hands
    (-10, 0), (10, 0),      # Hips
    (-20, 10), (20, 10),    # Knees
    (-30, 20), (30, 20),    # Feet
    (0, -10), (0, 10)       # Chest and Pelvis
]

# Jump parameters
jump_duration = 2.0  # seconds
jump_height = 50
start_x = width // 2
start_y = height // 2

# Motion parameters
lean_amplitude = 20
swing_amplitude = 15
swing_frequency = 2  # cycles per jump

# Main animation loop
running = True
time_elapsed = 0.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    
    # Calculate normalized phase [0, 1]
    phase = (time_elapsed % jump_duration) / jump_duration
    
    # Vertical motion (parabolic trajectory)
    vertical_offset = -4 * jump_height * phase * (phase - 1)
    current_y = start_y + vertical_offset
    
    # Horizontal body lean
    body_lean = lean_amplitude * phase

    # Update point positions
    for i, (dx, dy) in enumerate(points_offsets):
        # Apply body lean
        if i < 7:  # Upper body points
            x_offset = dx + body_lean
        else:  # Lower body points
            x_offset = dx - body_lean
        
        # Add limb swing for hands and feet
        if i in [4, 5, 6, 11, 12]:
            swing = swing_amplitude * math.sin(swing_frequency * 2 * math.pi * phase)
            x_offset += swing
        
        x = start_x + x_offset
        y = current_y + dy
        
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    pygame.display.flip()
    time_elapsed += clock.tick(60) / 1000.0  # Maintain 60 FPS

pygame.quit()
sys.exit()
