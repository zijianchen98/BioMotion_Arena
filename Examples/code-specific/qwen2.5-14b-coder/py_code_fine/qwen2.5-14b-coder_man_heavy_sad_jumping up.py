
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sad Man Jumping Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Point light properties
num_lights = 15
lights = []

# Sad man's initial position and size
man_x, man_y = width // 2, height - 100
man_width, man_height = 50, 100

# Jump parameters
jump_height = 150
gravity = 0.5
velocity = 0
is_jumping = False

# Function to create point lights
def create_lights():
    global lights
    lights = []
    for i in range(num_lights):
        angle = 2 * math.pi * i / num_lights
        x = man_x + man_width // 2 + int(math.cos(angle) * man_width // 2)
        y = man_y + man_height // 2 + int(math.sin(angle) * man_height // 2)
        lights.append((x, y))

# Main loop
running = True
clock = pygame.time.Clock()
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                velocity = -10

    # Update jump
    if is_jumping:
        man_y += velocity
        velocity += gravity
        if man_y >= height - man_height:
            man_y = height - man_height
            is_jumping = False

    # Create point lights based on man's position
    create_lights()

    # Clear screen
    screen.fill(black)

    # Draw point lights
    for light in lights:
        pygame.draw.circle(screen, white, light, 5)

    # Draw sad man
    pygame.draw.rect(screen, white, (man_x, man_y, man_width, man_height))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

    # Increment frame count
    frame_count += 1

# Quit Pygame
pygame.quit()
