
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Happy Man Jumping Forward")

# Define the number of point-lights
NUM_LIGHTS = 15

# Define the initial positions of the point-lights
lights = []
for i in range(NUM_LIGHTS):
    x = SCREEN_WIDTH // 2 + (i - NUM_LIGHTS // 2) * 10
    y = SCREEN_HEIGHT // 2
    lights.append([x, y])

# Define the jump parameters
JUMP_HEIGHT = 100
JUMP_DURATION = 60  # Frames
GRAVITY = 9.8 / JUMP_DURATION ** 2

# Define the frame rate
FPS = 60
clock = pygame.time.Clock()

# Main loop
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update the positions of the point-lights
    if frame < JUMP_DURATION:
        t = frame / JUMP_DURATION
        displacement = JUMP_HEIGHT * (t - t**2)
        for light in lights:
            light[1] = SCREEN_HEIGHT // 2 - displacement
    else:
        for light in lights:
            light[1] = SCREEN_HEIGHT // 2

    # Draw the point-lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light[0]), int(light[1])), 5)

    # Update the display
    pygame.display.flip()

    # Increment the frame counter
    frame += 1
    if frame >= 2 * JUMP_DURATION:
        frame = 0

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
