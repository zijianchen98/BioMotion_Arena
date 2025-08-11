
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Woman Sitting Down Animation")

# Define the woman's body parts positions
body_parts = {
    "head": (WIDTH // 2, HEIGHT // 4),
    "torso": (WIDTH // 2, HEIGHT // 2),
    "left_arm": (WIDTH // 2 - 50, HEIGHT // 2 - 30),
    "right_arm": (WIDTH // 2 + 50, HEIGHT // 2 - 30),
    "left_leg": (WIDTH // 2 - 30, HEIGHT // 2 + 50),
    "right_leg": (WIDTH // 2 + 30, HEIGHT // 2 + 50)
}

# Define the light positions based on body parts
light_positions = [
    (body_parts["head"][0] + 10 * math.cos(math.radians(angle)), body_parts["head"][1] + 10 * math.sin(math.radians(angle))) for angle in range(0, 360, 24)
] + [
    (body_parts["torso"][0] + 10 * math.cos(math.radians(angle)), body_parts["torso"][1] + 10 * math.sin(math.radians(angle))) for angle in range(0, 360, 24)
] + [
    (body_parts["left_arm"][0] + 10 * math.cos(math.radians(angle)), body_parts["left_arm"][1] + 10 * math.sin(math.radians(angle))) for angle in range(0, 360, 24)
] + [
    (body_parts["right_arm"][0] + 10 * math.cos(math.radians(angle)), body_parts["right_arm"][1] + 10 * math.sin(math.radians(angle))) for angle in range(0, 360, 24)
] + [
    (body_parts["left_leg"][0] + 10 * math.cos(math.radians(angle)), body_parts["left_leg"][1] + 10 * math.sin(math.radians(angle))) for angle in range(0, 360, 24)
] + [
    (body_parts["right_leg"][0] + 10 * math.cos(math.radians(angle)), body_parts["right_leg"][1] + 10 * math.sin(math.radians(angle))) for angle in range(0, 360, 24)
]

# Main loop
running = True
clock = pygame.time.Clock()
angle_offset = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    # Update light positions
    for i in range(NUM_LIGHTS):
        x, y = light_positions[i]
        angle = (i * 24 + angle_offset) % 360
        new_x = body_parts[list(body_parts.keys())[i // (NUM_LIGHTS // len(body_parts))]][0] + 10 * math.cos(math.radians(angle))
        new_y = body_parts[list(body_parts.keys())[i // (NUM_LIGHTS // len(body_parts))]][1] + 10 * math.sin(math.radians(angle))
        light_positions[i] = (new_x, new_y)
        pygame.draw.circle(screen, LIGHT_COLOR, (int(new_x), int(new_y)), 3)

    angle_offset += 1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
