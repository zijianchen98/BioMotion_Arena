
import pygame
import sys
import math

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5
NUM_POINTS = 15
FPS = 60

# Point-light positions
def update_positions(frame):
    positions = []
    time = frame / FPS
    for i in range(NUM_POINTS):
        angle = 2 * math.pi * i / NUM_POINTS + time * 3  # Running motion
        x = WIDTH // 2 + 100 * math.sin(angle)  # Horizontal oscillation
        y = HEIGHT // 2 + 50 * math.cos(angle)  # Vertical motion
        positions.append((x, y))
    return positions

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Animation of Running")
    clock = pygame.time.Clock()

    frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)

        # Update positions
        positions = update_positions(frame)

        # Draw point-lights
        for pos in positions:
            pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), POINT_RADIUS)

        pygame.display.flip()
        frame += 1
        clock.tick(FPS)

if __name__ == "__main__":
    main()
