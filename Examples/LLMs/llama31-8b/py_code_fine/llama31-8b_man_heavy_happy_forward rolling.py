
import pygame
import numpy as np

# Window size
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)

# Happyman properties
HAPPYMAN_RADIUS = 50

# Action properties
ACTION_TYPE = 'forward_roll'
ACTION_SPEED = 2

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

    def update(self, action_type, action_speed):
        if action_type == 'forward_roll':
            self.speed_x = action_speed
            self.speed_y = 0
        self.x += self.speed_x
        self.y += self.speed_y

        # Boundary checking
        if self.x < 0:
            self.x = 0
            self.speed_x *= -1
        elif self.x > WIDTH - LIGHT_RADIUS:
            self.x = WIDTH - LIGHT_RADIUS
            self.speed_x *= -1
        if self.y < 0:
            self.y = 0
            self.speed_y *= -1
        elif self.y > HEIGHT - LIGHT_RADIUS:
            self.y = HEIGHT - LIGHT_RADIUS
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, LIGHT_COLOR, (int(self.x), int(self.y)), LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Initialize point-lights
    lights = []
    for i in range(NUM_LIGHTS):
        angle = 2 * np.pi * i / NUM_LIGHTS
        x = WIDTH // 2 + HAPPYMAN_RADIUS * np.cos(angle)
        y = HEIGHT // 2 + HAPPYMAN_RADIUS * np.sin(angle)
        lights.append(PointLight(x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update point-lights
        for light in lights:
            light.update(ACTION_TYPE, ACTION_SPEED)

        # Draw background
        screen.fill((0, 0, 0))

        # Draw point-lights
        for light in lights:
            light.draw(screen)

        # Draw happyman (for reference)
        pygame.draw.circle(screen, (255, 255, 255), (WIDTH // 2, HEIGHT // 2), HAPPYMAN_RADIUS)

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
