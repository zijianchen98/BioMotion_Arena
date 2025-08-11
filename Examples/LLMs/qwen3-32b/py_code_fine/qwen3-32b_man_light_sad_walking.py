
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 4

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Man Walking")
clock = pygame.time.Clock()

# Walking motion parameters
walk_speed = 0.05  # Speed of motion
frame = 0
num_points = 15
positions = []

# Define joint positions relative to a central point (hip)
# These are simplified and approximate joint positions for a sad walking motion
# We will animate them using sine/cosine functions to simulate walking

# Joints: left hip, left knee, left ankle, right hip, right knee, right ankle, spine, neck, head, left shoulder, left elbow, left hand, right shoulder, right elbow, right hand
joint_offsets = [
    (0, 0),      # hip (center)
    (-50, 0),    # left hip
    (-50, -30),  # left knee
    (-50, -60),  # left ankle
    (50, 0),     # right hip
    (50, -30),   # right knee
    (50, -60),   # right ankle
    (0, -20),    # spine
    (0, -40),    # neck
    (0, -60),    # head
    (-30, -20),  # left shoulder
    (-30, -40),  # left elbow
    (-30, -60),  # left hand
    (30, -20),   # right shoulder
    (30, -40),   # right elbow
    (30, -60),   # right hand
]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    frame += 1

    # Calculate positions based on frame
    for i, (x_off, y_off) in enumerate(joint_offsets):
        if i in [1, 2, 3]:  # left leg
            angle = frame * walk_speed + math.pi * 0.5
            x = WIDTH // 2 + x_off + 30 * math.sin(angle)
            y = HEIGHT // 2 + y_off + 20 * math.cos(angle)
        elif i in [4, 5, 6]:  # right leg
            angle = frame * walk_speed - math.pi * 0.5
            x = WIDTH // 2 + x_off + 30 * math.sin(angle)
            y = HEIGHT // 2 + y_off + 20 * math.cos(angle)
        elif i in [9, 10, 11, 12, 13, 14]:  # arms and head
            angle = frame * walk_speed * 0.5
            if i in [9, 10, 11]:  # left arm
                x = WIDTH // 2 + x_off + 10 * math.sin(angle)
                y = HEIGHT // 2 + y_off + 10 * math.cos(angle)
            elif i in [12, 13, 14]:  # right arm
                x = WIDTH // 2 + x_off + 10 * math.sin(-angle)
                y = HEIGHT // 2 + y_off + 10 * math.cos(-angle)
            else:  # head
                x = WIDTH // 2 + x_off
                y = HEIGHT // 2 + y_off + 10 * math.sin(angle)
        else:  # torso
            x = WIDTH // 2 + x_off
            y = HEIGHT // 2 + y_off

        pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), POINT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
