
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants for animation
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Black background
POINT_COLOR = (255, 255, 255)  # White points
FPS = 60
POINT_SIZE = 5

# Biomechanical motion parameters
NUM_POINTS = 15

# Function to generate motion of point-lights representing forward rolling
def generate_biological_motion(frame):
    """
    Simulate forward rolling for a sadwoman using 15 point-lights.
    """

    points = np.zeros((NUM_POINTS, 3))  # Format: [x, y, z]
    radius = 100
    angular_velocity = 2 * np.pi / 100  # Angular velocity for rolling motion
    time = frame / FPS

    # Define relative positions of points for "limbs" and "body"
    offsets = [
        (-40, -40), (-40, 0), (-40, 40),
        (0, -40), (0, 0), (0, 40),
        (40, -40), (40, 0), (40, 40),
        (100, -20), (100, 20), (-100, -20), (-100, 20),
        (60, 60), (-60, 60)
    ]

    for i, offset in enumerate(offsets):
        # Calculate rolling motion
        angle = angular_velocity * time + i * np.pi / NUM_POINTS
        x = offset[0] + radius * np.cos(angle)
        y = offset[1] + radius * np.sin(angle)
        z = 0  # 0 depth since we're showing it in 2D
        points[i] = [x, y, z]

    return points

# Function to render points on the screen
def render_points(screen, points):
    for point in points:
        x = int(SCREEN_WIDTH / 2 + point[0])
        y = int(SCREEN_HEIGHT / 2 + point[1])
        pygame.draw.circle(screen, POINT_COLOR, (x, y), POINT_SIZE)

# Main function to run animation
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Biological Motion: Forward Rolling Animation')
    clock = pygame.time.Clock()
    running = True
    frame = 0

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Generate motion
        points = generate_biological_motion(frame)

        # Draw the screen
        screen.fill(BACKGROUND_COLOR)  # Clear with background color
        render_points(screen, points)

        # Update frame
        pygame.display.flip()
        frame += 1
        
        # Limit FPS
        clock.tick(FPS)

    pygame.quit()

# Run the animation
if __name__ == "__main__":
    main()
