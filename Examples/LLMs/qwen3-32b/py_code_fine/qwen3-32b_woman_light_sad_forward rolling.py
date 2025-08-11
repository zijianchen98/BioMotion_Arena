
import pygame
import math
import sys
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
NUM_FRAMES = 60  # Number of frames in the animation cycle
NUM_POINTS = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Joint positions relative to body for a rolling forward sad woman (simplified model)
# These are simplified and not anatomically precise, but designed to convey biological motion

# Joint names and their relative positions
# 0: head, 1: spine, 2: left shoulder, 3: right shoulder, 4: left elbow, 5: right elbow,
# 6: left hand, 7: right hand, 8: pelvis, 9: left hip, 10: right hip, 11: left knee,
# 12: right knee, 13: left ankle, 14: right ankle

# Rest position (relative to center)
rest_positions = [
    (0, -100),   # head
    (0, 0),      # spine
    (-30, 30),   # left shoulder
    (30, 30),    # right shoulder
    (-40, 80),   # left elbow
    (40, 80),    # right elbow
    (-50, 130),  # left hand
    (50, 130),   # right hand
    (0, 60),     # pelvis
    (-25, 100),  # left hip
    (25, 100),   # right hip
    (-30, 160),  # left knee
    (30, 160),   # right knee
    (-25, 210),  # left ankle
    (25, 210),   # right ankle
]

# Motion parameters
roll_speed = 0.05  # speed of rolling forward
sadness_factor = 0.8  # affects head and spine angles

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Forward Rolling")
clock = pygame.time.Clock()

def animate_points(frame):
    points = []
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    roll = frame * roll_speed  # Rolling forward

    for i, (x, y) in enumerate(rest_positions):
        # Apply rolling motion
        angle = roll * (i * 0.1)  # Different angles for different body parts
        dx = x * math.cos(angle) - y * math.sin(angle)
        dy = x * math.sin(angle) + y * math.cos(angle)
        px = center_x + dx
        py = center_y + dy

        # Apply sadness by lowering head and spine
        if i == 0:  # head
            py += 20 * math.sin(roll * 2)
        elif i == 1:  # spine
            py += 10 * math.sin(roll * 2)

        points.append((px, py))
    return points

def draw_points(points):
    screen.fill(BLACK)
    for p in points:
        pygame.draw.circle(screen, WHITE, (int(p[0]), int(p[1])), 5)

frame = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    points = animate_points(frame)
    draw_points(points)
    pygame.display.flip()
    frame = (frame + 1) % NUM_FRAMES

pygame.quit()
sys.exit()
