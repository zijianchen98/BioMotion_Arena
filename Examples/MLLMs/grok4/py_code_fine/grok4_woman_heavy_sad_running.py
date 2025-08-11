
import pygame
import math
import sys

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
FPS = 30

# Point-light representation of the sad woman
# Define positions of key points (the configuration can be adjusted for realism)
points = [
    (400, 100),  # Head
    (370, 150), (430, 150),  # Shoulders
    (360, 250), (440, 250),  # Elbows
    (350, 350), (450, 350),  # Hands
    (380, 450), (420, 450),  # Hips
    (390, 500),  # Thigh
    (370, 580), (430, 580),  # Knees
    (380, 600), (420, 600),  # Feet
]

def update_points(frame):
    """ Update the position of the points to simulate running. """
    # Simulated heavy weight affects leg positions
    weight_effect = 20  # Arbitrary value to simulate weight
    for i in range(len(points)):
        x, y = points[i]
        if i >= 8:  # For legs and feet
            # Simulate running motion with a vertical oscillation
            y += math.sin(frame / 10 + i) * weight_effect
        else:
            y += math.sin(frame / 10) * 5  # More subtle motion for upper body
        points[i] = (x, y)

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Point-Light Animation')
    
    clock = pygame.time.Clock()
    frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BACKGROUND_COLOR)

        # Update points for motion simulation
        update_points(frame)

        # Draw points on screen
        for x, y in points:
            pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), 5)

        pygame.display.flip()
        frame += 1
        clock.tick(FPS)

if __name__ == '__main__':
    main()
