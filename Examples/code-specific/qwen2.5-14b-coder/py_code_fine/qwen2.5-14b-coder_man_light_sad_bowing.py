
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Bowing Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
NUM_LIGHTS = 15
lights = [{'x': WIDTH // 2, 'y': HEIGHT // 2, 'radius': 5} for _ in range(NUM_LIGHTS)]

# Animation parameters
frame_count = 0
bow_angle = 0
bow_speed = 0.05

def draw_lights():
    screen.fill(BLACK)
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light['x']), int(light['y'])), light['radius'])

def update_lights():
    global bow_angle
    frame_count += 1

    # Bowing motion
    if frame_count < 120:
        bow_angle += bow_speed
    elif frame_count < 240:
        bow_angle -= bow_speed
    else:
        bow_angle = 0
        frame_count = 0

    # Update light positions based on bowing motion
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    radius = 100
    for i, light in enumerate(lights):
        angle = (i / NUM_LIGHTS) * 2 * math.pi + bow_angle
        light['x'] = center_x + radius * math.cos(angle)
        light['y'] = center_y + radius * math.sin(angle)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_lights()
    draw_lights()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
