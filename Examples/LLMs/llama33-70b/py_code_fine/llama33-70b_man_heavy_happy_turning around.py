
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point light positions and velocities
class PointLight:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

# Define point lights for the happy man
point_lights = [
    PointLight(100, 50, 0, 0),  # Head
    PointLight(120, 70, 0, 0),  # Right shoulder
    PointLight(80, 70, 0, 0),   # Left shoulder
    PointLight(120, 150, 0, 0), # Right elbow
    PointLight(80, 150, 0, 0),  # Left elbow
    PointLight(120, 250, 0, 0), # Right hand
    PointLight(80, 250, 0, 0),  # Left hand
    PointLight(100, 200, 0, 0), # Torso
    PointLight(100, 300, 0, 0), # Hips
    PointLight(120, 350, 0, 0), # Right knee
    PointLight(80, 350, 0, 0),  # Left knee
    PointLight(120, 450, 0, 0), # Right foot
    PointLight(80, 450, 0, 0),  # Left foot
    PointLight(90, 100, 0, 0),  # Weight (right side)
    PointLight(110, 100, 0, 0), # Weight (left side)
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Animation variables
angle = 0
turning_speed = 0.05

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update point light positions
    angle += turning_speed
    for i, point_light in enumerate(point_lights):
        if i == 0:  # Head
            point_light.x = 100 + 20 * math.sin(angle)
            point_light.y = 50 + 10 * math.cos(angle)
        elif i == 1:  # Right shoulder
            point_light.x = 120 + 20 * math.sin(angle + math.pi / 2)
            point_light.y = 70 + 10 * math.cos(angle + math.pi / 2)
        elif i == 2:  # Left shoulder
            point_light.x = 80 + 20 * math.sin(angle - math.pi / 2)
            point_light.y = 70 + 10 * math.cos(angle - math.pi / 2)
        elif i == 3:  # Right elbow
            point_light.x = 120 + 30 * math.sin(angle + math.pi / 2)
            point_light.y = 150 + 15 * math.cos(angle + math.pi / 2)
        elif i == 4:  # Left elbow
            point_light.x = 80 + 30 * math.sin(angle - math.pi / 2)
            point_light.y = 150 + 15 * math.cos(angle - math.pi / 2)
        elif i == 5:  # Right hand
            point_light.x = 120 + 40 * math.sin(angle + math.pi / 2)
            point_light.y = 250 + 20 * math.cos(angle + math.pi / 2)
        elif i == 6:  # Left hand
            point_light.x = 80 + 40 * math.sin(angle - math.pi / 2)
            point_light.y = 250 + 20 * math.cos(angle - math.pi / 2)
        elif i == 7:  # Torso
            point_light.x = 100 + 10 * math.sin(angle)
            point_light.y = 200 + 5 * math.cos(angle)
        elif i == 8:  # Hips
            point_light.x = 100 + 10 * math.sin(angle)
            point_light.y = 300 + 5 * math.cos(angle)
        elif i == 9:  # Right knee
            point_light.x = 120 + 20 * math.sin(angle + math.pi / 2)
            point_light.y = 350 + 10 * math.cos(angle + math.pi / 2)
        elif i == 10:  # Left knee
            point_light.x = 80 + 20 * math.sin(angle - math.pi / 2)
            point_light.y = 350 + 10 * math.cos(angle - math.pi / 2)
        elif i == 11:  # Right foot
            point_light.x = 120 + 30 * math.sin(angle + math.pi / 2)
            point_light.y = 450 + 15 * math.cos(angle + math.pi / 2)
        elif i == 12:  # Left foot
            point_light.x = 80 + 30 * math.sin(angle - math.pi / 2)
            point_light.y = 450 + 15 * math.cos(angle - math.pi / 2)
        elif i == 13:  # Weight (right side)
            point_light.x = 90 + 10 * math.sin(angle + math.pi / 2)
            point_light.y = 100 + 5 * math.cos(angle + math.pi / 2)
        elif i == 14:  # Weight (left side)
            point_light.x = 110 + 10 * math.sin(angle - math.pi / 2)
            point_light.y = 100 + 5 * math.cos(angle - math.pi / 2)

    # Draw everything
    screen.fill(BLACK)
    for point_light in point_lights:
        pygame.draw.circle(screen, WHITE, (int(point_light.x), int(point_light.y)), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
