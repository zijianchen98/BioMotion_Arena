
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_COLOR = (255, 255, 255)  # White
LIGHT_RADIUS = 5

# Animation properties
JUMP_HEIGHT = 200
JUMP_DURATION = 2  # seconds
FPS = 60

# Define the point-lights for the happy woman
# Each point-light represents a joint or a feature point on the body
point_lights = [
    {"name": "head", "x": 0, "y": 0, "dx": 0, "dy": 0},
    {"name": "left_eye", "x": -20, "y": -30, "dx": 0, "dy": 0},
    {"name": "right_eye", "x": 20, "y": -30, "dx": 0, "dy": 0},
    {"name": "left_shoulder", "x": -50, "y": 0, "dx": 0, "dy": 0},
    {"name": "right_shoulder", "x": 50, "y": 0, "dx": 0, "dy": 0},
    {"name": "left_elbow", "x": -70, "y": 50, "dx": 0, "dy": 0},
    {"name": "right_elbow", "x": 70, "y": 50, "dx": 0, "dy": 0},
    {"name": "left_hand", "x": -90, "y": 100, "dx": 0, "dy": 0},
    {"name": "right_hand", "x": 90, "y": 100, "dx": 0, "dy": 0},
    {"name": "left_hip", "x": -30, "y": 150, "dx": 0, "dy": 0},
    {"name": "right_hip", "x": 30, "y": 150, "dx": 0, "dy": 0},
    {"name": "left_knee", "x": -30, "y": 200, "dx": 0, "dy": 0},
    {"name": "right_knee", "x": 30, "y": 200, "dx": 0, "dy": 0},
    {"name": "left_ankle", "x": -30, "y": 250, "dx": 0, "dy": 0},
    {"name": "right_ankle", "x": 30, "y": 250, "dx": 0, "dy": 0},
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Animation variables
t = 0
jump_phase = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Update the point-lights
    for point_light in point_lights:
        # Update the x and y coordinates based on the jump phase
        if point_light["name"] == "head":
            point_light["x"] = 0
            point_light["y"] = -JUMP_HEIGHT * math.sin(2 * math.pi * t / JUMP_DURATION)
        elif point_light["name"] == "left_eye" or point_light["name"] == "right_eye":
            point_light["x"] = point_light["x"] + math.sin(2 * math.pi * t / JUMP_DURATION) * 10
            point_light["y"] = point_light["y"] - JUMP_HEIGHT * math.sin(2 * math.pi * t / JUMP_DURATION)
        elif point_light["name"] == "left_shoulder" or point_light["name"] == "right_shoulder":
            point_light["x"] = point_light["x"] + math.sin(2 * math.pi * t / JUMP_DURATION) * 20
            point_light["y"] = point_light["y"] - JUMP_HEIGHT * math.sin(2 * math.pi * t / JUMP_DURATION)
        elif point_light["name"] == "left_elbow" or point_light["name"] == "right_elbow":
            point_light["x"] = point_light["x"] + math.sin(2 * math.pi * t / JUMP_DURATION) * 30
            point_light["y"] = point_light["y"] - JUMP_HEIGHT * math.sin(2 * math.pi * t / JUMP_DURATION)
        elif point_light["name"] == "left_hand" or point_light["name"] == "right_hand":
            point_light["x"] = point_light["x"] + math.sin(2 * math.pi * t / JUMP_DURATION) * 40
            point_light["y"] = point_light["y"] - JUMP_HEIGHT * math.sin(2 * math.pi * t / JUMP_DURATION)
        elif point_light["name"] == "left_hip" or point_light["name"] == "right_hip":
            point_light["x"] = point_light["x"] + math.sin(2 * math.pi * t / JUMP_DURATION) * 10
            point_light["y"] = point_light["y"] - JUMP_HEIGHT * math.sin(2 * math.pi * t / JUMP_DURATION)
        elif point_light["name"] == "left_knee" or point_light["name"] == "right_knee":
            point_light["x"] = point_light["x"] + math.sin(2 * math.pi * t / JUMP_DURATION) * 20
            point_light["y"] = point_light["y"] - JUMP_HEIGHT * math.sin(2 * math.pi * t / JUMP_DURATION)
        elif point_light["name"] == "left_ankle" or point_light["name"] == "right_ankle":
            point_light["x"] = point_light["x"] + math.sin(2 * math.pi * t / JUMP_DURATION) * 30
            point_light["y"] = point_light["y"] - JUMP_HEIGHT * math.sin(2 * math.pi * t / JUMP_DURATION)

        # Draw the point-light
        pygame.draw.circle(screen, LIGHT_COLOR, (int(WIDTH / 2 + point_light["x"]), int(HEIGHT / 2 + point_light["y"])), LIGHT_RADIUS)

    # Update the animation variables
    t += 1 / FPS
    if t > JUMP_DURATION:
        t = 0

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
