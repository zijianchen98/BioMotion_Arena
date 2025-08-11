
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions and velocities
point_lights = [
    {"x": WIDTH // 2, "y": HEIGHT // 2, "vx": 0, "vy": 0},  # torso
    {"x": WIDTH // 2 - 50, "y": HEIGHT // 2 - 50, "vx": 0, "vy": 0},  # left shoulder
    {"x": WIDTH // 2 + 50, "y": HEIGHT // 2 - 50, "vx": 0, "vy": 0},  # right shoulder
    {"x": WIDTH // 2 - 100, "y": HEIGHT // 2, "vx": 0, "vy": 0},  # left elbow
    {"x": WIDTH // 2 + 100, "y": HEIGHT // 2, "vx": 0, "vy": 0},  # right elbow
    {"x": WIDTH // 2 - 150, "y": HEIGHT // 2 + 50, "vx": 0, "vy": 0},  # left wrist
    {"x": WIDTH // 2 + 150, "y": HEIGHT // 2 + 50, "vx": 0, "vy": 0},  # right wrist
    {"x": WIDTH // 2 - 200, "y": HEIGHT // 2 + 100, "vx": 0, "vy": 0},  # left hand
    {"x": WIDTH // 2 + 200, "y": HEIGHT // 2 + 100, "vx": 0, "vy": 0},  # right hand
    {"x": WIDTH // 2 - 50, "y": HEIGHT // 2 + 150, "vx": 0, "vy": 0},  # left hip
    {"x": WIDTH // 2 + 50, "y": HEIGHT // 2 + 150, "vx": 0, "vy": 0},  # right hip
    {"x": WIDTH // 2 - 100, "y": HEIGHT // 2 + 200, "vx": 0, "vy": 0},  # left knee
    {"x": WIDTH // 2 + 100, "y": HEIGHT // 2 + 200, "vx": 0, "vy": 0},  # right knee
    {"x": WIDTH // 2 - 150, "y": HEIGHT // 2 + 250, "vx": 0, "vy": 0},  # left ankle
    {"x": WIDTH // 2 + 150, "y": HEIGHT // 2 + 250, "vx": 0, "vy": 0},  # right ankle
]

# Waving hand animation parameters
waving_angle = 0
waving_amplitude = 50
waving_speed = 2

def update_point_lights():
    global waving_angle
    waving_angle += waving_speed
    if waving_angle > 360:
        waving_angle -= 360

    # Update left wrist and hand positions
    point_lights[6]["x"] = WIDTH // 2 - 150 + math.sin(math.radians(waving_angle)) * waving_amplitude
    point_lights[8]["x"] = WIDTH // 2 - 200 + math.sin(math.radians(waving_angle)) * waving_amplitude * 1.5

def draw_point_lights(screen):
    for point_light in point_lights:
        pygame.draw.circle(screen, WHITE, (int(point_light["x"]), int(point_light["y"])), 5)

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
        update_point_lights()
        draw_point_lights(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
