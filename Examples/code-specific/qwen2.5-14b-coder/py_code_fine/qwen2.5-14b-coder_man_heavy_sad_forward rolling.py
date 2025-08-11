
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point light properties
num_lights = 15
lights = []

# Sadman's body parts positions
body_parts = {
    "head": (400, 150),
    "torso": (400, 250),
    "left_arm": (350, 200),
    "right_arm": (450, 200),
    "left_leg": (375, 300),
    "right_leg": (425, 300)
}

# Function to calculate point lights based on body parts
def calculate_lights(body_parts):
    lights.clear()
    for part, position in body_parts.items():
        angle = math.radians(360 / num_lights)
        for i in range(num_lights):
            x = position[0] + 20 * math.cos(angle * i)
            y = position[1] + 20 * math.sin(angle * i)
            lights.append((x, y))

# Initial calculation of point lights
calculate_lights(body_parts)

# Animation loop
running = True
clock = pygame.time.Clock()
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update body parts positions for forward rolling motion
    for part in body_parts:
        if part == "head":
            body_parts[part] = (400 + 5 * math.sin(frame_count * 0.1), 150 + 5 * math.cos(frame_count * 0.1))
        elif part == "torso":
            body_parts[part] = (400 + 5 * math.sin(frame_count * 0.1), 250 + 5 * math.cos(frame_count * 0.1))
        elif part == "left_arm":
            body_parts[part] = (350 + 5 * math.sin(frame_count * 0.1), 200 + 5 * math.cos(frame_count * 0.1))
        elif part == "right_arm":
            body_parts[part] = (450 + 5 * math.sin(frame_count * 0.1), 200 + 5 * math.cos(frame_count * 0.1))
        elif part == "left_leg":
            body_parts[part] = (375 + 5 * math.sin(frame_count * 0.1), 300 + 5 * math.cos(frame_count * 0.1))
        elif part == "right_leg":
            body_parts[part] = (425 + 5 * math.sin(frame_count * 0.1), 300 + 5 * math.cos(frame_count * 0.1))

    # Recalculate point lights
    calculate_lights(body_parts)

    # Draw background
    screen.fill(BLACK)

    # Draw point lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, light, 3)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

    # Increment frame count
    frame_count += 1

# Quit Pygame
pygame.quit()
