
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of point-lights
NUM_LIGHTS = 15

# Happy woman model parameters
# These are simplified and can be adjusted for better realism
body_parts = {
    "head": {"x": WIDTH // 2, "y": HEIGHT // 4, "radius": 20},
    "torso": {"x": WIDTH // 2, "y": HEIGHT // 2, "radius": 30},
    "arm_left": {"x": WIDTH // 2 - 50, "y": HEIGHT // 2, "length": 100},
    "arm_right": {"x": WIDTH // 2 + 50, "y": HEIGHT // 2, "length": 100},
    "leg_left": {"x": WIDTH // 2 - 30, "y": HEIGHT // 2 + 50, "length": 150},
    "leg_right": {"x": WIDTH // 2 + 30, "y": HEIGHT // 2 + 50, "length": 150}
}

# Angle for turning
angle = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update body part positions
    angle += 0.01  # Adjust this value for faster or slower turning
    body_parts["head"]["x"] = WIDTH // 2 + math.cos(angle) * 50
    body_parts["head"]["y"] = HEIGHT // 4 + math.sin(angle) * 50
    body_parts["torso"]["x"] = WIDTH // 2 + math.cos(angle) * 50
    body_parts["torso"]["y"] = HEIGHT // 2 + math.sin(angle) * 50
    body_parts["arm_left"]["x"] = body_parts["torso"]["x"] + math.cos(angle + math.pi / 4) * 50
    body_parts["arm_left"]["y"] = body_parts["torso"]["y"] + math.sin(angle + math.pi / 4) * 50
    body_parts["arm_right"]["x"] = body_parts["torso"]["x"] + math.cos(angle - math.pi / 4) * 50
    body_parts["arm_right"]["y"] = body_parts["torso"]["y"] + math.sin(angle - math.pi / 4) * 50
    body_parts["leg_left"]["x"] = body_parts["torso"]["x"] + math.cos(angle + math.pi / 4) * 70
    body_parts["leg_left"]["y"] = body_parts["torso"]["y"] + math.sin(angle + math.pi / 4) * 70
    body_parts["leg_right"]["x"] = body_parts["torso"]["x"] + math.cos(angle - math.pi / 4) * 70
    body_parts["leg_right"]["y"] = body_parts["torso"]["y"] + math.sin(angle - math.pi / 4) * 70

    # Draw point-lights
    for i in range(NUM_LIGHTS):
        x = int(body_parts["head"]["x"] + math.cos(angle + i * (2 * math.pi / NUM_LIGHTS)) * 30)
        y = int(body_parts["head"]["y"] + math.sin(angle + i * (2 * math.pi / NUM_LIGHTS)) * 30)
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
