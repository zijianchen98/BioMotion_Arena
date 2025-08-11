
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions for the sad woman bowing
# Each point represents a joint in the body (e.g., head, shoulders, elbows, etc.)
point_lights = [
    {'x': WIDTH / 2, 'y': HEIGHT / 2 - 100, 'vx': 0, 'vy': 0},  # Head
    {'x': WIDTH / 2 - 50, 'y': HEIGHT / 2 - 50, 'vx': 0, 'vy': 0},  # Left shoulder
    {'x': WIDTH / 2 + 50, 'y': HEIGHT / 2 - 50, 'vx': 0, 'vy': 0},  # Right shoulder
    {'x': WIDTH / 2 - 100, 'y': HEIGHT / 2 + 50, 'vx': 0, 'vy': 0},  # Left elbow
    {'x': WIDTH / 2 + 100, 'y': HEIGHT / 2 + 50, 'vx': 0, 'vy': 0},  # Right elbow
    {'x': WIDTH / 2 - 150, 'y': HEIGHT / 2 + 150, 'vx': 0, 'vy': 0},  # Left hand
    {'x': WIDTH / 2 + 150, 'y': HEIGHT / 2 + 150, 'vx': 0, 'vy': 0},  # Right hand
    {'x': WIDTH / 2, 'y': HEIGHT / 2 + 100, 'vx': 0, 'vy': 0},  # Spine
    {'x': WIDTH / 2 - 50, 'y': HEIGHT / 2 + 200, 'vx': 0, 'vy': 0},  # Left hip
    {'x': WIDTH / 2 + 50, 'y': HEIGHT / 2 + 200, 'vx': 0, 'vy': 0},  # Right hip
    {'x': WIDTH / 2 - 100, 'y': HEIGHT / 2 + 300, 'vx': 0, 'vy': 0},  # Left knee
    {'x': WIDTH / 2 + 100, 'y': HEIGHT / 2 + 300, 'vx': 0, 'vy': 0},  # Right knee
    {'x': WIDTH / 2 - 150, 'y': HEIGHT / 2 + 400, 'vx': 0, 'vy': 0},  # Left foot
    {'x': WIDTH / 2 + 150, 'y': HEIGHT / 2 + 400, 'vx': 0, 'vy': 0},  # Right foot
    {'x': WIDTH / 2, 'y': HEIGHT / 2 + 250, 'vx': 0, 'vy': 0}  # Sad face indicator (just a point below the head)
]

# Animation parameters
animation_time = 0
bowing_angle = 0

def update_point_lights():
    global animation_time, bowing_angle
    animation_time += 1

    # Update bowing angle
    bowing_angle = math.sin(animation_time / 50.0) * math.pi / 4

    # Update point-light positions
    point_lights[0]['x'] = WIDTH / 2
    point_lights[0]['y'] = HEIGHT / 2 - 100 + math.sin(animation_time / 50.0) * 20

    point_lights[1]['x'] = WIDTH / 2 - 50 + math.sin(animation_time / 50.0) * 10
    point_lights[1]['y'] = HEIGHT / 2 - 50 + math.sin(animation_time / 50.0) * 20

    point_lights[2]['x'] = WIDTH / 2 + 50 + math.sin(animation_time / 50.0) * 10
    point_lights[2]['y'] = HEIGHT / 2 - 50 + math.sin(animation_time / 50.0) * 20

    point_lights[3]['x'] = WIDTH / 2 - 100 + math.sin(animation_time / 50.0) * 20
    point_lights[3]['y'] = HEIGHT / 2 + 50 + math.sin(animation_time / 50.0) * 20

    point_lights[4]['x'] = WIDTH / 2 + 100 + math.sin(animation_time / 50.0) * 20
    point_lights[4]['y'] = HEIGHT / 2 + 50 + math.sin(animation_time / 50.0) * 20

    point_lights[5]['x'] = WIDTH / 2 - 150 + math.sin(animation_time / 50.0) * 30
    point_lights[5]['y'] = HEIGHT / 2 + 150 + math.sin(animation_time / 50.0) * 20

    point_lights[6]['x'] = WIDTH / 2 + 150 + math.sin(animation_time / 50.0) * 30
    point_lights[6]['y'] = HEIGHT / 2 + 150 + math.sin(animation_time / 50.0) * 20

    point_lights[7]['x'] = WIDTH / 2
    point_lights[7]['y'] = HEIGHT / 2 + 100 + math.sin(animation_time / 50.0) * 20

    point_lights[8]['x'] = WIDTH / 2 - 50 + math.sin(animation_time / 50.0) * 10
    point_lights[8]['y'] = HEIGHT / 2 + 200 + math.sin(animation_time / 50.0) * 20

    point_lights[9]['x'] = WIDTH / 2 + 50 + math.sin(animation_time / 50.0) * 10
    point_lights[9]['y'] = HEIGHT / 2 + 200 + math.sin(animation_time / 50.0) * 20

    point_lights[10]['x'] = WIDTH / 2 - 100 + math.sin(animation_time / 50.0) * 20
    point_lights[10]['y'] = HEIGHT / 2 + 300 + math.sin(animation_time / 50.0) * 20

    point_lights[11]['x'] = WIDTH / 2 + 100 + math.sin(animation_time / 50.0) * 20
    point_lights[11]['y'] = HEIGHT / 2 + 300 + math.sin(animation_time / 50.0) * 20

    point_lights[12]['x'] = WIDTH / 2 - 150 + math.sin(animation_time / 50.0) * 30
    point_lights[12]['y'] = HEIGHT / 2 + 400 + math.sin(animation_time / 50.0) * 20

    point_lights[13]['x'] = WIDTH / 2 + 150 + math.sin(animation_time / 50.0) * 30
    point_lights[13]['y'] = HEIGHT / 2 + 400 + math.sin(animation_time / 50.0) * 20

    point_lights[14]['x'] = WIDTH / 2
    point_lights[14]['y'] = HEIGHT / 2 + 250 + math.sin(animation_time / 50.0) * 10

def draw_point_lights(screen):
    for point in point_lights:
        pygame.draw.circle(screen, (255, 255, 255), (int(point['x']), int(point['y'])), 5)

def main():
    global animation_time, bowing_angle
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        update_point_lights()
        draw_point_lights(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
