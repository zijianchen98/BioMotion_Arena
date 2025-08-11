
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set screen dimensions and background color
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sadwoman Running")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Define point-light positions for the "sadwoman running" biological motion
# Each frame captures the coordinates for each LED light
POINT_LIGHTS = [
    # Frames for point light animation
    [
        (400, 300), (420, 320), (380, 320), (400, 340), (420, 360), (380, 360),
        (400, 380), (430, 400), (370, 400), (400, 420), (410, 440), (390, 440),
        (420, 460), (400, 460), (380, 460)
    ],
    [
        (405, 310), (425, 330), (385, 330), (405, 355), (430, 375), (380, 375),
        (405, 395), (438, 418), (367, 418), (400, 440), (410, 460), (390, 460),
        (420, 480), (400, 480), (380, 480)
    ],
    [
        (395, 320), (415, 340), (375, 340), (397, 365), (415, 385), (372, 385),
        (392, 405), (420, 430), (370, 430), (390, 450), (405, 470), (375, 470),
        (415, 490), (380, 490), (355, 490)
    ],
]

# Smooth periodic movement using sinusoidal offset
def interpolate_positions(base_positions, frame_number):
    phase_shift = np.sin(frame_number / 20.0) * 10
    interpolated_positions = []
    for x, y in base_positions:
        interpolated_positions.append((x, y + phase_shift))
    return interpolated_positions

# Main animation loop
running = True
frame_index = 0
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current frame positions
    frame_positions = interpolate_positions(POINT_LIGHTS[frame_index % len(POINT_LIGHTS)], frame_index)

    # Draw the point-lights on the screen
    for pos in frame_positions:
        pygame.draw.circle(screen, WHITE, pos, 5)

    # Update frame index (cyclic motion)
    frame_index += 1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
