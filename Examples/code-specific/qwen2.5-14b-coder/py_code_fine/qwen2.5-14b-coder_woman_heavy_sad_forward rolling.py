
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Forward Rolling")

# Define the initial positions of the lights
lights = []
radius = 50
center_x, center_y = WIDTH // 2, HEIGHT // 2

for i in range(NUM_LIGHTS):
    angle = (2 * math.pi / NUM_LIGHTS) * i
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    lights.append([x, y])

# Function to update light positions
def update_lights(dt):
    global lights
    speed = 100  # Adjust this value to change the speed of the rolling motion
    for i in range(NUM_LIGHTS):
        angle = (2 * math.pi / NUM_LIGHTS) * i
        x = center_x + radius * math.cos(angle) - speed * dt * math.sin(angle)
        y = center_y + radius * math.sin(angle) + speed * dt * math.cos(angle)
        lights[i] = [x, y]

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get time since last frame
    dt = clock.get_time() / 1000.0

    # Update light positions
    update_lights(dt)

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the lights
    for light in lights:
        pygame.draw.circle(screen, LIGHT_COLOR, (int(light[0]), int(light[1])), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
