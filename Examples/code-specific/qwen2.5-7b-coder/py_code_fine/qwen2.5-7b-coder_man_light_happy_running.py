
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Man Running Animation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define point lights
num_lights = 15
point_lights = []

for i in range(num_lights):
    angle = 2 * math.pi * i / num_lights
    x = width // 2 + 200 * math.cos(angle)
    y = height // 2 + 200 * math.sin(angle)
    point_lights.append([x, y])

# Define running parameters
speed = 5
angle_change = 0.05

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update point lights positions
    for i, (x, y) in enumerate(point_lights):
        angle = 2 * math.pi * i / num_lights
        speed_x = speed * math.cos(angle + pygame.time.get_ticks() * angle_change)
        speed_y = speed * math.sin(angle + pygame.time.get_ticks() * angle_change)
        point_lights[i] = [x + speed_x, y + speed_y]

        # Wrap around edges
        if x < -5 or x > width + 5:
            speed_x *= -1
        if y < -5 or y > height + 5:
            speed_y *= -1

        # Draw point lights
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 2)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
