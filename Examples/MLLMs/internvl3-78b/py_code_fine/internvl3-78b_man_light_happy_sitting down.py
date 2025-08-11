
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
NUM_POINTS = 15

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation: Happy Man Sitting Down")

# Function to simulate the movement
def generate_sitting_motion(frame):
    # Example: A simplistic biomechanics-based model where each point follows a different trajectory
    points = []
    for i in range(NUM_POINTS):
        # Generate a circular movement at different phases and radii to simulate sitting
        angle = math.radians(frame * (360 / (NUM_POINTS * FPS)))
        radius = 70 + i * 5
        x = SCREEN_WIDTH // 2 + radius * math.cos(angle + math.radians(i * 20))
        y = SCREEN_HEIGHT // 2 + radius * math.sin(angle + math.radians(i * 20))
        points.append((x, y))
    return points

# Main loop
def main():
    clock = pygame.time.Clock()
    frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        
        points = generate_sitting_motion(frame)
        for point in points:
            pygame.draw.circle(screen, WHITE, point, 5)

        pygame.display.flip()
        clock.tick(FPS)
        frame += 1

if __name__ == "__main__":
    main()
