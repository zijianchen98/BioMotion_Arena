
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions for a running man with a heavy weight
# The points are distributed to represent the major joints of the body
points = [
    {"x": 0, "y": -100, "vx": 0, "vy": 0},  # Head
    {"x": -20, "y": -50, "vx": 0, "vy": 0},  # Left shoulder
    {"x": 20, "y": -50, "vx": 0, "vy": 0},  # Right shoulder
    {"x": -40, "y": 0, "vx": 0, "vy": 0},  # Left elbow
    {"x": 40, "y": 0, "vx": 0, "vy": 0},  # Right elbow
    {"x": -60, "y": 50, "vx": 0, "vy": 0},  # Left wrist
    {"x": 60, "y": 50, "vx": 0, "vy": 0},  # Right wrist
    {"x": 0, "y": 100, "vx": 0, "vy": 0},  # Hips
    {"x": -30, "y": 150, "vx": 0, "vy": 0},  # Left knee
    {"x": 30, "y": 150, "vx": 0, "vy": 0},  # Right knee
    {"x": -50, "y": 200, "vx": 0, "vy": 0},  # Left ankle
    {"x": 50, "y": 200, "vx": 0, "vy": 0},  # Right ankle
    {"x": -10, "y": 250, "vx": 0, "vy": 0},  # Left foot
    {"x": 10, "y": 250, "vx": 0, "vy": 0},  # Right foot
    {"x": 0, "y": 50, "vx": 0, "vy": 0},  # Heavy weight
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Animation parameters
running_speed = 5
weight_swing = 20

# Animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move points to simulate running
    for i, point in enumerate(points):
        if i == 0:  # Head
            point["x"] += running_speed
        elif i == 1 or i == 2:  # Shoulders
            point["x"] += running_speed
            point["y"] += math.sin(pygame.time.get_ticks() / 100) * 10
        elif i == 3 or i == 4:  # Elbows
            point["x"] += running_speed
            point["y"] += math.sin(pygame.time.get_ticks() / 100 + math.pi / 2) * 20
        elif i == 5 or i == 6:  # Wrists
            point["x"] += running_speed
            point["y"] += math.sin(pygame.time.get_ticks() / 100 + math.pi) * 30
        elif i == 7:  # Hips
            point["x"] += running_speed
        elif i == 8 or i == 9:  # Knees
            point["x"] += running_speed
            point["y"] += math.sin(pygame.time.get_ticks() / 100) * 20
        elif i == 10 or i == 11:  # Ankles
            point["x"] += running_speed
            point["y"] += math.sin(pygame.time.get_ticks() / 100 + math.pi / 2) * 30
        elif i == 12 or i == 13:  # Feet
            point["x"] += running_speed
            point["y"] += math.sin(pygame.time.get_ticks() / 100 + math.pi) * 20
        elif i == 14:  # Heavy weight
            point["x"] += running_speed
            point["y"] += math.sin(pygame.time.get_ticks() / 100) * weight_swing

    # Draw points
    screen.fill(BLACK)
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point["x"] + WIDTH / 2), int(point["y"] + HEIGHT / 2)), 5)

    # Update display
    pygame.display.flip()
    clock.tick(60)

    # Reset points if they go off the screen
    if points[0]["x"] > WIDTH:
        for point in points:
            point["x"] -= WIDTH

# Quit Pygame
pygame.quit()
