
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the point-lights for the sadman
lights = [
    {'x': 0, 'y': 0, 'dx': 0, 'dy': 0},  # Head
    {'x': -20, 'y': -50, 'dx': 0, 'dy': 0},  # Left shoulder
    {'x': 20, 'y': -50, 'dx': 0, 'dy': 0},  # Right shoulder
    {'x': -30, 'y': -100, 'dx': 0, 'dy': 0},  # Left elbow
    {'x': 30, 'y': -100, 'dx': 0, 'dy': 0},  # Right elbow
    {'x': -40, 'y': -150, 'dx': 0, 'dy': 0},  # Left wrist
    {'x': 40, 'y': -150, 'dx': 0, 'dy': 0},  # Right wrist
    {'x': 0, 'y': -200, 'dx': 0, 'dy': 0},  # Spine
    {'x': -20, 'y': -250, 'dx': 0, 'dy': 0},  # Left hip
    {'x': 20, 'y': -250, 'dx': 0, 'dy': 0},  # Right hip
    {'x': -30, 'y': -300, 'dx': 0, 'dy': 0},  # Left knee
    {'x': 30, 'y': -300, 'dx': 0, 'dy': 0},  # Right knee
    {'x': -40, 'y': -350, 'dx': 0, 'dy': 0},  # Left ankle
    {'x': 40, 'y': -350, 'dx': 0, 'dy': 0},  # Right ankle
    {'x': 0, 'y': -50, 'dx': 0, 'dy': 0},  # Weight
]

# Set up the animation parameters
jump_height = 100
jump_duration = 1000  # milliseconds
weight_offset = 20

# Main loop
clock = pygame.time.Clock()
running = True
jump_start_time = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the current time
    current_time = pygame.time.get_ticks() - jump_start_time

    # Calculate the vertical offset for the jump
    if current_time < jump_duration / 2:
        vertical_offset = -jump_height * (current_time / (jump_duration / 2))
    elif current_time < jump_duration:
        vertical_offset = -jump_height * (1 - (current_time - jump_duration / 2) / (jump_duration / 2))
    else:
        vertical_offset = 0

    # Update the lights
    for i, light in enumerate(lights):
        if i == 0:  # Head
            light['x'] = WIDTH / 2
            light['y'] = HEIGHT / 2 + vertical_offset
        elif i == 1:  # Left shoulder
            light['x'] = WIDTH / 2 - 20
            light['y'] = HEIGHT / 2 - 50 + vertical_offset
        elif i == 2:  # Right shoulder
            light['x'] = WIDTH / 2 + 20
            light['y'] = HEIGHT / 2 - 50 + vertical_offset
        elif i == 3:  # Left elbow
            light['x'] = WIDTH / 2 - 30
            light['y'] = HEIGHT / 2 - 100 + vertical_offset
        elif i == 4:  # Right elbow
            light['x'] = WIDTH / 2 + 30
            light['y'] = HEIGHT / 2 - 100 + vertical_offset
        elif i == 5:  # Left wrist
            light['x'] = WIDTH / 2 - 40
            light['y'] = HEIGHT / 2 - 150 + vertical_offset
        elif i == 6:  # Right wrist
            light['x'] = WIDTH / 2 + 40
            light['y'] = HEIGHT / 2 - 150 + vertical_offset
        elif i == 7:  # Spine
            light['x'] = WIDTH / 2
            light['y'] = HEIGHT / 2 - 200 + vertical_offset
        elif i == 8:  # Left hip
            light['x'] = WIDTH / 2 - 20
            light['y'] = HEIGHT / 2 - 250 + vertical_offset
        elif i == 9:  # Right hip
            light['x'] = WIDTH / 2 + 20
            light['y'] = HEIGHT / 2 - 250 + vertical_offset
        elif i == 10:  # Left knee
            light['x'] = WIDTH / 2 - 30
            light['y'] = HEIGHT / 2 - 300 + vertical_offset
        elif i == 11:  # Right knee
            light['x'] = WIDTH / 2 + 30
            light['y'] = HEIGHT / 2 - 300 + vertical_offset
        elif i == 12:  # Left ankle
            light['x'] = WIDTH / 2 - 40
            light['y'] = HEIGHT / 2 - 350 + vertical_offset
        elif i == 13:  # Right ankle
            light['x'] = WIDTH / 2 + 40
            light['y'] = HEIGHT / 2 - 350 + vertical_offset
        elif i == 14:  # Weight
            light['x'] = WIDTH / 2
            light['y'] = HEIGHT / 2 - 50 + vertical_offset + weight_offset

    # Draw everything
    screen.fill(BLACK)
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light['x']), int(light['y'])), 5)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
