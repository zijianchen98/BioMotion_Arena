
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define point-light positions for the happy man
# Each point represents a joint in the body
point_lights = [
    {"x": WIDTH // 2, "y": HEIGHT // 2 - 100, "name": "head"},  # head
    {"x": WIDTH // 2 - 30, "y": HEIGHT // 2 - 80, "name": "left_shoulder"},  # left shoulder
    {"x": WIDTH // 2 + 30, "y": HEIGHT // 2 - 80, "name": "right_shoulder"},  # right shoulder
    {"x": WIDTH // 2 - 60, "y": HEIGHT // 2 - 40, "name": "left_elbow"},  # left elbow
    {"x": WIDTH // 2 + 60, "y": HEIGHT // 2 - 40, "name": "right_elbow"},  # right elbow
    {"x": WIDTH // 2 - 90, "y": HEIGHT // 2 + 20, "name": "left_wrist"},  # left wrist
    {"x": WIDTH // 2 + 90, "y": HEIGHT // 2 + 20, "name": "right_wrist"},  # right wrist
    {"x": WIDTH // 2, "y": HEIGHT // 2 + 50, "name": "torso"},  # torso
    {"x": WIDTH // 2 - 30, "y": HEIGHT // 2 + 80, "name": "left_hip"},  # left hip
    {"x": WIDTH // 2 + 30, "y": HEIGHT // 2 + 80, "name": "right_hip"},  # right hip
    {"x": WIDTH // 2 - 60, "y": HEIGHT // 2 + 110, "name": "left_knee"},  # left knee
    {"x": WIDTH // 2 + 60, "y": HEIGHT // 2 + 110, "name": "right_knee"},  # right knee
    {"x": WIDTH // 2 - 90, "y": HEIGHT // 2 + 140, "name": "left_ankle"},  # left ankle
    {"x": WIDTH // 2 + 90, "y": HEIGHT // 2 + 140, "name": "right_ankle"},  # right ankle
    {"x": WIDTH // 2, "y": HEIGHT // 2 + 170, "name": "feet"}  # feet
]

# Animation variables
angle = 0
bowing = True

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Update point-light positions based on the bowing action
    for point_light in point_lights:
        if point_light["name"] == "head":
            point_light["x"] = WIDTH // 2
            point_light["y"] = HEIGHT // 2 - 100 + math.sin(angle) * 20
        elif point_light["name"] == "torso":
            point_light["x"] = WIDTH // 2
            point_light["y"] = HEIGHT // 2 + 50 + math.sin(angle) * 30
        elif point_light["name"] == "left_shoulder" or point_light["name"] == "right_shoulder":
            point_light["x"] = WIDTH // 2 + (30 if point_light["name"] == "right_shoulder" else -30)
            point_light["y"] = HEIGHT // 2 - 80 + math.sin(angle) * 20
        elif point_light["name"] == "left_elbow" or point_light["name"] == "right_elbow":
            point_light["x"] = WIDTH // 2 + (60 if point_light["name"] == "right_elbow" else -60)
            point_light["y"] = HEIGHT // 2 - 40 + math.sin(angle) * 20
        elif point_light["name"] == "left_wrist" or point_light["name"] == "right_wrist":
            point_light["x"] = WIDTH // 2 + (90 if point_light["name"] == "right_wrist" else -90)
            point_light["y"] = HEIGHT // 2 + 20 + math.sin(angle) * 20
        elif point_light["name"] == "left_hip" or point_light["name"] == "right_hip":
            point_light["x"] = WIDTH // 2 + (30 if point_light["name"] == "right_hip" else -30)
            point_light["y"] = HEIGHT // 2 + 80 + math.sin(angle) * 20
        elif point_light["name"] == "left_knee" or point_light["name"] == "right_knee":
            point_light["x"] = WIDTH // 2 + (60 if point_light["name"] == "right_knee" else -60)
            point_light["y"] = HEIGHT // 2 + 110 + math.sin(angle) * 20
        elif point_light["name"] == "left_ankle" or point_light["name"] == "right_ankle":
            point_light["x"] = WIDTH // 2 + (90 if point_light["name"] == "right_ankle" else -90)
            point_light["y"] = HEIGHT // 2 + 140 + math.sin(angle) * 20
        elif point_light["name"] == "feet":
            point_light["x"] = WIDTH // 2
            point_light["y"] = HEIGHT // 2 + 170 + math.sin(angle) * 10

        # Draw the point-light
        pygame.draw.circle(screen, WHITE, (int(point_light["x"]), int(point_light["y"])), 5)

    # Update the angle for the bowing action
    angle += 0.01
    if angle > 2 * math.pi:
        angle = 0

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)

# Quit Pygame
pygame.quit()
