
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sad Man Jumping Forward")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Point light properties
num_lights = 15
lights = []
for i in range(num_lights):
    angle = math.radians(360 / num_lights * i)
    x = width // 2 + 100 * math.cos(angle)
    y = height // 2 + 100 * math.sin(angle)
    lights.append((x, y))

# Animation parameters
gravity = 0.5
jump_height = 100
jump_duration = 100
frame_count = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update lights position
    if frame_count < jump_duration:
        t = frame_count / jump_duration
        vertical_offset = -jump_height * (t - t**2)
        for i in range(num_lights):
            angle = math.radians(360 / num_lights * i)
            x = width // 2 + 100 * math.cos(angle)
            y = height // 2 + 100 * math.sin(angle) + vertical_offset
            lights[i] = (x, y)
    else:
        for i in range(num_lights):
            angle = math.radians(360 / num_lights * i)
            x = width // 2 + 100 * math.cos(angle)
            y = height // 2 + 100 * math.sin(angle)
            lights[i] = (x, y)

    # Clear screen
    screen.fill(black)

    # Draw lights
    for light in lights:
        pygame.draw.circle(screen, white, light, 5)

    # Update display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

    # Increment frame count
    frame_count += 1

# Quit Pygame
pygame.quit()
