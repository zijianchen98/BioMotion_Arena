
import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Animation: Sadwoman Lying Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

# Defining point-light stimulus positions for a lying sadwoman
# Each point represents a key joint or part of the human body
points_base = [
    (400, 300),  # Head
    (375, 325), (425, 325),  # Shoulders (left, right)
    (350, 375), (450, 375),  # Elbows (left, right)
    (325, 425), (475, 425),  # Hands (left, right)
    (400, 375),  # Chest
    (375, 425), (425, 425),  # Hips (left, right)
    (350, 475), (450, 475),  # Knees (left, right)
    (325, 525), (475, 525),  # Feet (left, right)
]

# Motion parameters
angle_speed = 0.05  # Speed of oscillation
time = 0  # Time tracker for animation

# Animation loop
running = True
while running:
    screen.fill(BLACK)  # Clear the screen to black
    time += 1  # Increment time for animation phases

    # Calculate the positions of the points based on oscillation
    animated_points = []
    for idx, (x, y) in enumerate(points_base):
        amplitude = 5 + idx  # Amplitude increases slightly for lower body parts
        y_offset = math.sin(time * angle_speed + idx) * amplitude
        animated_points.append((x, y + y_offset))

    # Draw the animated points
    for point in animated_points:
        pygame.draw.circle(screen, WHITE, point, 5)  # White dots with radius 5

    # Check events, including quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Refresh the screen
    clock.tick(60)  # Limit FPS to 60

pygame.quit()
