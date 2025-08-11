
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Parameters for the "happyman" jumping forward
frames = 120
for_frame = 60
mid_frame = (frames - for_frame) // 2

# Function to calculate the position of a light at a given frame
def position(frame):
    # Ensure the frame is within the valid range
    frame = max(0, min(frame, frames - 1))
    
    # Calculate the horizontal position (forward jump)
    horizontal_amplitude = WIDTH * 0.4
    horizontal_position = WIDTH // 2 + int(horizontal_amplitude * math.sin(2 * math.pi * frame / frames))
    
    # Calculate the vertical position (upward jump)
    vertical_amplitude = HEIGHT * 0.2
    vertical_position = HEIGHT // 2 - int(vertical_amplitude * math.sin(2 * math.pi * frame / frames))
    
    return horizontal_position, vertical_position

# Main animation loop
frame_counter = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the 15 point-lights
    for i in range(15):
        frame = frame_counter + i * (frames // 15)
        x, y = position(frame % frames)
        pygame.draw.circle(screen, WHITE, (x, y), 3)
    
    # Update the display
    pygame.display.flip()
    
    # Increment the frame counter
    frame_counter = (frame_counter + 1) % frames
    
    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
