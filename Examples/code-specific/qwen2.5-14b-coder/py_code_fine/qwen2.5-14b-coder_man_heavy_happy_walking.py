
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Man Walking Animation")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Function to calculate light positions for walking animation
def get_light_positions(frame):
    positions = []
    step_length = 5
    leg_length = 40
    arm_length = 30
    head_radius = 10
    body_width = 20
    body_height = 50

    # Calculate body position
    x = (frame % (WIDTH + step_length)) - step_length
    y = HEIGHT - body_height - head_radius

    # Calculate leg positions
    leg_angle = math.sin(frame * 0.1) * 0.5
    left_leg_x = x + body_width / 2 - leg_length * math.cos(leg_angle)
    left_leg_y = y + body_height - leg_length * math.sin(leg_angle)
    right_leg_x = x + body_width / 2 + leg_length * math.cos(leg_angle)
    right_leg_y = y + body_height - leg_length * math.sin(leg_angle)

    # Calculate arm positions
    arm_angle = math.sin(frame * 0.1 + math.pi) * 0.5
    left_arm_x = x + body_width / 2 - arm_length * math.cos(arm_angle)
    left_arm_y = y + body_height / 2 - arm_length * math.sin(arm_angle)
    right_arm_x = x + body_width / 2 + arm_length * math.cos(arm_angle)
    right_arm_y = y + body_height / 2 - arm_length * math.sin(arm_angle)

    # Calculate head position
    head_x = x + body_width / 2
    head_y = y - head_radius

    # Add all positions to the list
    positions.append((head_x, head_y))
    positions.append((left_leg_x, left_leg_y))
    positions.append((right_leg_x, right_leg_y))
    positions.append((left_arm_x, left_arm_y))
    positions.append((right_arm_x, right_arm_y))

    # Add more lights to fill up to 15
    while len(positions) < NUM_LIGHTS:
        positions.append((x + body_width / 2, y + body_height / 2))

    return positions

# Main loop
frame = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BACKGROUND_COLOR)

    # Get current light positions
    light_positions = get_light_positions(frame)

    # Draw lights
    for pos in light_positions:
        pygame.draw.circle(screen, LIGHT_COLOR, pos, 5)

    # Update display
    pygame.display.flip()

    # Increment frame
    frame += 1

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
