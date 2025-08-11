
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Happy Man Turning Around")

# Number of point lights
NUM_LIGHTS = 15

# Happy man's initial position and size
man_x = SCREEN_WIDTH // 2
man_y = SCREEN_HEIGHT // 2
man_radius = 30

# Point light positions
lights = []
for i in range(NUM_LIGHTS):
    angle = 2 * math.pi * i / NUM_LIGHTS
    x = man_x + man_radius * math.cos(angle)
    y = man_y + man_radius * math.sin(angle)
    lights.append((x, y))

# Rotation speed
rotation_speed = 0.02

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update point light positions
    new_lights = []
    for x, y in lights:
        # Rotate each point light around the center of the happy man
        dx = x - man_x
        dy = y - man_y
        new_x = man_x + dx * math.cos(rotation_speed) - dy * math.sin(rotation_speed)
        new_y = man_y + dx * math.sin(rotation_speed) + dy * math.cos(rotation_speed)
        new_lights.append((new_x, new_y))

    lights = new_lights

    # Draw the point lights
    for x, y in lights:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
