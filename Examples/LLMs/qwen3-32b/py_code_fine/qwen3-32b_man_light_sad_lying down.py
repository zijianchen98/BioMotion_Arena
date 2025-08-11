
import pygame
import math
import sys
import numpy as np

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Lying Down - Point-Light Biological Motion")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 30
clock = pygame.time.Clock()

# Number of points and their initial positions (simplified skeleton)
# We'll define a 15-point skeleton: head, shoulders, elbows, wrists, hips, knees, ankles
# All positions will be relative to the center of the body
num_points = 15
positions = np.array([
    [0, -100],  # Head
    [-40, -60], # Left shoulder
    [40, -60],  # Right shoulder
    [-60, -20], # Left elbow
    [60, -20],  # Right elbow
    [-80, 10],  # Left wrist
    [80, 10],   # Right wrist
    [-40, 30],  # Left hip
    [40, 30],   # Right hip
    [-60, 80],  # Left knee
    [60, 80],   # Right knee
    [-80, 140], # Left ankle
    [80, 140],  # Right ankle
    [0, 0],     # Center of body (torso)
    [0, 50],    # Pelvis
])

# Function to smoothly animate the sad man lying down
def animate_sadman(t):
    t = t % (2 * math.pi)
    # We'll simulate the body relaxing and lying down with subtle movements
    # to give the impression of a sad, light-weight posture.

    head = [0, -100 + 10 * math.sin(t)]
    left_shoulder = [-40 + 5 * math.sin(t), -60 - 5 * math.sin(t)]
    right_shoulder = [40 - 5 * math.sin(t), -60 - 5 * math.sin(t)]
    left_elbow = [-60 + 5 * math.sin(t), -20 + 5 * math.sin(t)]
    right_elbow = [60 - 5 * math.sin(t), -20 + 5 * math.sin(t)]
    left_wrist = [-80 + 5 * math.sin(t), 10 + 5 * math.sin(t)]
    right_wrist = [80 - 5 * math.sin(t), 10 + 5 * math.sin(t)]
    left_hip = [-40 + 5 * math.sin(t), 30 + 5 * math.sin(t)]
    right_hip = [40 - 5 * math.sin(t), 30 + 5 * math.sin(t)]
    left_knee = [-60 + 5 * math.sin(t), 80 + 5 * math.sin(t)]
    right_knee = [60 - 5 * math.sin(t), 80 + 5 * math.sin(t)]
    left_ankle = [-80 + 5 * math.sin(t), 140 + 5 * math.sin(t)]
    right_ankle = [80 - 5 * math.sin(t), 140 + 5 * math.sin(t)]
    torso = [0, 0 + 10 * math.sin(t)]
    pelvis = [0, 50 + 5 * math.sin(t)]

    animated_positions = np.array([
        head,
        left_shoulder,
        right_shoulder,
        left_elbow,
        right_elbow,
        left_wrist,
        right_wrist,
        left_hip,
        right_hip,
        left_knee,
        right_knee,
        left_ankle,
        right_ankle,
        torso,
        pelvis
    ])

    return animated_positions

# Main loop
angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Animate the positions
    animated_positions = animate_sadman(angle)
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    for point in animated_positions:
        x = int(center_x + point[0])
        y = int(center_y + point[1])
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    angle += 0.05  # Control the speed of the animation

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
