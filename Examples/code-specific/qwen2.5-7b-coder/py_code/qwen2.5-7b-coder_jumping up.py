
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light properties
num_points = 15
points = []
for _ in range(num_points):
    x = width // 2 + random.randint(-100, 100)
    y = height // 2 + random.randint(-100, 100)
    points.append([x, y])

# Jump parameters
jump_height = 150
jump_duration = 30
gravity = 1
velocity = 0
is_jumping = False
start_time = None

clock = pygame.time.Clock()

def draw_point_light(x, y):
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    if not is_jumping:
        start_time = pygame.time.get_ticks()
        is_jumping = True

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    if elapsed_time < jump_duration:
        velocity += gravity * (elapsed_time / 1000)
        points[7][1] -= velocity
    else:
        is_jumping = False
        velocity = 0

    for point in points:
        draw_point_light(point[0], point[1])

    pygame.display.flip()
    clock.tick(60)
