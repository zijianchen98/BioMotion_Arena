
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
POINT_LIGHTS = 15
RADIUS = 5
RUNNING_ANIMATION_FRAMES = 18

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Representation of Running")

# Function to draw point lights
def draw_point_lights(positions):
    for pos in positions:
        pygame.draw.circle(screen, WHITE, pos, RADIUS)

# Function to create running animation sequence
def get_running_positions(frame):
    # Placeholder for real motion data; simulating a simple running cycle
    angle = math.pi * 2 * frame / RUNNING_ANIMATION_FRAMES
    step = 10
    positions = []
    
    # Generate point positions for each limb/joint
    for i in range(POINT_LIGHTS):
        x = int(WIDTH // 2 + step * math.sin(angle + i * math.pi / (POINT_LIGHTS // 2)))
        y = int(HEIGHT // 2 + (i - POINT_LIGHTS // 2) * step)
        positions.append((x, y))
    
    return positions

# Main loop
running = True
clock = pygame.time.Clock()
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Get positions based on the current frame
    point_light_positions = get_running_positions(frame)
    
    # Draw point lights
    draw_point_lights(point_light_positions)

    pygame.display.flip()
    frame = (frame + 1) % RUNNING_ANIMATION_FRAMES  # Loop frames
    clock.tick(FPS)

pygame.quit()
