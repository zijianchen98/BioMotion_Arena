
import pygame
import math
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
POINTS = 15
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
FPS = 60

# Function to initialize Pygame and create a window
def init_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Stimulus Animation")
    return screen

# Function to calculate the position of the points in a jumping motion
def get_point_positions(time):
    # Base coordinates for the points (representing a sad man)
    base_y = HEIGHT * 0.7
    start_x = WIDTH * 0.5

    # Calculate y positions with a simple jumping motion
    jump_height = 150 * math.sin(time * 2)  # Smooth up and down motion
    positions = []

    for i in range(POINTS):
        x = start_x + (i % 3) * 20 - 20  # Spread points horizontally
        y = base_y - jump_height + (i // 3) * 10  # Spread points vertically
        positions.append((x, y))

    return positions

# Main loop to run the animation
def main():
    screen = init_game()
    clock = pygame.time.Clock()
    time = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update the time for the animation
        time += 1 / FPS

        # Get the current positions of the points
        points = get_point_positions(time)

        # Fill the background
        screen.fill(BACKGROUND_COLOR)

        # Draw each point
        for point in points:
            pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), 5)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Entry point of the program
if __name__ == "__main__":
    main()
