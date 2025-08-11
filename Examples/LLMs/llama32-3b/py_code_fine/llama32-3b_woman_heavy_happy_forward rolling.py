
import pygame
import math
import random

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PointLight:
    def __init__(self, x, y, radius, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if self.x < 0 or self.x > WIDTH:
            self.velocity[0] *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.velocity[1] *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

def draw_happy_woman(screen):
    # Draw the happy woman's body
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 50, 2)

    # Draw the woman's head
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2 - 100), 30, 2)

    # Draw the woman's arms
    pygame.draw.line(screen, WHITE, (WIDTH // 2, HEIGHT // 2 - 50), (WIDTH // 2 - 50, HEIGHT // 2 + 50), 2)
    pygame.draw.line(screen, WHITE, (WIDTH // 2, HEIGHT // 2 - 50), (WIDTH // 2 + 50, HEIGHT // 2 + 50), 2)

    # Draw the woman's legs
    pygame.draw.line(screen, WHITE, (WIDTH // 2 - 50, HEIGHT // 2 + 50), (WIDTH // 2 - 150, HEIGHT // 2 + 150), 2)
    pygame.draw.line(screen, WHITE, (WIDTH // 2 + 50, HEIGHT // 2 + 50), (WIDTH // 2 + 150, HEIGHT // 2 + 150), 2)

def draw_point_lights(screen, lights):
    for light in lights:
        light.update()
        light.draw(screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Stimulus Animation")
    clock = pygame.time.Clock()

    # Define the point lights
    lights = []
    for i in range(15):
        angle = 2 * math.pi * i / 15
        radius = 50 + 10 * math.sin(angle)
        velocity = (random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
        lights.append(PointLight(WIDTH // 2 + radius * math.cos(angle), HEIGHT // 2 + radius * math.sin(angle), 2, velocity))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_happy_woman(screen)
        draw_point_lights(screen, lights)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
