
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the point-light positions for the running woman
# We'll use 15 points to represent the major joints and body parts
points = [
    {'x': 0, 'y': 0, 'vx': 0, 'vy': 0},  # head
    {'x': 0, 'y': 50, 'vx': 0, 'vy': 0},  # neck
    {'x': -20, 'y': 100, 'vx': 0, 'vy': 0},  # left shoulder
    {'x': 20, 'y': 100, 'vx': 0, 'vy': 0},  # right shoulder
    {'x': -30, 'y': 150, 'vx': 0, 'vy': 0},  # left elbow
    {'x': 30, 'y': 150, 'vx': 0, 'vy': 0},  # right elbow
    {'x': -40, 'y': 200, 'vx': 0, 'vy': 0},  # left wrist
    {'x': 40, 'y': 200, 'vx': 0, 'vy': 0},  # right wrist
    {'x': 0, 'y': 250, 'vx': 0, 'vy': 0},  # torso
    {'x': -20, 'y': 300, 'vx': 0, 'vy': 0},  # left hip
    {'x': 20, 'y': 300, 'vx': 0, 'vy': 0},  # right hip
    {'x': -30, 'y': 350, 'vx': 0, 'vy': 0},  # left knee
    {'x': 30, 'y': 350, 'vx': 0, 'vy': 0},  # right knee
    {'x': -40, 'y': 400, 'vx': 0, 'vy': 0},  # left ankle
    {'x': 40, 'y': 400, 'vx': 0, 'vy': 0},  # right ankle
]

# Set up the movement patterns for each point
def update_points(points, t):
    for i, point in enumerate(points):
        if i == 0:  # head
            point['x'] = 100 + 20 * math.sin(t)
            point['y'] = 100 + 10 * math.sin(t)
        elif i == 1:  # neck
            point['x'] = 100 + 20 * math.sin(t)
            point['y'] = 150 + 10 * math.sin(t)
        elif i == 2:  # left shoulder
            point['x'] = 80 + 30 * math.sin(t)
            point['y'] = 200 + 20 * math.sin(t)
        elif i == 3:  # right shoulder
            point['x'] = 120 + 30 * math.cos(t)
            point['y'] = 200 + 20 * math.cos(t)
        elif i == 4:  # left elbow
            point['x'] = 60 + 40 * math.sin(t)
            point['y'] = 250 + 30 * math.sin(t)
        elif i == 5:  # right elbow
            point['x'] = 140 + 40 * math.cos(t)
            point['y'] = 250 + 30 * math.cos(t)
        elif i == 6:  # left wrist
            point['x'] = 40 + 50 * math.sin(t)
            point['y'] = 300 + 40 * math.sin(t)
        elif i == 7:  # right wrist
            point['x'] = 160 + 50 * math.cos(t)
            point['y'] = 300 + 40 * math.cos(t)
        elif i == 8:  # torso
            point['x'] = 100 + 20 * math.sin(t)
            point['y'] = 350 + 10 * math.sin(t)
        elif i == 9:  # left hip
            point['x'] = 80 + 30 * math.sin(t)
            point['y'] = 400 + 20 * math.sin(t)
        elif i == 10:  # right hip
            point['x'] = 120 + 30 * math.cos(t)
            point['y'] = 400 + 20 * math.cos(t)
        elif i == 11:  # left knee
            point['x'] = 60 + 40 * math.sin(t)
            point['y'] = 450 + 30 * math.sin(t)
        elif i == 12:  # right knee
            point['x'] = 140 + 40 * math.cos(t)
            point['y'] = 450 + 30 * math.cos(t)
        elif i == 13:  # left ankle
            point['x'] = 40 + 50 * math.sin(t)
            point['y'] = 500 + 40 * math.sin(t)
        elif i == 14:  # right ankle
            point['x'] = 160 + 50 * math.cos(t)
            point['y'] = 500 + 40 * math.cos(t)

# Main loop
t = 0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the points
    update_points(points, t)
    t += 0.1

    # Draw everything
    screen.fill(BLACK)
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point['x']), int(point['y'])), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
