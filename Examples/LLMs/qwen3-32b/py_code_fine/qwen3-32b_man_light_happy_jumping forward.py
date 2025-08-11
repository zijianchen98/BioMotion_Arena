
import pygame
import math
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Happyman Jumping Forward")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Frame rate
FPS = 60

# Time-based animation parameters
start_time = time.time()
duration = 2.0  # 2 seconds for the jump animation

# Joint positions (relative to center of the body) in a standing pose
# Each joint is represented as a tuple (x, y)
# We will animate these over time to simulate jumping forward
# The joints represent: head, shoulders, elbows, wrists, hips, knees, ankles

# Initial joint positions (in relative coordinates)
joint_positions = [
    (0, -100),  # head
    (-30, -60),  # left shoulder
    (-30, -10),  # left elbow
    (-30, 30),   # left wrist
    (30, -60),   # right shoulder
    (30, -10),   # right elbow
    (30, 30),    # right wrist
    (-30, 30),   # left hip
    (-30, 60),   # left knee
    (-30, 90),   # left ankle
    (30, 30),    # right hip
    (30, 60),    # right knee
    (30, 90),    # right ankle
    (-10, 10),   # left foot (toe)
    (10, 10),    # right foot (toe)
]

# Convert to a list of lists for mutability
joint_positions = [list(pos) for pos in joint_positions]

# Animation parameters
jump_height = 50
jump_distance = 200
jump_duration = duration

# Function to interpolate joint positions over time
def animate_jump(t):
    # t is the normalized time (0 <= t <= 1)
    # We'll use a simple sine function to model the jump
    # Vertical jump
    y_offset = jump_height * (1 - math.cos(math.pi * t))
    # Horizontal jump
    x_offset = jump_distance * t
    # Apply the offset to all joints
    for i in range(len(joint_positions)):
        joint_positions[i][0] += x_offset
        joint_positions[i][1] -= y_offset

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate elapsed time and normalize to [0, 1]
    elapsed_time = time.time() - start_time
    t = min(1.0, elapsed_time / jump_duration)

    # Animate the jump
    animate_jump(t)

    # Draw the point-light stimulus
    for joint in joint_positions:
        pygame.draw.circle(screen, WHITE, (int(joint[0] + WIDTH // 2), int(joint[1] + HEIGHT // 2)), 5)

    pygame.display.flip()
    clock.tick(FPS)

    # End the animation after the jump is complete
    if t >= 1.0:
        running = False

pygame.quit()
sys.exit()
