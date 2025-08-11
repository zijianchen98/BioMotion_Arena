
import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion")

def create_sadman_data():
    """
    Creates 15 point positions for the sadman in a lying-down pose.
    The points represent major skeletal joints (head, shoulders, elbows, etc.)
    and are stored as 2D coordinates in a coherent structure.
    """
    # Base coordinates (lying down sadman proportions)
    # Head, neck, shoulders, elbows, wrists, chest, hips, knees, feet
    points = np.array([
        [400, 200], # Head
        [400, 220], # Neck
        [370, 240], # Left shoulder
        [430, 240], # Right shoulder
        [360, 260], # Left elbow
        [440, 260], # Right elbow
        [350, 280], # Left wrist
        [450, 280], # Right wrist
        [400, 260], # Chest
        [380, 300], # Left hip
        [420, 300], # Right hip
        [370, 340], # Left knee
        [430, 340], # Right knee
        [360, 380], # Left foot
        [440, 380]  # Right foot
    ])
    return points

def animate_sadman(points, frame):
    """
    Apply smooth cyclical animation based on biomechanical plausibility.
    The animation simulates breathing and minimal limb movement.
    """
    # Breathing effect (simulated through sinusoidal modulation of the chest)
    breathing_amplitude = 5
    points[8][1] += int(breathing_amplitude * np.sin(frame * 0.1))

    # Limb oscillations (simulate cyclical motion around hips and knees)
    oscillation_amplitude = 5
    points[9][1] += int(oscillation_amplitude * np.sin(frame * 0.1))
    points[10][1] -= int(oscillation_amplitude * np.sin(frame * 0.1))
    points[11][1] += int(oscillation_amplitude * np.sin(frame * 0.1))
    points[12][1] -= int(oscillation_amplitude * np.sin(frame * 0.1))

    return points

def draw_points(screen, points):
    """
    Draw point-light locations on the screen.
    """
    for point in points:
        pygame.draw.circle(screen, WHITE, point, 5)

def main():
    clock = pygame.time.Clock()
    frame = 0

    # Initial positions of the points
    base_points = create_sadman_data()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)  # Clear screen with black background

        # Animate sadman's motion
        animated_points = animate_sadman(np.copy(base_points), frame)

        # Draw sadman
        draw_points(screen, animated_points)

        # Increment frame for animation
        frame += 1

        pygame.display.flip()  # Update display
        clock.tick(FPS)  # Maintain frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
