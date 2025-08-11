
import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Constants for the screen size and frame rate
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
FPS = 30
CLOCK = pygame.time.Clock()

# Color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Coordinates for the points (each tuple represents a point)
points = [
    # This list will have exactly 15 white points to represent the body
    (110, 130), (140, 150), (140, 130), (140, 150), (110, 150), (80, 150), (80, 130),
    (80, 150), (110, 150), (140, 130), (140, 150), (110, 150), (110, 130), (140, 130), (110, 150)
]

# Function to draw the scene
def draw_scene(screen):
    screen.fill(BLACK)
    for point in points:
        pygame.draw.circle(screen, WHITE, point, 5)
    pygame.display.flip()

# Main function to handle the animation loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        draw_scene(screen)
        
        CLOCK.tick(FPS)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
