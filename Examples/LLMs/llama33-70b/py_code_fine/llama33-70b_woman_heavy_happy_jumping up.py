
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions for the happy woman
# Each point represents a joint or a point of interest on the body
point_lights = [
    # Head
    {"x": 0, "y": 0, "vx": 0, "vy": 0},
    # Left shoulder
    {"x": -10, "y": -20, "vx": 0, "vy": 0},
    # Right shoulder
    {"x": 10, "y": -20, "vx": 0, "vy": 0},
    # Left elbow
    {"x": -20, "y": -10, "vx": 0, "vy": 0},
    # Right elbow
    {"x": 20, "y": -10, "vx": 0, "vy": 0},
    # Left wrist
    {"x": -30, "y": 0, "vx": 0, "vy": 0},
    # Right wrist
    {"x": 30, "y": 0, "vx": 0, "vy": 0},
    # Left hip
    {"x": -10, "y": 20, "vx": 0, "vy": 0},
    # Right hip
    {"x": 10, "y": 20, "vx": 0, "vy": 0},
    # Left knee
    {"x": -15, "y": 40, "vx": 0, "vy": 0},
    # Right knee
    {"x": 15, "y": 40, "vx": 0, "vy": 0},
    # Left ankle
    {"x": -20, "y": 60, "vx": 0, "vy": 0},
    # Right ankle
    {"x": 20, "y": 60, "vx": 0, "vy": 0},
    # Heavy weight (left hand)
    {"x": -30, "y": 0, "vx": 0, "vy": 0},
    # Heavy weight (right hand)
    {"x": 30, "y": 0, "vx": 0, "vy": 0},
]

# Animation parameters
jump_height = 100
jump_duration = 1000  # milliseconds
weight_offset = 10

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Animation loop
running = True
t = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update point-light positions
    t += 1 / 60  # increment time by 1/60th of a second
    if t > jump_duration / 1000:
        t = 0

    # Calculate jump position
    jump_y = -jump_height * math.sin(2 * math.pi * t / (jump_duration / 1000))

    # Update point-light positions
    for i, point in enumerate(point_lights):
        if i == 0:  # head
            point["x"] = 0
            point["y"] = jump_y
        elif i == 1 or i == 2:  # shoulders
            point["x"] = point["x"] + (i - 1) * 20
            point["y"] = jump_y - 20
        elif i == 3 or i == 4:  # elbows
            point["x"] = point["x"] + (i - 3) * 40
            point["y"] = jump_y - 10
        elif i == 5 or i == 6:  # wrists
            point["x"] = point["x"] + (i - 5) * 60
            point["y"] = jump_y
        elif i == 7 or i == 8:  # hips
            point["x"] = point["x"] + (i - 7) * 20
            point["y"] = jump_y + 20
        elif i == 9 or i == 10:  # knees
            point["x"] = point["x"] + (i - 9) * 30
            point["y"] = jump_y + 40
        elif i == 11 or i == 12:  # ankles
            point["x"] = point["x"] + (i - 11) * 40
            point["y"] = jump_y + 60
        elif i == 13 or i == 14:  # heavy weights
            point["x"] = point_lights[5]["x"] + (i - 13) * weight_offset
            point["y"] = point_lights[5]["y"]

    # Draw everything
    screen.fill((0, 0, 0))
    for point in point_lights:
        pygame.draw.circle(screen, (255, 255, 255), (int(WIDTH / 2 + point["x"]), int(HEIGHT / 2 + point["y"])), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
