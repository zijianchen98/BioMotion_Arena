
import numpy as np
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Turning Around - Point-Light Stimulus")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define the body parts (simplified for a woman turning around)
body_parts = [
    ("head", (0, 0)),
    ("neck", (0, -50)),
    ("torso", (0, -100)),
    ("right_shoulder", (50, -100)),
    ("right_elbow", (100, -120)),
    ("right_wrist", (120, -140)),
    ("right_hand", (140, -160)),
    ("left_shoulder", (-50, -100)),
    ("left_elbow", (-100, -120)),
    ("left_wrist", (-120, -140)),
    ("left_hand", (-140, -160)),
    ("right_hip", (50, -150)),
    ("right_knee", (80, -180)),
    ("right_ankle", (100, -210)),
    ("right_foot", (120, -240)),
    ("left_hip", (-50, -150)),
    ("left_knee", (-80, -180)),
    ("left_ankle", (-100, -210)),
    ("left_foot", (-120, -240)),
]

# Create a list of point-light positions based on body parts
point_lights = [pygame.Vector2(x, y) for (_, (x, y)) in body_parts[:15]]

# Animation parameters
amplitude = 100  # Maximum displacement from center
frequency = 0.01  # Controls the speed of the turning motion
phase_shift = 0  # Initial phase shift
angle = 0  # Rotation angle

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update point-light positions based on rotation
    for i, light in enumerate(point_lights):
        # Calculate rotation angle for each point based on distance from center
        radius = math.hypot(light.x, light.y)
        angle_i = math.atan2(light.y, light.x)
        new_angle = angle + (angle_i + phase_shift) * frequency
        new_x = radius * math.cos(new_angle)
        new_y = radius * math.sin(new_angle)
        light.x, light.y = new_x, new_y

    # Draw point-lights
    for light in point_lights:
        pygame.draw.circle(screen, WHITE, (int(light.x + WIDTH / 2), int(light.y + HEIGHT / 2)), 3)

    pygame.display.flip()

pygame.quit()
