
import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Point-Light Stimulus Animation")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

points = [
    (0, 80, 0),    # head
    (-20, 60, 0),  # left shoulder
    (20, 60, 0),   # right shoulder
    (-25, 40, 5),  # left elbow
    (25, 40, 5),   # right elbow
    (-30, 20, 10), # left wrist
    (30, 20, 10),  # right wrist
    (-32, 10, 15), # left hand
    (32, 10, 15),  # right hand
    (-10, -20, 0), # left hip
    (10, -20, 0),  # right hip
    (-15, -50, 5), # left knee
    (15, -50, 5),  # right knee
    (-20, -80, 10),# left ankle
    (20, -80, 10)  # right ankle
]

scale = 2
center_x = 400
center_y = 400

clock = pygame.time.Clock()
fps = 30

running = True
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    theta = (frame * 2) % 360  # 2 degrees per frame
    theta_rad = math.radians(theta)

    for point in points:
        x, y, z = point
        x_rot = x * math.cos(theta_rad) - z * math.sin(theta_rad)
        screen_x = center_x + scale * x_rot
        screen_y = center_y - scale * y  # y remains the same
        pygame.draw.circle(screen, WHITE, (int(screen_x), int(screen_y)), 5)

    pygame.display.flip()
    clock.tick(fps)
    frame += 1

pygame.quit()
