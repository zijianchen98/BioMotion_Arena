
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)  # White

# Background properties
BACKGROUND_COLOR = (0, 0, 0)  # Black

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, angle, radius):
        self.x = WIDTH / 2 + radius * math.cos(angle)
        self.y = HEIGHT / 2 + radius * math.sin(angle)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Initialize point-lights
    lights = []
    for i in range(NUM_LIGHTS):
        light = PointLight(WIDTH / 2, HEIGHT / 2)
        lights.append(light)

    # Define movement parameters
    angle = 0
    radius = 100
    speed = 0.05

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update point-lights
        for i, light in enumerate(lights):
            light.update(angle + i * math.pi / 8, radius)

        # Draw background and point-lights
        screen.fill(BACKGROUND_COLOR)
        for light in lights:
            pygame.draw.circle(screen, LIGHT_COLOR, (int(light.x), int(light.y)), LIGHT_RADIUS)

        # Update angle and radius to simulate rolling motion
        angle += speed
        radius = 100 + 50 * math.sin(angle)

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
