
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_COLOR = (255, 255, 255)  # White
LIGHT_RADIUS = 5

# Sadman properties
SADMAN_HEIGHT = 200
SADMAN_WIDTH = 100

# Turning animation properties
TURN_DURATION = 2000  # milliseconds
TURN_START_ANGLE = 0
TURN_END_ANGLE = math.pi

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, angle):
        # Update point-light position based on sadman's movement
        self.x = WIDTH / 2 + math.cos(angle) * (SADMAN_WIDTH / 2)
        self.y = HEIGHT / 2 + math.sin(angle) * (SADMAN_HEIGHT / 2)

class Sadman:
    def __init__(self):
        self.lights = [
            PointLight(WIDTH / 2, HEIGHT / 2 - SADMAN_HEIGHT / 2),  # Head
            PointLight(WIDTH / 2 - SADMAN_WIDTH / 4, HEIGHT / 2 - SADMAN_HEIGHT / 4),  # Left shoulder
            PointLight(WIDTH / 2 + SADMAN_WIDTH / 4, HEIGHT / 2 - SADMAN_HEIGHT / 4),  # Right shoulder
            PointLight(WIDTH / 2 - SADMAN_WIDTH / 2, HEIGHT / 2),  # Left hip
            PointLight(WIDTH / 2 + SADMAN_WIDTH / 2, HEIGHT / 2),  # Right hip
            PointLight(WIDTH / 2 - SADMAN_WIDTH / 4, HEIGHT / 2 + SADMAN_HEIGHT / 4),  # Left knee
            PointLight(WIDTH / 2 + SADMAN_WIDTH / 4, HEIGHT / 2 + SADMAN_HEIGHT / 4),  # Right knee
            PointLight(WIDTH / 2 - SADMAN_WIDTH / 2, HEIGHT / 2 + SADMAN_HEIGHT / 2),  # Left ankle
            PointLight(WIDTH / 2 + SADMAN_WIDTH / 2, HEIGHT / 2 + SADMAN_HEIGHT / 2),  # Right ankle
            PointLight(WIDTH / 2, HEIGHT / 2 - SADMAN_HEIGHT / 2 + SADMAN_HEIGHT / 4),  # Chest
            PointLight(WIDTH / 2 - SADMAN_WIDTH / 4, HEIGHT / 2 - SADMAN_HEIGHT / 4 + SADMAN_HEIGHT / 4),  # Left upper arm
            PointLight(WIDTH / 2 + SADMAN_WIDTH / 4, HEIGHT / 2 - SADMAN_HEIGHT / 4 + SADMAN_HEIGHT / 4),  # Right upper arm
            PointLight(WIDTH / 2 - SADMAN_WIDTH / 4, HEIGHT / 2 + SADMAN_HEIGHT / 4 - SADMAN_HEIGHT / 4),  # Left lower arm
            PointLight(WIDTH / 2 + SADMAN_WIDTH / 4, HEIGHT / 2 + SADMAN_HEIGHT / 4 - SADMAN_HEIGHT / 4),  # Right lower arm
            PointLight(WIDTH / 2, HEIGHT / 2 + SADMAN_HEIGHT / 2 - SADMAN_HEIGHT / 4),  # Lower back
        ]

    def update(self, angle):
        for light in self.lights:
            light.update(angle)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    sadman = Sadman()
    start_time = pygame.time.get_ticks()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        if elapsed_time > TURN_DURATION:
            running = False

        angle = TURN_START_ANGLE + (TURN_END_ANGLE - TURN_START_ANGLE) * (elapsed_time / TURN_DURATION)
        sadman.update(angle)

        screen.fill((0, 0, 0))  # Black background
        for light in sadman.lights:
            pygame.draw.circle(screen, LIGHT_COLOR, (int(light.x), int(light.y)), LIGHT_RADIUS)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
