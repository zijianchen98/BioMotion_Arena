
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
LIGHT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Set display and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation")
clock = pygame.time.Clock()

# Define initial positions for point lights based on wave motion
def generate_light_positions(t):
    positions = []
    # Static base points
    base_y = HEIGHT // 2
    for i in range(NUM_LIGHTS):
        x_offset = (i % 5) * 50 - 100  # Adjusting x position
        y_offset = base_y + math.sin(t + (i * math.pi / 10)) * 30  # Sinusoidal motion for waving effect
        positions.append((WIDTH // 2 + x_offset, y_offset))
    return positions

# Main loop
running = True
t = 0  # Time variable for animation
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BACKGROUND_COLOR)

    # Update light positions
    light_positions = generate_light_positions(t)

    # Draw point lights
    for pos in light_positions:
        pygame.draw.circle(screen, LIGHT_COLOR, (int(pos[0]), int(pos[1])), 5)

    # Display the updated content
    pygame.display.flip()
    
    # Increment time
    t += 0.1
    
    # Limit frames per second
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
