
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
G = 2.0  # Gravity

# Set up the drawing window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sadman Jumping Forward")

def draw_points(points):
    screen.fill(BLACK)
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)
    pygame.display.flip()

def animate_jump():
    # Initial positions (example: could be joints of a skeleton or points of a stimulus)
    points_positions = [
        [WIDTH // 2 + 0, HEIGHT // 3], # Head
        [WIDTH // 2 - 20, HEIGHT // 3 + 20], # Right Shoulder
        [WIDTH // 2 + 20, HEIGHT // 3 + 20], # Left Shoulder
        [WIDTH // 2 - 20, HEIGHT // 3 + 80], # Right Hip
        [WIDTH // 2 + 20, HEIGHT // 3 + 80], # Left Hip
        [WIDTH // 2 - 20, HEIGHT // 3 + 120], # Right Knee
        [WIDTH // 2 + 20, HEIGHT // 3 + 120], # Left Knee
        [WIDTH // 2 - 20, HEIGHT // 3 + 190], # Right Ankle
        [WIDTH // 2 + 20, HEIGHT // 3 + 190], # Left Ankle
        [WIDTH // 2 - 20, HEIGHT // 3 + 260], # Right Foot
        [WIDTH // 2 + 20, HEIGHT // 3 + 260], # Left Foot
        [WIDTH // 2 - 70, HEIGHT // 3 + 40], # Right Hand
        [WIDTH // 2 - 30, HEIGHT // 3 + 40], # Right Elbow
        [WIDTH // 2 + 30, HEIGHT // 3 + 40], # Left Elbow
        [WIDTH // 2 + 70, HEIGHT // 3 + 40] # Left Hand
    ]

    jump_velocity = [0, -50]
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for point in points_positions:
            point[1] += jump_velocity[1]

            # Apply gravity
            jump_velocity[1] += G

            # Restrict vertical position to stay within screen bounds
            if point[1] > HEIGHT - 50:
                point[1] = HEIGHT - 50
                jump_velocity[1] = 0  # Stop jumping to mimic sadman style

        draw_points(points_positions)
        clock.tick(FPS)

# Run the animation
animate_jump()
