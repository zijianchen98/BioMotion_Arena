
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sad Man Bowing Animation')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Point light parameters
num_lights = 15
lights = [{'x': width // 2, 'y': height // 2, 'vx': random.uniform(-1, 1), 'vy': random.uniform(-1, 1)} for _ in range(num_lights)]

# Animation parameters
clock = pygame.time.Clock()
fps = 60
running = True

while running:
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update positions
    for light in lights:
        light['x'] += light['vx']
        light['y'] += light['vy']
        
        # Simulate bowing motion
        if light['y'] > height * 0.7:
            light['vy'] *= -1
            light['y'] -= 10
        
        # Keep within bounds
        if light['x'] < 0 or light['x'] > width:
            light['vx'] *= -1
        if light['y'] < 0:
            light['vy'] *= -1
    
    # Draw points
    for light in lights:
        pygame.draw.circle(screen, white, (int(light['x']), int(light['y'])), 2)
    
    pygame.display.flip()
    clock.tick(fps)

# Quit Pygame
pygame.quit()
