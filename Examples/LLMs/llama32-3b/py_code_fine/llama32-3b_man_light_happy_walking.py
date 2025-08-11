
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen (width, height).
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Point-Light Animation")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Define the point-lights
point_lights = []
for i in range(15):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    point_lights.append([x, y])

# Define the action parameters
action_duration = 10  # seconds
action_step = 0.1  # seconds
num_steps = int(action_duration / action_step)

# Define the animation parameters
animation_speed = 0.1  # seconds
animation_step = 0.01  # seconds

# Animation variables
x_offset = 0
y_offset = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    screen.fill(BLACK)

    # Move the point-lights
    for i, (x, y) in enumerate(point_lights):
        # Calculate the angle and distance of the point-light from the camera
        angle = math.atan2(y - size[1] / 2, x - size[0] / 2)
        distance = math.sqrt((x - size[0] / 2) ** 2 + (y - size[1] / 2) ** 2)

        # Move the point-light based on the action parameters
        if action_step <= num_steps:
            x += math.cos(angle) * 10 * action_step
            y += math.sin(angle) * 10 * action_step
        else:
            x += math.cos(angle) * 10 * animation_step
            y += math.sin(angle) * 10 * animation_step

        # Limit the movement to the screen boundaries
        x = max(0, min(x, size[0]))
        y = max(0, min(y, size[1]))

        # Draw the point-light
        pygame.draw.circle(screen, WHITE, [int(x), int(y)], 2)

        # Update the animation variables
        x_offset += 0.1
        y_offset += 0.1

        # Draw a black circle at the center of the screen
        pygame.draw.circle(screen, BLACK, [size[0] / 2, size[1] / 2], 10)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
