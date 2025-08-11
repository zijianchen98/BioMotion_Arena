
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Man Bowing Animation")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to draw a point light
def draw_point_light(x, y):
    pygame.draw.circle(screen, LIGHT_COLOR, (int(x), int(y)), LIGHT_RADIUS)

# Function to calculate the position of each point light
def calculate_light_positions(frame, num_lights):
    positions = []
    angle_step = 2 * math.pi / num_lights
    radius = 150 + 20 * math.sin(frame / 10.0)  # Slight oscillation for bowing effect
    center_x = WIDTH // 2
    center_y = HEIGHT // 2 + 50  # Adjusted for bowing down
    for i in range(num_lights):
        angle = i * angle_step
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        positions.append((x, y))
    return positions

# Main loop
frame = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BACKGROUND_COLOR)

    # Calculate and draw point lights
    light_positions = calculate_light_positions(frame, NUM_LIGHTS)
    for pos in light_positions:
        draw_point_light(*pos)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    # Increment frame counter
    frame += 1

# Quit Pygame
pygame.quit()
sys.exit()
