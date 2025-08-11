
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
POINT_LIGHT_COLOR = (255, 255, 255)
NUM_POINTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation - Sad Woman Jumping Up")
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y, radius=3):
        self.x = x
        self.y = y
        self.radius = radius
        self.phase_offset = math.radians(x * 0.1)  # Different phase offset based on initial x position
    
    def update(self, time, amplitude=50, frequency=0.5):
        # Simulate jumping motion with sinusoidal movement
        self.y = HEIGHT // 2 + amplitude * math.sin(frequency * time + self.phase_offset)
    
    def draw(self, surface):
        pygame.draw.circle(surface, POINT_LIGHT_COLOR, (int(self.x), int(self.y)), self.radius)

# Create point lights
point_lights = []
for i in range(NUM_POINTS):
    angle = 2 * math.pi * i / NUM_POINTS
    x = WIDTH // 2 + int(math.cos(angle) * WIDTH // 4)
    y = HEIGHT // 2 + int(math.sin(angle) * HEIGHT // 4)
    point_lights.append(PointLight(x, y))

# Animation loop
running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Clear the screen
    screen.fill(BACKGROUND_COLOR)
    
    # Calculate time in seconds
    time_seconds = (pygame.time.get_ticks() - start_time) / 1000.0
    
    # Update and draw point lights
    for point_light in point_lights:
        point_light.update(time_seconds)
        point_light.draw(screen)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()
