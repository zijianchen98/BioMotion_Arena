
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Solid black background
LIGHT_COLOR = (255, 255, 255)  # White point-lights

# Set up animation variables
FPS = 60
DURATION = 5  # seconds

# Define the 15 point-lights for the sad woman
LIGHTS = [
    {"x": 0, "y": -100, "dx": 0, "dy": 0},  # Head
    {"x": -20, "y": -80, "dx": 0, "dy": 0},  # Left shoulder
    {"x": 20, "y": -80, "dx": 0, "dy": 0},  # Right shoulder
    {"x": -40, "y": 0, "dx": 0, "dy": 0},  # Left elbow
    {"x": 40, "y": 0, "dx": 0, "dy": 0},  # Right elbow
    {"x": -60, "y": 80, "dx": 0, "dy": 0},  # Left hand
    {"x": 60, "y": 80, "dx": 0, "dy": 0},  # Right hand
    {"x": 0, "y": 100, "dx": 0, "dy": 0},  # Hips
    {"x": -20, "y": 120, "dx": 0, "dy": 0},  # Left knee
    {"x": 20, "y": 120, "dx": 0, "dy": 0},  # Right knee
    {"x": -40, "y": 140, "dx": 0, "dy": 0},  # Left ankle
    {"x": 40, "y": 140, "dx": 0, "dy": 0},  # Right ankle
    {"x": -10, "y": -40, "dx": 0, "dy": 0},  # Left breast
    {"x": 10, "y": -40, "dx": 0, "dy": 0},  # Right breast
    {"x": 0, "y": 60, "dx": 0, "dy": 0},  # Belly button
]

# Define the motion for each point-light
def update_lights(t):
    angle = math.radians(t * 180 / DURATION)
    for i, light in enumerate(LIGHTS):
        if i == 0:  # Head
            light["x"] = 0
            light["y"] = -100 * math.cos(angle)
        elif i == 1:  # Left shoulder
            light["x"] = -20 * math.cos(angle)
            light["y"] = -80 * math.sin(angle)
        elif i == 2:  # Right shoulder
            light["x"] = 20 * math.cos(angle)
            light["y"] = -80 * math.sin(angle)
        elif i == 3:  # Left elbow
            light["x"] = -40 * math.cos(angle)
            light["y"] = 0 * math.sin(angle)
        elif i == 4:  # Right elbow
            light["x"] = 40 * math.cos(angle)
            light["y"] = 0 * math.sin(angle)
        elif i == 5:  # Left hand
            light["x"] = -60 * math.cos(angle)
            light["y"] = 80 * math.sin(angle)
        elif i == 6:  # Right hand
            light["x"] = 60 * math.cos(angle)
            light["y"] = 80 * math.sin(angle)
        elif i == 7:  # Hips
            light["x"] = 0
            light["y"] = 100 * math.cos(angle)
        elif i == 8:  # Left knee
            light["x"] = -20 * math.cos(angle)
            light["y"] = 120 * math.sin(angle)
        elif i == 9:  # Right knee
            light["x"] = 20 * math.cos(angle)
            light["y"] = 120 * math.sin(angle)
        elif i == 10:  # Left ankle
            light["x"] = -40 * math.cos(angle)
            light["y"] = 140 * math.sin(angle)
        elif i == 11:  # Right ankle
            light["x"] = 40 * math.cos(angle)
            light["y"] = 140 * math.sin(angle)
        elif i == 12:  # Left breast
            light["x"] = -10 * math.cos(angle)
            light["y"] = -40 * math.sin(angle)
        elif i == 13:  # Right breast
            light["x"] = 10 * math.cos(angle)
            light["y"] = -40 * math.sin(angle)
        elif i == 14:  # Belly button
            light["x"] = 0
            light["y"] = 60 * math.cos(angle)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Main animation loop
running = True
t = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the point-lights
    update_lights(t)

    # Draw the background and point-lights
    screen.fill(BACKGROUND_COLOR)
    for light in LIGHTS:
        pygame.draw.circle(screen, LIGHT_COLOR, (int(WIDTH / 2 + light["x"]), int(HEIGHT / 2 + light["y"])), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    # Increment the time
    t += 1 / FPS
    if t > DURATION:
        t = 0

# Quit Pygame
pygame.quit()
