
import pygame
import math
import sys

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
POINT_LIGHTS = 15
POINT_LIGHT_RADIUS = 5
POINT_LIGHT_COLOR = WHITE

# Sad man properties
MAN_WIDTH, MAN_HEIGHT = 50, 100
MAN_COLOR = (200, 0, 0)  # Red color for sad man

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Man:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_point_lights(screen, point_lights):
    for i, point_light in enumerate(point_lights):
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, (point_light.x, point_light.y), POINT_LIGHT_RADIUS)

def draw_man(screen, man, point_lights):
    pygame.draw.rect(screen, MAN_COLOR, (man.x - MAN_WIDTH // 2, man.y - MAN_HEIGHT // 2, MAN_WIDTH, MAN_HEIGHT))

def animate(point_lights, man, angle, gravity):
    for i in range(len(point_lights)):
        dx = WIDTH // 2 - point_lights[i].x
        dy = HEIGHT // 2 - point_lights[i].y
        distance = math.sqrt(dx**2 + dy**2)
        angle_rad = math.atan2(dy, dx)
        point_lights[i].x = WIDTH // 2 + distance * math.cos(angle_rad)
        point_lights[i].y = HEIGHT // 2 + distance * math.sin(angle_rad)

        # Update man position
        man.x = WIDTH // 2 + math.cos(angle) * 100
        man.y = HEIGHT // 2 + math.sin(angle) * 100

        # Update angle
        angle += 0.01

        # Apply gravity
        angle += gravity

    return point_lights, man, angle

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = [PointLight(WIDTH // 2 + math.cos(i * 2 * math.pi / POINT_LIGHTS) * 200, HEIGHT // 2 + math.sin(i * 2 * math.pi / POINT_LIGHTS) * 200) for i in range(POINT_LIGHTS)]
    man = Man(WIDTH // 2, HEIGHT // 2)

    angle = 0
    gravity = 0.01

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        draw_point_lights(screen, point_lights)
        draw_man(screen, man, point_lights)

        point_lights, man, angle = animate(point_lights, man, angle, gravity)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
