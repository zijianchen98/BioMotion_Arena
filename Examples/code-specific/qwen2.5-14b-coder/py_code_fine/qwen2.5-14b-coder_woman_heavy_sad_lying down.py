
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Lying Down Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
num_lights = 15
lights = []
for i in range(num_lights):
    x = WIDTH // 2 + (i - num_lights // 2) * 20  # Distribute lights horizontally
    y = HEIGHT // 2 + (i - num_lights // 2) * 20  # Distribute lights vertically
    lights.append((x, y))

# Animation parameters
frame_count = 0
total_frames = 60 * 5  # 5 seconds at 60 FPS

def draw_lights():
    screen.fill(BLACK)
    for x, y in lights:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

def update_lights(frame):
    # Simple sine wave motion for demonstration purposes
    for i, (x, y) in enumerate(lights):
        offset = i * 0.5
        lights[i] = (
            x + 20 * math.sin(math.radians(frame + offset)),
            y + 10 * math.cos(math.radians(frame + offset))
        )

clock = pygame.time.Clock()

while frame_count < total_frames:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update_lights(frame_count)
    draw_lights()
    pygame.display.flip()
    clock.tick(60)
    frame_count += 1

pygame.quit()
sys.exit()
