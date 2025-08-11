
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Biological Motion Animation')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the happy woman's point-lights
point_lights = [
    {'pos': (width // 2, height), 'vel': (0, -5)},  # Head
    {'pos': (width // 2 - 30, height - 50), 'vel': (0, -3)},  # Left shoulder
    {'pos': (width // 2 + 30, height - 50), 'vel': (0, -3)},  # Right shoulder
    {'pos': (width // 2 - 40, height - 100), 'vel': (0, -5)},  # Left elbow
    {'pos': (width // 2 + 40, height - 100), 'vel': (0, -5)},  # Right elbow
    {'pos': (width // 2 - 50, height - 150), 'vel': (0, -7)},  # Left wrist
    {'pos': (width // 2 + 50, height - 150), 'vel': (0, -7)},  # Right wrist
    {'pos': (width // 2 - 15, height - 200), 'vel': (0, -4)},  # Left hip
    {'pos': (width // 2 + 15, height - 200), 'vel': (0, -4)},  # Right hip
    {'pos': (width // 2 - 25, height - 250), 'vel': (0, -6)},  # Left knee
    {'pos': (width // 2 + 25, height - 250), 'vel': (0, -6)},  # Right knee
    {'pos': (width // 2 - 25, height - 300), 'vel': (0, -5)},  # Left ankle
    {'pos': (width // 2 + 25, height - 300), 'vel': (0, -5)},  # Right ankle
]

# Clock to control the speed of the animation
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Update the position of each point-light and draw it
    for light in point_lights:
        light['pos'] = (light['pos'][0], light['pos'][1] + light['vel'][1])

        # If point-light goes off screen, reset its position
        if light['pos'][1] < 0:
            light['pos'] = (light['pos'][0], height)

        # Draw the point-light
        pygame.draw.circle(screen, WHITE, light['pos'], 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
