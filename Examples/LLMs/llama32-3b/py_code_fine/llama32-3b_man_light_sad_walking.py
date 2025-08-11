
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 5)

def draw_body(point_light):
    angle = math.atan2(point_light.y, point_light.x)
    x = WIDTH // 2 + math.cos(angle) * 200
    y = HEIGHT // 2 + math.sin(angle) * 200
    pygame.draw.line(screen, WHITE, (int(point_light.x), int(point_light.y)), (int(x), int(y)), 5)

def main():
    clock = pygame.time.Clock()
    point_lights = [PointLight(WIDTH // 2 + math.cos(i * math.pi * 2 / LIGHTS), HEIGHT // 2 + math.sin(i * math.pi * 2 / LIGHTS)) for i in range(LIGHTS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point_light in point_lights:
            point_light.move()
            point_light.draw()
            draw_body(point_light)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
