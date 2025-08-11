
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happyman Running")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 30

# Number of joints (points)
NUM_JOINTS = 15

# Define the joints (as indices for clarity)
HEAD = 0
LEFT_ELBOW = 1
LEFT_HAND = 2
RIGHT_ELBOW = 3
RIGHT_HAND = 4
LEFT_KNEE = 5
LEFT_FOOT = 6
RIGHT_KNEE = 7
RIGHT_FOOT = 8
LEFT_SHOULDER = 9
RIGHT_SHOULDER = 10
LEFT_HIP = 11
RIGHT_HIP = 12
WAIST = 13
CHEST = 14

# Body part lengths (in pixels)
ARM_LENGTH = 100
LEG_LENGTH = 120
CHEST_WIDTH = 60
CHEST_HEIGHT = 60
WAIST_WIDTH = 50
WAIST_HEIGHT = 40
HEAD_RADIUS = 15

# Animation parameters
base_speed = 4  # base horizontal speed
step_frequency = 0.2  # how fast the legs move
arm_frequency = 0.2  # how fast the arms move

# Initial positions (relative to the center of the body)
def get_initial_positions(x, y):
    positions = [
        (x, y - 100),            # HEAD
        (x - 50, y - 20),        # LEFT_ELBOW
        (x - 100, y + 10),       # LEFT_HAND
        (x + 50, y - 20),        # RIGHT_ELBOW
        (x + 100, y + 10),       # RIGHT_HAND
        (x - 30, y + 60),        # LEFT_KNEE
        (x - 50, y + 130),       # LEFT_FOOT
        (x + 30, y + 60),        # RIGHT_KNEE
        (x + 50, y + 130),       # RIGHT_FOOT
        (x - 40, y - 50),        # LEFT_SHOULDER
        (x + 40, y - 50),        # RIGHT_SHOULDER
        (x - 30, y + 40),        # LEFT_HIP
        (x + 30, y + 40),        # RIGHT_HIP
        (x, y - 20),             # WAIST
        (x, y - 40),             # CHEST
    ]
    return positions

# Update joint positions based on time
def update_positions(positions, time):
    x, y = positions[WAIST]
    dx = base_speed * time

    # Update body position
    new_positions = [
        (x + dx, y - 100),            # HEAD
        (x + dx - 50, y - 20),        # LEFT_ELBOW
        (x + dx - 100, y + 10),       # LEFT_HAND
        (x + dx + 50, y - 20),        # RIGHT_ELBOW
        (x + dx + 100, y + 10),       # RIGHT_HAND
        (x + dx - 30, y + 60),        # LEFT_KNEE
        (x + dx - 50, y + 130),       # LEFT_FOOT
        (x + dx + 30, y + 60),        # RIGHT_KNEE
        (x + dx + 50, y + 130),       # RIGHT_FOOT
        (x + dx - 40, y - 50),        # LEFT_SHOULDER
        (x + dx + 40, y - 50),        # RIGHT_SHOULDER
        (x + dx - 30, y + 40),        # LEFT_HIP
        (x + dx + 30, y + 40),        # RIGHT_HIP
        (x + dx, y - 20),             # WAIST
        (x + dx, y - 40),             # CHEST
    ]

    # Add leg motion (running)
    leg_offset = math.sin(time * step_frequency) * 15
    new_positions[LEFT_KNEE] = (new_positions[LEFT_KNEE][0], new_positions[LEFT_KNEE][1] + leg_offset)
    new_positions[LEFT_FOOT] = (new_positions[LEFT_FOOT][0], new_positions[LEFT_FOOT][1] + leg_offset)
    new_positions[RIGHT_KNEE] = (new_positions[RIGHT_KNEE][0], new_positions[RIGHT_KNEE][1] - leg_offset)
    new_positions[RIGHT_FOOT] = (new_positions[RIGHT_FOOT][0], new_positions[RIGHT_FOOT][1] - leg_offset)

    # Add arm motion (running)
    arm_offset = math.sin(time * arm_frequency) * 20
    new_positions[LEFT_ELBOW] = (new_positions[LEFT_ELBOW][0], new_positions[LEFT_ELBOW][1] - arm_offset)
    new_positions[LEFT_HAND] = (new_positions[LEFT_HAND][0], new_positions[LEFT_HAND][1] - arm_offset)
    new_positions[RIGHT_ELBOW] = (new_positions[RIGHT_ELBOW][0], new_positions[RIGHT_ELBOW][1] + arm_offset)
    new_positions[RIGHT_HAND] = (new_positions[RIGHT_HAND][0], new_positions[RIGHT_HAND][1] + arm_offset)

    return new_positions

# Main loop
def main():
    time = 0
    running = True
    positions = get_initial_positions(WIDTH // 2, HEIGHT // 2)

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        time += 1 / FPS
        positions = update_positions(positions, time)

        # Draw the points
        for pos in positions:
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
