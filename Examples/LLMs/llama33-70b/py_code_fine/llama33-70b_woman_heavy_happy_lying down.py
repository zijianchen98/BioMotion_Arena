
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)

# Set up point-light positions and velocities
NUM_POINTS = 15
points = [
    {"x": WIDTH / 2, "y": HEIGHT / 2, "vx": 0, "vy": 0},  # Head
    {"x": WIDTH / 2 - 50, "y": HEIGHT / 2 - 50, "vx": -2, "vy": -2},  # Left shoulder
    {"x": WIDTH / 2 + 50, "y": HEIGHT / 2 - 50, "vx": 2, "vy": -2},  # Right shoulder
    {"x": WIDTH / 2 - 100, "y": HEIGHT / 2, "vx": -1, "vy": 0},  # Left elbow
    {"x": WIDTH / 2 + 100, "y": HEIGHT / 2, "vx": 1, "vy": 0},  # Right elbow
    {"x": WIDTH / 2 - 150, "y": HEIGHT / 2 + 50, "vx": -1, "vy": 1},  # Left wrist
    {"x": WIDTH / 2 + 150, "y": HEIGHT / 2 + 50, "vx": 1, "vy": 1},  # Right wrist
    {"x": WIDTH / 2, "y": HEIGHT / 2 + 100, "vx": 0, "vy": 2},  # Torso
    {"x": WIDTH / 2 - 50, "y": HEIGHT / 2 + 150, "vx": -1, "vy": 2},  # Left hip
    {"x": WIDTH / 2 + 50, "y": HEIGHT / 2 + 150, "vx": 1, "vy": 2},  # Right hip
    {"x": WIDTH / 2 - 100, "y": HEIGHT / 2 + 200, "vx": -1, "vy": 1},  # Left knee
    {"x": WIDTH / 2 + 100, "y": HEIGHT / 2 + 200, "vx": 1, "vy": 1},  # Right knee
    {"x": WIDTH / 2 - 150, "y": HEIGHT / 2 + 250, "vx": -1, "vy": 0},  # Left ankle
    {"x": WIDTH / 2 + 150, "y": HEIGHT / 2 + 250, "vx": 1, "vy": 0},  # Right ankle
    {"x": WIDTH / 2, "y": HEIGHT / 2 + 300, "vx": 0, "vy": -1}  # Feet
]

# Set up animation variables
frame_rate = 60
clock = pygame.time.Clock()

# Create display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move points
    for point in points:
        point["x"] += point["vx"]
        point["y"] += point["vy"]

        # Boundary checking
        if point["x"] < 0 or point["x"] > WIDTH:
            point["vx"] = -point["vx"]
        if point["y"] < 0 or point["y"] > HEIGHT:
            point["vy"] = -point["vy"]

    # Draw points
    screen.fill(BACKGROUND_COLOR)
    for point in points:
        pygame.draw.circle(screen, POINT_COLOR, (int(point["x"]), int(point["y"])), 5)

    # Update display
    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()
