
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Number of point lights
NUM_LIGHTS = 15

# Point light properties
LIGHT_RADIUS = 2
LIGHT_COLOR = WHITE
LIGHT_SPEED = 2

class PointLight:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def update(self):
        self.angle += LIGHT_SPEED

    def draw(self, screen):
        # Calculate the position of the point light
        light_x = self.x + math.cos(self.angle) * LIGHT_RADIUS
        light_y = self.y + math.sin(self.angle) * LIGHT_RADIUS

        # Draw the point light
        pygame.draw.circle(screen, LIGHT_COLOR, (int(light_x), int(light_y)), LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Create point lights
    lights = []
    for i in range(NUM_LIGHTS):
        angle = i * math.pi / 10
        lights.append(PointLight(random.randint(0, WIDTH), random.randint(0, HEIGHT), angle))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Update and draw point lights
        for light in lights:
            light.update()
            light.draw(screen)

        # Ensure point lights are within the screen boundaries
        for light in lights:
            if light.x - LIGHT_RADIUS < 0:
                light.x = LIGHT_RADIUS
            elif light.x + LIGHT_RADIUS > WIDTH:
                light.x = WIDTH - LIGHT_RADIUS
            if light.y - LIGHT_RADIUS < 0:
                light.y = LIGHT_RADIUS
            elif light.y + LIGHT_RADIUS > HEIGHT:
                light.y = HEIGHT - LIGHT_RADIUS

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
