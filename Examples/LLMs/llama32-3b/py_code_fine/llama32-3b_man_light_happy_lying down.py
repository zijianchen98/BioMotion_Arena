
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHT_RADIUS = 5
POINT_LIGHT_SPAWN_RATE = 10  # Lower values result in more point lights
POINT_LIGHT_SPEED = 2
POINT_LIGHT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the point lights
point_lights = []

# Function to generate point lights
def generate_point_lights():
    global point_lights
    point_lights = []
    for _ in range(15):
        angle = math.pi / 12 * _  # 12 segments in a circle
        x = WIDTH // 2 + math.sin(angle) * 200
        y = HEIGHT // 2 + math.cos(angle) * 200
        point_lights.append((x, y))

# Function to draw point lights
def draw_point_lights():
    screen.fill(BLACK)
    for point_light in point_lights:
        x, y = point_light
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, (int(x), int(y)), POINT_LIGHT_RADIUS)

# Function to update point lights
def update_point_lights():
    global point_lights
    for i, point_light in enumerate(point_lights):
        angle = math.pi / 12 * i  # 12 segments in a circle
        x = WIDTH // 2 + math.sin(angle) * 200 + math.sin(angle + math.pi / 6) * POINT_LIGHT_SPEED
        y = HEIGHT // 2 + math.cos(angle) * 200 + math.cos(angle + math.pi / 6) * POINT_LIGHT_SPEED
        point_lights[i] = (x, y)

# Main loop
generate_point_lights()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_point_lights()
    draw_point_lights()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
