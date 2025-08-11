
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)  # White
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Sad man with heavy weight properties
MAN_HEIGHT = 200
MAN_WIDTH = 50
WEIGHT_HEIGHT = 50
WEIGHT_WIDTH = 50

# Jumping motion properties
JUMP_HEIGHT = 100
JUMP_DURATION = 1000  # milliseconds

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, time):
        # Update point-light position based on jumping motion
        if time < JUMP_DURATION / 2:
            self.y -= (JUMP_HEIGHT / (JUMP_DURATION / 2)) * time
        else:
            self.y += (JUMP_HEIGHT / (JUMP_DURATION / 2)) * (time - JUMP_DURATION / 2)

    def draw(self, screen):
        pygame.draw.circle(screen, LIGHT_COLOR, (int(self.x), int(self.y)), LIGHT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Create point-lights for sad man with heavy weight
    point_lights = [
        PointLight(WIDTH / 2, HEIGHT / 2),  # Head
        PointLight(WIDTH / 2 - 20, HEIGHT / 2 + 20),  # Left shoulder
        PointLight(WIDTH / 2 + 20, HEIGHT / 2 + 20),  # Right shoulder
        PointLight(WIDTH / 2, HEIGHT / 2 + 40),  # Chest
        PointLight(WIDTH / 2 - 20, HEIGHT / 2 + 60),  # Left elbow
        PointLight(WIDTH / 2 + 20, HEIGHT / 2 + 60),  # Right elbow
        PointLight(WIDTH / 2, HEIGHT / 2 + 80),  # Waist
        PointLight(WIDTH / 2 - 20, HEIGHT / 2 + 100),  # Left hip
        PointLight(WIDTH / 2 + 20, HEIGHT / 2 + 100),  # Right hip
        PointLight(WIDTH / 2, HEIGHT / 2 + 120),  # Left knee
        PointLight(WIDTH / 2, HEIGHT / 2 + 140),  # Right knee
        PointLight(WIDTH / 2 - 20, HEIGHT / 2 + 160),  # Left ankle
        PointLight(WIDTH / 2 + 20, HEIGHT / 2 + 160),  # Right ankle
        PointLight(WIDTH / 2, HEIGHT / 2 + 180),  # Weight
        PointLight(WIDTH / 2, HEIGHT / 2 + 200),  # Weight bottom
    ]

    running = True
    time = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Update and draw point-lights
        for point_light in point_lights:
            point_light.update(time)
            point_light.draw(screen)

        # Update time
        time += 10
        if time > JUMP_DURATION:
            time = 0

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
