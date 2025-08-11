
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sad Woman Jumping Up")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Point light properties
num_lights = 15
lights = []
for i in range(num_lights):
    angle = (i / num_lights) * 2 * math.pi
    x = width // 2 + 100 * math.cos(angle)
    y = height // 2 + 100 * math.sin(angle)
    lights.append([x, y])

# Animation parameters
frame_count = 0
max_frames = 60  # Total frames for one complete jump cycle
jump_height = 200

def draw_lights():
    screen.fill(black)
    for light in lights:
        pygame.draw.circle(screen, white, (int(light[0]), int(light[1])), 5)

def update_lights(frame):
    t = frame / max_frames
    for i in range(num_lights):
        angle = (i / num_lights) * 2 * math.pi
        x = width // 2 + 100 * math.cos(angle)
        y = height // 2 + 100 * math.sin(angle) - jump_height * (t ** 2)  # Parabolic motion
        lights[i] = [x, y]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_lights(frame_count)
    draw_lights()
    pygame.display.flip()

    frame_count += 1
    if frame_count >= max_frames:
        frame_count = 0

    pygame.time.Clock().tick(60)  # 60 FPS

pygame.quit()
sys.exit()
