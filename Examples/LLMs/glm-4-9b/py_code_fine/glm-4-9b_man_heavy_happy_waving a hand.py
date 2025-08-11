
import pygame
import math
import numpy as np

# Initialize pygame
pygame.init()

# Set up the display
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Point-Light Stimulus Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Parameters for the animation
num_lights = 15
hand_wave_speed = 0.05
hand_wave_amplitude = 100
person_height = 150
person_position = np.array([width // 2, height // 2])

# Define the positions of the point-lights on the person
light_positions = [
    [person_position[0] - 50, person_position[1] + 50],  # Head
    [person_position[0] - 30, person_position[1] + 100], # Left shoulder
    [person_position[0], person_position[1] + 100],     # Torso
    [person_position[0] + 30, person_position[1] + 100], # Right shoulder
    [person_position[0] - 40, person_position[1] + 150], # Left elbow
    [person_position[0], person_position[1] + 150],     # Right elbow
    [person_position[0] - 40, person_position[1] + 200], # Left hand
    [person_position[0], person_position[1] + 200],     # Right hand
    [person_position[0] + 40, person_position[1] + 200], # Right hand waved
    [person_position[0] - 40, person_position[1] + 250], # Left knee
    [person_position[0], person_position[1] + 250],     # Right knee
    [person_position[0] - 40, person_position[1] + 300], # Left ankle
    [person_position[0], person_position[1] + 300],     # Right ankle
    [person_position[0] - 20, person_position[1] + 350], # Left foot
    [person_position[0], person_position[1] + 350]      # Right foot
]

# Time variable for the wave motion
t = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate the new positions for the hand wave
    right_hand_index = 7
    left_hand_index = 6
    new_right_hand_x = light_positions[right_hand_index][0] + math.sin(t) * hand_wave_amplitude
    new_left_hand_x = light_positions[left_hand_index][0] - math.sin(t) * hand_wave_amplitude
    light_positions[right_hand_index][0] = new_right_hand_x
    light_positions[left_hand_index][0] = new_left_hand_x

    # Draw the point-lights
    for pos in light_positions:
        pygame.draw.circle(screen, WHITE, pos, 5)

    # Update the display
    pygame.display.flip()

    # Increment the time variable
    t += hand_wave_speed

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
