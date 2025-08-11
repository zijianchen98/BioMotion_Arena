
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define the point lights
lights = [pygame.Rect(0, HEIGHT/2, 10, 10) for _ in range(15)]

def draw_lights():
    for light in lights:
        pygame.draw.rect(screen, (255, 255, 255), light)

def move_lights():
    for light in lights:
        light.x += 1
        if light.x > WIDTH:
            light.x = 0

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        draw_lights()
        move_lights()
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
