
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Biological Motion - Lying Down Sadman")

# Animation parameters
fps = 60
clock = pygame.time.Clock()

# Helper function for generating point coordinates to simulate biomechanical motion
def generate_points(frame, center_x, center_y):
    """ This function determines the coordinates of 15 points representing a human body."""
    points = []

    # Head
    points.append((center_x + math.sin(frame / 10) * 2, center_y - 100))

    # Shoulders
    points.append((center_x - 30, center_y - 80))
    points.append((center_x + 30, center_y - 80))

    # Arms
    points.append((center_x - 50 + math.sin(frame / 20) * 5, center_y - 40))
    points.append((center_x + 50 + math.sin(frame / 20) * 5, center_y - 40))

    # Torso
    points.append((center_x - 30, center_y - 60))
    points.append((center_x + 30, center_y - 60))
    points.append((center_x, center_y - 40))

    # Legs
    points.append((center_x - 30 + math.sin(frame / 15) * 5, center_y - 10))
    points.append((center_x + 30 + math.sin(frame / 15) * 5, center_y - 10))
    points.append((center_x - 40 + math.sin(frame / 15) * 6, center_y + 20))
    points.append((center_x + 40 + math.sin(frame / 15) * 6, center_y + 20))

    # Feet
    points.append((center_x - 50 + math.sin(frame / 10) * 3, center_y + 50))
    points.append((center_x + 50 + math.sin(frame / 10) * 3, center_y + 50))

    # Bottom hip point
    points.append((center_x, center_y + 30))

    return points

def draw_points(screen, points):
    """Draws the points on the screen."""
    for point in points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 5)

def main():
    # Central position of the animation
    center_x = screen_width // 2
    center_y = screen_height // 2

    frame = 0

    running = True
    while running:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Generate biomechanical points
        points = generate_points(frame, center_x, center_y)

        # Draw points
        draw_points(screen, points)

        # Update frame counter
        frame += 1

        # Refresh screen
        pygame.display.flip()

        # Control frame rate
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
