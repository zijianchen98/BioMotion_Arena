
import pygame
import math
import sys

# Screen dimensions
WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Point light parameters
NUM_LIGHTS = 15
RADIUS = 100
SPEED = 0.02  # Adjust for speed of turning

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation")

def draw_point_lights(angle):
    screen.fill((0, 0, 0))  # Clear screen with black background
    for i in range(NUM_LIGHTS):
        # Calculate angle for each point light
        theta = angle + (i * (2 * math.pi / NUM_LIGHTS))  # Spread lights around circle
        x = CENTER_X + RADIUS * math.cos(theta)  # X position of point light
        y = CENTER_Y + RADIUS * math.sin(theta)  # Y position of point light
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)  # Draw points

def main():
    clock = pygame.time.Clock()
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_point_lights(angle)
        angle += SPEED  # Increment angle to simulate turning around

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Cap frame rate at 60 FPS

if __name__ == "__main__":
    main()
