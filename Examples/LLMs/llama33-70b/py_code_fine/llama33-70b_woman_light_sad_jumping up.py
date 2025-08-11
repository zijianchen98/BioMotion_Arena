
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the 15 point-lights for the sad woman
# Each point-light is represented by its x, y coordinates and a label
point_lights = [
    {"label": "head", "x": WIDTH // 2, "y": HEIGHT // 2 - 100},
    {"label": "left_shoulder", "x": WIDTH // 2 - 50, "y": HEIGHT // 2 - 50},
    {"label": "right_shoulder", "x": WIDTH // 2 + 50, "y": HEIGHT // 2 - 50},
    {"label": "left_elbow", "x": WIDTH // 2 - 100, "y": HEIGHT // 2},
    {"label": "right_elbow", "x": WIDTH // 2 + 100, "y": HEIGHT // 2},
    {"label": "left_wrist", "x": WIDTH // 2 - 150, "y": HEIGHT // 2 + 50},
    {"label": "right_wrist", "x": WIDTH // 2 + 150, "y": HEIGHT // 2 + 50},
    {"label": "left_hip", "x": WIDTH // 2 - 50, "y": HEIGHT // 2 + 100},
    {"label": "right_hip", "x": WIDTH // 2 + 50, "y": HEIGHT // 2 + 100},
    {"label": "left_knee", "x": WIDTH // 2 - 50, "y": HEIGHT // 2 + 200},
    {"label": "right_knee", "x": WIDTH // 2 + 50, "y": HEIGHT // 2 + 200},
    {"label": "left_ankle", "x": WIDTH // 2 - 50, "y": HEIGHT // 2 + 300},
    {"label": "right_ankle", "x": WIDTH // 2 + 50, "y": HEIGHT // 2 + 300},
    {"label": "left_foot", "x": WIDTH // 2 - 50, "y": HEIGHT // 2 + 350},
    {"label": "right_foot", "x": WIDTH // 2 + 50, "y": HEIGHT // 2 + 350},
]

# Define the jumping motion
def jumping_motion(point_lights, t):
    # Calculate the vertical displacement
    displacement = 100 * math.sin(t)

    # Update the point-lights' positions
    for point_light in point_lights:
        if point_light["label"] == "head":
            point_light["x"] = WIDTH // 2
            point_light["y"] = HEIGHT // 2 - 100 + displacement
        elif point_light["label"] == "left_shoulder" or point_light["label"] == "right_shoulder":
            point_light["x"] = WIDTH // 2 - 50 if point_light["label"] == "left_shoulder" else WIDTH // 2 + 50
            point_light["y"] = HEIGHT // 2 - 50 + displacement
        elif point_light["label"] == "left_elbow" or point_light["label"] == "right_elbow":
            point_light["x"] = WIDTH // 2 - 100 if point_light["label"] == "left_elbow" else WIDTH // 2 + 100
            point_light["y"] = HEIGHT // 2 + displacement
        elif point_light["label"] == "left_wrist" or point_light["label"] == "right_wrist":
            point_light["x"] = WIDTH // 2 - 150 if point_light["label"] == "left_wrist" else WIDTH // 2 + 150
            point_light["y"] = HEIGHT // 2 + 50 + displacement
        elif point_light["label"] == "left_hip" or point_light["label"] == "right_hip":
            point_light["x"] = WIDTH // 2 - 50 if point_light["label"] == "left_hip" else WIDTH // 2 + 50
            point_light["y"] = HEIGHT // 2 + 100 + displacement
        elif point_light["label"] == "left_knee" or point_light["label"] == "right_knee":
            point_light["x"] = WIDTH // 2 - 50 if point_light["label"] == "left_knee" else WIDTH // 2 + 50
            point_light["y"] = HEIGHT // 2 + 200 + displacement
        elif point_light["label"] == "left_ankle" or point_light["label"] == "right_ankle":
            point_light["x"] = WIDTH // 2 - 50 if point_light["label"] == "left_ankle" else WIDTH // 2 + 50
            point_light["y"] = HEIGHT // 2 + 300 + displacement
        elif point_light["label"] == "left_foot" or point_light["label"] == "right_foot":
            point_light["x"] = WIDTH // 2 - 50 if point_light["label"] == "left_foot" else WIDTH // 2 + 50
            point_light["y"] = HEIGHT // 2 + 350 + displacement

# Main loop
t = 0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BACKGROUND_COLOR)

    # Draw the point-lights
    jumping_motion(point_lights, t)
    for point_light in point_lights:
        pygame.draw.circle(screen, LIGHT_COLOR, (int(point_light["x"]), int(point_light["y"])), 5)

    # Update the display
    pygame.display.flip()

    # Increment the time
    t += 0.1

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
