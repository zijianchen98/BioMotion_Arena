
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Define the class for point light
class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def move(self):
        self.angle += 0.01
        self.x = WIDTH / 2 + math.sin(self.angle) * 100
        self.y = HEIGHT / 2 + math.cos(self.angle) * 100

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 5)

# Create a list of point lights
point_lights = [PointLight(WIDTH / 2 + math.sin(i / 15) * 150, HEIGHT / 2 + math.cos(i / 15) * 150) for i in range(POINT_LIGHTS)]

# Set up the action
action = 'running'

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw each point light
    for light in point_lights:
        light.move()
        light.draw()

    # Draw the sadman
    if action == 'running':
        # Draw the sadman's body
        pygame.draw.ellipse(screen, WHITE, (WIDTH / 2 - 50, HEIGHT / 2 - 50, 100, 100))

        # Draw the sadman's head
        pygame.draw.circle(screen, WHITE, (WIDTH / 2, HEIGHT / 2 - 25), 25)

        # Draw the sadman's arms
        pygame.draw.line(screen, WHITE, (WIDTH / 2 - 25, HEIGHT / 2 + 25), (WIDTH / 2 + 25, HEIGHT / 2 + 25), 5)
        pygame.draw.line(screen, WHITE, (WIDTH / 2 - 25, HEIGHT / 2 - 25), (WIDTH / 2 + 25, HEIGHT / 2 - 25), 5)

        # Draw the sadman's legs
        pygame.draw.line(screen, WHITE, (WIDTH / 2 - 25, HEIGHT / 2 - 75), (WIDTH / 2 + 25, HEIGHT / 2 - 75), 5)
        pygame.draw.line(screen, WHITE, (WIDTH / 2 - 25, HEIGHT / 2 + 25), (WIDTH / 2 + 25, HEIGHT / 2 + 25), 5)

        # Draw the sadman's weight
        pygame.draw.circle(screen, WHITE, (WIDTH / 2, HEIGHT / 2 - 50), 10)
    else:
        # Draw the sadman's body
        pygame.draw.ellipse(screen, WHITE, (WIDTH / 2 - 50, HEIGHT / 2 - 50, 100, 100))

        # Draw the sadman's head
        pygame.draw.circle(screen, WHITE, (WIDTH / 2, HEIGHT / 2 - 25), 25)

        # Draw the sadman's arms
        pygame.draw.line(screen, WHITE, (WIDTH / 2 - 25, HEIGHT / 2 + 25), (WIDTH / 2 + 25, HEIGHT / 2 + 25), 5)
        pygame.draw.line(screen, WHITE, (WIDTH / 2 - 25, HEIGHT / 2 - 25), (WIDTH / 2 + 25, HEIGHT / 2 - 25), 5)

        # Draw the sadman's legs
        pygame.draw.line(screen, WHITE, (WIDTH / 2 - 25, HEIGHT / 2 - 75), (WIDTH / 2 + 25, HEIGHT / 2 - 75), 5)
        pygame.draw.line(screen, WHITE, (WIDTH / 2 - 25, HEIGHT / 2 + 25), (WIDTH / 2 + 25, HEIGHT / 2 + 25), 5)

        # Draw the sadman's weight
        pygame.draw.circle(screen, WHITE, (WIDTH / 2, HEIGHT / 2 - 50), 10)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
