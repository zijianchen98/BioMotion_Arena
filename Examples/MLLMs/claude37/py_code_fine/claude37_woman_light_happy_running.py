
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up parameters
WIDTH, HEIGHT = 800, 600
FPS = 30
POINT_LIGHTS = 15
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
ANIMATION_DURATION = 3  # seconds

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Animation')
clock = pygame.time.Clock()

# Generate initial positions of point-lights
def create_point_lights():
    return [(WIDTH // 2 + np.random.uniform(-50, 50), HEIGHT // 2 + np.random.uniform(-50, 50)) for _ in range(POINT_LIGHTS)]

def update_positions(positions, frame):
    # Simple running pattern (oscillating motion)
    for i in range(POINT_LIGHTS):
        x, y = positions[i]
        y = y + np.sin((frame + i) * 0.2) * 2  # Vertical oscillation
        positions[i] = (x, y)
    return positions

# Main loop
running = True
frames = 0
point_lights = create_point_lights()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    # Update positions for animation
    point_lights = update_positions(point_lights, frames)

    # Draw point-lights
    for pos in point_lights:
        pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), 5)

    pygame.display.flip()
    frames += 1
    clock.tick(FPS)

    # Stop after certain duration
    if frames >= FPS * ANIMATION_DURATION:
        running = False

pygame.quit()
