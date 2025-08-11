
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling FPS
clock = pygame.time.Clock()
fps = 30

# Arm movement parameters
amplitude = math.radians(60)  # Swing angle in radians
frequency = 1                 # Oscillation frequency
upper_arm_length = 40
lower_arm_length = 30
elbow_bend = math.radians(45)  # Fixed elbow bend

# Body points relative to torso (dynamically updated)
torso_x, torso_y = width // 2, height // 2
body_points = {
    'head': (0, -100),
    'torso': (0, 0),
    'r_shoulder': (50, -30),
    'r_elbow': (0, 0),  # Updated dynamically
    'r_hand': (0, 0),   # Updated dynamically
    'l_shoulder': (-50, -30),
    'l_elbow': (-30, 0),
    'l_hand': (-50, 30),
    'hips': (0, 30),
    'r_hip': (20, 30),
    'r_knee': (20, 60),
    'r_foot': (20, 90),
    'l_hip': (-20, 30),
    'l_knee': (-20, 60),
    'l_foot': (-20, 90)
}

time_elapsed = 0.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    time_elapsed += 1/fps

    # Calculate arm dynamics
    theta = amplitude * math.sin(2 * math.pi * frequency * time_elapsed)
    phi = theta + elbow_bend

    # Update right arm positions
    rs_x, rs_y = body_points['r_shoulder']
    re_x = rs_x + upper_arm_length * math.sin(theta)
    re_y = rs_y + upper_arm_length * math.cos(theta)
    body_points['r_elbow'] = (re_x, re_y)
    
    rh_x = re_x + lower_arm_length * math.sin(phi)
    rh_y = re_y + lower_arm_length * math.cos(phi)
    body_points['r_hand'] = (rh_x, rh_y)

    # Add head bobbing
    body_points['head'] = (0, -100 + 5 * math.sin(2 * math.pi * 0.5 * time_elapsed))

    # Convert to screen coordinates and draw
    for point in body_points.values():
        x = torso_x + point[0]
        y = torso_y + point[1]
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
