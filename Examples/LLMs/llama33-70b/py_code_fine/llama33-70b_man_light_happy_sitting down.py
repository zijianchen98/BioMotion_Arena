
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions and velocities
points = [
    {'x': 100, 'y': 100, 'vx': 0, 'vy': 2},  # head
    {'x': 120, 'y': 120, 'vx': 1, 'vy': 2},  # right shoulder
    {'x': 80, 'y': 120, 'vx': -1, 'vy': 2},  # left shoulder
    {'x': 110, 'y': 150, 'vx': 0.5, 'vy': 3},  # right elbow
    {'x': 90, 'y': 150, 'vx': -0.5, 'vy': 3},  # left elbow
    {'x': 120, 'y': 200, 'vx': 1, 'vy': 4},  # right hand
    {'x': 80, 'y': 200, 'vx': -1, 'vy': 4},  # left hand
    {'x': 100, 'y': 250, 'vx': 0, 'vy': 2},  # torso
    {'x': 110, 'y': 300, 'vx': 0.5, 'vy': 3},  # right hip
    {'x': 90, 'y': 300, 'vx': -0.5, 'vy': 3},  # left hip
    {'x': 120, 'y': 350, 'vx': 1, 'vy': 4},  # right knee
    {'x': 80, 'y': 350, 'vx': -1, 'vy': 4},  # left knee
    {'x': 110, 'y': 400, 'vx': 0.5, 'vy': 3},  # right ankle
    {'x': 90, 'y': 400, 'vx': -0.5, 'vy': 3},  # left ankle
    {'x': 100, 'y': 450, 'vx': 0, 'vy': 2}  # feet
]

def update_points(points):
    for point in points:
        point['x'] += point['vx']
        point['y'] += point['vy']

        # boundary checking
        if point['x'] < 0 or point['x'] > WIDTH:
            point['vx'] *= -1
        if point['y'] < 0 or point['y'] > HEIGHT:
            point['vy'] *= -1

def draw_points(screen, points):
    screen.fill((0, 0, 0))  # fill with black
    for point in points:
        pygame.draw.circle(screen, (255, 255, 255), (int(point['x']), int(point['y'])), 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_points(points)
        draw_points(screen, points)

        # adjust the movement to simulate sitting down
        if points[0]['y'] > 300:
            for point in points:
                point['vy'] = 0

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
