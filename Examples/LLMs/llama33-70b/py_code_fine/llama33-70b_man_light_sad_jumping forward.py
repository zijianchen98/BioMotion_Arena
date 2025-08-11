
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions and velocities
point_lights = [
    {"x": 100, "y": 200, "vx": 2, "vy": -5},  # Head
    {"x": 120, "y": 220, "vx": 1, "vy": -4},  # Left shoulder
    {"x": 80, "y": 220, "vx": 3, "vy": -4},  # Right shoulder
    {"x": 100, "y": 250, "vx": 2, "vy": -3},  # Left elbow
    {"x": 120, "y": 250, "vx": 1, "vy": -3},  # Right elbow
    {"x": 100, "y": 280, "vx": 2, "vy": -2},  # Left wrist
    {"x": 120, "y": 280, "vx": 1, "vy": -2},  # Right wrist
    {"x": 100, "y": 300, "vx": 2, "vy": -1},  # Left hip
    {"x": 120, "y": 300, "vx": 1, "vy": -1},  # Right hip
    {"x": 100, "y": 330, "vx": 2, "vy": 0},  # Left knee
    {"x": 120, "y": 330, "vx": 1, "vy": 0},  # Right knee
    {"x": 100, "y": 360, "vx": 2, "vy": 1},  # Left ankle
    {"x": 120, "y": 360, "vx": 1, "vy": 1},  # Right ankle
    {"x": 100, "y": 390, "vx": 2, "vy": 2},  # Left toe
    {"x": 120, "y": 390, "vx": 1, "vy": 2},  # Right toe
]

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move point-lights
    for point_light in point_lights:
        point_light["x"] += point_light["vx"]
        point_light["y"] += point_light["vy"]

        # Boundary checking
        if point_light["x"] < 0 or point_light["x"] > WIDTH:
            point_light["vx"] *= -1
        if point_light["y"] < 0 or point_light["y"] > HEIGHT:
            point_light["vy"] *= -1

    # Draw background and point-lights
    screen.fill((0, 0, 0))
    for point_light in point_lights:
        pygame.draw.circle(screen, (255, 255, 255), (int(point_light["x"]), int(point_light["y"])), 5)

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
