
import pygame
import math

# Initialize Pygame
pygame.init()

# Set screen dimensions and frame rate
screen_width, screen_height = 400, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Point-Light Biological Motion Animation')
clock = pygame.time.Clock()
fps = 30

# Define point positions
points = [
    (200, 100),  # Head
    (180, 200),  # Shoulder 1
    (220, 200),  # Shoulder 2
    (160, 250),  # Elbow 1
    (240, 250),  # Elbow 2
    (140, 300),  # Hand 1
    (260, 300),  # Hand 2
    (200, 200),  # Neck
    (200, 300),  # Waist
    (180, 350),  # Hip 1
    (220, 350),  # Hip 2
    (160, 400),  # Knee 1
    (240, 400),  # Knee 2
    (140, 450),  # Foot 1
    (260, 450),  # Foot 2
]

# Wave motion parameters
wave_amp = 20
wave_freq = 0.1

def draw_points(points):
    screen.fill((0, 0, 0))
    for point in points:
        pygame.draw.circle(screen, (255, 255, 255), point, 5)

def update_positions(points, t):
    # Animate waving hand motion
    points[6] = (140 + wave_amp * math.sin(wave_freq * t), 300)
    points[7] = (260 + wave_amp * math.sin(wave_freq * t), 300)

t = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen and update positions
    draw_points(points)
    update_positions(points, t)

    pygame.display.flip()
    clock.tick(fps)
    t += 1

pygame.quit()
