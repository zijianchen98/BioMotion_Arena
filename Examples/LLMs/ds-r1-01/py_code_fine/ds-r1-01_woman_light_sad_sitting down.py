
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()
bg_color = (0, 0, 0)
point_color = (255, 255, 255)
point_radius = 5

# Define point configurations
points = [
    # Head
    {'initial_x': 400, 'initial_y': 100, 'target_x': 400, 'target_y': 150, 'phase': 0.0},
    # Neck
    {'initial_x': 400, 'initial_y': 120, 'target_x': 400, 'target_y': 170, 'phase': 0.1},
    # Left Shoulder
    {'initial_x': 370, 'initial_y': 130, 'target_x': 360, 'target_y': 180, 'phase': 0.2},
    # Right Shoulder
    {'initial_x': 430, 'initial_y': 130, 'target_x': 440, 'target_y': 180, 'phase': 0.2},
    # Left Elbow
    {'initial_x': 350, 'initial_y': 160, 'target_x': 340, 'target_y': 200, 'phase': 0.3},
    # Right Elbow
    {'initial_x': 450, 'initial_y': 160, 'target_x': 460, 'target_y': 200, 'phase': 0.3},
    # Left Wrist
    {'initial_x': 330, 'initial_y': 190, 'target_x': 320, 'target_y': 220, 'phase': 0.4},
    # Right Wrist
    {'initial_x': 470, 'initial_y': 190, 'target_x': 480, 'target_y': 220, 'phase': 0.4},
    # Torso
    {'initial_x': 400, 'initial_y': 150, 'target_x': 400, 'target_y': 200, 'phase': 0.5},
    # Left Hip
    {'initial_x': 380, 'initial_y': 170, 'target_x': 380, 'target_y': 250, 'phase': 0.6},
    # Right Hip
    {'initial_x': 420, 'initial_y': 170, 'target_x': 420, 'target_y': 250, 'phase': 0.6},
    # Left Knee
    {'initial_x': 380, 'initial_y': 220, 'target_x': 380, 'target_y': 250, 'phase': 0.7},
    # Right Knee
    {'initial_x': 420, 'initial_y': 220, 'target_x': 420, 'target_y': 250, 'phase': 0.7},
    # Left Ankle
    {'initial_x': 380, 'initial_y': 270, 'target_x': 380, 'target_y': 250, 'phase': 0.8},
    # Right Ankle
    {'initial_x': 420, 'initial_y': 270, 'target_x': 420, 'target_y': 250, 'phase': 0.8},
]

# Animation parameters
duration = 2000  # Animation duration in milliseconds

# Main loop
time_passed = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)

    # Update time
    dt = clock.tick(30)
    time_passed += dt
    if time_passed >= duration:
        time_passed = 0

    t = time_passed / duration  # Normalized time [0, 1]

    # Update and draw points
    for point in points:
        phase = point['phase']
        if phase < 1.0:
            adjusted_t = max(0.0, (t - phase) / (1 - phase))
        else:
            adjusted_t = t
        adjusted_t = min(adjusted_t, 1.0)

        # Smooth transition using sinusoidal easing
        progress = (1 - math.cos(math.pi * adjusted_t)) / 2

        # Calculate current position
        current_x = point['initial_x'] + (point['target_x'] - point['initial_x']) * progress
        current_y = point['initial_y'] + (point['target_y'] - point['initial_y']) * progress

        # Draw the point
        pygame.draw.circle(screen, point_color, (int(current_x), int(current_y)), point_radius)

    pygame.display.flip()

pygame.quit()
sys.exit()
