
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sad Woman Jumping Forward")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
num_lights = 15
lights = []

# Function to initialize point lights
def init_lights():
    for _ in range(num_lights):
        x = width // 2
        y = height // 2
        lights.append({'x': x, 'y': y, 'dx': 0, 'dy': 0})

# Function to update point lights
def update_lights(frame):
    for i, light in enumerate(lights):
        # Calculate angle for each light
        angle = (i / num_lights) * 2 * math.pi
        
        # Calculate radius based on frame
        radius = 50 + 50 * math.sin(frame / 20 + i * 0.5)
        
        # Update position
        light['x'] = width // 2 + radius * math.cos(angle)
        light['y'] = height // 2 + radius * math.sin(angle)
        
        # Add vertical motion for jumping effect
        light['y'] += -100 * math.sin(frame / 10)

# Main loop
running = True
frame = 0
init_lights()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    update_lights(frame)
    
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light['x']), int(light['y'])), 5)
    
    pygame.display.flip()
    frame += 1
    pygame.time.Clock().tick(60)

pygame.quit()
