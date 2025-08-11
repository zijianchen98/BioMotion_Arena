
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Man Waving Hand")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Function to draw a point light
def draw_light(x, y):
    pygame.draw.circle(screen, LIGHT_COLOR, (int(x), int(y)), 5)

# Main loop
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BACKGROUND_COLOR)

    # Calculate positions for the point lights
    for i in range(NUM_LIGHTS):
        # Simple wave motion for demonstration
        x = WIDTH // 2 + (i - NUM_LIGHTS // 2) * 20
        y = HEIGHT // 2 + 50 * math.sin(angle + i * 0.5)
        draw_light(x, y)

    # Update display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

    # Increment angle for next frame
    angle += 0.1

# Quit Pygame
pygame.quit()
