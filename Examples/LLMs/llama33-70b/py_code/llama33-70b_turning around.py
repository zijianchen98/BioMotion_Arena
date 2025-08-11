
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions (15 points)
# Head, torso, left/right shoulders, left/right elbows, left/right wrists, left/right hips, left/right knees, left/right ankles
points = [
    (0, -100),  # Head
    (0, 0),     # Torso
    (-50, -50), # Left shoulder
    (50, -50),  # Right shoulder
    (-100, -100), # Left elbow
    (100, -100), # Right elbow
    (-150, -150), # Left wrist
    (150, -150), # Right wrist
    (-50, 50),   # Left hip
    (50, 50),    # Right hip
    (-100, 150), # Left knee
    (100, 150),  # Right knee
    (-150, 250), # Left ankle
    (150, 250),  # Right ankle
    (0, 100)     # Waist
]

# Rotation angle
angle = 0

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Calculate new point positions based on rotation
    rotated_points = []
    for point in points:
        x = point[0] * math.cos(math.radians(angle)) - point[1] * math.sin(math.radians(angle))
        y = point[0] * math.sin(math.radians(angle)) + point[1] * math.cos(math.radians(angle))
        rotated_points.append((x + WIDTH // 2, y + HEIGHT // 2))

    # Draw point-lights
    for point in rotated_points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    # Update rotation angle
    angle = (angle + 1) % 360

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
