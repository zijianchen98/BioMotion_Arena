
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Point-light positions and velocities
point_lights = [
    {"x": 0, "y": 0, "vx": 0, "vy": 0},  # Head
    {"x": -20, "y": -30, "vx": 0, "vy": 0},  # Left shoulder
    {"x": 20, "y": -30, "vx": 0, "vy": 0},  # Right shoulder
    {"x": -30, "y": -10, "vx": 0, "vy": 0},  # Left elbow
    {"x": 30, "y": -10, "vx": 0, "vy": 0},  # Right elbow
    {"x": -40, "y": 10, "vx": 0, "vy": 0},  # Left wrist
    {"x": 40, "y": 10, "vx": 0, "vy": 0},  # Right wrist
    {"x": -10, "y": -40, "vx": 0, "vy": 0},  # Left hip
    {"x": 10, "y": -40, "vx": 0, "vy": 0},  # Right hip
    {"x": -20, "y": -60, "vx": 0, "vy": 0},  # Left knee
    {"x": 20, "y": -60, "vx": 0, "vy": 0},  # Right knee
    {"x": -30, "y": -80, "vx": 0, "vy": 0},  # Left ankle
    {"x": 30, "y": -80, "vx": 0, "vy": 0},  # Right ankle
    {"x": 0, "y": -50, "vx": 0, "vy": 0},  # Torso
    {"x": 0, "y": -90, "vx": 0, "vy": 0},  # Hips
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Animation parameters
angle = 0
speed = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update point-light positions
    angle += 0.1
    for i, point_light in enumerate(point_lights):
        if i == 0:  # Head
            point_light["x"] = 0 + math.sin(angle) * 10
            point_light["y"] = -50 + math.cos(angle) * 10
        elif i == 1:  # Left shoulder
            point_light["x"] = -20 + math.sin(angle) * 5
            point_light["y"] = -30 + math.cos(angle) * 5
        elif i == 2:  # Right shoulder
            point_light["x"] = 20 + math.sin(angle) * 5
            point_light["y"] = -30 + math.cos(angle) * 5
        elif i == 3:  # Left elbow
            point_light["x"] = -30 + math.sin(angle) * 10
            point_light["y"] = -10 + math.cos(angle) * 10
        elif i == 4:  # Right elbow
            point_light["x"] = 30 + math.sin(angle) * 10
            point_light["y"] = -10 + math.cos(angle) * 10
        elif i == 5:  # Left wrist
            point_light["x"] = -40 + math.sin(angle) * 15
            point_light["y"] = 10 + math.cos(angle) * 15
        elif i == 6:  # Right wrist
            point_light["x"] = 40 + math.sin(angle) * 15
            point_light["y"] = 10 + math.cos(angle) * 15
        elif i == 7:  # Left hip
            point_light["x"] = -10 + math.sin(angle) * 5
            point_light["y"] = -40 + math.cos(angle) * 5
        elif i == 8:  # Right hip
            point_light["x"] = 10 + math.sin(angle) * 5
            point_light["y"] = -40 + math.cos(angle) * 5
        elif i == 9:  # Left knee
            point_light["x"] = -20 + math.sin(angle) * 10
            point_light["y"] = -60 + math.cos(angle) * 10
        elif i == 10:  # Right knee
            point_light["x"] = 20 + math.sin(angle) * 10
            point_light["y"] = -60 + math.cos(angle) * 10
        elif i == 11:  # Left ankle
            point_light["x"] = -30 + math.sin(angle) * 15
            point_light["y"] = -80 + math.cos(angle) * 15
        elif i == 12:  # Right ankle
            point_light["x"] = 30 + math.sin(angle) * 15
            point_light["y"] = -80 + math.cos(angle) * 15
        elif i == 13:  # Torso
            point_light["x"] = 0 + math.sin(angle) * 5
            point_light["y"] = -50 + math.cos(angle) * 5
        elif i == 14:  # Hips
            point_light["x"] = 0 + math.sin(angle) * 5
            point_light["y"] = -90 + math.cos(angle) * 5

        # Update position based on speed and angle
        point_light["x"] += speed * math.cos(angle)
        point_light["y"] += speed * math.sin(angle)

    # Draw everything
    screen.fill((0, 0, 0))
    for point_light in point_lights:
        pygame.draw.circle(screen, (255, 255, 255), (int(point_light["x"] + WIDTH // 2), int(point_light["y"] + HEIGHT // 2)), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
