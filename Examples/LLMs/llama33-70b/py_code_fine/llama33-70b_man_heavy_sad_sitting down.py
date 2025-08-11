
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions and velocities
point_lights = [
    {"x": 100, "y": 100, "vx": 0, "vy": 0},  # Head
    {"x": 120, "y": 150, "vx": 0, "vy": 0},  # Right shoulder
    {"x": 80, "y": 150, "vx": 0, "vy": 0},   # Left shoulder
    {"x": 120, "y": 200, "vx": 0, "vy": 0},  # Right elbow
    {"x": 80, "y": 200, "vx": 0, "vy": 0},   # Left elbow
    {"x": 120, "y": 250, "vx": 0, "vy": 0},  # Right hand
    {"x": 80, "y": 250, "vx": 0, "vy": 0},   # Left hand
    {"x": 100, "y": 300, "vx": 0, "vy": 0},  # Torso
    {"x": 120, "y": 350, "vx": 0, "vy": 0},  # Right hip
    {"x": 80, "y": 350, "vx": 0, "vy": 0},   # Left hip
    {"x": 120, "y": 400, "vx": 0, "vy": 0},  # Right knee
    {"x": 80, "y": 400, "vx": 0, "vy": 0},   # Left knee
    {"x": 120, "y": 450, "vx": 0, "vy": 0},  # Right ankle
    {"x": 80, "y": 450, "vx": 0, "vy": 0},   # Left ankle
    {"x": 100, "y": 500, "vx": 0, "vy": 0},  # Weight
]

# Animation parameters
frame_rate = 60
animation_duration = 3  # seconds

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Animation loop
running = True
frame = 0
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update point-light positions
    for i, point_light in enumerate(point_lights):
        if i == 0:  # Head
            point_light["x"] = 100 + math.sin(frame / 10) * 10
            point_light["y"] = 100 + frame / 10
        elif i == 1:  # Right shoulder
            point_light["x"] = 120 + math.sin(frame / 10) * 10
            point_light["y"] = 150 + frame / 10
        elif i == 2:  # Left shoulder
            point_light["x"] = 80 + math.sin(frame / 10) * 10
            point_light["y"] = 150 + frame / 10
        elif i == 3:  # Right elbow
            point_light["x"] = 120 + math.sin(frame / 10) * 10
            point_light["y"] = 200 + frame / 10
        elif i == 4:  # Left elbow
            point_light["x"] = 80 + math.sin(frame / 10) * 10
            point_light["y"] = 200 + frame / 10
        elif i == 5:  # Right hand
            point_light["x"] = 120 + math.sin(frame / 10) * 10
            point_light["y"] = 250 + frame / 10
        elif i == 6:  # Left hand
            point_light["x"] = 80 + math.sin(frame / 10) * 10
            point_light["y"] = 250 + frame / 10
        elif i == 7:  # Torso
            point_light["x"] = 100 + math.sin(frame / 10) * 10
            point_light["y"] = 300 + frame / 10
        elif i == 8:  # Right hip
            point_light["x"] = 120 + math.sin(frame / 10) * 10
            point_light["y"] = 350 + frame / 10
        elif i == 9:  # Left hip
            point_light["x"] = 80 + math.sin(frame / 10) * 10
            point_light["y"] = 350 + frame / 10
        elif i == 10:  # Right knee
            point_light["x"] = 120 + math.sin(frame / 10) * 10
            point_light["y"] = 400 + frame / 10
        elif i == 11:  # Left knee
            point_light["x"] = 80 + math.sin(frame / 10) * 10
            point_light["y"] = 400 + frame / 10
        elif i == 12:  # Right ankle
            point_light["x"] = 120 + math.sin(frame / 10) * 10
            point_light["y"] = 450 + frame / 10
        elif i == 13:  # Left ankle
            point_light["x"] = 80 + math.sin(frame / 10) * 10
            point_light["y"] = 450 + frame / 10
        elif i == 14:  # Weight
            point_light["x"] = 100 + math.sin(frame / 10) * 10
            point_light["y"] = 500 + frame / 10

    # Draw point-lights
    screen.fill((0, 0, 0))
    for point_light in point_lights:
        pygame.draw.circle(screen, (255, 255, 255), (int(point_light["x"]), int(point_light["y"])), 5)

    # Update display
    pygame.display.flip()

    # Cap frame rate
    clock.tick(frame_rate)

    # Increment frame counter
    frame += 1

    # Stop animation after duration
    if frame / frame_rate >= animation_duration:
        running = False

# Quit Pygame
pygame.quit()
