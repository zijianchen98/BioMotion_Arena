
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion: Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Body parameters
torso_length = 50
shoulder_width = 40
upper_arm = 35
lower_arm = 30
thigh_length = 45
shin_length = 40

# Point configuration: (base_x, base_y, amp_x, amp_y, phase)
points_config = [
    # Head
    (0, -torso_length, 0, 5, 0),
    # Left shoulder
    (-shoulder_width/2, -torso_length, 15, 25, 0.2),
    # Right shoulder
    (shoulder_width/2, -torso_length, 15, 25, 0.2),
    # Left elbow
    (-shoulder_width/2-upper_arm, -torso_length, 20, 35, 0.3),
    # Right elbow
    (shoulder_width/2+upper_arm, -torso_length, 20, 35, 0.3),
    # Left hand
    (-shoulder_width/2-upper_arm-lower_arm, -torso_length, 25, 40, 0.4),
    # Right hand
    (shoulder_width/2+upper_arm+lower_arm, -torso_length, 25, 40, 0.4),
    # Left hip
    (-15, 0, 10, 20, 0.5),
    # Right hip
    (15, 0, 10, 20, 0.5),
    # Left knee
    (-15, thigh_length, 15, 30, 0.6),
    # Right knee
    (15, thigh_length, 15, 30, 0.6),
    # Left ankle
    (-15, thigh_length+shin_length, 20, 35, 0.7),
    # Right ankle
    (15, thigh_length+shin_length, 20, 35, 0.7),
    # Left foot
    (-25, thigh_length+shin_length, 25, 40, 0.8),
    # Right foot
    (25, thigh_length+shin_length, 25, 40, 0.8)
]

# Animation parameters
jump_duration = 1.5
forward_speed = 120
amplitude = 60
hip_start_x = 100
hip_start_y = height//2 + 100  # Lower start for heavier figure

clock = pygame.time.Clock()
time_elapsed = 0

def calculate_position(hip_x, hip_y, t, config):
    points = []
    for (base_x, base_y, amp_x, amp_y, phase) in config:
        angle = 2 * math.pi * (t + phase)
        x = hip_x + base_x + amp_x * math.sin(angle)
        y = hip_y + base_y - amp_y * abs(math.cos(angle))  # More mechanical movement
        points.append((int(x), int(y)))
    return points

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000.0
    time_elapsed += dt
    t = (time_elapsed % jump_duration) / jump_duration

    # Hip trajectory (parabolic)
    hip_x = hip_start_x + forward_speed * time_elapsed
    hip_y = hip_start_y - amplitude * (1 - (2*t - 1)**2)  # Parabolic curve

    # Calculate points
    point_positions = calculate_position(hip_x, hip_y, t, points_config)

    # Draw
    screen.fill(BLACK)
    for pos in point_positions:
        pygame.draw.circle(screen, WHITE, pos, 6)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
