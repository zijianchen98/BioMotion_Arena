
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Parameters for the running woman
radius = 50  #_radius of the circle representing the woman_
center = [WIDTH // 2, HEIGHT // 2]  # starting center of the circle
angle = 0  # initial angle
speed = 0.02  # angular speed for running
leg_length = 30  # length of the legs visualized by point-lights
arm_length = 30  # length of the arms visualized by point-lights

# Function to get the position of a point-light based on angle and length
def get_position(angle, length, offset):
    x = center[0] + offset + length * math.cos(angle)
    y = center[1] + length * math.sin(angle)
    return (int(x), int(y))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update the angle for running motion
    angle += speed

    # Draw the 15 point-lights representing the woman
    for i in range(15):
        # Calculate positions for legs, arms, and the torso based on the angle
        leg_angle = angle + (i / 3) * (math.pi / 4)  # Spread legs and arms
        arm_angle = angle - (i / 3) * (math.pi / 4)  # Spread legs and arms
        leg_pos = get_position(leg_angle, leg_length, 0)
        arm_pos = get_position(arm_angle, arm_length, 50)
        
        # Draw point-lights (legs and arms)
        pygame.draw.circle(screen, WHITE, leg_pos, 3)
        pygame.draw.circle(screen, WHITE, arm_pos, 3)
        
        # Draw point-light for the torso
        torso_pos = get_position(angle, radius, 50)
        pygame.draw.circle(screen, WHITE, torso_pos, 5)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
