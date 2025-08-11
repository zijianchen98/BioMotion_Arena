
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sad Man Walking Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
num_lights = 15
lights = []

# Initial positions and velocities for the lights
for i in range(num_lights):
    x = width // 2 + (i - num_lights // 2) * 10
    y = height // 2
    dx = 0
    dy = 0
    lights.append((x, y, dx, dy))

# Animation parameters
frame_count = 0
walk_speed = 2
leg_length = 50
arm_length = 30
torso_length = 40

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update positions
    frame_count += 1
    time = frame_count / 60.0

    # Calculate leg movement
    left_leg_angle = math.sin(time * 4) * 10
    right_leg_angle = math.sin(time * 4 + math.pi) * 10

    # Calculate arm movement
    left_arm_angle = math.sin(time * 4 + math.pi / 2) * 10
    right_arm_angle = math.sin(time * 4 - math.pi / 2) * 10

    # Update light positions
    for i, (x, y, dx, dy) in enumerate(lights):
        if i == 0:  # Torso
            x = width // 2 + walk_speed * math.sin(time)
            y = height // 2 + torso_length * math.cos(time)
        elif i == 1:  # Head
            x = width // 2 + walk_speed * math.sin(time)
            y = height // 2 - torso_length * math.cos(time) - 20
        elif i == 2:  # Left Shoulder
            x = width // 2 + walk_speed * math.sin(time) - 20
            y = height // 2 - torso_length * math.cos(time) + 10
        elif i == 3:  # Right Shoulder
            x = width // 2 + walk_speed * math.sin(time) + 20
            y = height // 2 - torso_length * math.cos(time) + 10
        elif i == 4:  # Left Elbow
            x = width // 2 + walk_speed * math.sin(time) - 20 + arm_length * math.sin(left_arm_angle)
            y = height // 2 - torso_length * math.cos(time) + 10 - arm_length * math.cos(left_arm_angle)
        elif i == 5:  # Right Elbow
            x = width // 2 + walk_speed * math.sin(time) + 20 + arm_length * math.sin(right_arm_angle)
            y = height // 2 - torso_length * math.cos(time) + 10 - arm_length * math.cos(right_arm_angle)
        elif i == 6:  # Left Hand
            x = width // 2 + walk_speed * math.sin(time) - 20 + arm_length * math.sin(left_arm_angle) - 10
            y = height // 2 - torso_length * math.cos(time) + 10 - arm_length * math.cos(left_arm_angle) - 10
        elif i == 7:  # Right Hand
            x = width // 2 + walk_speed * math.sin(time) + 20 + arm_length * math.sin(right_arm_angle) + 10
            y = height // 2 - torso_length * math.cos(time) + 10 - arm_length * math.cos(right_arm_angle) - 10
        elif i == 8:  # Left Hip
            x = width // 2 + walk_speed * math.sin(time) - 20
            y = height // 2 + torso_length * math.cos(time) + 10
        elif i == 9:  # Right Hip
            x = width // 2 + walk_speed * math.sin(time) + 20
            y = height // 2 + torso_length * math.cos(time) + 10
        elif i == 10:  # Left Knee
            x = width // 2 + walk_speed * math.sin(time) - 20 + leg_length * math.sin(left_leg_angle)
            y = height // 2 + torso_length * math.cos(time) + 10 + leg_length * math.cos(left_leg_angle)
        elif i == 11:  # Right Knee
            x = width // 2 + walk_speed * math.sin(time) + 20 + leg_length * math.sin(right_leg_angle)
            y = height // 2 + torso_length * math.cos(time) + 10 + leg_length * math.cos(right_leg_angle)
        elif i == 12:  # Left Foot
            x = width // 2 + walk_speed * math.sin(time) - 20 + leg_length * math.sin(left_leg_angle) - 10
            y = height // 2 + torso_length * math.cos(time) + 10 + leg_length * math.cos(left_leg_angle) + 10
        elif i == 13:  # Right Foot
            x = width // 2 + walk_speed * math.sin(time) + 20 + leg_length * math.sin(right_leg_angle) + 10
            y = height // 2 + torso_length * math.cos(time) + 10 + leg_length * math.cos(right_leg_angle) + 10
        elif i == 14:  # Center of Mass
            x = width // 2 + walk_speed * math.sin(time)
            y = height // 2 + torso_length * math.cos(time)

        lights[i] = (x, y, dx, dy)

    # Draw lights
    for x, y, dx, dy in lights:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 3)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
