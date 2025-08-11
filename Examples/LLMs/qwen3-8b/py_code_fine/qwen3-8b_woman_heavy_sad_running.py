
import numpy as np
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Running - Point-Light Stimulus")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define the 15 body joints (simplified skeletal structure)
# Based on a human body for a running motion
body_joints = [
    # Head
    (400, 100),
    # Shoulders
    (300, 200), (500, 200),
    # Elbows
    (250, 300), (450, 300),
    # Hands
    (200, 400), (500, 400),
    # Hips
    (350, 450),
    # Knees
    (300, 550), (400, 550),
    # Ankles
    (250, 600), (450, 600)
]

# Define a simple running motion cycle (simplified sine wave for smooth movement)
def get_position(index, time, amplitude, frequency, phase):
    return (int(body_joints[index][0] + amplitude * math.sin(time * frequency + phase)),
            int(body_joints[index][1] + amplitude * math.sin(time * frequency + phase + 1.5)))

# Main loop
def main():
    running = True
    time = 0
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        # Update positions based on time
        for i in range(len(body_joints)):
            if i == 0:  # Head
                x, y = get_position(i, time, 30, 0.005, 0)
            elif i == 1 or i == 2:  # Shoulders
                x, y = get_position(i, time, 20, 0.005, 0.2)
            elif i == 3 or i == 4:  # Elbows
                x, y = get_position(i, time, 15, 0.005, 0.4)
            elif i == 5 or i == 6:  # Hands
                x, y = get_position(i, time, 25, 0.005, 0.6)
            elif i == 7:  # Hip
                x, y = get_position(i, time, 10, 0.005, 0.8)
            elif i == 8 or i == 9:  # Knees
                x, y = get_position(i, time, 15, 0.005, 1.0)
            elif i == 10 or i == 11:  # Ankles
                x, y = get_position(i, time, 20, 0.005, 1.2)
            else:
                x, y = body_joints[i]

            # Draw the point-light
            pygame.draw.circle(screen, WHITE, (x, y), 3)

        # Update time
        time += 0.05

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
