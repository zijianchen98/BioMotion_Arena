
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_LIGHTS = 15
LIGHT_RADIUS = 4
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sad Man Running Animation")

# Define the skeleton structure
skeleton = [
    {"name": "head", "x": SCREEN_WIDTH // 2, "y": SCREEN_HEIGHT // 4},
    {"name": "torso", "x": SCREEN_WIDTH // 2, "y": SCREEN_HEIGHT // 2},
    {"name": "left_arm", "x": SCREEN_WIDTH // 2 - 50, "y": SCREEN_HEIGHT // 2},
    {"name": "right_arm", "x": SCREEN_WIDTH // 2 + 50, "y": SCREEN_HEIGHT // 2},
    {"name": "left_leg", "x": SCREEN_WIDTH // 2 - 50, "y": SCREEN_HEIGHT * 3 // 4},
    {"name": "right_leg", "x": SCREEN_WIDTH // 2 + 50, "y": SCREEN_HEIGHT * 3 // 4},
    {"name": "left_foot", "x": SCREEN_WIDTH // 2 - 70, "y": SCREEN_HEIGHT * 7 // 8},
    {"name": "right_foot", "x": SCREEN_WIDTH // 2 + 70, "y": SCREEN_HEIGHT * 7 // 8}
]

# Function to draw the skeleton
def draw_skeleton(frame):
    lights = []
    for i, joint in enumerate(skeleton):
        angle = math.sin(frame / 10.0 + i) * 10
        x = joint["x"] + int(math.cos(angle) * 20)
        y = joint["y"] + int(math.sin(angle) * 20)
        lights.append((x, y))
    
    screen.fill(BACKGROUND_COLOR)
    for light in lights:
        pygame.draw.circle(screen, LIGHT_COLOR, light, LIGHT_RADIUS)
    pygame.display.flip()

# Main loop
frame = 0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_skeleton(frame)
    frame += 1
    clock.tick(30)

pygame.quit()
sys.exit()
