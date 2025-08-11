
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_COLOR = (255, 255, 255)  # White
LIGHT_RADIUS = 5

# Animation properties
FPS = 60
DURATION = 2  # seconds

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, t):
        # Define the movement trajectory for each point-light
        # These are simplified examples and may need to be adjusted for a more realistic motion
        if self.x < WIDTH // 2:
            self.x = WIDTH // 2 + math.sin(t * 2 * math.pi) * 50
            self.y = HEIGHT // 2 + math.cos(t * 2 * math.pi) * 50
        elif self.x < WIDTH // 2 + 100:
            self.x = WIDTH // 2 + 100 + math.sin(t * 2 * math.pi) * 20
            self.y = HEIGHT // 2 + 50 + math.cos(t * 2 * math.pi) * 20
        else:
            self.x = WIDTH // 2 + 200 + math.sin(t * 2 * math.pi) * 10
            self.y = HEIGHT // 2 + 100 + math.cos(t * 2 * math.pi) * 10

    def draw(self, screen):
        pygame.draw.circle(screen, LIGHT_COLOR, (int(self.x), int(self.y)), LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Initialize point-lights
    point_lights = [
        PointLight(WIDTH // 2 - 50, HEIGHT // 2 - 50),  # Head
        PointLight(WIDTH // 2 - 30, HEIGHT // 2 - 30),  # Shoulder
        PointLight(WIDTH // 2 - 10, HEIGHT // 2 - 10),  # Elbow
        PointLight(WIDTH // 2 + 10, HEIGHT // 2 - 10),  # Wrist
        PointLight(WIDTH // 2 + 30, HEIGHT // 2 - 30),  # Hand
        PointLight(WIDTH // 2 - 50, HEIGHT // 2 + 50),  # Hip
        PointLight(WIDTH // 2 - 30, HEIGHT // 2 + 30),  # Knee
        PointLight(WIDTH // 2 - 10, HEIGHT // 2 + 10),  # Ankle
        PointLight(WIDTH // 2 + 10, HEIGHT // 2 + 10),  # Foot
        PointLight(WIDTH // 2 + 30, HEIGHT // 2 + 30),  # Toe
        PointLight(WIDTH // 2 - 20, HEIGHT // 2 - 20),  # Upper arm
        PointLight(WIDTH // 2 + 20, HEIGHT // 2 - 20),  # Upper arm
        PointLight(WIDTH // 2 - 20, HEIGHT // 2 + 20),  # Thigh
        PointLight(WIDTH // 2 + 20, HEIGHT // 2 + 20),  # Thigh
        PointLight(WIDTH // 2, HEIGHT // 2),  # Torso
    ]

    running = True
    t = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill screen with black

        # Update and draw point-lights
        for point_light in point_lights:
            point_light.update(t)
            point_light.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

        t += 1 / FPS
        if t > DURATION:
            t = 0

    pygame.quit()

if __name__ == "__main__":
    main()
