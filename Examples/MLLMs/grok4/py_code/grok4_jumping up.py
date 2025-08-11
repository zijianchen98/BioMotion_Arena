
import pygame
import math
import time

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black
POINT_COLOR = (255, 255, 255)  # White
POINT_COUNT = 15
FPS = 30

# Define the main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Stimulus Animation")

    # Define initial positions for 15 point-lights
    points = []
    for i in range(POINT_COUNT):
        # Randomly distribute lights at the start in a vertical line
        points.append((WIDTH // 2, HEIGHT // 2 + i * 15))

    clock = pygame.time.Clock()
    jumping = True
    start_time = time.time()
    
    while jumping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jumping = False
        
        # Fill the background
        screen.fill(BACKGROUND_COLOR)

        # Calculate the jump motion (simple sine wave)
        elapsed_time = time.time() - start_time
        jump_height = 200 * abs(math.sin(elapsed_time * 3))  # Adjustable speed
        for i, (x, y) in enumerate(points):
            # Move points upwards and downwards in a jumping fashion
            screen_y = HEIGHT // 2 + (i - 7) * 15 - jump_height if i > 0 else HEIGHT // 2 - jump_height
            pygame.draw.circle(screen, POINT_COLOR, (x, screen_y), 5)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
