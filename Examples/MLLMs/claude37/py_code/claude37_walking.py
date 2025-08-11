
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5

# Walking pattern data for point-lights (representing the human body joints)
def create_walking_pattern(frame):
    # Adjust the frame's sine and cosine for realistic movement
    time = frame * 0.1
    # Joint positions for the walking motion
    joint_positions = [
        (WIDTH / 2 + 30 * math.sin(time), HEIGHT / 2 - 50 + 25 * math.cos(time)),  # Head
        (WIDTH / 2 - 15, HEIGHT / 2),  # Shoulders
        (WIDTH / 2 + 15, HEIGHT / 2),  # Shoulders
        (WIDTH / 2 - 30, HEIGHT / 2 + 50),  # Hip Left
        (WIDTH / 2 + 30, HEIGHT / 2 + 50),  # Hip Right
        (WIDTH / 2 - 45, HEIGHT / 2 + 100 + 10 * math.sin(time)),  # Knee Left
        (WIDTH / 2 + 45, HEIGHT / 2 + 100 + 10 * math.cos(time)),  # Knee Right
        (WIDTH / 2 - 60, HEIGHT / 2 + 150),  # Foot Left
        (WIDTH / 2 + 60, HEIGHT / 2 + 150),  # Foot Right
        (WIDTH / 2 - 30, HEIGHT / 2 + 50),  # Ankle left
        (WIDTH / 2 + 30, HEIGHT / 2 + 50)   # Ankle right
    ]
    
    # Adding additional points as needed
    joint_positions += [
        (WIDTH / 2, HEIGHT / 2 - 100),  # Neck
        (WIDTH / 2 - 50, HEIGHT / 2 + 50),  # Elbow Left
        (WIDTH / 2 + 50, HEIGHT / 2 + 50),  # Elbow Right
        (WIDTH / 2 - 10, HEIGHT / 2 + 80),  # Mid-leg Left
        (WIDTH / 2 + 10, HEIGHT / 2 + 80)   # Mid-leg Right
    ]
    
    return joint_positions

# Main loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Walking Animation")
    clock = pygame.time.Clock()
    running = True
    frame = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        screen.fill(BACKGROUND_COLOR)
        joint_positions = create_walking_pattern(frame)

        # Draw the point-lights
        for position in joint_positions:
            pygame.draw.circle(screen, POINT_COLOR, (int(position[0]), int(position[1])), POINT_RADIUS)

        pygame.display.flip()
        frame += 1
        clock.tick(30)  # Control the frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
