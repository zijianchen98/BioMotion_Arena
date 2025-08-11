
import pygame
import numpy as np
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
POINT_LIGHT_COLOR = (255, 255, 255)
POINT_LIGHT_COUNT = 15

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Jumping Forward")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5

    def update(self, t):
        # Define the motion of the point light
        # This is a simple harmonic motion for the jumping action
        period = 2 * np.pi
        amplitude = 50
        omega = 2 * np.pi / period
        self.y = HEIGHT // 2 + amplitude * np.sin(omega * t)

def main():
    # Initialize point lights
    point_lights = []
    for _ in range(POINT_LIGHT_COUNT):
        x = np.random.randint(0, WIDTH)
        y = np.random.randint(0, HEIGHT)
        point_lights.append(PointLight(x, y))

    t = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update point lights
        for point_light in point_lights:
            point_light.update(t)

        # Draw everything
        screen.fill(BACKGROUND_COLOR)
        for point_light in point_lights:
            pygame.draw.circle(screen, POINT_LIGHT_COLOR, (int(point_light.x), int(point_light.y)), point_light.radius)

        pygame.display.flip()
        clock.tick(FPS)
        t += 0.1

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
