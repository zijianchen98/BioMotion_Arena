
import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class PointLight:
    def __init__(self, x, y, angle, distance):
        self.x = x
        self.y = y
        self.angle = angle
        self.distance = distance
        self.speed = random.uniform(0.5, 2.0)

    def update(self):
        self.angle += self.speed

    def draw(self):
        light_x = self.x + self.distance * math.cos(self.angle)
        light_y = self.y + self.distance * math.sin(self.angle)
        pygame.draw.circle(screen, WHITE, (int(light_x), int(light_y)), 2)

def main():
    clock = pygame.time.Clock()
    lights = []
    for i in range(NUM_LIGHTS):
        angle = i * math.pi / NUM_LIGHTS * 2
        distance = 200 + 50 * math.sin(angle)
        lights.append(PointLight(400, 300, angle, distance))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for light in lights:
            light.update()
            light.draw()

        if random.random() < 0.05:
            lights.append(PointLight(400, 300, 0, 200))

        if random.random() < 0.05:
            lights.pop()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
