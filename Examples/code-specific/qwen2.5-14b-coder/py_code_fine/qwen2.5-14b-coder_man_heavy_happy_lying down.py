
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Man Lying Down Animation")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Define the body parts and their initial positions
body_parts = {
    "head": [400, 150],
    "torso": [400, 250],
    "left_arm": [300, 200],
    "right_arm": [500, 200],
    "left_leg": [350, 350],
    "right_leg": [450, 350]
}

# Function to draw the point lights
def draw_lights(positions):
    screen.fill(BACKGROUND_COLOR)
    for pos in positions:
        pygame.draw.circle(screen, LIGHT_COLOR, pos, 5)
    pygame.display.flip()

# Main loop
running = True
frame_count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update positions based on frame count
    for part, pos in body_parts.items():
        if part == "head":
            pos[1] = 150 + 10 * math.sin(frame_count * 0.1)
        elif part == "torso":
            pos[1] = 250 + 5 * math.sin(frame_count * 0.1)
        elif part == "left_arm":
            pos[0] = 300 + 10 * math.cos(frame_count * 0.1)
            pos[1] = 200 + 5 * math.sin(frame_count * 0.1)
        elif part == "right_arm":
            pos[0] = 500 - 10 * math.cos(frame_count * 0.1)
            pos[1] = 200 + 5 * math.sin(frame_count * 0.1)
        elif part == "left_leg":
            pos[0] = 350 + 10 * math.cos(frame_count * 0.1)
            pos[1] = 350 + 5 * math.sin(frame_count * 0.1)
        elif part == "right_leg":
            pos[0] = 450 - 10 * math.cos(frame_count * 0.1)
            pos[1] = 350 + 5 * math.sin(frame_count * 0.1)

    # Calculate light positions
    light_positions = []
    for i in range(NUM_LIGHTS):
        angle = 2 * math.pi * i / NUM_LIGHTS
        x = WIDTH // 2 + 100 * math.cos(angle)
        y = HEIGHT // 2 + 100 * math.sin(angle)
        light_positions.append([x, y])

    # Draw the lights
    draw_lights(light_positions)

    # Increment frame count
    frame_count += 1

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
