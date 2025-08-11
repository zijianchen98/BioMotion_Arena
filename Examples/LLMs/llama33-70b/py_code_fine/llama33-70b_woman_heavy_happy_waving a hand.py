
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_COLOR = (255, 255, 255)  # White
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Waving motion parameters
WAVE_AMPLITUDE = 50
WAVE_SPEED = 0.05

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, time, wave_offset):
        # Update position based on waving motion
        self.x = self.x + WAVE_AMPLITUDE * math.sin(time * WAVE_SPEED + wave_offset)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Initialize point-lights
    lights = [
        PointLight(100, 200),  # Head
        PointLight(120, 220),  # Left shoulder
        PointLight(80, 220),   # Right shoulder
        PointLight(120, 250),  # Left elbow
        PointLight(80, 250),   # Right elbow
        PointLight(120, 280),  # Left wrist
        PointLight(80, 280),   # Right wrist
        PointLight(100, 300),  # Torso
        PointLight(120, 350),  # Left hip
        PointLight(80, 350),   # Right hip
        PointLight(120, 380),  # Left knee
        PointLight(80, 380),   # Right knee
        PointLight(120, 410),  # Left ankle
        PointLight(80, 410),   # Right ankle
        PointLight(100, 450),  # Heavy weight
    ]

    running = True
    time = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Update and draw point-lights
        for i, light in enumerate(lights):
            light.update(time, i * 0.1)  # Offset waving motion for each light
            pygame.draw.circle(screen, LIGHT_COLOR, (int(light.x), int(light.y)), 5)

        # Waving hand motion
        lights[5].x = lights[5].x + 20 * math.sin(time * WAVE_SPEED)  # Left wrist
        lights[6].x = lights[6].x - 20 * math.sin(time * WAVE_SPEED)  # Right wrist

        # Heavy weight motion
        lights[14].y = lights[14].y + 10 * math.sin(time * WAVE_SPEED)  # Heavy weight

        pygame.display.flip()
        clock.tick(60)
        time += 1

    pygame.quit()

if __name__ == "__main__":
    main()
