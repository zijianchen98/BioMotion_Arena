
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions for the sad man running
# Each point-light represents a joint in the body
point_lights = [
    {'x': 0.5, 'y': 0.1, 'vx': 0.01, 'vy': 0.02},  # Head
    {'x': 0.4, 'y': 0.3, 'vx': 0.02, 'vy': 0.01},  # Left shoulder
    {'x': 0.6, 'y': 0.3, 'vx': -0.02, 'vy': 0.01},  # Right shoulder
    {'x': 0.4, 'y': 0.5, 'vx': 0.03, 'vy': 0.02},  # Left elbow
    {'x': 0.6, 'y': 0.5, 'vx': -0.03, 'vy': 0.02},  # Right elbow
    {'x': 0.4, 'y': 0.7, 'vx': 0.04, 'vy': 0.03},  # Left hand
    {'x': 0.6, 'y': 0.7, 'vx': -0.04, 'vy': 0.03},  # Right hand
    {'x': 0.5, 'y': 0.4, 'vx': 0.01, 'vy': 0.02},  # Torso
    {'x': 0.5, 'y': 0.6, 'vx': 0.02, 'vy': 0.03},  # Hips
    {'x': 0.3, 'y': 0.8, 'vx': 0.05, 'vy': 0.04},  # Left knee
    {'x': 0.7, 'y': 0.8, 'vx': -0.05, 'vy': 0.04},  # Right knee
    {'x': 0.3, 'y': 0.9, 'vx': 0.06, 'vy': 0.05},  # Left ankle
    {'x': 0.7, 'y': 0.9, 'vx': -0.06, 'vy': 0.05},  # Right ankle
    {'x': 0.5, 'y': 0.2, 'vx': 0.01, 'vy': 0.01},  # Sad face (forehead)
    {'x': 0.5, 'y': 0.15, 'vx': 0.01, 'vy': 0.01}  # Sad face (chin)
]

def update_point_lights(point_lights):
    for point_light in point_lights:
        point_light['x'] += point_light['vx']
        point_light['y'] += point_light['vy']

        # Boundary checking to keep the point-lights within the window
        if point_light['x'] < 0 or point_light['x'] > 1:
            point_light['vx'] *= -1
        if point_light['y'] < 0 or point_light['y'] > 1:
            point_light['vy'] *= -1

def draw_point_lights(screen, point_lights):
    screen.fill(BLACK)
    for point_light in point_lights:
        x = int(point_light['x'] * WIDTH)
        y = int(point_light['y'] * HEIGHT)
        pygame.draw.circle(screen, WHITE, (x, y), 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_point_lights(point_lights)
        draw_point_lights(screen, point_lights)

        # Simulate the running motion by moving the point-lights in a sinusoidal pattern
        for i, point_light in enumerate(point_lights):
            point_light['y'] += 0.001 * math.sin(i * 0.1 + pygame.time.get_ticks() * 0.01)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
