
import pygame
import numpy as np
import math

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
WAVE_AMPLITUDE = 50  # Height of wave motion
WAVE_FREQUENCY = 0.05  # Speed of wave motion

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Animation')
clock = pygame.time.Clock()

# Define the positions of the point-lights
def create_light_positions():
    return [
        (WIDTH // 2 - 20, HEIGHT // 2 + i * 20) for i in range(-7, 8)  # Vertical positions
    ] + [
        (WIDTH // 2 + 20, HEIGHT // 2 + i * 20) for i in range(-7, 8)  # Additional positions for the waving hand
    ]

point_lights = create_light_positions()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Black background

        # Update point-light positions for waving motion
        for index, (x, y) in enumerate(point_lights):
            if index < 8:  # Main body
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 5)
            else:  # Waving hand
                wave_y = y - WAVE_AMPLITUDE * math.sin(pygame.time.get_ticks() * WAVE_FREQUENCY + index)
                pygame.draw.circle(screen, (255, 255, 255), (x, wave_y), 5)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
