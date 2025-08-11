
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Jump Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
num_lights = 15
lights = []

# Initial positions of the lights (simplified model)
initial_positions = [
    (100, 400), (120, 380), (140, 360), (160, 340), (180, 320),
    (200, 300), (220, 280), (240, 260), (260, 240), (280, 220),
    (300, 200), (320, 180), (340, 160), (360, 140), (380, 120)
]

# Initialize lights with initial positions
for pos in initial_positions:
    lights.append(pos)

# Jump parameters
jump_height = 200
gravity = 0.5
velocity = -10
frame_count = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update light positions
    if frame_count < 20:  # Ascent phase
        velocity += gravity
        for i in range(num_lights):
            new_y = lights[i][1] + velocity
            lights[i] = (lights[i][0], new_y)
    elif frame_count < 40:  # Descent phase
        velocity += gravity
        for i in range(num_lights):
            new_y = lights[i][1] + velocity
            lights[i] = (lights[i][0], new_y)
    else:
        frame_count = 0  # Reset for next jump

    # Increment frame count
    frame_count += 1

    # Clear screen
    screen.fill(BLACK)

    # Draw lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, light, 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
