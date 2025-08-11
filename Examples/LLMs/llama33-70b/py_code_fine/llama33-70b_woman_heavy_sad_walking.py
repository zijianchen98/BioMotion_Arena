
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_COLOR = (255, 255, 255)  # White
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Woman's walking properties
WALKING_SPEED = 2  # pixels per frame
HEAVY_WEIGHT_OFFSET = 10  # pixels

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, angle, offset_x, offset_y):
        self.x = WIDTH // 2 + math.cos(angle) * 100 + offset_x
        self.y = HEIGHT // 2 + math.sin(angle) * 100 + offset_y

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Initialize point-lights
    lights = [
        PointLight(0, 0),  # Head
        PointLight(0, 0),  # Left shoulder
        PointLight(0, 0),  # Right shoulder
        PointLight(0, 0),  # Left elbow
        PointLight(0, 0),  # Right elbow
        PointLight(0, 0),  # Left wrist
        PointLight(0, 0),  # Right wrist
        PointLight(0, 0),  # Left hip
        PointLight(0, 0),  # Right hip
        PointLight(0, 0),  # Left knee
        PointLight(0, 0),  # Right knee
        PointLight(0, 0),  # Left ankle
        PointLight(0, 0),  # Right ankle
        PointLight(0, 0),  # Heavy weight (left hand)
        PointLight(0, 0),  # Heavy weight (right hand)
    ]

    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BACKGROUND_COLOR)

        # Update point-lights
        lights[0].update(angle, 0, -50)  # Head
        lights[1].update(angle + math.pi / 2, -20, -30)  # Left shoulder
        lights[2].update(angle + math.pi / 2, 20, -30)  # Right shoulder
        lights[3].update(angle + math.pi / 2, -40, 0)  # Left elbow
        lights[4].update(angle + math.pi / 2, 40, 0)  # Right elbow
        lights[5].update(angle + math.pi / 2, -60, 30)  # Left wrist
        lights[6].update(angle + math.pi / 2, 60, 30)  # Right wrist
        lights[7].update(angle, -20, 50)  # Left hip
        lights[8].update(angle, 20, 50)  # Right hip
        lights[9].update(angle + math.pi / 2, -40, 80)  # Left knee
        lights[10].update(angle + math.pi / 2, 40, 80)  # Right knee
        lights[11].update(angle + math.pi / 2, -60, 110)  # Left ankle
        lights[12].update(angle + math.pi / 2, 60, 110)  # Right ankle
        lights[13].update(angle + math.pi / 2, -80, 40)  # Heavy weight (left hand)
        lights[14].update(angle + math.pi / 2, 80, 40)  # Heavy weight (right hand)

        # Draw point-lights
        for light in lights:
            pygame.draw.circle(screen, LIGHT_COLOR, (int(light.x), int(light.y)), 5)

        pygame.display.update()
        angle += 0.01
        clock.tick(60)

if __name__ == "__main__":
    main()
