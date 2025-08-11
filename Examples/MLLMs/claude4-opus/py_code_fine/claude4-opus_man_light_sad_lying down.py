
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation of a Sad Man Lying Down")

# Function to draw point lights
def draw_point_lights(positions):
    for pos in positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

# Define the positions of the point lights (skeleton joints)
# The coordinates below represent the 'lying down' pose
def update_point_lights(time):
    # Adjust the Y positions for a sad demeanor
    # Example configuration for point lights representing body joints
    return [
        (WIDTH // 2, HEIGHT // 3 - 30 + 10 * math.sin(time * 0.5)),  # Head
        (WIDTH // 2 - 15, HEIGHT // 3 + 10),  # Left Shoulder
        (WIDTH // 2 + 15, HEIGHT // 3 + 10),  # Right Shoulder
        (WIDTH // 2 - 30, HEIGHT // 3 + 50),  # Left Elbow
        (WIDTH // 2 + 30, HEIGHT // 3 + 50),  # Right Elbow
        (WIDTH // 2 - 15, HEIGHT // 3 + 100),  # Left Hand
        (WIDTH // 2 + 15, HEIGHT // 3 + 100),  # Right Hand
        (WIDTH // 2 - 15, HEIGHT // 2 + 30),  # Left Hip
        (WIDTH // 2 + 15, HEIGHT // 2 + 30),  # Right Hip
        (WIDTH // 2 - 15, HEIGHT // 2 + 70),  # Left Knee
        (WIDTH // 2 + 15, HEIGHT // 2 + 70),  # Right Knee
        (WIDTH // 2 - 15, HEIGHT // 2 + 110), # Left Foot
        (WIDTH // 2 + 15, HEIGHT // 2 + 110), # Right Foot
        (WIDTH // 2 - 15, HEIGHT // 2 + 60),  # Lower Body point
        (WIDTH // 2 + 15, HEIGHT // 2 + 60),  # Lower Body point
    ]

# Main loop
def main():
    clock = pygame.time.Clock()
    time = 0

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear screen
        screen.fill(BLACK)

        # Update and draw point lights
        positions = update_point_lights(time)
        draw_point_lights(positions)

        # Update display
        pygame.display.flip()
        
        # Increment time
        time += 1 / FPS

        # Frame rate control
        clock.tick(FPS)

# Run the animation
if __name__ == "__main__":
    main()
