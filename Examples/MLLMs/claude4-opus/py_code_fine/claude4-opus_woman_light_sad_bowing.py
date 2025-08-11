
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)
POINT_LIGHTS = 15
FPS = 30

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Function to initialize point positions for a bowing motion
def create_point_lights():
    points = []
    # Define the initial positions of 15 point-lights
    for i in range(POINT_LIGHTS):
        x = WIDTH // 2 + (i % 5 - 2) * 10      # Horizontal spreading
        y = HEIGHT // 2 + (i // 5 - 1) * 10     # Vertical arrangement
        points.append((x, y))
    return points

# Function to update positions for a bowing action
def update_bowing(points, frame):
    # Simulate a bowing motion by altering y values based on the frame number
    for i in range(POINT_LIGHTS):
        # Bowing down motion
        points[i] = (points[i][0], points[i][1] + np.sin(frame / 10 + i) * 2)

# Main animation loop
def main():
    clock = pygame.time.Clock()
    running = True
    points = create_point_lights()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        frame = pygame.time.get_ticks() // 100
        update_bowing(points, frame)

        # Draw everything
        screen.fill(BACKGROUND_COLOR)
        for point in points:
            pygame.draw.circle(screen, LIGHT_COLOR, (int(point[0]), int(point[1])), 5)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Run the animation
if __name__ == "__main__":
    main()
