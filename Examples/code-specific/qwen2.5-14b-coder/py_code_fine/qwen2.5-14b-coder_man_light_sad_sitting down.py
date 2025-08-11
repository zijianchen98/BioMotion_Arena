
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Sitting Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of point lights
NUM_LIGHTS = 15

# Sad man's body parts positions and sizes
body_parts = {
    "head": {"x": WIDTH // 2, "y": HEIGHT // 4, "radius": 20},
    "torso": {"x": WIDTH // 2, "y": HEIGHT // 2, "width": 30, "height": 50},
    "left_arm": {"x": WIDTH // 2 - 50, "y": HEIGHT // 2 + 10, "length": 40},
    "right_arm": {"x": WIDTH // 2 + 50, "y": HEIGHT // 2 + 10, "length": 40},
    "left_leg": {"x": WIDTH // 2 - 20, "y": HEIGHT // 2 + 50, "length": 60},
    "right_leg": {"x": WIDTH // 2 + 20, "y": HEIGHT // 2 + 50, "length": 60}
}

# Function to draw a body part
def draw_body_part(x, y, radius=None, width=None, height=None, length=None):
    if radius:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), radius)
    elif width and height:
        pygame.draw.rect(screen, WHITE, (int(x), int(y), width, height))
    elif length:
        pygame.draw.line(screen, WHITE, (int(x), int(y)), (int(x), int(y) + length), 5)

# Main loop
running = True
clock = pygame.time.Clock()
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate positions for point lights
    light_positions = []
    for i in range(NUM_LIGHTS):
        angle = math.radians(360 * i / NUM_LIGHTS)
        x = body_parts["head"]["x"] + 100 * math.cos(angle)
        y = body_parts["head"]["y"] + 100 * math.sin(angle)
        light_positions.append((x, y))

    # Draw body parts
    draw_body_part(body_parts["head"]["x"], body_parts["head"]["y"], radius=body_parts["head"]["radius"])
    draw_body_part(body_parts["torso"]["x"], body_parts["torso"]["y"], width=body_parts["torso"]["width"], height=body_parts["torso"]["height"])
    draw_body_part(body_parts["left_arm"]["x"], body_parts["left_arm"]["y"], length=body_parts["left_arm"]["length"])
    draw_body_part(body_parts["right_arm"]["x"], body_parts["right_arm"]["y"], length=body_parts["right_arm"]["length"])
    draw_body_part(body_parts["left_leg"]["x"], body_parts["left_leg"]["y"], length=body_parts["left_leg"]["length"])
    draw_body_part(body_parts["right_leg"]["x"], body_parts["right_leg"]["y"], length=body_parts["right_leg"]["length"])

    # Draw point lights
    for x, y in light_positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 3)

    pygame.display.flip()
    clock.tick(30)
    frame_count += 1

pygame.quit()
sys.exit()
