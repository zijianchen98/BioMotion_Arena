
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_POINTS = 15
POINT_RADIUS = 5
POINT_COLOR = (255, 255, 255)  # White

# Animation properties
FPS = 60
DURATION = 5  # seconds

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define point-light positions for the sad man lying down
def get_point_positions(t):
    # Head
    head_x = WIDTH / 2
    head_y = HEIGHT / 2 - 100
    head_x += 10 * math.sin(2 * math.pi * t)  # slight movement

    # Body
    body_x = WIDTH / 2
    body_y = HEIGHT / 2

    # Arms
    arm1_x = body_x - 50
    arm1_y = body_y - 50
    arm1_x += 20 * math.sin(2 * math.pi * t)  # movement
    arm2_x = body_x + 50
    arm2_y = body_y - 50
    arm2_x -= 20 * math.sin(2 * math.pi * t)  # movement

    # Legs
    leg1_x = body_x - 30
    leg1_y = body_y + 50
    leg1_x += 15 * math.sin(2 * math.pi * t)  # movement
    leg2_x = body_x + 30
    leg2_y = body_y + 50
    leg2_x -= 15 * math.sin(2 * math.pi * t)  # movement

    # Weight
    weight_x = body_x
    weight_y = body_y + 100
    weight_x += 10 * math.sin(2 * math.pi * t)  # slight movement

    # Additional points for smooth movement
    points = [
        (head_x, head_y),
        (body_x, body_y),
        (arm1_x, arm1_y),
        (arm2_x, arm2_y),
        (leg1_x, leg1_y),
        (leg2_x, leg2_y),
        (weight_x, weight_y),
        (body_x - 20, body_y - 20),
        (body_x + 20, body_y - 20),
        (body_x - 20, body_y + 20),
        (body_x + 20, body_y + 20),
        (arm1_x - 10, arm1_y - 10),
        (arm2_x + 10, arm2_y - 10),
        (leg1_x - 10, leg1_y + 10),
        (leg2_x + 10, leg2_y + 10),
    ]
    return points

# Main animation loop
running = True
t = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with black
    screen.fill((0, 0, 0))

    # Draw point-lights
    points = get_point_positions(t)
    for point in points:
        pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), POINT_RADIUS)

    # Update display
    pygame.display.flip()

    # Cap framerate
    clock.tick(FPS)

    # Increment time
    t += 1 / FPS
    if t > DURATION:
        t = 0

# Quit Pygame
pygame.quit()
