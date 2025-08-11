
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions
point_lights = [
    # Head
    {'x': 0, 'y': -100, 'vx': 0, 'vy': 0},
    # Torso
    {'x': 0, 'y': 0, 'vx': 0, 'vy': 0},
    # Left arm
    {'x': -50, 'y': -50, 'vx': 2, 'vy': 4},
    {'x': -70, 'y': -20, 'vx': 2, 'vy': -4},
    # Right arm
    {'x': 50, 'y': -50, 'vx': -2, 'vy': 4},
    {'x': 70, 'y': -20, 'vx': -2, 'vy': -4},
    # Left leg
    {'x': -20, 'y': 100, 'vx': 2, 'vy': -4},
    {'x': -40, 'y': 150, 'vx': 2, 'vy': 4},
    # Right leg
    {'x': 20, 'y': 100, 'vx': -2, 'vy': -4},
    {'x': 40, 'y': 150, 'vx': -2, 'vy': 4},
    # Left foot
    {'x': -20, 'y': 200, 'vx': 2, 'vy': -4},
    # Right foot
    {'x': 20, 'y': 200, 'vx': -2, 'vy': -4},
    # Heavy weight
    {'x': 0, 'y': 50, 'vx': 0, 'vy': 0},
    # Sad face (2 points for eyes)
    {'x': -10, 'y': -120, 'vx': 0, 'vy': 0},
    {'x': 10, 'y': -120, 'vx': 0, 'vy': 0},
]

def draw_point_lights(screen, point_lights):
    for point_light in point_lights:
        pygame.draw.circle(screen, WHITE, (int(point_light['x'] + WIDTH / 2), int(point_light['y'] + HEIGHT / 2)), 5)

def update_point_lights(point_lights):
    for point_light in point_lights:
        point_light['x'] += point_light['vx']
        point_light['y'] += point_light['vy']

        # Keep the point-lights within the window
        if point_light['x'] > WIDTH / 2:
            point_light['x'] = WIDTH / 2
            point_light['vx'] = -point_light['vx']
        elif point_light['x'] < -WIDTH / 2:
            point_light['x'] = -WIDTH / 2
            point_light['vx'] = -point_light['vx']

        if point_light['y'] > HEIGHT / 2:
            point_light['y'] = HEIGHT / 2
            point_light['vy'] = -point_light['vy']
        elif point_light['y'] < -HEIGHT / 2:
            point_light['y'] = -HEIGHT / 2
            point_light['vy'] = -point_light['vy']

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
        draw_point_lights(screen, point_lights)
        update_point_lights(point_lights)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
