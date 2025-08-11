
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Point light positions
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_SPEED = 2

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def update(self):
        self.angle += LIGHT_SPEED / 100
        self.x = WIDTH / 2 + math.cos(self.angle) * 100
        self.y = HEIGHT / 2 + math.sin(self.angle) * 100

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    lights = []
    for i in range(NUM_LIGHTS):
        angle = i * 2 * math.pi / NUM_LIGHTS
        x = WIDTH / 2 + math.cos(angle) * 100
        y = HEIGHT / 2 + math.sin(angle) * 100
        lights.append(PointLight(x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for light in lights:
            light.update()
            pygame.draw.circle(screen, (255, 255, 255), (int(light.x), int(light.y)), LIGHT_RADIUS)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
