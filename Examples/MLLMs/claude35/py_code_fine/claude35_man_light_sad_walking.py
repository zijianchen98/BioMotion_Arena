
import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
POINT_LIGHTS = 15
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Walking Animation")
clock = pygame.time.Clock()

# Function to draw the point-lights
def draw_point_lights(positions):
    for pos in positions:
        pygame.draw.circle(screen, WHITE, pos, 5)  # Draw each light as a small circle

# Function to update positions for a walking motion
def update_positions(frame):
    positions = []
    # Create a basic walking cycle
    for i in range(POINT_LIGHTS):
        x = WIDTH // 2 + int(50 * math.sin(2 * math.pi * (frame / 30.0) + (i * math.pi / 15)))
        y = HEIGHT // 2 + (i * 10)  # Simple vertical alignment
        positions.append((x, y))
    return positions

# Main loop
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # Clear the screen with black
    point_light_positions = update_positions(frame)  # Update positions
    draw_point_lights(point_light_positions)  # Draw points
    pygame.display.flip()  # Update the display

    frame += 1  # Increment frame count
    clock.tick(FPS)  # Maintain FPS

# Quit Pygame
pygame.quit()
