
import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
FPS = 30
POINT_COUNT = 15

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Stimulus Animation')

# Function to calculate points positions for "running" motion
def update_positions(frame):
    positions = []
    for i in range(POINT_COUNT):
        angle = 2 * np.pi * i / POINT_COUNT
        x = WIDTH // 2 + (20 * np.cos(frame * 0.1 + angle))  # Adjust movement
        y = HEIGHT // 2 + (100 - i * 5) + (10 * np.sin(frame * 0.1 + angle))
        positions.append((x, y))
    return positions

def main():
    clock = pygame.time.Clock()
    running = True
    frame = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill background
        screen.fill(BACKGROUND_COLOR)
        
        # Update and draw point-lights
        positions = update_positions(frame)
        for pos in positions:
            pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), 5)

        # Update display
        pygame.display.flip()
        
        # Increment frame
        frame += 1
        
        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
