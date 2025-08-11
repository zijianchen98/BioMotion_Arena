
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Forward Rolling")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Parameters for the rolling motion
center = (WIDTH // 2, HEIGHT // 3)
radius = 80  # Radius of the circle representing the man
num_lights = 15  # Number of point-lights
speed = 0.05  # Angular speed of rotation

# Define joint positions relative to center (approximating a man's body)
joints = [
    (0, -radius),       # Head
    (-radius // 2, 0),  # Torso left
    (radius // 2, 0),   # Torso right
    (-radius, radius // 2),  # Hips left
    (radius, radius // 2),   # Hips right
    (-radius // 2, radius),  # Left leg
    (radius // 2, radius)   # Right leg
]

def getLightPositions(time):
    positions = []
    angles = [2 * math.pi * i / num_lights for i in range(num_lights)]
    for angle in angles:
        # Forward rolling motion
        rotated_angle = angle + speed * time
        x = center[0] + radius * math.sin(rotated_angle)
        y = center[1] + radius * math.cos(rotated_angle)
        positions.append((x, y))
    return positions

def draw_joints(light_positions, time):
    # Rotate joints to simulate rolling
    rotated_joints = []
    for joint in joints:
        # Apply a rolling motion to joints
        angle_shift = speed * time
        rotated_x = center[0] + joint[0] * math.cos(angle_shift) - joint[1] * math.sin(angle_shift)
        rotated_y = center[1] + joint[0] * math.sin(angle_shift) + joint[1] * math.cos(angle_shift)
        rotated_joints.append((rotated_x, rotated_y))
    
    # Draw joints
    for pos in rotated_joints:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 3)
    
    # Draw connections between joints for better visualization
    connections = [
        (0, 1), (0, 2), (1, 3), (2, 3),  # Head, torso, hips
        (3, 4), (4, 5), (3, 6), (6, 5)   # Legs
    ]
    for start, end in connections:
        pygame.draw.line(screen, WHITE, rotated_joints[start], rotated_joints[end], 1)

# Main loop
clock = pygame.time.Clock()
time_elapsed = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)
    
    # Get current light positions based on time
    light_positions = getLightPositions(time_elapsed)
    
    # Draw the point-lights and joints
    draw_joints(light_positions, time_elapsed)
    
    # Update the display
    pygame.display.flip()
    
    # Increment time
    time_elapsed += 0.1
    
    # Control the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
