
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_COLOR = (255, 255, 255)  # White
LIGHT_RADIUS = 5

# Jumping motion properties
JUMP_HEIGHT = 200
JUMP_DURATION = 2  # seconds

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, t):
        # Update position based on jumping motion
        self.x = self.x
        self.y = self.y - JUMP_HEIGHT * (1 - abs(t - 0.5) / 0.5)

    def draw(self, screen):
        pygame.draw.circle(screen, LIGHT_COLOR, (int(self.x), int(self.y)), LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Initialize point-lights
    lights = [
        PointLight(100, 500),  # Head
        PointLight(120, 520),  # Right shoulder
        PointLight(80, 520),   # Left shoulder
        PointLight(100, 550),  # Right elbow
        PointLight(100, 550),  # Left elbow
        PointLight(120, 580),  # Right hand
        PointLight(80, 580),   # Left hand
        PointLight(100, 600),  # Right hip
        PointLight(100, 600),  # Left hip
        PointLight(120, 620),  # Right knee
        PointLight(80, 620),   # Left knee
        PointLight(120, 640),  # Right ankle
        PointLight(80, 640),   # Left ankle
        PointLight(100, 660),  # Right foot
        PointLight(100, 660),  # Left foot
    ]

    running = True
    t = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update point-lights
        for light in lights:
            light.update(t)

        # Draw everything
        screen.fill((0, 0, 0))  # Black background
        for light in lights:
            light.draw(screen)

        # Update display
        pygame.display.flip()

        # Cap framerate
        clock.tick(60)

        # Update time
        t += 1 / 60
        if t > JUMP_DURATION:
            t = 0

    pygame.quit()

if __name__ == "__main__":
    main()
