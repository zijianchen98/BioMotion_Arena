
import pygame
import math
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sadman Forward Rolling Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

# Animation parameters
NUM_FRAMES = 120  # Total frames for the animation
LIGHT_RADIUS = 5

# Define the joint positions (relative to center of mass) in a "sad" posture
# We will simulate a forward rolling action using a simplified biomechanical model
# Joint order: head, shoulders (left, right), hips (left, right), knees (left, right), ankles (left, right), feet (left, right), center of mass

joint_positions = [
    (0, -100),     # Head
    (-30, -60),    # Left shoulder
    (30, -60),     # Right shoulder
    (-30, 20),     # Left hip
    (30, 20),      # Right hip
    (-30, 100),    # Left knee
    (30, 100),     # Right knee
    (-30, 200),    # Left ankle
    (30, 200),     # Right ankle
    (-20, 250),    # Left foot
    (20, 250),     # Right foot
    (0, 0),        # Center of mass
    (-20, -80),    # Left arm
    (20, -80),     # Right arm
    (-20, -120),   # Left hand
    (20, -120)     # Right hand
]

# Function to rotate a point around the origin
def rotate_point(point, angle):
    x, y = point
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    new_x = x * cos_theta - y * sin_theta
    new_y = x * sin_theta + y * cos_theta
    return (new_x, new_y)

# Function to animate the rolling action
def animate_rolling(joints, frame):
    angle = (2 * math.pi / NUM_FRAMES) * frame  # Full rotation over NUM_FRAMES
    rolled_joints = [rotate_point(p, angle) for p in joints]
    return rolled_joints

# Main loop
frame = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Animate the rolling action
    animated_joints = animate_rolling(joint_positions, frame)

    # Draw point-lights
    for x, y in animated_joints:
        pygame.draw.circle(screen, WHITE, (int(WIDTH / 2 + x), int(HEIGHT / 2 + y)), LIGHT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)
    frame = (frame + 1) % NUM_FRAMES

pygame.quit()
sys.exit()
