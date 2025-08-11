
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PointLight:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Stimulus Animation")
    clock = pygame.time.Clock()

    # Define the points of the bowing action
    points = [
        PointLight(100, 100, 10),
        PointLight(150, 150, 10),
        PointLight(200, 100, 10),
        PointLight(150, 50, 10),
        PointLight(100, 0, 10),
        PointLight(50, 0, 10),
        PointLight(0, 0, 10),
        PointLight(-50, 0, 10),
        PointLight(-100, 0, 10),
        PointLight(-150, 0, 10),
        PointLight(-200, 0, 10),
        PointLight(-150, 50, 10),
        PointLight(-100, 100, 10),
        PointLight(-50, 150, 10),
        PointLight(0, 200, 10),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Draw the point lights
        for point in points:
            point.draw(screen)

        # Update the point lights' positions
        for i, point in enumerate(points):
            # Calculate the angle of the point light
            angle = i * math.pi / 14

            # Calculate the x and y coordinates of the point light
            x = WIDTH / 2 + 200 * math.cos(angle)
            y = HEIGHT / 2 + 200 * math.sin(angle)

            # Update the point light's position
            point.x = x
            point.y = y

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
