
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Sitting Down Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_SPEED = 2

# Sad woman sitting down keyframe positions
keyframes = [
    # Head
    [(400, 200), (400, 200), (400, 200), (400, 200), (400, 200)],
    # Left Arm
    [(350, 250), (350, 270), (350, 290), (350, 310), (350, 330)],
    # Right Arm
    [(450, 250), (450, 270), (450, 290), (450, 310), (450, 330)],
    # Torso
    [(400, 300), (400, 320), (400, 340), (400, 360), (400, 380)],
    # Left Leg
    [(350, 400), (350, 420), (350, 440), (350, 460), (350, 480)],
    # Right Leg
    [(450, 400), (450, 420), (450, 440), (450, 460), (450, 480)]
]

# Function to interpolate between two points
def interpolate(p1, p2, t):
    return (p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t)

# Main loop
running = True
clock = pygame.time.Clock()
frame_index = 0
frame_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate current positions of lights
    for i in range(NUM_LIGHTS):
        part_index = i // 3
        light_index = i % 3
        if frame_index < len(keyframes[part_index]) - 1:
            start_pos = keyframes[part_index][frame_index]
            end_pos = keyframes[part_index][frame_index + 1]
            current_pos = interpolate(start_pos, end_pos, frame_time)
        else:
            current_pos = keyframes[part_index][-1]

        # Draw point light
        pygame.draw.circle(screen, WHITE, (int(current_pos[0]), int(current_pos[1])), LIGHT_RADIUS)

    pygame.display.flip()

    # Update frame index and time
    frame_time += clock.get_time() / 1000.0
    if frame_time >= 1.0:
        frame_time = 0
        frame_index = (frame_index + 1) % len(keyframes[0])

    clock.tick(60)

pygame.quit()
