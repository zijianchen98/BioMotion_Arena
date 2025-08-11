
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sadman Bowing Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of point-lights
num_lights = 15

# Initialize point-lights
lights = []
for _ in range(num_lights):
    x = random.randint(0, width)
    y = random.randint(0, height)
    speed_x = random.uniform(-1, 1)
    speed_y = random.uniform(-1, 1)
    lights.append([x, y, speed_x, speed_y])

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update and draw point-lights
    for i, (x, y, speed_x, speed_y) in enumerate(lights):
        # Move point-light
        x += speed_x
        y += speed_y
        
        # Bounce off walls
        if x <= 0 or x >= width:
            speed_x = -speed_x
        if y <= 0 or y >= height:
            speed_y = -speed_y
        
        # Draw point-light
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 2)
        
        # Update position
        lights[i] = [x, y, speed_x, speed_y]

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
