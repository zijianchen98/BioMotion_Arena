
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
POINT_RADIUS = 5
NUM_POINTS = 15

# Positions of the points representing joints
# This is simplified for the waving motion
points = [
    (400, 200),  # Head
    (375, 250), (425, 250),  # Shoulders
    (350, 300), (450, 300),  # Elbows
    (325, 350), (475, 350),  # Hands
]

# Animation Parameters
angle = 0
wave_amplitude = 50
wave_frequency = 1

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Waving Hand")
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill((0, 0, 0))

    # Calculate the motion for the wave
    angle += 0.1  # Increment the angle for smooth motion
    hand_offset = wave_amplitude * math.sin(wave_frequency * angle)

    # Update the positions of the points to reflect waving motion
    waving_hand_position = (375 + hand_offset, 350)
    points[5] = waving_hand_position  # Update hand position

    # Draw the points
    for point in points:
        pygame.draw.circle(screen, (255, 255, 255), (int(point[0]), int(point[1])), POINT_RADIUS)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
