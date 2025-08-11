
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation: Sad Man with Heavy Weight Bowing")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Parameters for the bowing motion
center = (WIDTH // 2, HEIGHT // 2)
radius = 100
speed = 0.01  # Speed of the bowing motion
time = 0

def draw_pointlicht(point, radius):
    pygame.draw.circle(screen, WHITE, point, radius)

def main():
    global time
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Calculate the angle for the bowing motion
        angle = math.sin(time) * math.pi  # Range from -pi to pi
        shoulder_offset = math.pi / 4
        torso_height = 150
        head_radius = 5
        limb_radius = 3

        # Bowing translation
        translation = np.array([0, math.sin(angle) * 50])

        # Body points (relative to center)
        body_points = {
            "head": np.array([0, -torso_height/2 - head_radius]) + translation,
            "neck": np.array([0, -torso_height/2]) + translation,
            "left_shoulder": np.array([-20, -torso_height/2 + shoulder_offset]) + translation,
            "right_shoulder": np.array([20, -torso_height/2 + shoulder_offset]) + translation,
            "left_elbow": np.array([-40, -torso_height/2 + shoulder_offset + 30]) + translation,
            "right_elbow": np.array([40, -torso_height/2 + shoulder_offset + 30]) + translation,
            "left_hand": np.array([-50, -torso_height/2 + shoulder_offset + 60]) + translation,
            "right_hand": np.array([50, -torso_height/2 + shoulder_offset + 60]) + translation,
            "left_hip": np.array([-20, torso_height/2]) + translation,
            "right_hip": np.array([20, torso_height/2]) + translation,
            "left_knee": np.array([-20, torso_height/2 + 50]) + translation,
            "right_knee": np.array([20, torso_height/2 + 50]) + translation,
            "left_foot": np.array([-20, torso_height/2 + 100]) + translation,
            "right_foot": np.array([20, torso_height/2 + 100]) + translation,
            "weight": np.array([0, torso_height/2 + 150]) + translation
        }

        # Draw 15 point-lights at key anatomical locations
        for point in body_points.values():
            draw_pointlicht(point.astype(int), limb_radius)
            draw_pointlicht(center.astype(int), head_radius)

        # Update the display
        pygame.display.flip()

        # Increment time
        time += speed

        # Control the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
