
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_LIGHT_COLOR = (255, 255, 255)
NUM_POINT_LIGHTS = 15

# Set up point light positions and velocities
point_lights = [
    {"x": 100, "y": 200, "vx": 0, "vy": 0},  # head
    {"x": 120, "y": 220, "vx": 0, "vy": 0},  # right shoulder
    {"x": 80, "y": 220, "vx": 0, "vy": 0},  # left shoulder
    {"x": 140, "y": 250, "vx": 2, "vy": 0},  # right arm
    {"x": 60, "y": 250, "vx": -2, "vy": 0},  # left arm
    {"x": 120, "y": 280, "vx": 0, "vy": 0},  # right hand
    {"x": 80, "y": 280, "vx": 0, "vy": 0},  # left hand
    {"x": 100, "y": 300, "vx": 0, "vy": 0},  # torso
    {"x": 120, "y": 320, "vx": 0, "vy": 0},  # right hip
    {"x": 80, "y": 320, "vx": 0, "vy": 0},  # left hip
    {"x": 140, "y": 350, "vx": 2, "vy": 0},  # right leg
    {"x": 60, "y": 350, "vx": -2, "vy": 0},  # left leg
    {"x": 120, "y": 380, "vx": 0, "vy": 0},  # right foot
    {"x": 80, "y": 380, "vx": 0, "vy": 0},  # left foot
    {"x": 100, "y": 400, "vx": 0, "vy": 0}  # heavy weight
]

# Set up animation variables
waving_arm = "right"
waving_angle = 0

# Create display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move point lights
    for point_light in point_lights:
        point_light["x"] += point_light["vx"]
        point_light["y"] += point_light["vy"]

    # Update waving arm position
    if waving_arm == "right":
        point_lights[3]["x"] = 140 + math.sin(waving_angle) * 20
        point_lights[3]["y"] = 250 + math.cos(waving_angle) * 20
        waving_angle += 0.1
        if waving_angle > math.pi:
            waving_arm = "left"
    else:
        point_lights[4]["x"] = 60 + math.sin(waving_angle) * 20
        point_lights[4]["y"] = 250 + math.cos(waving_angle) * 20
        waving_angle += 0.1
        if waving_angle > math.pi:
            waving_arm = "right"
            waving_angle = 0

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    for point_light in point_lights:
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, (int(point_light["x"]), int(point_light["y"])), 5)

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
