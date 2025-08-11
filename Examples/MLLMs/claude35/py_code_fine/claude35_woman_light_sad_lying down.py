
import pygame
import sys
import numpy as np

# **Constants**
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
NUM_POINTS = 15
FPS = 30

# **Point-light configuration**
# Initial positions of the lights for a lying down position
initial_positions = [
    (400, 150), (380, 200), (420, 200),     # Head
    (360, 250), (440, 250),                 # Shoulders
    (350, 300), (450, 300),                 # Elbows
    (340, 350), (460, 350),                 # Hands
    (350, 400), (450, 400),                 # Hips
    (320, 450), (480, 450),                 # Knees
    (300, 500), (500, 500),                 # Feet
]

# **Animate the Motion**
def animate(points):
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Point-light Animation - Sad Woman Lying Down')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)

        # **Draw each point/light**
        for x, y in points:
            pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), 5)

        pygame.display.flip()
        clock.tick(FPS)

        # **Update positions for the animation**
        for i in range(len(points)):
            # Simulate a slight undulation, moving up and down
            y_offset = 0.5 * np.sin(pygame.time.get_ticks() * 0.005 + i)
            points[i] = (points[i][0], points[i][1] + y_offset)

# **Main Function**
def main():
    pygame.init()
    points = initial_positions.copy()
    animate(points)

if __name__ == "__main__":
    main()
