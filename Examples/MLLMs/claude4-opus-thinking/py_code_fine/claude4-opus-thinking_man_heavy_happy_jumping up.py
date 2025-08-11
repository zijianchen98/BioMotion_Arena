
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation of Jumping Happyman")

# Point light positions (approximate relative positions)
body_positions = [
    (400, 300), # Main body
    (380, 250), (420, 250), # Shoulders
    (370, 210), (430, 210), # Hands
    (390, 180), (410, 180), # Head
    (390, 320), (410, 320), # Knees
    (380, 350), (420, 350), # Feet
    (390, 350), (410, 350), # Feet
    (380, 290), (420, 290), # Elbows
    (390, 330), (410, 330)  # Ankles
]

def calculate_jump(t):
    """ Calculate vertical position during jump using a sine wave for smooth motion. """
    height = 100 * np.sin(t * np.pi)  # Amplitude = 100
    return height

def main():
    clock = pygame.time.Clock()
    running = True
    t = 0.0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)  # Fill the screen with black

        # Update time for jump animation
        t += 0.05
        jump_height = calculate_jump(t)

        # Draw point lights based on calculated positions
        for pos in body_positions:
            x, y = pos
            pygame.draw.circle(screen, WHITE, (x, y - jump_height), 5)  # y is reduced by jump_height

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Control the frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
