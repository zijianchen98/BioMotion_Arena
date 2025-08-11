
import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30

# Walking motion parameters
num_points = 15
point_radius = 5
speed = 5

# Point light positions relative to the walking pattern
points = [
    (-10, -20), (10, -20),  # Head
    (-20, 0), (0, 0), (20, 0),  # Shoulders
    (-20, 40), (0, 40), (20, 40),  # Hips
    (-30, 80), (0, 80), (30, 80),  # Legs
    (-20, 120), (20, 120),  # Feet
]

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Walking Animation")
    clock = pygame.time.Clock()

    # Animation parameters
    t = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BLACK)

        # Update points for animation
        for i in range(num_points):
            x = WIDTH // 2 + points[i][0] * math.cos(t / 10) + points[i][0] * (i % 3)
            y = HEIGHT // 2 + points[i][1] - (t % 100) * speed + (points[i][1] % 3) * 10
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), point_radius)

        # Increment time
        t += 1
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
