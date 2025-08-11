
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_COLOR = (255, 255, 255)  # White
LIGHT_RADIUS = 5

# Walking parameters
WALKING_SPEED = 2  # pixels per frame
LEG_LENGTH = 50
ARM_LENGTH = 30
BODY_HEIGHT = 100

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, phase):
        # Update position based on walking phase
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, LIGHT_COLOR, (int(self.x), int(self.y)), LIGHT_RADIUS)

class Walker:
    def __init__(self):
        self.lights = [
            PointLight(0, -BODY_HEIGHT / 2),  # Head
            PointLight(-LEG_LENGTH / 2, -BODY_HEIGHT / 2),  # Left shoulder
            PointLight(LEG_LENGTH / 2, -BODY_HEIGHT / 2),  # Right shoulder
            PointLight(-ARM_LENGTH / 2, -BODY_HEIGHT / 2 + ARM_LENGTH),  # Left elbow
            PointLight(ARM_LENGTH / 2, -BODY_HEIGHT / 2 + ARM_LENGTH),  # Right elbow
            PointLight(-ARM_LENGTH / 2, -BODY_HEIGHT / 2 + 2 * ARM_LENGTH),  # Left wrist
            PointLight(ARM_LENGTH / 2, -BODY_HEIGHT / 2 + 2 * ARM_LENGTH),  # Right wrist
            PointLight(-LEG_LENGTH / 2, BODY_HEIGHT / 2),  # Left hip
            PointLight(LEG_LENGTH / 2, BODY_HEIGHT / 2),  # Right hip
            PointLight(-LEG_LENGTH / 2, BODY_HEIGHT / 2 + LEG_LENGTH),  # Left knee
            PointLight(LEG_LENGTH / 2, BODY_HEIGHT / 2 + LEG_LENGTH),  # Right knee
            PointLight(-LEG_LENGTH / 2, BODY_HEIGHT / 2 + 2 * LEG_LENGTH),  # Left ankle
            PointLight(LEG_LENGTH / 2, BODY_HEIGHT / 2 + 2 * LEG_LENGTH),  # Right ankle
            PointLight(0, BODY_HEIGHT / 2 + LEG_LENGTH),  # Center of mass
            PointLight(0, -BODY_HEIGHT / 2 - LEG_LENGTH),  # Top of head
        ]

    def update(self, phase):
        # Update positions of all point-lights based on walking phase
        self.lights[0].x = 0  # Head
        self.lights[0].y = -BODY_HEIGHT / 2 + math.sin(phase) * 10

        self.lights[1].x = -LEG_LENGTH / 2 + math.sin(phase) * 10  # Left shoulder
        self.lights[1].y = -BODY_HEIGHT / 2

        self.lights[2].x = LEG_LENGTH / 2 - math.sin(phase) * 10  # Right shoulder
        self.lights[2].y = -BODY_HEIGHT / 2

        self.lights[3].x = -ARM_LENGTH / 2 + math.sin(phase) * 15  # Left elbow
        self.lights[3].y = -BODY_HEIGHT / 2 + ARM_LENGTH

        self.lights[4].x = ARM_LENGTH / 2 - math.sin(phase) * 15  # Right elbow
        self.lights[4].y = -BODY_HEIGHT / 2 + ARM_LENGTH

        self.lights[5].x = -ARM_LENGTH / 2 + math.sin(phase) * 20  # Left wrist
        self.lights[5].y = -BODY_HEIGHT / 2 + 2 * ARM_LENGTH

        self.lights[6].x = ARM_LENGTH / 2 - math.sin(phase) * 20  # Right wrist
        self.lights[6].y = -BODY_HEIGHT / 2 + 2 * ARM_LENGTH

        self.lights[7].x = -LEG_LENGTH / 2 + math.sin(phase) * 10  # Left hip
        self.lights[7].y = BODY_HEIGHT / 2

        self.lights[8].x = LEG_LENGTH / 2 - math.sin(phase) * 10  # Right hip
        self.lights[8].y = BODY_HEIGHT / 2

        self.lights[9].x = -LEG_LENGTH / 2 + math.sin(phase) * 20  # Left knee
        self.lights[9].y = BODY_HEIGHT / 2 + LEG_LENGTH

        self.lights[10].x = LEG_LENGTH / 2 - math.sin(phase) * 20  # Right knee
        self.lights[10].y = BODY_HEIGHT / 2 + LEG_LENGTH

        self.lights[11].x = -LEG_LENGTH / 2 + math.sin(phase) * 25  # Left ankle
        self.lights[11].y = BODY_HEIGHT / 2 + 2 * LEG_LENGTH

        self.lights[12].x = LEG_LENGTH / 2 - math.sin(phase) * 25  # Right ankle
        self.lights[12].y = BODY_HEIGHT / 2 + 2 * LEG_LENGTH

        self.lights[13].x = 0  # Center of mass
        self.lights[13].y = BODY_HEIGHT / 2 + LEG_LENGTH + math.sin(phase) * 10

        self.lights[14].x = 0  # Top of head
        self.lights[14].y = -BODY_HEIGHT / 2 - LEG_LENGTH + math.sin(phase) * 10

    def draw(self, screen):
        for light in self.lights:
            light.draw(screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    walker = Walker()
    phase = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill screen with black

        walker.update(phase)
        walker.draw(screen)

        phase += 0.1  # Increment walking phase

        pygame.display.flip()
        clock.tick(60)  # Limit frame rate to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
