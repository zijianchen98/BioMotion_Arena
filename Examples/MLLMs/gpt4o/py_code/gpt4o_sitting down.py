
import pygame
import numpy as np
import sys

# Initialize pygame
pygame.init()

# Screen dimensions and setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Biological Motion")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frames per second
fps = 60
clock = pygame.time.Clock()

# Define the point-light structure for 'lying down'
# Positions represent the joints (x, y) and change over time
# Define initial positions for lying-down posture
points = np.array([
    [400, 300],  # head
    [385, 320],  # left shoulder
    [415, 320],  # right shoulder
    [385, 340],  # left elbow
    [415, 340],  # right elbow
    [375, 360],  # left wrist
    [425, 360],  # right wrist
    [400, 360],  # torso
    [385, 380],  # left hip
    [415, 380],  # right hip
    [375, 400],  # left knee
    [425, 400],  # right knee
    [370, 420],  # left ankle
    [430, 420],  # right ankle
    [400, 280],  # chin
])

# Define the simulated movement for each point
def simulate_movement(points, t):
    """Simulates realistic point motion."""
    # Oscillatory movement for lying down
    movement = np.sin(t + np.arange(len(points)) * 0.4) * 5
    points[:, 0] += np.cos(t) * 2  # Horizontal subtle motion
    points[:, 1] += movement      # Vertical subtle motion
    return points

# Main animation loop
def main():
    running = True
    time_elapsed = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill screen with black background
        screen.fill(BLACK)
        
        # Simulate realistic movement
        time_elapsed += 0.05
        new_points = simulate_movement(points.copy(), time_elapsed)
        
        # Draw the points
        for point in new_points:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

        # Update the display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(fps)

    pygame.quit()
    sys.exit()

# Run the main function
if __name__ == "__main__":
    main()
