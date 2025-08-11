
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Sitting Down Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
NUM_LIGHTS = 15
lights = []
for i in range(NUM_LIGHTS):
    x = WIDTH // 2 + (i - NUM_LIGHTS // 2) * 10
    y = HEIGHT // 2 + (i - NUM_LIGHTS // 2) * 10
    lights.append((x, y))

# Animation parameters
FPS = 60
clock = pygame.time.Clock()
angle = 0

def draw_lights(angle):
    screen.fill(BLACK)
    for i, (x, y) in enumerate(lights):
        # Calculate new position based on angle
        dx = 100 * math.sin(math.radians(angle + i * 20))
        dy = 50 * math.cos(math.radians(angle + i * 20))
        new_x = x + dx
        new_y = y + dy
        
        # Draw the point light
        pygame.draw.circle(screen, WHITE, (int(new_x), int(new_y)), 5)
    
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update angle for animation
    angle += 1
    if angle >= 360:
        angle = 0
    
    draw_lights(angle)
    clock.tick(FPS)

pygame.quit()
sys.exit()
