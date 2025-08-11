
import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Point-Light Stimulus Animation')

# Load the point-light image
point_light = pygame.transform.scale(pygame.image.load('point_light.png'), (10, 10))

# Animation settings
num_lights = 15
light_size = 20
speed = 2
frame_rate = 15

# Function to create a point light at a random location
def create_light():
    x = random.randint(0, 800 - light_size)
    y = random.randint(0, 600 - light_size)
    return pygame.Rect(x, y, light_size, light_size)

# Initial setup
lights = []
for _ in range(num_lights):
    lights.append(create_light())

# Main loop
running = True
last_time = time.time()
while running:
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw light positions
    for light in lights:
        light.move_ip(random.randint(-speed, speed), random.randint(-speed, speed))
        screen.fill((0, 0, 0))
        for light in lights:
            screen.blit(point_light, (light.x, light.y))
        pygame.display.flip()

    # Frame rate control
    elapsed_time = current_time - last_time
    if elapsed_time < 1.0 / frame_rate:
        time.sleep(1.0 / frame_rate - elapsed_time)
    last_time = time.time()

pygame.quit()
