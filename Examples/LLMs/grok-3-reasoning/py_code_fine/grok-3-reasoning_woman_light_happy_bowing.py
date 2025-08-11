
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Define points in model coordinates (y increases upwards)
points = [
    (-10, 0),   # left ankle
    (10, 0),    # right ankle
    (-10, 100), # left knee
    (10, 100),  # right knee
    (-20, 200), # left hip
    (20, 200),  # right hip
    (0, 300),   # torso
    (0, 400),   # neck
    (0, 500),   # head
    (-30, 350), # left shoulder
    (30, 350),  # right shoulder
    (-40, 300), # left elbow
    (40, 300),  # right elbow
    (-50, 250), # left wrist
    (50, 250)   # right wrist
]

pivot = (0, 200)
theta_max = math.pi / 4  # 45 degrees
T = 60  # period in frames

frame = 0
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # black background

    # Calculate theta
    t = frame % T
    theta = theta_max * (1 - math.cos(2 * math.pi * t / T)) / 2

    for point in points:
        if point[1] > pivot[1]:
            dx = point[0] - pivot[0]
            dy = point[1] - pivot[1]
            x_rot = pivot[0] + dx * math.cos(theta) - dy * math.sin(theta)
            y_rot = pivot[1] + dx * math.sin(theta) + dy * math.cos(theta)
        else:
            x_rot, y_rot = point

        screen_x = screen_width / 2 + x_rot
        screen_y = screen_height - y_rot
        pygame.draw.circle(screen, (255, 255, 255), (int(screen_x), int(screen_y)), 5)

    pygame.display.flip()
    clock.tick(30)  # 30 fps
    frame += 1

pygame.quit()
