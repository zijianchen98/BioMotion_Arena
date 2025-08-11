
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Point-light positions
point_lights = [
    # Head
    {"x": WIDTH / 2, "y": HEIGHT / 2 - 100, "dx": 0, "dy": 0},
    # Body
    {"x": WIDTH / 2, "y": HEIGHT / 2, "dx": 0, "dy": 0},
    # Left shoulder
    {"x": WIDTH / 2 - 50, "y": HEIGHT / 2 - 50, "dx": 0, "dy": 0},
    # Left elbow
    {"x": WIDTH / 2 - 100, "y": HEIGHT / 2, "dx": 0, "dy": 0},
    # Left hand
    {"x": WIDTH / 2 - 150, "y": HEIGHT / 2 + 50, "dx": 0, "dy": 0},
    # Right shoulder
    {"x": WIDTH / 2 + 50, "y": HEIGHT / 2 - 50, "dx": 0, "dy": 0},
    # Right elbow
    {"x": WIDTH / 2 + 100, "y": HEIGHT / 2, "dx": 0, "dy": 0},
    # Right hand
    {"x": WIDTH / 2 + 150, "y": HEIGHT / 2 + 50, "dx": 0, "dy": 0},
    # Left hip
    {"x": WIDTH / 2 - 50, "y": HEIGHT / 2 + 100, "dx": 0, "dy": 0},
    # Left knee
    {"x": WIDTH / 2 - 50, "y": HEIGHT / 2 + 150, "dx": 0, "dy": 0},
    # Left foot
    {"x": WIDTH / 2 - 50, "y": HEIGHT / 2 + 200, "dx": 0, "dy": 0},
    # Right hip
    {"x": WIDTH / 2 + 50, "y": HEIGHT / 2 + 100, "dx": 0, "dy": 0},
    # Right knee
    {"x": WIDTH / 2 + 50, "y": HEIGHT / 2 + 150, "dx": 0, "dy": 0},
    # Right foot
    {"x": WIDTH / 2 + 50, "y": HEIGHT / 2 + 200, "dx": 0, "dy": 0},
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Animation variables
angle = 0
speed = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move point-lights
    point_lights[5]["x"] = WIDTH / 2 + 150 + 50 * math.sin(angle)
    point_lights[5]["y"] = HEIGHT / 2 + 50 + 50 * math.cos(angle)
    point_lights[6]["x"] = WIDTH / 2 + 200 + 50 * math.sin(angle)
    point_lights[6]["y"] = HEIGHT / 2 + 100 + 50 * math.cos(angle)
    point_lights[7]["x"] = WIDTH / 2 + 250 + 50 * math.sin(angle)
    point_lights[7]["y"] = HEIGHT / 2 + 150 + 50 * math.cos(angle)

    angle += 0.01

    # Draw everything
    screen.fill((0, 0, 0))
    for point_light in point_lights:
        pygame.draw.circle(screen, (255, 255, 255), (int(point_light["x"]), int(point_light["y"])), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
