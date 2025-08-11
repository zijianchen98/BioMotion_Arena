
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
LIGHT_RADIUS = 2
JUMP_SPEED = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Light:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.uniform(-JUMP_SPEED, JUMP_SPEED)
        self.speed_y = random.uniform(-JUMP_SPEED, JUMP_SPEED)
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.angle += 0.01

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), LIGHT_RADIUS)

def main():
    clock = pygame.time.Clock()
    lights = [Light(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_LIGHTS)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        for light in lights:
            light.update()
            light.draw(screen)

            # Check if the light is off the screen and reset its position
            if light.x < 0 or light.x > WIDTH or light.y < 0 or light.y > HEIGHT:
                light.x = random.randint(0, WIDTH)
                light.y = random.randint(0, HEIGHT)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
