
import pygame
import sys
import numpy as np

# Initializing Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
POINT_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)

# Function to create jumping motion
def jump_animation(t):
    # Adjust these parameters to suit the motion needed
    height = 100  # Maximum height of jump
    jump_speed = 10  # Speed of the jump
    
    # Jumping trajectory (parabola)
    if t < 0.5:  # Going up
        y_offset = -4 * height * (t - 0.5)**2 + height
    else:  # Coming down
        y_offset = 4 * height * (t - 1.5)**2
    
    return y_offset

# Main function
def main():
    # Setting up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Jump Animation")
    clock = pygame.time.Clock()

    # Initial positions of points (15 points)
    points = [
        (WIDTH // 2 - 30, HEIGHT // 2 + 30), (WIDTH // 2 - 15, HEIGHT // 2 + 40), (WIDTH // 2, HEIGHT // 2 + 50),
        (WIDTH // 2 + 15, HEIGHT // 2 + 40), (WIDTH // 2 + 30, HEIGHT // 2 + 30),
        (WIDTH // 2 - 40, HEIGHT // 2), (WIDTH // 2 - 30, HEIGHT // 2 - 20), (WIDTH // 2 - 15, HEIGHT // 2 - 30),
        (WIDTH // 2, HEIGHT // 2 - 40), (WIDTH // 2 + 15, HEIGHT // 2 - 30), (WIDTH // 2 + 30, HEIGHT // 2 - 20),
        (WIDTH // 2 + 40, HEIGHT // 2), (WIDTH // 2 - 30, HEIGHT // 2 + 30), (WIDTH // 2 + 30, HEIGHT // 2 + 30), 
        (WIDTH // 2, HEIGHT // 2 + 70)
    ]

    running = True
    frame = 0

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate time from the frame
        t = (frame % (FPS * 2)) / (FPS * 2)  # Normalized time for a full jump cycle

        # Update the background
        screen.fill(BG_COLOR)

        # Draw points with updated positions based on the jump
        for i, (x, y) in enumerate(points):
            # Update the vertical position for the jumping effect
            y_offset = jump_animation(t)
            if i == 14:  # Head point
                adjusted_y = y - y_offset  # Head point moves less
            else:
                adjusted_y = y - (y_offset * (i / 14))  # Other points scale

            pygame.draw.circle(screen, POINT_COLOR, (x, int(adjusted_y)), 5)

        # Update display
        pygame.display.flip()

        # Increment frame
        frame += 1
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
