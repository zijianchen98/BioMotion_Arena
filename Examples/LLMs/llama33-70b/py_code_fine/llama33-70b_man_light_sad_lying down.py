
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions and velocities
point_lights = [
    {'x': WIDTH / 2, 'y': HEIGHT / 2, 'vx': 0, 'vy': -2},  # Head
    {'x': WIDTH / 2 - 20, 'y': HEIGHT / 2 - 20, 'vx': 1, 'vy': -2},  # Left shoulder
    {'x': WIDTH / 2 + 20, 'y': HEIGHT / 2 - 20, 'vx': -1, 'vy': -2},  # Right shoulder
    {'x': WIDTH / 2 - 40, 'y': HEIGHT / 2 + 20, 'vx': 1, 'vy': 2},  # Left elbow
    {'x': WIDTH / 2 + 40, 'y': HEIGHT / 2 + 20, 'vx': -1, 'vy': 2},  # Right elbow
    {'x': WIDTH / 2 - 60, 'y': HEIGHT / 2 + 60, 'vx': 1, 'vy': 2},  # Left wrist
    {'x': WIDTH / 2 + 60, 'y': HEIGHT / 2 + 60, 'vx': -1, 'vy': 2},  # Right wrist
    {'x': WIDTH / 2, 'y': HEIGHT / 2 + 100, 'vx': 0, 'vy': 2},  # Spine
    {'x': WIDTH / 2 - 20, 'y': HEIGHT / 2 + 140, 'vx': 1, 'vy': 2},  # Left hip
    {'x': WIDTH / 2 + 20, 'y': HEIGHT / 2 + 140, 'vx': -1, 'vy': 2},  # Right hip
    {'x': WIDTH / 2 - 40, 'y': HEIGHT / 2 + 180, 'vx': 1, 'vy': 2},  # Left knee
    {'x': WIDTH / 2 + 40, 'y': HEIGHT / 2 + 180, 'vx': -1, 'vy': 2},  # Right knee
    {'x': WIDTH / 2 - 60, 'y': HEIGHT / 2 + 220, 'vx': 1, 'vy': 2},  # Left ankle
    {'x': WIDTH / 2 + 60, 'y': HEIGHT / 2 + 220, 'vx': -1, 'vy': 2},  # Right ankle
    {'x': WIDTH / 2, 'y': HEIGHT / 2 + 260, 'vx': 0, 'vy': 2}  # Feet
]

def update_point_lights(point_lights):
    for light in point_lights:
        light['x'] += light['vx']
        light['y'] += light['vy']

        # Boundary checking
        if light['x'] < 0 or light['x'] > WIDTH:
            light['vx'] *= -1
        if light['y'] < 0 or light['y'] > HEIGHT:
            light['vy'] *= -1

def draw_point_lights(screen, point_lights):
    for light in point_lights:
        pygame.draw.circle(screen, WHITE, (int(light['x']), int(light['y'])), 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        update_point_lights(point_lights)
        draw_point_lights(screen, point_lights)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
