
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light positions and movement
class PointLight:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Boundary checking
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.speed_x *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.speed_y *= -1

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create point lights
point_lights = [
    PointLight(100, 100, 5),
    PointLight(150, 150, 5),
    PointLight(200, 200, 5),
    PointLight(250, 250, 5),
    PointLight(300, 300, 5),
    PointLight(350, 350, 5),
    PointLight(400, 400, 5),
    PointLight(450, 450, 5),
    PointLight(500, 500, 5),
    PointLight(550, 550, 5),
    PointLight(600, 600, 5),
    PointLight(650, 650, 5),
    PointLight(700, 700, 5),
    PointLight(750, 750, 5),
    PointLight(800, 100, 5),
]

# Animation parameters
angle = 0
scale = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.fill(BLACK)

    # Draw point lights
    for i, point_light in enumerate(point_lights):
        # Calculate new position based on angle and scale
        x = WIDTH // 2 + math.cos(angle + i * math.pi / 7) * 200 * scale
        y = HEIGHT // 2 + math.sin(angle + i * math.pi / 7) * 200 * scale

        # Update point light position
        point_light.x = x
        point_light.y = y

        # Draw point light
        pygame.draw.circle(screen, WHITE, (int(point_light.x), int(point_light.y)), point_light.radius)

    # Update angle and scale
    angle += 0.01
    scale = 1 + 0.1 * math.sin(angle)

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
