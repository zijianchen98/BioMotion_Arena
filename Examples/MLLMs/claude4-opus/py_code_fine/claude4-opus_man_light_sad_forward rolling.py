
import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)  # Black
LIGHT_COLOR = (255, 255, 255)  # White

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Stimulus Animation')
clock = pygame.time.Clock()

# Function to update positions of point-lights
def update_positions(t):
    positions = []
    angle = math.radians(360 / NUM_LIGHTS)
    
    # Define positions for point-lights based on human motion (forward roll)
    for i in range(NUM_LIGHTS):
        x = 400 + 50 * math.sin(t + i * angle)  # x-coordinate oscillates
        y = 300 + 70 * math.cos(t + i * angle)  # y-coordinate drops down
        positions.append((int(x), int(y)))
    
    return positions

# Main loop
running = True
t = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update positions
    positions = update_positions(t)

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the point-lights
    for pos in positions:
        pygame.draw.circle(screen, LIGHT_COLOR, pos, LIGHT_RADIUS)

    # Update the display
    pygame.display.flip()
    
    # Increment time
    t += math.pi / FPS
    clock.tick(FPS)

# Clean up
pygame.quit()
