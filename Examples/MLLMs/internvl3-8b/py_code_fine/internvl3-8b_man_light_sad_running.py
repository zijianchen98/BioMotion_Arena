
import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sad Man Runner")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Number of lights
num_lights = 15

# Light points (x, y)
lights = [(100, 500), (150, 500), (175, 480), (200, 475), (225, 450), (250, 430),
          (275, 420), (300, 400), (325, 375), (350, 360), (375, 335), (400, 310),
          (425, 285), (450, 255), (475, 225)]

# Velocity of the lights
speed = 3
direction = [1, 0]

def move_lights():
    global lights
    new_lights = []
    for light in lights:
        x, y = light
        y += speed * direction[1]
        x += speed * direction[0]
        if x > width:
            direction[0] = -direction[0]
            x = 2 * width - x
        if x < 0:
            direction[0] = -direction[0]
            x = -x
        if y > height:
            direction[1] = -direction[1]
            y = 2 * height - y
        if y < 0:
            direction[1] = -direction[1]
            y = -y
        new_lights.append((x, y))
    lights = new_lights

def draw_lights():
    screen.fill(black)
    for light in lights:
        pygame.draw.circle(screen, white, light, 5)
    pygame.display.flip()

# Main loop
running = True
frame_count = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    move_lights()
    draw_lights()
    
    if direction == [1, 0]:
        direction[0] = 0
        direction[1] = 1
    
    clock.tick(60)
    
pygame.quit()
