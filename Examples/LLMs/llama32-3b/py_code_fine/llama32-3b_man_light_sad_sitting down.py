
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light properties
POINT_LIGHTS = 15
POINT_LIGHT_RADIUS = 5
POINT_LIGHT_SPAWN_RATE = 100

# Action properties
ACTION = "sitting down"
ACTION_STEPS = 10

class PointLight:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = random.uniform(0.05, 0.15)
        self.target_x = x
        self.target_y = y

    def update(self):
        if self.target_x!= self.x or self.target_y!= self.y:
            if self.x < self.target_x:
                self.x += self.speed
            else:
                self.x -= self.speed
            if self.y < self.target_y:
                self.y += self.speed
            else:
                self.y -= self.speed
            self.angle = math.atan2(self.y - self.target_y, self.x - self.target_x)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), POINT_LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = []
    for _ in range(POINT_LIGHTS):
        point_lights.append(PointLight(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.uniform(0, 2 * math.pi)))

    action_step = 0
    action_angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for point_light in point_lights:
            point_light.update()
            point_light.target_x = WIDTH / 2
            point_light.target_y = HEIGHT / 2
            point_light.draw(screen)

        if action_step < ACTION_STEPS:
            action_angle += 0.01
            for point_light in point_lights:
                point_light.target_x = WIDTH / 2 + math.cos(action_angle) * 100
                point_light.target_y = HEIGHT / 2 + math.sin(action_angle) * 100
        else:
            for point_light in point_lights:
                point_light.target_x = WIDTH / 2
                point_light.target_y = HEIGHT / 2

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
