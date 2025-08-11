
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Torso base position (center of screen)
torso_x, torso_y = width // 2, height // 2

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    current_time = pygame.time.get_ticks() / 1000  # Current time in seconds

    # Torso sway parameters
    sway_frequency = 1
    sway_amplitude = 5
    torso_shift = sway_amplitude * math.sin(2 * math.pi * sway_frequency * current_time)
    current_torso_x = torso_x + torso_shift

    # Right arm parameters
    upper_arm_length = 40
    forearm_length = 30
    theta_0 = math.radians(30)
    delta_theta = math.radians(30)
    arm_frequency = 1

    theta = theta_0 + delta_theta * math.sin(2 * math.pi * arm_frequency * current_time)

    # Right shoulder position
    right_shoulder_x = current_torso_x + 40
    right_shoulder_y = torso_y

    # Calculate elbow and hand positions
    right_elbow_x = right_shoulder_x + upper_arm_length * math.sin(theta)
    right_elbow_y = right_shoulder_y + upper_arm_length * math.cos(theta)
    right_hand_x = right_elbow_x + forearm_length * math.cos(theta)
    right_hand_y = right_elbow_y - forearm_length * math.sin(theta)

    # Define all 15 points
    points = [
        (current_torso_x, torso_y - 50),         # Head
        (current_torso_x, torso_y - 25),         # Neck
        (current_torso_x - 40, torso_y),         # Left shoulder
        (right_shoulder_x, right_shoulder_y),    # Right shoulder
        (current_torso_x - 60, torso_y + 30),    # Left elbow
        (right_elbow_x, right_elbow_y),          # Right elbow
        (current_torso_x - 80, torso_y + 60),    # Left hand
        (right_hand_x, right_hand_y),            # Right hand
        (current_torso_x - 30, torso_y + 100),   # Left hip
        (current_torso_x + 30, torso_y + 100),   # Right hip
        (current_torso_x - 40, torso_y + 150),   # Left knee
        (current_torso_x + 40, torso_y + 150),   # Right knee
        (current_torso_x - 50, torso_y + 200),   # Left foot
        (current_torso_x + 50, torso_y + 200),   # Right foot
        (current_torso_x, torso_y)               # Torso
    ]

    # Draw all points
    for point in points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 5)

    pygame.display.flip()
    clock.tick(30)
