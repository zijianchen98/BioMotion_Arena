
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)

# Animation properties
FPS = 60
DURATION = 10  # seconds

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, t):
        # Simulate rolling motion
        self.x = WIDTH / 2 + 100 * math.sin(t * 2 * math.pi * 2)
        self.y = HEIGHT / 2 + 100 * math.cos(t * 2 * math.pi * 2)

        # Add some randomness to simulate weight and sadness
        self.x += 20 * math.sin(t * 2 * math.pi * 5)
        self.y += 20 * math.cos(t * 2 * math.pi * 5)

class SadMan:
    def __init__(self):
        self.lights = [
            PointLight(WIDTH / 2, HEIGHT / 2),  # head
            PointLight(WIDTH / 2 - 50, HEIGHT / 2 - 50),  # left shoulder
            PointLight(WIDTH / 2 + 50, HEIGHT / 2 - 50),  # right shoulder
            PointLight(WIDTH / 2 - 50, HEIGHT / 2),  # left elbow
            PointLight(WIDTH / 2 + 50, HEIGHT / 2),  # right elbow
            PointLight(WIDTH / 2 - 50, HEIGHT / 2 + 50),  # left hand
            PointLight(WIDTH / 2 + 50, HEIGHT / 2 + 50),  # right hand
            PointLight(WIDTH / 2, HEIGHT / 2 + 100),  # torso
            PointLight(WIDTH / 2 - 50, HEIGHT / 2 + 150),  # left hip
            PointLight(WIDTH / 2 + 50, HEIGHT / 2 + 150),  # right hip
            PointLight(WIDTH / 2 - 50, HEIGHT / 2 + 200),  # left knee
            PointLight(WIDTH / 2 + 50, HEIGHT / 2 + 200),  # right knee
            PointLight(WIDTH / 2 - 50, HEIGHT / 2 + 250),  # left foot
            PointLight(WIDTH / 2 + 50, HEIGHT / 2 + 250),  # right foot
            PointLight(WIDTH / 2, HEIGHT / 2 + 300),  # weight
        ]

    def update(self, t):
        for light in self.lights:
            light.update(t)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for light in self.lights:
            pygame.draw.circle(screen, LIGHT_COLOR, (int(light.x), int(light.y)), LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    sad_man = SadMan()
    t = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        sad_man.update(t)
        sad_man.draw(screen)
        pygame.display.flip()
        t += 1 / FPS
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
