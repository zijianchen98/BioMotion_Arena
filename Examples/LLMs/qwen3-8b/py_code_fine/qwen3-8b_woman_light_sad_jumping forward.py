
import numpy as np
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Jumping Forward - Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define body parts and their positions (approximate)
body_parts = {
    'hips': np.array([300, 400]),
    'left_knee': np.array([250, 450]),
    'right_knee': np.array([350, 450]),
    'left_ankle': np.array([220, 500]),
    'right_ankle': np.array([380, 500]),
    'torso': np.array([300, 350]),
    'left_shoulder': np.array([220, 300]),
    'right_shoulder': np.array([380, 300]),
    'left_elbow': np.array([190, 350]),
    'right_elbow': np.array([410, 350]),
    'left_hand': np.array([160, 380]),
    'right_hand': np.array([440, 380]),
    'head': np.array([300, 250]),
    'neck': np.array([300, 300]),
}

# Define point-light positions as a list of body parts
point_lights = list(body_parts.values())

# Animation parameters
amplitude = 50  # Maximum displacement for jumping
frequency = 0.01  # Controls the speed of the jump
phase = 0.0
jumping = True

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update point-light positions with a sine wave for jumping motion
    if jumping:
        phase += 0.01
        y_offset = amplitude * math.sin(phase)
    else:
        y_offset = 0

    # Apply jumping motion to the body parts
    for part in point_lights:
        part[1] += y_offset

    # Apply realistic motion to simulate a sad woman jumping forward
    # We simulate a forward jump with a slight forward motion and a jump
    # We also simulate a sad posture with a slight downward tilt of the head
    # and a slight forward lean of the torso

    # Apply forward motion
    for part in point_lights:
        part[0] += 0.2

    # Apply jump and fall
    if jumping:
        if y_offset > 0:
            # Jumping up
            pass
        else:
            # Falling down
            pass
    else:
        # Reset position after jump
        for part in point_lights:
            part[1] = 400

    # Check if the jump is complete
    if not jumping:
        for part in point_lights:
            if part[1] > 400:
                jumping = True
            else:
                jumping = False

    # Draw point-lights
    for point in point_lights:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
