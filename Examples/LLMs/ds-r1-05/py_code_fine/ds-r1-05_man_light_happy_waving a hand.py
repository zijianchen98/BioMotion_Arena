
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Clock to control frame rate
clock = pygame.time.Clock()

# Static points (13 points)
static_points = [
    (width/2, 100),  # Head
    (width/2, 150),  # Neck
    (width/2 - 30, 180),  # Left shoulder
    (width/2, 200), (width/2, 250), (width/2, 300),  # Torso (3 points)
    (width/2, 350),  # Hips
    # Left arm (shoulder, elbow, hand)
    (width/2 - 30, 180),
    (width/2 - 60, 210),
    (width/2 - 90, 240),
    # Legs (left hip, left foot; right hip, right foot)
    (width/2 - 30, 350),
    (width/2 - 30, 450),
    (width/2 + 30, 350),
    (width/2 + 30, 450),
    # Right shoulder (static)
    (width/2 + 30, 180)
]

# Parameters for right arm motion
shoulder_x, shoulder_y = width/2 + 30, 180  # Right shoulder position
L1 = 50  # Upper arm length
L2 = 40  # Forearm length
theta0 = math.pi / 4  # Initial angle (45 degrees)
amplitude = math.pi / 4  # Swing range
period = 1  # Animation period in seconds

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate current angle based on time
    current_time = pygame.time.get_ticks() / 1000  # Convert to seconds
    current_theta = theta0 + amplitude * math.sin(2 * math.pi * current_time / period)

    # Compute right elbow and hand positions
    elbow_x = shoulder_x + L1 * math.sin(current_theta)
    elbow_y = shoulder_y + L1 * math.cos(current_theta)
    hand_x = elbow_x + L2 * math.cos(current_theta)
    hand_y = elbow_y - L2 * math.sin(current_theta)

    # Dynamic points (right elbow and hand)
    dynamic_points = [(elbow_x, elbow_y), (hand_x, hand_y)]

    # Combine static and dynamic points
    all_points = static_points + dynamic_points

    # Draw
    screen.fill(black)
    for point in all_points:
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 5)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
