
import pygame
from math import sin, cos, pi

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Waving Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Parameters
scale = 150
margin = 50
L1 = 0.5  # Upper arm length
L2 = 0.5  # Forearm length
A_shoulder = 20 * pi / 180  # Amplitude for shoulder angle
A_elbow = 30 * pi / 180  # Amplitude for elbow angle
omega = 2 * pi / 1.0  # Angular frequency for 1 second period

# Define fixed points' local positions
points = [
    (0, 0),  # 0 head
    (-0.5, 0.5),  # 1 left shoulder
    (0.5, 0.5),  # 2 right shoulder
    (-0.5, 1.0),  # 3 left elbow
    (0.5, 1.0),  # 4 right elbow initial
    (-0.5, 1.5),  # 5 left wrist
    (0.5, 1.5),  # 6 right wrist initial
    (-0.3, 2.0),  # 7 left hip
    (0.3, 2.0),  # 8 right hip
    (-0.3, 2.5),  # 9 left knee
    (0.3, 2.5),  # 10 right knee
    (-0.3, 3.0),  # 11 left ankle
    (0.3, 3.0),  # 12 right ankle
    (-0.3, 3.2),  # 13 left foot
    (0.3, 3.2),  # 14 right foot
]

# Function to convert local coordinates to screen coordinates
def local_to_screen(x, y):
    screen_x = width / 2 + x * scale
    screen_y = margin + y * scale
    return (int(screen_x), int(screen_y))

# Set up the clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get current time in seconds
    t = pygame.time.get_ticks() / 1000.0
    
    # Compute angles
    theta_shoulder = pi / 2 + A_shoulder * sin(omega * t)
    theta_elbow = A_elbow * sin(omega * t)
    
    # Compute right elbow and wrist positions
    shoulder_x, shoulder_y = points[2]  # right shoulder
    elbow_x = shoulder_x + L1 * cos(theta_shoulder)
    elbow_y = shoulder_y + L1 * sin(theta_shoulder)
    wrist_x = elbow_x + L2 * cos(theta_shoulder + theta_elbow)
    wrist_y = elbow_y + L2 * sin(theta_shoulder + theta_elbow)
    
    # Update points
    points[4] = (elbow_x, elbow_y)
    points[6] = (wrist_x, wrist_y)
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw all points
    for point in points:
        screen_point = local_to_screen(point[0], point[1])
        pygame.draw.circle(screen, WHITE, screen_point, 5)
    
    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
