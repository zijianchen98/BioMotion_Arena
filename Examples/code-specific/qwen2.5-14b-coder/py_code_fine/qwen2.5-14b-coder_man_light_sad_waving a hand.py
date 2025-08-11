
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sad Man Waving Hand")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Number of point lights
NUM_LIGHTS = 15

# Sad man's hand parameters
hand_center_x = SCREEN_WIDTH // 2
hand_center_y = SCREEN_HEIGHT // 2
hand_radius = 50
wave_amplitude = 20
wave_frequency = 0.5

# Function to calculate point light positions
def calculate_light_positions(angle):
    positions = []
    for i in range(NUM_LIGHTS):
        angle_offset = (i / NUM_LIGHTS) * 2 * math.pi
        x = hand_center_x + hand_radius * math.cos(angle + angle_offset)
        y = hand_center_y + hand_radius * math.sin(angle + angle_offset)
        positions.append((x, y))
    return positions

# Main loop
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update angle for waving motion
    angle += wave_frequency
    if angle > 2 * math.pi:
        angle -= 2 * math.pi

    # Calculate light positions
    light_positions = calculate_light_positions(angle)

    # Draw background
    screen.fill(BLACK)

    # Draw point lights
    for pos in light_positions:
        pygame.draw.circle(screen, WHITE, pos, 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
