
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Central point for the animation
center_x, center_y = width // 2, height // 2

# Define joint parameters for 15 points
joints = [
    # Head (1)
    {'radius': 0, 'y_offset': -70, 'phase': 0, 'swing_amp': 0, 'swing_phase': 0},
    # Left Shoulder (2)
    {'radius': 40, 'y_offset': -40, 'phase': 0, 'swing_amp': 3, 'swing_phase': 0},
    # Right Shoulder (3)
    {'radius': 40, 'y_offset': -40, 'phase': math.pi, 'swing_amp': 3, 'swing_phase': 0},
    # Left Elbow (4)
    {'radius': 60, 'y_offset': -20, 'phase': math.pi/2, 'swing_amp': 5, 'swing_phase': 0},
    # Right Elbow (5)
    {'radius': 60, 'y_offset': -20, 'phase': 3*math.pi/2, 'swing_amp': 5, 'swing_phase': 0},
    # Left Hand (6)
    {'radius': 80, 'y_offset': 0, 'phase': math.pi, 'swing_amp': 7, 'swing_phase': 0},
    # Right Hand (7)
    {'radius': 80, 'y_offset': 0, 'phase': 0, 'swing_amp': 7, 'swing_phase': 0},
    # Chest (8)
    {'radius': 0, 'y_offset': -50, 'phase': 0, 'swing_amp': 0, 'swing_phase': 0},
    # Left Hip (9)
    {'radius': 35, 'y_offset': 10, 'phase': 0, 'swing_amp': 10, 'swing_phase': 0},
    # Right Hip (10)
    {'radius': 35, 'y_offset': 10, 'phase': math.pi, 'swing_amp': 10, 'swing_phase': math.pi},
    # Left Knee (11)
    {'radius': 50, 'y_offset': 50, 'phase': math.pi/2, 'swing_amp': 15, 'swing_phase': 0},
    # Right Knee (12)
    {'radius': 50, 'y_offset': 50, 'phase': 3*math.pi/2, 'swing_amp': 15, 'swing_phase': math.pi},
    # Left Foot (13)
    {'radius': 60, 'y_offset': 90, 'phase': math.pi, 'swing_amp': 20, 'swing_phase': 0},
    # Right Foot (14)
    {'radius': 60, 'y_offset': 90, 'phase': 0, 'swing_amp': 20, 'swing_phase': math.pi},
    # Mid-Hips (15)
    {'radius': 0, 'y_offset': 20, 'phase': 0, 'swing_amp': 0, 'swing_phase': 0},
]

# Main animation loop
angle = 0
swing_angle = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Update motion parameters
    angle += 0.03  # Rotation speed
    swing_angle += 0.15  # Limb movement speed

    # Draw all joints
    for joint in joints:
        # Calculate dynamic position
        x = center_x + joint['radius'] * math.cos(angle + joint['phase'])
        y = center_y + joint['y_offset'] + joint['swing_amp'] * math.sin(swing_angle + joint['swing_phase'])
        
        # Draw white point-light
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
sys.exit()
