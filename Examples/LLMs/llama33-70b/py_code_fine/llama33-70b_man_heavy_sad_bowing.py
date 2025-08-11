
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions and velocities
point_lights = [
    {"x": 200, "y": 100, "vx": 0, "vy": 0},  # Head
    {"x": 220, "y": 120, "vx": 0, "vy": 2},  # Right shoulder
    {"x": 180, "y": 120, "vx": 0, "vy": 2},  # Left shoulder
    {"x": 240, "y": 150, "vx": 2, "vy": 2},  # Right elbow
    {"x": 160, "y": 150, "vx": -2, "vy": 2},  # Left elbow
    {"x": 260, "y": 180, "vx": 2, "vy": 1},  # Right wrist
    {"x": 140, "y": 180, "vx": -2, "vy": 1},  # Left wrist
    {"x": 200, "y": 200, "vx": 0, "vy": 2},  # Spine
    {"x": 220, "y": 250, "vx": 1, "vy": 2},  # Right hip
    {"x": 180, "y": 250, "vx": -1, "vy": 2},  # Left hip
    {"x": 240, "y": 280, "vx": 1, "vy": 1},  # Right knee
    {"x": 160, "y": 280, "vx": -1, "vy": 1},  # Left knee
    {"x": 260, "y": 310, "vx": 1, "vy": 0},  # Right ankle
    {"x": 140, "y": 310, "vx": -1, "vy": 0},  # Left ankle
    {"x": 200, "y": 350, "vx": 0, "vy": -1},  # Weight
]

# Initialize Pygame
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

        # Bowing motion
        if point_light["y"] > HEIGHT - 50:
            point_light["vy"] = -2
        elif point_light["y"] < 50:
            point_light["vy"] = 2

    # Draw background and point-lights
    screen.fill((0, 0, 0))
    for point_light in point_lights:
        pygame.draw.circle(screen, (255, 255, 255), (int(point_light["x"]), int(point_light["y"])), 5)

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
