
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the point-lights for the happy man
point_lights = [
    {"x": WIDTH / 2, "y": HEIGHT / 2 - 100, "name": "head"},  # Head
    {"x": WIDTH / 2 - 20, "y": HEIGHT / 2 - 80, "name": "left_shoulder"},  # Left shoulder
    {"x": WIDTH / 2 + 20, "y": HEIGHT / 2 - 80, "name": "right_shoulder"},  # Right shoulder
    {"x": WIDTH / 2 - 40, "y": HEIGHT / 2 - 40, "name": "left_elbow"},  # Left elbow
    {"x": WIDTH / 2 + 40, "y": HEIGHT / 2 - 40, "name": "right_elbow"},  # Right elbow
    {"x": WIDTH / 2 - 60, "y": HEIGHT / 2 + 20, "name": "left_hand"},  # Left hand
    {"x": WIDTH / 2 + 60, "y": HEIGHT / 2 + 20, "name": "right_hand"},  # Right hand
    {"x": WIDTH / 2, "y": HEIGHT / 2 + 60, "name": "torso"},  # Torso
    {"x": WIDTH / 2 - 20, "y": HEIGHT / 2 + 100, "name": "left_hip"},  # Left hip
    {"x": WIDTH / 2 + 20, "y": HEIGHT / 2 + 100, "name": "right_hip"},  # Right hip
    {"x": WIDTH / 2 - 40, "y": HEIGHT / 2 + 140, "name": "left_knee"},  # Left knee
    {"x": WIDTH / 2 + 40, "y": HEIGHT / 2 + 140, "name": "right_knee"},  # Right knee
    {"x": WIDTH / 2 - 60, "y": HEIGHT / 2 + 180, "name": "left_foot"},  # Left foot
    {"x": WIDTH / 2 + 60, "y": HEIGHT / 2 + 180, "name": "right_foot"},  # Right foot
    {"x": WIDTH / 2, "y": HEIGHT / 2 - 120, "name": "neck"}  # Neck
]

# Define the bowing motion
def bow(t):
    angle = math.pi / 2 * math.sin(t)
    for point in point_lights:
        if point["name"] == "head":
            point["x"] = WIDTH / 2
            point["y"] = HEIGHT / 2 - 100 + 50 * math.sin(t)
        elif point["name"] == "left_shoulder":
            point["x"] = WIDTH / 2 - 20
            point["y"] = HEIGHT / 2 - 80 + 30 * math.sin(t)
        elif point["name"] == "right_shoulder":
            point["x"] = WIDTH / 2 + 20
            point["y"] = HEIGHT / 2 - 80 + 30 * math.sin(t)
        elif point["name"] == "left_elbow":
            point["x"] = WIDTH / 2 - 40
            point["y"] = HEIGHT / 2 - 40 + 20 * math.sin(t)
        elif point["name"] == "right_elbow":
            point["x"] = WIDTH / 2 + 40
            point["y"] = HEIGHT / 2 - 40 + 20 * math.sin(t)
        elif point["name"] == "left_hand":
            point["x"] = WIDTH / 2 - 60
            point["y"] = HEIGHT / 2 + 20 + 10 * math.sin(t)
        elif point["name"] == "right_hand":
            point["x"] = WIDTH / 2 + 60
            point["y"] = HEIGHT / 2 + 20 + 10 * math.sin(t)
        elif point["name"] == "torso":
            point["x"] = WIDTH / 2
            point["y"] = HEIGHT / 2 + 60 + 40 * math.sin(t)
        elif point["name"] == "left_hip":
            point["x"] = WIDTH / 2 - 20
            point["y"] = HEIGHT / 2 + 100 + 30 * math.sin(t)
        elif point["name"] == "right_hip":
            point["x"] = WIDTH / 2 + 20
            point["y"] = HEIGHT / 2 + 100 + 30 * math.sin(t)
        elif point["name"] == "left_knee":
            point["x"] = WIDTH / 2 - 40
            point["y"] = HEIGHT / 2 + 140 + 20 * math.sin(t)
        elif point["name"] == "right_knee":
            point["x"] = WIDTH / 2 + 40
            point["y"] = HEIGHT / 2 + 140 + 20 * math.sin(t)
        elif point["name"] == "left_foot":
            point["x"] = WIDTH / 2 - 60
            point["y"] = HEIGHT / 2 + 180 + 10 * math.sin(t)
        elif point["name"] == "right_foot":
            point["x"] = WIDTH / 2 + 60
            point["y"] = HEIGHT / 2 + 180 + 10 * math.sin(t)
        elif point["name"] == "neck":
            point["x"] = WIDTH / 2
            point["y"] = HEIGHT / 2 - 120 + 20 * math.sin(t)

# Main loop
t = 0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the point-lights
    bow(t)
    for point in point_lights:
        pygame.draw.circle(screen, WHITE, (int(point["x"]), int(point["y"])), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

    # Update the time
    t += 0.01

# Quit Pygame
pygame.quit()
