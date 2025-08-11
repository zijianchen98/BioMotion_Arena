
import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Set up display variables
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Point-Light Animation')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define point-light positions
def get_point_light_positions(theta):
    # Base positions of the point lights for the sad man waving
    head = (screen_width // 2, screen_height // 4)
    shoulder_left = (screen_width // 2 - 20, screen_height // 3)
    shoulder_right = (screen_width // 2 + 20, screen_height // 3)
    hand_left = (screen_width // 2 - 60 * np.cos(theta), screen_height // 3 + 60 * np.sin(theta))
    hand_right = (screen_width // 2 + 60 * np.cos(theta), screen_height // 3 + 60 * np.sin(theta))
    
    return [
        head, shoulder_left, shoulder_right,
        hand_left,
        (screen_width // 2 - 10, screen_height // 3 + 20),  # torso
        (screen_width // 2 + 10, screen_height // 3 + 20),  
    ]

# Main loop
clock = pygame.time.Clock()
angle = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BLACK)

    # Update angle for hand waving motion
    angle += 0.1
    if angle > 2 * np.pi:
        angle = 0

    # Get the current positions of the point lights
    positions = get_point_light_positions(angle)
    
    # Draw point lights
    for position in positions:
        pygame.draw.circle(screen, WHITE, (int(position[0]), int(position[1])), 5)
    
    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
