
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define point-light positions and velocities for the happy woman sitting down
# These positions and velocities are approximate and based on human biomechanics
point_lights = [
    {"position": np.array([WIDTH / 2, HEIGHT / 2]), "velocity": np.array([0, 0])},  # head
    {"position": np.array([WIDTH / 2 - 50, HEIGHT / 2 - 100]), "velocity": np.array([0, 5])},  # left shoulder
    {"position": np.array([WIDTH / 2 + 50, HEIGHT / 2 - 100]), "velocity": np.array([0, 5])},  # right shoulder
    {"position": np.array([WIDTH / 2 - 100, HEIGHT / 2 - 50]), "velocity": np.array([0, 5])},  # left elbow
    {"position": np.array([WIDTH / 2 + 100, HEIGHT / 2 - 50]), "velocity": np.array([0, 5])},  # right elbow
    {"position": np.array([WIDTH / 2 - 150, HEIGHT / 2 + 50]), "velocity": np.array([0, 10])},  # left wrist
    {"position": np.array([WIDTH / 2 + 150, HEIGHT / 2 + 50]), "velocity": np.array([0, 10])},  # right wrist
    {"position": np.array([WIDTH / 2, HEIGHT / 2 + 100]), "velocity": np.array([0, 10])},  # torso
    {"position": np.array([WIDTH / 2 - 50, HEIGHT / 2 + 150]), "velocity": np.array([0, 15])},  # left hip
    {"position": np.array([WIDTH / 2 + 50, HEIGHT / 2 + 150]), "velocity": np.array([0, 15])},  # right hip
    {"position": np.array([WIDTH / 2 - 100, HEIGHT / 2 + 200]), "velocity": np.array([0, 20])},  # left knee
    {"position": np.array([WIDTH / 2 + 100, HEIGHT / 2 + 200]), "velocity": np.array([0, 20])},  # right knee
    {"position": np.array([WIDTH / 2 - 150, HEIGHT / 2 + 250]), "velocity": np.array([0, 25])},  # left ankle
    {"position": np.array([WIDTH / 2 + 150, HEIGHT / 2 + 250]), "velocity": np.array([0, 25])},  # right ankle
    {"position": np.array([WIDTH / 2, HEIGHT / 2 + 300]), "velocity": np.array([0, 30])},  # feet
]

# Animation variables
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move point-lights
    for point_light in point_lights:
        point_light["position"] += point_light["velocity"]

        # Boundary checking to prevent point-lights from moving off the screen
        if point_light["position"][0] < 0 or point_light["position"][0] > WIDTH:
            point_light["velocity"][0] *= -1
        if point_light["position"][1] < 0 or point_light["position"][1] > HEIGHT:
            point_light["velocity"][1] *= -1

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    for point_light in point_lights:
        pygame.draw.circle(screen, POINT_COLOR, (int(point_light["position"][0]), int(point_light["position"][1])), 5)

    # Update display
    pygame.display.flip()

    # Cap framerate
    clock.tick(60)

# Quit Pygame
pygame.quit()
