
import pygame
import math
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
base_positions = [
    (200, 300), (220, 300), (240, 300), (230, 310), (230, 290),
    (250, 320), (250, 280), (260, 310), (260, 290), (250, 310),
    (250, 290), (240, 330), (240, 270), (230, 340), (230, 260)
]
amplitude = 5
frequency = 0.2
radius = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    time = pygame.time.get_ticks() / 1000
    offset_x = amplitude * math.sin(2 * math.pi * frequency * time)
    screen.fill((0, 0, 0))
    for base_x, base_y in base_positions:
        x = base_x + offset_x
        y = base_y
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), radius)
    pygame.display.flip()
    clock.tick(60)
